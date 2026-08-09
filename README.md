# Atelier

**Fábrica de productos de vitrina de Geosdata.** Cada producto resuelve un dolor real y sistematizable de un micronegocio o independiente — ⏱️ reduce tiempo, 💰 ahorra plata o 📈 genera ingreso. La IA se usa solo donde suma (4 de 14). Un motor común: agregar un producto IA = un archivo de config, sin rebuild.

🔗 **En vivo:** https://atelier.geosdata.com · 🗺️ [Roadmap](docs/ROADMAP.md) · 📘 [Handbook](docs/handbook/)

---

## Catálogo (14 productos)

### 🤖 Con IA (motor FastAPI + Gemini vision)
| Producto | Dolor que resuelve | ROI | Demo | Doc |
|---|---|---|---|---|
| Factura a datos | pasar facturas/recibos a datos contables a mano | ⏱️💰 | [abrir](https://atelier.geosdata.com/soluciones/factura-a-datos/) | [README](docs/products/receipt/README.md) |
| Clasificador de residuos | no saber en qué caneca va (norma CO 3 canecas) | ⏱️ | [abrir](https://atelier.geosdata.com/soluciones/clasificador-de-residuos/) | [README](docs/products/waste/README.md) |
| Diagnóstico de cultivo | detectar plaga/enfermedad sin agrónomo (Caribe) | 💰📈 | [abrir](https://atelier.geosdata.com/soluciones/diagnostico-de-cultivo/) | [README](docs/products/crop/README.md) |
| Revisor de exámenes | corregir + **detectar dominio inflado** (mastery-check) | ⏱️ | [abrir](https://atelier.geosdata.com/soluciones/revisor-de-examenes/) | [README](docs/products/exam/README.md) |

### 💼 Negocio (cálculo en navegador)
| Producto | Dolor | ROI | Demo | Doc |
|---|---|---|---|---|
| Precio de venta / margen | fijar precio sin perder plata | 💰📈 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-precio-de-venta/) | [README](docs/products/calculadora-precio-de-venta/README.md) |
| Punto de equilibrio | cuánto vender para no perder | 💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-punto-de-equilibrio/) | [README](docs/products/calculadora-punto-de-equilibrio/README.md) |
| Generador de cotización (PDF) | armar cotización a mano | ⏱️📈 | [abrir](https://atelier.geosdata.com/soluciones/generador-de-cotizacion/) | [README](docs/products/generador-de-cotizacion/README.md) |
| Generador de QR | QR para cobro/menú/link | ⏱️ | [abrir](https://atelier.geosdata.com/soluciones/generador-de-qr/) | [README](docs/products/generador-de-qr/README.md) |

### 👷 Laboral (cálculo en navegador)
| Producto | Dolor | ROI | Demo | Doc |
|---|---|---|---|---|
| Recargos y horas extra | liquidar recargos sin errores | ⏱️💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-recargos-2026/) | [README](docs/products/calculadora-recargos-2026/README.md) |
| Liquidación de contrato | calcular liquidación laboral | ⏱️💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-liquidacion-contrato-2026/) | [README](docs/products/calculadora-liquidacion-contrato-2026/README.md) |
| Prima de servicios | calcular prima | ⏱️ | [abrir](https://atelier.geosdata.com/soluciones/calculadora-prima-servicios-2026/) | [README](docs/products/calculadora-prima-servicios-2026/README.md) |

### 🧾 Contable (cálculo en navegador)
| Producto | Dolor | ROI | Demo | Doc |
|---|---|---|---|---|
| Retención en la fuente (salarios) | retención a mano | ⏱️💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-retencion-salarios-2026/) | [README](docs/products/calculadora-retencion-salarios-2026/README.md) |
| Retención en la fuente (proveedores) | retención a mano | ⏱️💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-retencion-pagos-2026/) | [README](docs/products/calculadora-retencion-pagos-2026/README.md) |

### 🏠 Vivienda (cálculo en navegador)
| Producto | Dolor | ROI | Demo | Doc |
|---|---|---|---|---|
| Incremento legal de arriendo | cuánto puedo subir legalmente | 💰 | [abrir](https://atelier.geosdata.com/soluciones/calculadora-incremento-arriendo-2026/) | [README](docs/products/calculadora-incremento-arriendo-2026/README.md) |

---

## Arquitectura

```
api/    FastAPI (Python 3.12) → Cloud Run. Motor IA + registro de productos.
web/    Astro + Tailwind → Cloudflare Pages. Landing por producto + calculadoras client-side.
docs/   Handbook (6/6), roadmap, README por producto.
```

- **Productos IA:** un motor común (`api/app/services/`) toma archivo → Gemini vision con `response_schema` Pydantic → JSON validado. Retry con backoff (429/500/503), rate-limit 20 req/min por IP.
- **Calculadoras:** cálculo determinista en el navegador (cero backend, cero costo servidor).

## Agregar un producto IA

1. `api/app/products/<slug>.py`: definí `output_schema` (Pydantic), `prompt`, `input_kind`, `accepted_mime`, `subtitle`, opcional `context`, y llamá a `register(...)`.
2. Importalo en `api/app/products/__init__.py`.

La landing aparece sola (genérica, lee `GET /products`). No se toca el motor ni el front. Detalle en [`docs/handbook/01-Architecture.md`](docs/handbook/01-Architecture.md).

## Correr local

```
cd api
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
cp .env.example .env    # poner GEMINI_API_KEY
./.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8080
```

## Deploy (no git-push)

```
# Web (Astro → Cloudflare Pages)
cd web && npm run build && wrangler pages deploy dist --project-name atelier

# API (FastAPI → Cloud Run)
cd api && gcloud run deploy atelier --source . --region us-central1 --project geosdata
```

## Endpoints API

- `GET /health`
- `GET /products` — catálogo registrado (slug, title, subtitle, input, accept).
- `POST /process/{slug}` — multipart `file` → resultado estructurado.
