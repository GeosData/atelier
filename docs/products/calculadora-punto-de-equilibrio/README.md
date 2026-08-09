# Calculadora de punto de equilibrio
> Calcula cuánto hay que vender para dejar de perder y empezar a ganar.

**Para quién:** dueños de negocio con un producto o servicio principal que quieren saber su meta mínima de ventas.
**ROI:** 📈 fija la meta de ventas real para no operar en pérdida sin saberlo.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-punto-de-equilibrio/

## Qué hace
Pide los costos fijos del mes, el precio de venta por unidad y el costo variable por unidad. Devuelve el punto de equilibrio en unidades y en pesos, y avisa si el precio no alcanza a cubrir el costo por unidad (no hay punto de equilibrio posible).

## Entrada → Salida
Entrada: costos fijos del mes (COP), precio de venta por unidad (COP), costo por unidad (COP).

Calcula: margen de contribución (`precio − costo por unidad`), unidades para no perder (`costos fijos ÷ margen de contribución`) y esas unidades convertidas a pesos.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro.
