# 01 — Estado del arte

> Fuente: scout research 2026-08-01. Pregunta clave: ¿el "mastery-check" (señalar cuándo la nota no refleja dominio real) es hueco real o ya tomado?

## Correctores IA globales (EN)
| Herramienta | Qué hace | Mastery-check | Precio |
|---|---|---|---|
| Gradescope (Turnitin) | clustering de respuestas, rúbricas, manuscrito/código | no | ~$1-3/est [unverified] |
| MagicSchool AI | feedback escritura, genera rúbricas/quizzes | no | freemium |
| CoGrader | gramática/estructura + **flag texto-IA con evidencia** | no (flag IA ≠ dominio) | ~$10-20/mes, free 100/mes |
| EssayGrader | corrige ensayo 30s, detección IA/plagio | no | free 25/mes |
| Brisk Teaching | Brisk Grader en Google Docs, rúbrica | no | freemium |
| Class Companion | feedback por rúbrica + reintentos ilimitados | no (loop reintento) | gratis docentes |
| Quizizz/Wayground | autograde MCQ, skill gaps a nivel clase | no (agregado, no individual) | freemium |
| Formative (Luna AI) | smart grouping, analítica tiempo real | no (agregado) | freemium |

## Apps LATAM/español (competencia directa)
| App | Qué hace | Mastery-check | Precio |
|---|---|---|---|
| Corrigiendo.es | OCR manuscrito, criterios LOMLOE, nota+feedback 20-60s | no | free 30/mes |
| SmartGrade | 30 exámenes <5min, 95% precisión, Classroom/Moodle | no | no publicado |
| Examino | escanea con celular, ensayos/cálculos | no | free 10/mes |
| FotoExamen, Calificación IA Docentes (iOS MX) | foto→nota genérico | no [unverified] | — |

Todo el segmento ES = "foto → nota → feedback", con menos madurez que las globales.

## Detectores de texto-IA (categoría distinta)
Turnitin (falsos positivos 1-4%, hasta 18.7% en no-nativos), GPTZero (67% detección real, 23% falsos positivos). Miran la entrega aislada, no el patrón del alumno. Ruidosos. NO es mastery-check.

## Fundamento teórico (existe, nadie lo bajó a aula)
**Person-fit statistics / aberrant response patterns** en IRT (estadísticos *lz*, CUSUM): detectan cuando el examinado acierta ítems difíciles y falla los fáciles (copia/filtración/adivinanza). Se usa en exámenes estandarizados de gran escala (licencias, certificaciones), **NO en herramientas de aula para docentes**. El artículo NIU ("homework isn't proof of learning") confirma el problema pedagógico pero su solución propuesta es rediseño de curso, no software.

## VEREDICTO: hueco real 🟢
El mastery-check NO lo cubre ningún corrector de exámenes (ni 8 globales ni 5 LATAM). Lo más cerca = detección de texto-IA aislado (problema distinto, ruidoso). La teoría que lo resolvería (person-fit/IRT) vive en psicometría de alto-stakes, nadie la bajó al bolsillo del docente. **Diferencial defendible** mientras se mantenga simple y verificable ("acertó lo difícil, falló lo fácil"; "esta respuesta no calza con su trabajo previo"), no un motor psicométrico completo desde el día 1.
