# Clasificador de residuos por foto
> Le toma una foto a un residuo y dice en qué caneca va y cómo prepararlo.

**Para quién:** hogares y negocios en Colombia que no tienen claro el estándar de las 3 canecas.
**ROI:** ⏱️ evita dudar o buscar en internet cada vez que sale un residuo distinto de lo común.
**Motor:** IA (Gemini vision)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/clasificador-de-residuos/

## Qué hace
Recibe una foto de un residuo doméstico o de negocio y lo clasifica según el estándar colombiano de tres canecas (blanco = reciclable, verde = orgánico, negro = no aprovechable; más categoría peligroso para residuos que lo requieren). Da instrucciones cortas de preparación antes de botarlo. Si la foto es ambigua, baja la confianza y lo explica.

## Entrada → Salida
Input: imagen (jpeg/png/webp).

Output (JSON):
| Campo | Descripción |
|---|---|
| `item` | Qué parece ser el objeto |
| `category` | reciclable / organico / no_aprovechable / peligroso |
| `bin_color` | Blanco, verde o negro según el estándar colombiano |
| `instructions` | Cómo prepararlo antes de botarlo |
| `confidence` | Certeza de la clasificación (0-1) |
| `notes` | Se llena cuando la imagen no es clara |

## Cómo está hecho
Config de 1 archivo (`waste.py`) sobre el motor común: schema Pydantic + prompt contextualizado a la norma colombiana de 3 canecas, forzado como structured output por Gemini vision.
