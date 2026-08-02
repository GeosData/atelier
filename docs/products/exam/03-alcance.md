# 03 — Alcance

## v1 (lo que entra)
- Docente sube **foto o PDF** de un examen resuelto (una hoja / un alumno por vez).
- IA lee el examen (visión multimodal) → **califica por pregunta** + **feedback en español** por respuesta.
- **Chequeo de dominio**: marca respuestas donde la nota alta huele a poco dominio real (respuesta correcta pero inconsistente con el nivel del resto, patrón copia-IA, respuesta "de memoria" sin razonamiento). Con justificación legible, no caja negra.
- **Demo pública sin login** para probar (subí un examen de ejemplo → resultado). Login Google solo si el docente quiere guardar/historial.
- Salida clara y cómoda: vista por pregunta, nota total, y panel "en quién enfocar refuerzo".

## Fuera de v1 (backlog)
- Multi-alumno / lote (subir 30 exámenes de una).
- Banco de exámenes, generación de exámenes.
- Integración LMS (Classroom, Moodle).
- App móvil nativa.
- Rúbricas personalizadas avanzadas (v1 = rúbrica inferida + ajuste simple).

## Formatos v1
- Entrada: imagen (jpg/png) y PDF de una hoja.
- Tipos de pregunta: opción múltiple + respuesta corta/abierta (donde el mastery-check aporta más). Ensayo largo = backlog.

## Criterio de "listo v1"
Demo en vivo en dominio público, un docente sube un examen real y obtiene calificación + al menos una señal de dominio dudoso justificada, sin instrucciones. Experiencia completa, no MVP mínimo.
