# Calculadora de retención en la fuente por salarios 2026
> Calcula cuánta retención se descuenta de un salario, con la base real después de deducciones.

**Para quién:** empleados y áreas de nómina que quieren verificar el descuento de retención en la fuente.
**ROI:** 💰 evita sorpresas por retención mal calculada al no aplicar deducciones y renta exenta.
**Motor:** Cálculo en navegador (sin IA)
**Demo en vivo:** https://atelier.geosdata.com/soluciones/calculadora-retencion-salarios-2026/

## Qué hace
Pide el ingreso laboral gravable del mes y deducciones opcionales (dependientes económicos, intereses de vivienda, medicina prepagada), calcula la base real de retención después de aportes, deducciones y renta exenta, y aplica la tabla del Art. 383 del Estatuto Tributario con el UVT vigente ($52.374) para dar la retención del mes.

## Entrada → Salida
Entrada: ingreso laboral gravable del mes (COP), si tiene dependientes económicos (deduce 10% hasta 32 UVT), intereses de vivienda al mes (opcional, tope 100 UVT), medicina prepagada al mes (opcional, tope 16 UVT).

Calcula: descuenta aportes obligatorios a salud y pensión (8%), resta deducciones (dependientes, vivienda, salud, cada una con su tope en UVT) y renta exenta (25% de lo que queda, tope 240 UVT), con el total de deducciones + exenta limitado al 40% del ingreso ya sin aportes. La base resultante se convierte a UVT y se aplica contra la tabla progresiva del Art. 383.

## Cómo está hecho
Client-side, cero backend: toda la lógica corre en JavaScript embebido en la página Astro, con la tabla del Art. 383 y el UVT 2026 hardcodeados.
