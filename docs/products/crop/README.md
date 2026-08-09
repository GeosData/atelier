# Diagnóstico de cultivo por foto
> Le toma una foto a una hoja o fruto y dice qué plaga o enfermedad tiene y cómo tratarla.

**Para quién:** pequeños agricultores del Caribe/Córdoba que no tienen un agrónomo a la mano en el momento.
**ROI:** 💰 evita perder cosecha por tratar tarde o con el insumo equivocado; 📈 orienta la compra del agroinsumo correcto.
**Motor:** IA (Gemini vision)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/diagnostico-de-cultivo/

## Qué hace
Recibe una foto de una hoja, fruto o planta e identifica la plaga o enfermedad más probable (o "sano"), con una segunda hipótesis si aplica. Estima severidad y propone tratamientos concretos (orgánicos y químicos) con dosis y precauciones de seguridad. Contextualizado a plagas comunes del Caribe colombiano (sigatoka negra, moko, gusano cogollero, antracnosis, mildeo, entre otras).

## Entrada → Salida
Input: imagen (jpeg/png/webp).

Output (JSON):
| Campo | Descripción |
|---|---|
| `crop` | Cultivo identificado en la imagen, si se puede |
| `diagnosis` | Plaga o enfermedad, o "sano" |
| `also_possible` | Segunda hipótesis |
| `severity` | leve / moderado / severo |
| `treatments[]` | Lista: enfoque (orgánico/químico), acción, precaución/dosis |
| `prevention` | Recomendación de prevención |
| `confidence` | Certeza del diagnóstico (0-1) |
| `notes` | Se llena cuando la foto no es clara o se sugiere confirmar con agrónomo |

## Cómo está hecho
Config de 1 archivo (`crop.py`) sobre el motor común: schema Pydantic + prompt con contexto agronómico regional fijo, forzado como structured output por Gemini vision.
