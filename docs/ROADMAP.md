# Roadmap — atelier

> Fábrica de productos de vitrina. Motor único (file→LLM→schema, Gemini vision), un config por producto. Cada producto es un imán de inbound; el foso/distribución se resuelve a nivel portafolio.

## Productos
| Slug | Qué hace | Estado | Landing | Deploy |
|---|---|---|---|---|
| receipt | Factura/recibo → datos contables | motor listo | pendiente | no |
| waste | Clasifica residuo por foto (3 canecas CO) | motor listo | pendiente | no |
| crop | Diagnóstico de cultivo por foto | motor listo | pendiente | no |
| exam | Corrige examen + detecta dominio inflado (mastery-check) | motor listo, mastery-check verificado e2e (sintético) | pendiente | no |

## exam (gradecheck) — próximo foco
Discovery completo en `docs/products/exam/` (00-04). Diferencial verificado por scout: nadie hace mastery-check (ni Gradescope ni apps LATAM). 
- [x] Probar `/process/exam` → mastery-check dispara bien (examen sintético patrón aberrante: flageó difíciles-correctas, `overall_mastery_confidence` 0.3, alerta "acertó difíciles, falló fáciles"). Pendiente: repetir con foto de examen manuscrito real.
- [ ] Soporte PDF: `03-alcance` pide imagen Y PDF, pero `exam.py` solo acepta jpg/png/webp. Agregar `application/pdf` a `accepted_mime` (Gemini lo lee nativo).
- [ ] Clonar `web/index.html` → landing exam apuntando a `/process/exam` (hoy la web es receipt-only, hardcodeada).
- [ ] Cerrar nombre público del producto (`gradecheck` vs realgrade/gradelens, ver 02-nombres)

## Gobernanza / infra (transversal)
- [x] Repo git local
- [x] Repo remoto GitHub `GeosData/atelier` + push (SSH, rama `main`)
- [ ] Deploy: api → Cloud Run, web → CF Pages (wrangler)
- [x] Nombre final de la fábrica: `atelier` (confirmado Josse)
- [ ] Robustez deploy: el provider Gemini devuelve 503 en picos de demanda (visto en test); agregar retry/backoff propio antes de exponer demo pública
- [ ] Tracker Linear (team GeosData) — este ROADMAP.md es puente hasta entonces
- [ ] Subdominio por producto (o dominio propio si crece)

## Regla
El motor no se toca para sumar producto: nuevo producto = `products/<slug>.py` + import + landing. Ver `docs/handbook/01-Architecture.md`.
