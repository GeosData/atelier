# Calculadora de liquidación de contrato 2026
> Calcula cuánto corresponde de liquidación al terminar un contrato laboral en Colombia.

**Para quién:** empleadores y empleados que quieren verificar la liquidación sin hacerla a mano.
**ROI:** 💰 evita errores en cesantías, intereses, prima y vacaciones al liquidar un contrato.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-liquidacion-contrato-2026/

## Qué hace
Pide el salario mensual y las fechas de ingreso y retiro, y calcula cada concepto de la liquidación por separado: cesantías, intereses sobre cesantías, prima de servicios proporcional y vacaciones proporcionales, según el Código Sustantivo del Trabajo.

## Entrada → Salida
Entrada: salario mensual (COP), fecha de ingreso, fecha de retiro.

Calcula: días trabajados en base 360 (año comercial), sobre una base salarial que suma el auxilio de transporte si el salario no lo supera. Cesantías = base × días ÷ 360. Intereses sobre cesantías = cesantías × días × 12% ÷ 360. Prima = base × días del semestre en curso ÷ 360 (solo cuenta desde el inicio del semestre o el ingreso, lo que sea después). Vacaciones = salario (sin auxilio) × días ÷ 720.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro.
