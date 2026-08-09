# Revisor de exámenes (nombre en definición)
> Califica un examen resuelto por foto y avisa cuando la nota no refleja dominio real del tema.

**Para quién:** docentes que corrigen a mano y quieren detectar dominio inflado, no solo sumar puntos.
**ROI:** ⏱️ ahorra tiempo de corrección manual pregunta por pregunta.
**Motor:** IA (Gemini vision)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/revisor-de-examenes/

## Qué hace
Recibe la foto o PDF de un examen resuelto por un estudiante y, además de calificar cada pregunta (correcta, dificultad, puntaje, feedback en español), corre un mastery-check: detecta patrones donde una respuesta correcta o de buen puntaje probablemente no refleja comprensión real (acertó lo difícil y falló lo fácil, respuesta correcta sin desarrollo o con desarrollo contradictorio, redacción que suena memorizada). No acusa de uso de IA, describe la inconsistencia. Este mastery-check es el diferencial: ni Gradescope ni las apps de corrección en LATAM lo hacen.

## Entrada → Salida
Input: imagen o PDF.

Output (JSON):
| Campo | Descripción |
|---|---|
| `subject`, `student_name` | Metadatos si son legibles |
| `questions[]` | Por pregunta: número, enunciado, respuesta del estudiante, si es correcta, dificultad (facil/media/dificil), puntaje, puntaje máximo, feedback, `mastery_flag` + `mastery_reason` |
| `total_score`, `max_total` | Nota total |
| `mastery_alerts[]` | Alertas en español para el docente, ej. "acertó las difíciles y falló las fáciles" |
| `overall_mastery_confidence` | Qué tanto la nota refleja dominio real (0 inflada, 1 sólida) |
| `confidence` | Certeza global de la lectura (0-1) |
| `notes` | Se llena cuando el examen es ilegible |

## Cómo está hecho
Config de 1 archivo (`exam.py`) sobre el motor común: schema Pydantic + prompt con el mastery-check como instrucción explícita, forzado como structured output por Gemini vision. Nombre público todavía en definición (working `gradecheck`, candidatos `realgrade`/`gradelens`).
