# Generador de cotización
> Arma una cotización profesional en minutos y la descarga en PDF, sin registro.

**Para quién:** negocios e independientes que hoy cotizan en Word o WhatsApp sin un formato fijo.
**ROI:** ⏱️ ahorra armar el documento desde cero cada vez que hay que cotizar.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/generador-de-cotizacion/

## Qué hace
Pide datos del negocio, del cliente y una lista de ítems (descripción, cantidad, valor unitario). Arma el documento con subtotal, IVA opcional (19%) y total, vigencia y notas, y lo deja listo para descargar/imprimir como PDF vía el diálogo de impresión del navegador.

## Entrada → Salida
Entrada: nombre/contacto/NIT del negocio, nombre del cliente, número de cotización, ítems (descripción, cantidad, valor unitario), si suma IVA, días de vigencia, notas opcionales.

Calcula: total por ítem (`cantidad × valor unitario`), subtotal, IVA si aplica, total, y arma el documento imprimible con esos datos.

## Cómo está hecho
Client-side, cero backend: arma el documento en el DOM y usa `window.print()` para exportar a PDF; no se guarda ni se envía ningún dato.
