# 00 — Necesidad

> Working name: `gradecheck` (provisional, cerrar en 02-nombres).
> Origen: análisis decks Hanademi + ranking demanda CO (2026-08-01). Ver vault `Reporting/Scouts/hanademi-decks-moat/briefing_2026-08-01.md`.

## Necesidad
El docente pierde horas calificando exámenes a mano, y —desde que existe la IA— la nota dejó de reflejar dominio real: un alumno saca buena tarea con IA y luego cae en el examen presencial. El docente no tiene forma barata de (a) corregir rápido ni (b) detectar cuándo la nota está inflada.

Evidencia:
- Demanda real CO limpia (autocomplete gl=co): "corregir examenes con ia", "mejor ia para corregir examenes", "corregir examenes rapido", "gratis". Intención de docente, directa.
- Dato del dolor de dominio (deck `ai-can-raise-scores-and-lower-mastery`, CEPR 21577, n=26.811): tareas con IA +18% en nota, exámenes mensuales −20% en dominio → la nota sube mientras el aprendizaje baja.

## HU (combo)
Como **docente**, quiero **subir un examen (foto/PDF) y que la IA lo califique con feedback por respuesta**, y **además me señale las respuestas donde la nota alta no refleja dominio real** (patrón copia-IA / inconsistencia tarea-vs-examen), para **calificar en minutos y saber en quién enfocar refuerzo**.

- Entra por la demanda alta: corregir rápido (imán).
- Se diferencia por el ángulo que nadie cubre: chequeo de dominio real (foso de producto, no me-too de corrector).

## Usuario
Docente de aula (colegio/instituto CO). No-tech. Buyer típico del taller Geosdata. Canal = inbound/pull (la vitrina lo trae; no requiere gremio previo — es producto de consumidor-educador, no B2B con canal).

## Criterios de aceptación (v1)
- Sube foto/PDF de un examen resuelto → obtiene calificación por pregunta + feedback en español.
- Marca al menos 1 señal de dominio dudoso con justificación legible (no caja negra).
- Corre en vivo en un dominio público (demo autoexplicativa, sin login para probar).
- Experiencia completa y cómoda, no MVP mínimo (login Google si hay cuenta).

## Rol en el portafolio
Vitrina-imán (submarca edu Jotive / Geosdata). No se apuesta negocio: se deja vivo como demo, mide inbound. El foso/distribución se resuelve a nivel portafolio, no aquí. Si algún docente pide "su versión" → pedido a medida = ingreso.

## Abierto (siguiente en discovery)
- 01-estado-del-arte: correctores IA existentes (qué hacen, qué NO — el mastery-check es el hueco).
- 02-nombres: `gradecheck` vs alternativas (el nombre debería insinuar dominio-real, no solo "corregir").
- 03-alcance: v1 solo imagen/PDF de examen; ¿scope de materias/formatos?
- 04-decisiones: motor (Gemini vision), stack (landing-template + api FastAPI Cloud Run), sin login para probar.
