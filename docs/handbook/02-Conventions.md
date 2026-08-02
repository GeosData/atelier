# Conventions

- Identificadores en inglés. Strings de UI en el idioma del producto.
- Sin comentarios ni docstrings: naming semántico. Si algo necesita comentario, renombrar.
- Arquitectura por capas. `main.py` solo bootstrap.
- Un producto = un archivo en `products/`. El core no conoce productos concretos.
- Config desde env (pydantic-settings). Sin secretos en el repo.
- Output siempre con `confidence`; si falta un dato, `notes` lo explica. El modelo no inventa.
