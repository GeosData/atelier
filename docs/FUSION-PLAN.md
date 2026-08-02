# Plan de fusión — atelier como sistema único

> Decisión Josse (2026-08-02): fusionar todo hacia atelier. atelier = sistema y vitrina única, absorbiendo las calculadoras + vitrinas + newsletter de geosdata.com. Ejecutar incremental y reversible-first; nada destructivo sobre el geosdata.com vivo hasta el cutover verificado.

## atelier = 3 superficies

| Superficie | Qué es | Endpoint | Estado |
|---|---|---|---|
| `products/` | Tools de IA (archivo→LLM→schema) | `POST /process/{slug}` · `GET /products` | 4 vivos (receipt/exam/crop/waste) |
| `tools/` | Calculadoras deterministas (inputs→función pura→resultado) | `POST /compute/{slug}` · `GET /tools` | tipo probado, 1 portada (punto-equilibrio) |
| front/vitrina | El sitio (galería + páginas + blog + vitrinas producto) | estático/Astro | **pendiente: mover el Astro de geosdata-com** |

## Lo que hay que absorber de geosdata-com (F:\geosdata\geosdata-com, Astro)

- 8 calculadoras (`src/pages/soluciones/*.astro`): recargos, liquidación, prima, incremento-arriendo, precio-venta, punto-equilibrio, retención-salarios, retención-pagos. → mover la fórmula de cada una a `api/app/tools/<slug>.py`; la página Astro llama `/compute/{slug}`.
- Vitrinas de producto (`src/data/apps.ts`: pagao, lugantes, …) con waitlist/pricing.
- Newsletter cableado (Resend/Neon vía newsletter.geosdata.com).
- Blog, about/contact/products/projects, i18n (en/), design system (Tailwind, tokens geo-*, **Inter → revisar, es look IA-default**).

## Orden de ejecución (reversible-first)

1. **[hecho]** Motor soporta tipo determinista + `punto-equilibrio` portada (prueba e2e).
2. **Portar las 7 calculadoras restantes** a `tools/` (mecánico: fórmula → función pura + schema). Reversible, no toca geosdata.com.
3. **Decidir el front de atelier** (bifurcación pendiente): 
   - (a) **mover** el Astro de geosdata-com dentro de `atelier/web` (monorepo paraguas: `api/` + `web/`). Menos churn: se mueve, no se reconstruye. Las páginas de calculadora pasan a llamar `/compute`; las de IA a `/process`.
   - (b) reconstruir el front en atelier desde cero (más churn, oportunidad de matar el look Inter).
4. **Migrar vitrinas de producto + newsletter + blog** al front de atelier.
5. **Cutover DNS** geosdata.com → deploy de atelier (RIESGOSO, gated). Verificar en pages.dev antes.
6. **Retirar geosdata-com** (repo/deploy) solo tras cutover verificado. Nunca antes.

## Reglas de seguridad

- geosdata.com sigue sirviendo vivo hasta el paso 5 verificado.
- Nada de borrar geosdata-com hasta el paso 6.
- Cada calculadora portada se verifica contra el resultado de la página Astro original (mismos inputs → mismo output) antes de considerarla migrada.
- DNS y deploy de producción = solo con go explícito de Josse.

## Bifurcación abierta (paso 3)

Mover el Astro existente a `atelier/web` (a) vs reconstruir (b). (a) es días y conserva SEO/diseño/newsletter; (b) es semanas pero limpia el look IA-default. Recomendado: (a) ahora, y mejorar el diseño por encima después (no bloquear la fusión con un rediseño).
