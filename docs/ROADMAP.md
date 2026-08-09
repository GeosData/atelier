# Roadmap — atelier

> Fábrica de productos de vitrina. Motor único (file→LLM→schema, Gemini vision) + calculadoras client-side deterministas. Un config por producto IA; una ruta Astro por calculadora.
> **Modelo:** cada producto resuelve un dolor real y sistematizable (⏱️ reduce tiempo · 💰 ahorra · 📈 genera). IA solo donde suma. Cada producto es un imán de inbound + material de **build-in-public**. El foso/distribución se resuelve a nivel portafolio.
> **Estado global (2026-08-09):** LIVE en `atelier.geosdata.com` · 14 productos (4 IA + 10 calculadoras) · ~90% listo para publicar full.

---

## Estado de publicación

| Componente | URL | Estado |
|---|---|---|
| Web | `https://atelier.geosdata.com` (CF Pages) | ✅ LIVE |
| API | `https://atelier-448285277410.us-central1.run.app` (Cloud Run) | ✅ LIVE |
| API dominio propio | `api.atelier.geosdata.com` | ⏳ pendiente domain-mapping (no visible al usuario) |
| Fusión geosdata.com → atelier | pasos 1-4 hechos, 5-6 (DNS cutover) gateados | 🔒 esperando go |

**Gaps para "100% publicado" (P0):** cerrar nombre público de `exam` · decidir go del DNS cutover (fusion pasos 5-6) · verificar los 14 responden en prod.

---

## Productos (14)

### IA (motor Gemini vision, 4)
| Slug | Dolor que resuelve | ROI | Estado |
|---|---|---|---|
| **receipt** | pasar facturas/recibos a datos contables a mano | ⏱️💰 | ✅ completo, e2e |
| **waste** | no saber en qué caneca va cada residuo (norma CO 3 canecas) | ⏱️ | ✅ completo |
| **crop** | diagnosticar plaga/enfermedad de cultivo sin agrónomo (Caribe/Córdoba) | 💰📈 | ✅ completo |
| **exam** | corregir exámenes + **detectar dominio inflado** (mastery-check, nadie lo hace) | ⏱️ | 🟡 motor listo, falta nombre público |

### Calculadoras (client-side, cero costo servidor, 10)
| Slug/tool | Dolor | ROI |
|---|---|---|
| precio-venta / margen | fijar precio sin perder plata | 💰📈 |
| punto-equilibrio | saber cuánto vender para no perder | 💰 |
| cotizaciones (PDF) | armar cotización a mano | ⏱️📈 |
| QR | generar QR para cobro/menú/link | ⏱️ |
| recargos / horas extra | liquidar recargos sin errores | ⏱️💰 |
| liquidación de contrato | calcular liquidación laboral | ⏱️💰 |
| prima de servicios | calcular prima | ⏱️ |
| retención en la fuente (salarios) | retención a mano | ⏱️💰 |
| retención en la fuente (proveedores) | retención a mano | ⏱️💰 |
| incremento legal de arriendo | cuánto puedo subir legalmente | 💰 |

> QR y cotización hoy son inline-JS (no `Product` formal). Aceptable; formalizar solo si crecen.

---

## Roadmap por producto

> Cada producto: mejoras concretas + el ángulo build-in-public (qué se cuenta al construir/mejorar en público).

### receipt — Factura a datos
- **Mejoras:** exportar a CSV/Excel · soportar múltiples facturas de una · detectar moneda/impuesto mejor.
- **Build-in-public:** "extraigo datos de facturas reales con vision + schema Pydantic, e2e — así lo armé".

### waste — Clasificador de residuos
- **Mejoras:** modo lote (varias fotos) · fichas por material · localizar norma por ciudad.
- **Build-in-public:** "clasificador contextualizado a la norma colombiana de 3 canecas, no un genérico gringo".

### crop — Diagnóstico de cultivo
- **Mejoras:** guía de tratamiento accionable (producto + dosis) · cultivos más allá del Caribe · historial por finca.
- **Build-in-public:** "diagnóstico de plagas para el agro del Caribe/Córdoba, plagas locales reales".

