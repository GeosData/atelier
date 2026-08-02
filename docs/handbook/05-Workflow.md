# Workflow

## Sacar un producto nuevo

1. Elegir una tesis/fuente con problema probado + demo con wow.
2. `products/<slug>.py`: schema + prompt + mime + subtitle. Registrar en `products/__init__.py`.
3. Probar `POST /process/<slug>` con un archivo real.
4. Nada en el front: el producto aparece solo en la galería y su landing es `product.html?p=<slug>`.
5. Deploy: api a Cloud Run, web a Cloudflare Pages.
6. 1 pieza build-in-public → gate humano → Pheme.

## Medir

Qué vitrina genera inbound. Los que traen contactos se profundizan a producto real;
el resto queda de vitrina barata.
