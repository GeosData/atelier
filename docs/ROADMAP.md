# Roadmap — atelier

> Fábrica de productos de vitrina. Motor único (file→LLM→schema, Gemini vision), un config por producto. Cada producto es un imán de inbound; el foso/distribución se resuelve a nivel portafolio.

## Productos
| Slug | Qué hace | Estado | Landing | Deploy |
|---|---|---|---|---|
| receipt | Factura/recibo → datos contables | motor listo | pendiente | no |
| waste | Clasifica residuo por foto (3 canecas CO) | motor listo | pendiente | no |
| crop | Diagnóstico de cultivo por foto | motor listo | pendiente | no |
| exam | Corrige examen + detecta dominio inflado (mastery-check) | motor listo, sin probar e2e | pendiente | no |

## exam (gradecheck) — próximo foco
Discovery completo en `docs/products/exam/` (00-04). Diferencial verificado por scout: nadie hace mastery-check (ni Gradescope ni apps LATAM). 
- [ ] Probar `/process/exam` con foto de examen real → validar que el mastery-check dispara bien
- [ ] Clonar `web/index.html` → landing exam apuntando a `/process/exam`
- [ ] Cerrar nombre público del producto (`gradecheck` vs realgrade/gradelens, ver 02-nombres)

## Gobernanza / infra (transversal)
- [x] Repo git local
- [ ] Repo remoto GitHub `GeosData/atelier` + push
- [ ] Deploy: api → Cloud Run, web → CF Pages (wrangler)
- [ ] Nombre final de la fábrica (working `atelier`)
- [ ] Tracker Linear (team GeosData) — este ROADMAP.md es puente hasta entonces
- [ ] Subdominio por producto (o dominio propio si crece)

## Regla
El motor no se toca para sumar producto: nuevo producto = `products/<slug>.py` + import + landing. Ver `docs/handbook/01-Architecture.md`.