### exam — Revisor de exámenes *(BLOQUEADOR: nombre)*
- **P0:** cerrar nombre público → recomendación del discovery: **`realgrade`** o **`gradelens`** (insinúan el diferencial "la nota real", mejor que `gradecheck`). Decisión de Josse → actualizar `Product.subtitle` → redeploy API.
- **Mejoras:** rúbrica configurable · reporte por estudiante · export.
- **Build-in-public (el más fuerte):** "el único revisor que detecta dominio inflado (acertó las difíciles, falló las fáciles) — ni Gradescope ni apps LATAM lo hacen".

### Calculadoras (transversal)
- **Mejoras:** cada una con CTA claro + copiar resultado + compartir · SEO por dolor ("cómo calcular X en Colombia").
- **Build-in-public:** "10 calculadoras client-side, cero costo servidor — sistematización pura sin IA".

---

## Mejoras transversales (priorizadas)

### P0 — cerrar publicación
- [ ] Nombre público de `exam` (Josse decide `realgrade`/`gradelens`) + redeploy.
- [ ] Decidir go del DNS cutover (fusion pasos 5-6) o dejar geosdata.com con 301 a atelier.
- [ ] Smoke-test de los 14 en prod (una pasada real por cada uno).

### P1 — mejorar existentes + convertir (vitrina → pedido)
- [ ] **CTA post-resultado en cada tool:** cuando el usuario ve el resultado y le sirvió → "¿lo necesitás integrado a tu negocio / a medida? escribinos". Pull, no push. Hoy la tool resuelve pero no captura el pedido a medida (que es el modelo de negocio). **Esta es la mejora de mayor ROI.**
- [ ] **Analytics de uso por tool** (qué se usa más = señal de demanda real que decide qué construir next). Sin esto, el pipeline de dolores es a ciegas.
- [ ] Discovery docs (00-04) para receipt/waste/crop (copiar template de exam).

### P2 — build-in-public + escalar
- [ ] Narrativa "cómo lo construí" por producto → posts (canal a definir; OPSEC: nada DN).
- [ ] `api.atelier.geosdata.com` domain-mapping.
- [ ] `GEMINI_API_KEY` → Secret Manager.
- [ ] Tracker Linear (team GeosData); este ROADMAP.md es puente.

---

## Build-in-public loop

```
dolor verificado → producto en atelier → construir/mejorar EN PÚBLICO (post)
      ↑                                              ↓
   pipeline de dolores  ←  analytics de uso + CTA/pedidos  ←  gate Josse (aprobar en lote)
```

El uso real de cada tool + los pedidos que entren por el CTA alimentan qué dolor atacar next. El contenido sale del trabajo real (armé X, esto pasó), no de tendencias.

---

## Pipeline de dolores (próximos productos)

> Regla de entrada: proceso repetitivo real · sistematizable · ROI en tiempo/plata · buen build-in-public · IA opcional. Verificar demanda (autocomplete gl=co + reviews) ANTES de construir — no inventar.

Candidatos sembrados (hipótesis, a verificar):
| Dolor | Sector/actor | ROI | IA |
|---|---|---|---|
| recordatorio de revacunación | veterinaria / petshop | 📈 | no |
| cobro de pensiones + mora | colegio/academia chica | 📈💰 | no |
| cuadre de caja vs comisiones apps | restaurante con domicilios | 💰 | no |
| agenda + no-shows | barbería / salón | 📈 | no |
| orden de servicio + historial | taller moto/carro | ⏱️📈 | no |
| liquidación de fletes/viáticos | transportador / carga | 💰 | no |
| facturación electrónica DIAN | independiente / contador | ⏱️ | opc. |

Fuentes de dolores reales: reviews de apps del sector · foros/grupos del oficio · autocomplete gl=co · tesis Unicórdoba.

---

## Regla del motor
El motor no se toca para sumar producto IA: nuevo = `products/<slug>.py` + import + landing genérica lee `/products`. Calculadora nueva = ruta Astro client-side. Ver `docs/handbook/01-Architecture.md`.
