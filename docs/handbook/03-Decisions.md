# Decisions

- **Motor único config-driven**: sumar producto = un config, no un repo nuevo. Baja el costo
  marginal de cada vitrina a casi cero. Alternativa descartada: un repo por producto (no escala manual).
- **Gemini como provider por defecto**: costo/volumen para vitrina, no calidad máxima. `VisionProvider`
  deja cambiar de proveedor sin tocar controllers/products.
- **Structured output por schema del producto**: validación en la capa del modelo (response_schema),
  no parsing frágil aguas abajo.
- **Demo pública sin auth + rate-limit**: la vitrina es imán, la fricción cero es el punto. Rate-limit
  para no exponer un hueco de costo.
- **Nombre de trabajo "atelier"**: matchea "atelier de soluciones". Sujeto a confirmación de Josse.
