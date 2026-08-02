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
2. **[hecho]** 7 calculadoras restantes portadas a `tools/` (fórmulas transcritas fielmente, auditadas, 8 tools VIVAS en prod `/compute` rev 00003).
3. **[hecho 3a]** Front Astro de geosdata-com COPIADO a `atelier/web` (43 rutas, build OK). Dirección elegida: (a) mover, no reconstruir. Galería estática vieja en `web/_legacy-static/`. Sitio vivo geosdata-com intacto.
4. **[hecho] Integración del front** (reversible, no tocó prod):
   - **[hecho]** 4 páginas Astro de tools de IA (`factura-a-datos`, `revisor-de-examenes`, `diagnostico-de-cultivo`, `clasificador-de-residuos`) → `POST /process/{slug}`, render formateado (exam resalta mastery_flag). Matchean el diseño de las calculadoras (Archivo + IBM Plex Mono, acento pino). Verificado visualmente en preview.
   - **[hecho]** Taller lista las 4 tools de IA (cards + filtro "IA").
   - **[DECIDIDO NO]** Rewire calculadoras → `/compute`: se quedan client-side (mejor UX: instantáneo, offline, cero costo servidor). Las 8 tools `/compute` quedan como superficie de API sin usar por la web (riesgo de drift de fórmula; decisión keep/remove pendiente, no urge).
   - Nota diseño: las calculadoras/tools NO usan Inter (usan Archivo+IBM Plex Mono); el look ya es distintivo. Inter solo en tokens globales, revisable aparte.
5. **[gated] Cutover DNS** geosdata.com → deploy Astro de atelier. Verificar en pages.dev primero. Solo con go de Josse.
6. **[gated] Retirar geosdata-com** (repo/deploy) solo tras cutover verificado.

## Conexión distribuidora → productos (plan Camino 1, gated, listo para go)

Estado 2026-08-02: geosdata.com (CF Pages `geosdata-com`, repo `F:\geosdata\geosdata-com`) NO menciona atelier — desconectado. Su taller (`Home.astro §taller`) lista cards desde `i18n/home.ts` (`cards[].href` → sus propias `/soluciones/*`). Las calculadoras existen en LOS DOS dominios = contenido duplicado; y las páginas de calculadora en atelier tienen `canonical` → geosdata.com (heredado de la copia).

**Camino 1 (recomendado, atelier dueño de las tools). Pasos concretos:**
1. **atelier**: cambiar el `canonical` de las 14 tool pages → su URL en atelier.geosdata.com (hoy apunta a geosdata.com). Redeploy atelier.
2. **geosdata-com** `i18n/home.ts`: repuntar `cards[].href` de las calculadoras → `https://atelier.geosdata.com/soluciones/<slug>/`; agregar las 4 tools IA como cards nuevas apuntando a atelier; CTA "todas las herramientas" → atelier.
3. **geosdata-com** redirects: crear `public/_redirects` con `301` de `/soluciones/* → https://atelier.geosdata.com/soluciones/:splat` (CF Pages soporta `_redirects`). Verifica que el splat mapea (los slugs son idénticos, vinieron de ahí).
4. **geosdata-com**: borrar las páginas `src/pages/soluciones/*.astro` (quedan cubiertas por el redirect). Blog/vitrinas/marketing se quedan.
5. Build + deploy geosdata-com (wrangler, proyecto `geosdata-com`). Verificar: geosdata.com/soluciones/<x> → 301 → atelier; taller linkea a atelier; geosdata.com marketing intacto.
6. Riesgo/rollback: es el sitio vivo principal. Verificar redirects en preview antes de main. Rollback = revertir `_redirects` + restaurar páginas (git).

**Camino 2 (fallback):** solo repuntar taller + CTA, sin redirect ni borrar; deja duplicado, canonical se queda en geosdata. Cero riesgo, menos limpio.

## Reglas de seguridad

- geosdata.com sigue sirviendo vivo hasta el paso 5 verificado.
- Nada de borrar geosdata-com hasta el paso 6.
- Cada calculadora portada se verifica contra el resultado de la página Astro original (mismos inputs → mismo output) antes de considerarla migrada.
- DNS y deploy de producción = solo con go explícito de Josse.

## Bifurcación abierta (paso 3)

Mover el Astro existente a `atelier/web` (a) vs reconstruir (b). (a) es días y conserva SEO/diseño/newsletter; (b) es semanas pero limpia el look IA-default. Recomendado: (a) ahora, y mejorar el diseño por encima después (no bloquear la fusión con un rediseño).
