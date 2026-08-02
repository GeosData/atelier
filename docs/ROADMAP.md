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
- [x] Soporte PDF: `accepted_mime` de exam y receipt incluye `application/pdf`; verificado e2e con PDF real (calificó + flageó difícil-correcta).
- [x] Landing: `web/product.html?p=exam` genérica (lee `/products`), no hay que clonar nada. Falta solo copy/nombre público en el subtítulo.
- [ ] Cerrar nombre público del producto (`gradecheck` vs realgrade/gradelens, ver 02-nombres) → hoy el subtítulo sale del `Product.subtitle`.

## Gobernanza / infra (transversal)
- [x] Repo git local
- [x] Repo remoto GitHub `GeosData/atelier` + push (SSH, rama `main`)
- [x] Deploy: api → Cloud Run (`https://atelier-448285277410.us-central1.run.app`, proyecto geosdata, us-central1) · web → CF Pages (`https://atelier-af1.pages.dev`). Verificado prod e2e (receipt con imagen real). Seguimiento: mover `GEMINI_API_KEY` de env-var a Secret Manager.
- [x] Nombre final de la fábrica: `atelier` (confirmado Josse)
- [x] Robustez: provider Gemini reintenta 429/500/503 con backoff exponencial (4 intentos)
- [ ] Tracker Linear (team GeosData) — este ROADMAP.md es puente hasta entonces
- [x] Front en `atelier.geosdata.com` (CF Pages custom domain, sirve 200). API en run.app.
- [ ] `api.atelier.geosdata.com` → requiere Cloud Run domain-mapping + verificación de dominio (diferido; run.app funciona, el usuario no la ve). Hoy la web apunta a la run.app.
- [ ] Landing por producto en subdominio propio si un producto crece (hoy todos bajo `atelier.geosdata.com/product.html?p=<slug>`)

## Regla
El motor no se toca para sumar producto: nuevo producto = `products/<slug>.py` + import + landing. Ver `docs/handbook/01-Architecture.md`.
