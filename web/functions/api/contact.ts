import { Env, resolveConfig, MAX_FIELD_LENGTH } from "../_lib/config";
import { jsonResponse, isValidEmail, escapeHtml } from "../_lib/http";

interface ContactPayload {
  name?: string;
  email?: string;
  subject?: string;
  message?: string;
  company?: string;
}

function buildEmailBody(name: string, email: string, subject: string, message: string) {
  const text = `Nombre: ${name}\nEmail: ${email}\nAsunto: ${subject}\n\nMensaje:\n${message}`;
  const html =
    "<h2>Nuevo mensaje de contacto</h2>" +
    `<p><strong>Nombre:</strong> ${escapeHtml(name)}</p>` +
    `<p><strong>Email:</strong> ${escapeHtml(email)}</p>` +
    `<p><strong>Asunto:</strong> ${escapeHtml(subject)}</p>` +
    "<p><strong>Mensaje:</strong></p>" +
    `<p>${escapeHtml(message).replace(/\n/g, "<br>")}</p>`;
  return { text, html };
}

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  const config = resolveConfig(env);
  if (!config || !env.EMAIL_API_KEY) {
    return jsonResponse({ ok: false, error: "service_unavailable" }, 503);
  }

  const origin = request.headers.get("origin");
  if (origin && origin !== config.allowedOrigin) {
    return jsonResponse({ ok: false, error: "origin_not_allowed" }, 403);
  }

  let payload: ContactPayload;
  try {
    payload = await request.json();
  } catch {
    return jsonResponse({ ok: false, error: "invalid_body" }, 400);
  }

  const looksLikeBot = typeof payload.company === "string" && payload.company.trim().length > 0;
  if (looksLikeBot) {
    return jsonResponse({ ok: true }, 200);
  }

  const name = (payload.name ?? "").trim();
  const email = (payload.email ?? "").trim();
  const subject = (payload.subject ?? "").trim();
  const message = (payload.message ?? "").trim();

  if (!name || !email || !subject || !message) {
    return jsonResponse({ ok: false, error: "missing_fields" }, 400);
  }
  if (!isValidEmail(email)) {
    return jsonResponse({ ok: false, error: "invalid_email" }, 400);
  }
  if (
    name.length > MAX_FIELD_LENGTH ||
    subject.length > MAX_FIELD_LENGTH ||
    message.length > MAX_FIELD_LENGTH
  ) {
    return jsonResponse({ ok: false, error: "field_too_long" }, 400);
  }

  const { text, html } = buildEmailBody(name, email, subject, message);

  const upstream = await fetch(`${config.serviceUrl}/emails/send`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "x-api-key": env.EMAIL_API_KEY,
      "x-tenant-id": config.tenantId,
    },
    body: JSON.stringify({
      to: config.recipient,
      subject: `[Geosdata] ${subject}`,
      text,
      html,
      reply_to: email,
    }),
  });

  if (!upstream.ok) {
    return jsonResponse({ ok: false, error: "send_failed" }, 502);
  }

  return jsonResponse({ ok: true }, 200);
};
