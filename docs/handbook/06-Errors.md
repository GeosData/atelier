# Errors / Runbook

- **415 Unsupported Media Type**: el mime del archivo no está en `accepted_mime` del producto.
  Revisar qué envía el cliente (`Content-Type` del multipart).
- **422**: falta el campo `file` en el multipart.
- **429**: rate-limit por IP superado (`RATE_LIMIT_PER_MINUTE`).
- **500 al llamar al modelo**: casi siempre `GEMINI_API_KEY` ausente/inválida o `VISION_MODEL` inexistente.
  Verificar `.env`. La app importa sin key, pero `/process` la necesita.
- **Output con confidence baja / notes lleno**: imagen ilegible o campo ausente. Es comportamiento
  esperado (el modelo no inventa), no un bug.
