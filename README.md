# Atelier

Fábrica de productos de vitrina. Un motor común convierte un archivo (imagen/audio/texto)
en un resultado estructurado vía LLM. Cada producto de vitrina = un config, no un rebuild.

## Estructura

```
api/    FastAPI → Cloud Run. Motor + registro de productos.
web/    Demo estática (landing por producto) → Cloudflare Pages.
docs/   Handbook.
```

## Agregar un producto

1. Crear `api/app/products/<slug>.py`: define el `output_schema` (Pydantic), el `prompt`,
   el `input_kind` y los `accepted_mime`, y llama a `register(...)`.
2. Importarlo en `api/app/products/__init__.py`.
3. (Opcional) clonar `web/index.html` apuntando a `/process/<slug>`.

No se toca el core.

## Correr local

```
cd api
python -m venv .venv
./.venv/Scripts/python.exe -m pip install -r requirements.txt
cp .env.example .env   # poner GEMINI_API_KEY
./.venv/Scripts/python.exe -m uvicorn app.main:app --reload --port 8080
```

Demo: abrir `web/index.html` (apunta a localhost:8080).

## Endpoints

- `GET /health`
- `GET /products` — catálogo registrado.
- `POST /process/{slug}` — multipart `file` → resultado estructurado.

Primer producto: `receipt` (foto de factura/recibo → datos contables).
