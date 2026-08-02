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
   el `input_kind`, los `accepted_mime`, el `subtitle` y (opcional) `context`, y llama a `register(...)`.
2. Importarlo en `api/app/products/__init__.py`.

Listo. La web no se toca: el producto aparece solo en la galería (`web/index.html`) y su landing
es `web/product.html?p=<slug>`, que lee título/subtítulo/tipos aceptados desde `GET /products`
y renderiza el resultado de forma genérica. No se toca el core ni el front.

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
- `GET /products` — catálogo registrado (slug, title, subtitle, input, accept).
- `POST /process/{slug}` — multipart `file` → resultado estructurado.

Productos: `receipt` · `waste` · `crop` · `exam`.

## Web

- `web/index.html` — galería, lista los productos desde `/products`.
- `web/product.html?p=<slug>` — landing genérica: subir archivo → resultado renderizado.

Estático, self-contained. Deploy a Cloudflare Pages con wrangler (no git push).
