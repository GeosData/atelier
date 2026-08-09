# Factura o recibo a datos
> Convierte la foto de una factura o recibo en datos listos para contabilidad, sin digitarlos a mano.

**Para quién:** comerciantes, freelancers y contadores que hoy pasan facturas a Excel o al software contable a mano.
**ROI:** ⏱️ ahorra los minutos de digitación por cada factura, y elimina errores de transcripción de totales.
**Motor:** IA (Gemini vision)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/factura-a-datos/

## Qué hace
Recibe una foto o PDF de una factura o recibo y extrae los campos legibles: proveedor, número de documento, fecha, moneda, subtotal, impuesto, total e ítems de línea. Si un campo no es legible lo deja vacío y lo explica en notas, en vez de inventarlo.

## Entrada → Salida
Input: imagen (jpeg/png/webp) o PDF.

Output (JSON):
| Campo | Descripción |
|---|---|
| `vendor` | Nombre del proveedor/emisor |
| `document_number` | Número de factura o recibo |
| `issued_at` | Fecha ISO si es legible |
| `currency` | Moneda mostrada en el documento |
| `subtotal`, `tax`, `total` | Montos, sin separadores de miles |
| `line_items[]` | Lista de ítems: descripción, cantidad, valor unitario, monto |
| `confidence` | Certeza global sobre los totales (0-1) |
| `notes` | Se llena cuando algo es ilegible o falta |

## Cómo está hecho
Config de 1 archivo (`receipt.py`) sobre el motor común: schema Pydantic + prompt, forzado como structured output por Gemini vision.
