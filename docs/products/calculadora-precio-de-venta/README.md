# Calculadora de precio de venta y margen de ganancia
> Calcula a cómo vender un producto para ganar lo que quieres, sin adivinar.

**Para quién:** comerciantes y emprendedores que ponen precios "a ojo".
**ROI:** 💰 evita perder plata por confundir margen con markup al fijar precios.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-precio-de-venta/

## Qué hace
Pide el costo del producto y el porcentaje de ganancia deseado, sobre el costo (markup) o sobre el precio de venta (margen), con opción de sumar IVA. Devuelve el precio de venta, la ganancia por unidad, el margen real sobre el precio y el markup real sobre el costo.

## Entrada → Salida
Entrada: costo del producto (COP), modo de ganancia (markup o margen), porcentaje de ganancia, si suma IVA (19%).

Calcula: precio de venta según el modo elegido (`costo × (1 + %)` para markup, `costo ÷ (1 − %)` para margen), ganancia por unidad, margen real, markup real y, si aplica, el precio final con IVA.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro.
