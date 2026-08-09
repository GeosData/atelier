# Calculadora de incremento de arriendo 2026
> Calcula cuánto le pueden subir legalmente el arriendo a alguien en 2026 y si la propuesta se pasa de ley.

**Para quién:** arrendatarios y arrendadores que quieren verificar si un aumento de canon es legal.
**ROI:** 📈 da el tope legal exacto para negociar o defender la renovación del contrato.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-incremento-arriendo-2026/

## Qué hace
Pide el canon actual y, opcionalmente, el valor nuevo que proponen. Calcula el aumento máximo legal para 2026 según el IPC del año anterior (5,1%, tope fijado por la Ley 820 de 2003) y, si se ingresa el valor propuesto, indica si se pasa del límite legal.

## Entrada → Salida
Entrada: canon actual (COP), valor nuevo propuesto (opcional, para verificar legalidad).

Calcula: canon máximo legal = canon actual × (1 + 5,1%); si se ingresa un valor propuesto, lo compara contra ese máximo y señala si excede el tope.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro, con el IPC 2026 hardcodeado.
