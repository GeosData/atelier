# Calculadora de retención en la fuente por pagos 2026
> Calcula cuánta retención en la fuente hay que practicar al pagarle a un proveedor.

**Para quién:** negocios que le pagan a proveedores y no siempre tienen claro si toca retener.
**ROI:** 💰 evita omitir una retención obligatoria o retener de más por concepto mal identificado.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-retencion-pagos-2026/

## Qué hace
Pide el concepto del pago (compra de bienes, servicios generales, honorarios y comisiones, arrendamiento de inmueble o de bien mueble), el valor antes de IVA y si el proveedor declara renta o es persona jurídica, y calcula la retención aplicando la base mínima y la tarifa vigente de cada concepto.

## Entrada → Salida
Entrada: concepto del pago, valor del pago antes de IVA (COP), si el proveedor declara renta o es persona jurídica.

Calcula: verifica si el pago supera la base mínima UVT del concepto y, si aplica, retención = valor del pago × tarifa del concepto (con tarifa distinta según si el proveedor declara renta o no, cuando aplica).

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro, con bases mínimas y tarifas por concepto hardcodeadas.
