# Calculadora de recargos nocturnos, dominicales y festivos 2026
> Calcula cuánto se paga de más por turnos nocturnos, dominicales y festivos con los porcentajes vigentes.

**Para quién:** negocios que abren de noche, domingos o festivos y liquidan recargos a mano en Excel.
**ROI:** 💰 evita pagar de menos (riesgo laboral) o de más por error de cálculo.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-recargos-2026/

## Qué hace
Pide el salario mensual del empleado y el periodo aplicable (antes o después de julio de 2026, cuando cambia el porcentaje de recargo dominical/festivo por la reforma laboral, Ley 2466 de 2025), y calcula el recargo real según las horas trabajadas en cada franja.

## Entrada → Salida
Entrada: salario mensual (COP), periodo (enero-junio 2026 con dominical/festivo al 80%, o desde julio 2026 al 90%), horas trabajadas en cada franja (nocturno, dominical/festivo).

Calcula: valor hora ordinaria = salario ÷ 240. Recargo nocturno 35%, recargo dominical/festivo diurno según el periodo (80% hasta junio 2026, 90% desde julio 2026) y su combinación nocturna; horas extra diurnas +25%, extra nocturnas +75%, sobre el valor hora.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro, con los porcentajes de la reforma laboral 2026 hardcodeados.
