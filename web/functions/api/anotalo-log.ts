import { neon } from '@neondatabase/serverless';

interface Env {
  ANOTALO_DB_URL: string;
  ANOTALO_LOG_KEY: string;
}

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json' },
  });
}

function esc(s: string): string {
  return s.replace(/[<>&]/g, (m) => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;' }[m] as string));
}

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  const url = new URL(request.url);
  if (url.searchParams.get('key') !== env.ANOTALO_LOG_KEY) {
    return new Response('No autorizado. Falta ?key=', { status: 401 });
  }
  const sql = neon(env.ANOTALO_DB_URL);
  const filas = (await sql`
    SELECT id, device, version, contenido, creado_at
    FROM anotalo_logs ORDER BY id DESC LIMIT 200
  `) as { id: number; device: string; version: string; contenido: string; creado_at: string }[];

  const items = filas.map((f) => `
    <article>
      <header>#${f.id} · ${esc(f.device || '')} · v${esc(f.version || '')} · ${new Date(f.creado_at).toLocaleString('es-CO')}</header>
      <pre>${esc(f.contenido || '')}</pre>
    </article>`).join('');

  const html = `<!doctype html><html lang="es"><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>anota.lo · registros de voz</title>
    <style>
      body{font-family:system-ui,sans-serif;background:#f7f6f2;color:#16211c;margin:0;padding:1rem;max-width:760px;margin:0 auto}
      h1{font-size:1.2rem}
      article{background:#fff;border:1px solid #d5d4cb;border-radius:10px;padding:.8rem 1rem;margin-bottom:.7rem}
      header{font-size:.72rem;color:#6b7770;font-family:ui-monospace,monospace;margin-bottom:.4rem}
      pre{white-space:pre-wrap;word-break:break-word;font-size:.82rem;margin:0;font-family:ui-monospace,monospace}
      .vacio{color:#6b7770;text-align:center;padding:2rem}
    </style></head><body>
    <h1>Registros de voz — anota.lo (${filas.length})</h1>
    ${items || '<p class="vacio">Todavía no hay registros.</p>'}
  </body></html>`;

  return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8' } });
};

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  if (request.headers.get('x-anotalo-key') !== env.ANOTALO_LOG_KEY) {
    return json({ ok: false, error: 'no autorizado' }, 401);
  }

  let body: { contenido?: unknown; device?: unknown; version?: unknown };
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: 'json inválido' }, 400);
  }

  const contenido = String(body.contenido ?? '').slice(0, 200000);
  if (!contenido.trim()) return json({ ok: false, error: 'vacío' }, 400);
  const device = String(body.device ?? '').slice(0, 120);
  const version = String(body.version ?? '').slice(0, 40);

  try {
    const sql = neon(env.ANOTALO_DB_URL);
    await sql`INSERT INTO anotalo_logs (device, version, contenido) VALUES (${device}, ${version}, ${contenido})`;
    return json({ ok: true });
  } catch (e) {
    return json({ ok: false, error: String((e as Error)?.message ?? e) }, 500);
  }
};
