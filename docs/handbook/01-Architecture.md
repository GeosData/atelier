# Architecture

Motor único, muchos productos. El valor está en que sumar un producto no toca el core.

## Capas (api)

```
routes/        HTTP surface. Sin lógica.
controllers/   Orquesta: valida entrada, llama al engine, arma la respuesta.
services/
  engine.py    Selecciona provider, valida mime, devuelve el schema del producto.
  providers/   Abstracción de LLM. gemini.py implementa VisionProvider.
products/       Catálogo. registry.py = tipos + registro. <slug>.py = un producto.
schemas/        (reservado para DTOs transversales)
middleware/     rate_limit.py
config.py       Settings desde env.
main.py         Bootstrap: crea app, CORS, middleware, router. Nada más.
```

## Flujo de una request

`POST /process/{slug}` → controller lee el archivo, valida tamaño → `engine.run(product, bytes, mime)`
→ provider llama al modelo con `response_schema=product.output_schema` → Pydantic valida → JSON.

## Deploy (paved-road)

- `api` → contenedor → Google Cloud Run. DB no requerida para la vitrina.
- `web` → Cloudflare Pages (wrangler, no git push).
- Un subdominio por producto (o dominio propio si el producto crece).
