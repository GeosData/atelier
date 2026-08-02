# 04 — Decisiones (stack + producto)

> Aplica el paved-road Geosdata. Cada decisión = contexto + elección + por qué + alternativa descartada.

## D1 — Motor IA: Gemini visión
- **Elección:** Gemini (flash / flash-lite) como motor multimodal por-request para leer el examen y calificar.
- **Por qué:** entra por costo/volumen, es el motor default de productos Geosdata; visión + JSON estructurado nativo.
- **Descartado:** Claude/GPT visión (mejor calidad, peor costo para vitrina de volumen). Reevaluar si la lectura de manuscrito falla.

## D2 — Web: landing-template Astro → CF Pages
- **Elección:** clonar `F:\geosdata\landing-template`, editar config; deploy CF Pages con wrangler (NO git push).
- **Por qué:** edge/estático = Cloudflare por paved-road; template ya trae waitlist a newsletter.
- **Descartado:** front desde cero (reinventar); Vercel (se reserva para casos con dominio propio).

## D3 — Motor/API: producto dentro de `atelier` (REVISADO 2026-08-01)
- **Elección:** gradecheck NO es API nueva — es un producto del motor `atelier` (`F:\geosdata\atelier`, file→LLM→schema, Gemini vision, FastAPI→Cloud Run, rate-limit ya hechos). Implementado = `api/app/products/exam.py` (slug `exam`) + import en `products/__init__.py`. Endpoint `POST /process/exam`.
- **Por qué:** la fábrica-vitrina ya existe; agregar producto = 1 archivo sin tocar core. Reusar > reconstruir.
- **Descartado:** monorepo/API desde cero (lo que decía la v1 de este doc) — sobra, atelier lo cubre.

## D4 — Auth: demo pública + Google opcional
- **Elección:** probar sin login (demo abierta con rate-limit); login Google (Clerk o api-auth según dominio) solo para guardar historial.
- **Por qué:** comodidad del usuario, no MVP mínimo; el imán necesita fricción cero para probar.
- **Riesgo:** demo abierta = abuso → rate-limit por IP desde el día 1.

## D5 — Repo y estructura (REVISADO 2026-08-01)
- **Elección:** gradecheck vive DENTRO del repo `atelier`, no repo propio. Código = `products/exam.py`. Web = clonar `atelier/web/index.html` apuntando a `/process/exam` (landing propia por producto). Este discovery (00-04) se reubica a `atelier/docs/products/exam/`.
- **Por qué:** atelier ES la fábrica; un producto vitrina = config + landing, no repo. El foso/distribución se resuelve a nivel portafolio.
- **Descartado:** repo `GeosData/gradecheck` independiente — fragmenta la fábrica.
- **Pendiente:** atelier aún no tiene repo GitHub remoto ni deploy ni nombre final (ver memoria atelier-fabrica-vitrina) → cerrar eso desbloquea el deploy de exam.

## D6 — Diferencial = mastery-check
- **Elección:** el chequeo de dominio real es el núcleo del producto, no un extra.
- **Condición:** confirmar en `01-estado-del-arte` que es hueco real. Si un grande ya lo hace → pivotar ángulo antes de código.

## Convenciones
- Código en inglés, sin comentarios (naming autoexplicativo).
- Secretos en `.env` central, no en repo.
