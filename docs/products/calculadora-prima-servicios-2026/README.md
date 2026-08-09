# Calculadora de prima de servicios 2026
> Calcula cuánto corresponde de prima de servicios en un semestre.

**Para quién:** empleadores y empleados que quieren verificar el pago de prima de junio o diciembre.
**ROI:** 💰 evita pagar o recibir de menos por no incluir el auxilio de transporte en la base.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-prima-servicios-2026/

## Qué hace
Pide el salario mensual y los días trabajados en el semestre (hasta 180), y calcula la prima correspondiente según el Art. 306 del Código Sustantivo del Trabajo: 30 días de salario por año, 15 por semestre completo, incluyendo el auxilio de transporte en la base cuando aplica.

## Entrada → Salida
Entrada: salario mensual (COP), días trabajados en el semestre (0-180).

Calcula: prima = (salario base × días trabajados) ÷ 360.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro.
