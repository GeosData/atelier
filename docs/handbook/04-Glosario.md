# Glosario

- **Producto de vitrina**: mini-app demoable que resuelve un problema ya probado (por una tesis/fuente).
  Su fin es ser imán de pedidos a medida por inbound, no ganar un mercado.
- **Motor / engine**: capa que toma (archivo, producto) y devuelve el schema del producto vía LLM.
- **Product config**: `products/<slug>.py`. Prompt + schema + input_kind + mime aceptados.
- **Provider**: implementación de LLM (gemini). Intercambiable.
- **Molde**: patrón de input. A=imagen, B=audio, C=texto. La ola 1 es mayoría molde A.
