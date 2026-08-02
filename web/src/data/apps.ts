// Product showcase data — vitrinas /apps/<slug>
// Source of truth: vault Proyectos/Geosdata/productos/*/README.md
//
// Resend Audience strategy B (2026-05-25): single audience `geosdata-global`.
// Free plan cap 3 audiences — segmentación per-producto via Neon newsletter-db `subscribers.product` field.
// Form submit → POST https://newsletter.geosdata.com/subscribers (api-newsletter Cloud Run dual-write).
// Broadcasts targeted: api-newsletter pulls emails by product from Neon → Resend send API recipient list.
// Upgrade Resend Pro $20/mes → migrar a audience per producto (trigger = primer pago Pagao).

export interface AppPricing {
  name: string;
  price: string;
  features: string[];
  highlight?: boolean;
}

export interface AppShowcase {
  slug: string;
  name: string;
  emoji: string;
  tagline: string;
  description: string;
  status: string;
  buyer: string;
  pains: string[];
  features: { icon: string; title: string; description: string }[];
  pricing: AppPricing[];
  waitlistUuid: string;
  waitlistTitle: string;
  waitlistDescription: string;
  techStack: string[];
  accent: string; // hex
  notTarget?: string[];
  liveUrl?: string;
  liveLabel?: string;
  toolUrl?: string;
  toolLabel?: string;
}

export const apps: Record<string, AppShowcase> = {
  pagao: {
    slug: "pagao",
    name: "Pagao",
    emoji: "💸",
    tagline: "Cobranza en ruta para PYMES LATAM",
    description:
      "SaaS de cobranza para pequeñas empresas con 1-3 cobradores en ruta. El cobrador registra pagos en Android offline-first; el administrador ve todo sincronizado en el dashboard web. Sin SAP, sin contratos largos, sin compliance enterprise.",
    status: "Closed beta — abierta lista de espera",
    buyer:
      "PYMES LATAM con 1-3 cobradores en ruta que hoy usan Excel, papel o WhatsApp. Pagadiarios formales, distribuidores consumo masivo, ISP barriales, ventas por catálogo, distribuidores agro.",
    pains: [
      "Cobrador anota en papel y al final del día se transcribe — pérdida de pagos y errores",
      "Admin no sabe en tiempo real cuánto se cobró ni dónde está cada cobrador",
      "Cliente queda con saldo y nadie lo recuerda hasta que reclama",
    ],
    features: [
      {
        icon: "📱",
        title: "App cobrador offline-first",
        description: "Funciona sin internet. Sincroniza al volver a cobertura.",
      },
      {
        icon: "📊",
        title: "Dashboard admin en vivo",
        description: "Ve pagos, saldos y rutas en tiempo real desde la web.",
      },
      {
        icon: "🔔",
        title: "Recordatorios automáticos",
        description: "Email + WhatsApp al cliente cuando hay cuotas vencidas.",
      },
      {
        icon: "🏢",
        title: "Multi-tenant",
        description: "Cada empresa tiene su propio espacio aislado.",
      },
    ],
    pricing: [
      {
        name: "Plan Único",
        price: "30.000 COP / mes",
        highlight: true,
        features: [
          "Hasta 3 cobradores",
          "Clientes ilimitados",
          "Pago vía Nequi",
          "Soporte por bugs",
          "Mes a mes, sin contrato",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Únete a la beta cerrada",
    waitlistDescription:
      "Te avisamos cuando abramos cupos para nuevas empresas. Sin spam, solo el aviso.",
    techStack: ["FastAPI", "Kotlin + Jetpack Compose", "Next.js", "PostgreSQL", "Multi-tenant"],
    accent: "#1d4ed8",
    notTarget: [
      "Empresas con más de 5 cobradores (necesitan jerarquía)",
      "Quien necesita facturación electrónica DIAN integrada",
      "Integración contable con SAP / Siigo / Alegra / World Office",
      "Cooperativas vigiladas SuperSolidaria",
      "Bancos y fintechs reguladas",
    ],
  },

  lugantes: {
    slug: "lugantes",
    name: "Lugantes",
    emoji: "🏛️",
    tagline: "Lugares antes — historia LATAM en tu bolsillo",
    description:
      "Guía cultural geo-localizada de ciudades intermedias LATAM. Cada lugar tiene reconstrucción artística IA del pasado, foto del presente, narración en audio y mapa. Curaduría humana, no Wikipedia. Empieza por Montería, Cartagena, Cali.",
    status: "Pre-lanzamiento — próximamente en Google Play",
    buyer:
      "Turista cultural LATAM y residente curioso de ciudades intermedias (Montería, Cartagena, Cali, Medellín). 25-55 años. Disfruta caminar el centro histórico con contexto, prefiere experiencia auditiva manos libres mientras camina.",
    pains: [
      "Wikipedia/Google Maps no cuentan historia local de plazas e iglesias en ciudades intermedias",
      "Guías turísticas en papel solo cubren capitales mundiales — Montería, Sincelejo, Manizales quedan invisibles",
      "Tours guiados presenciales caros y con horario fijo — el turista quiere autonomía",
    ],
    features: [
      { icon: "🏛️", title: "Reconstrucciones IA", description: "Cómo se veía el lugar hace 50, 100 o 200 años." },
      { icon: "🎧", title: "Narración audio", description: "Relato corto en español neutro LATAM, manos libres mientras caminas." },
      { icon: "🗺️", title: "Mapa interactivo", description: "Lugares cercanos + ruta sugerida para visita a pie." },
      { icon: "📖", title: "Relatos curados", description: "Historias humanas verificadas, no auto-generadas." },
      { icon: "📡", title: "Funciona offline", description: "Descarga ciudad completa. Sin datos en zonas sin señal." },
    ],
    pricing: [
      {
        name: "Free (con anuncios)",
        price: "$0",
        highlight: true,
        features: ["Acceso completo a todas las ciudades disponibles", "Reconstrucciones IA + audio + mapa", "Anuncios discretos"],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Aviso de lanzamiento Lugantes",
    waitlistDescription:
      "Te avisamos cuando esté disponible en Google Play y cuando agreguemos tu ciudad.",
    techStack: ["Kotlin + Jetpack Compose", "FastAPI", "PostgreSQL", "Cloudflare R2", "Minimax TTS", "OpenStreetMap"],
    accent: "#d97706",
  },

  smartshop: {
    slug: "smartshop",
    name: "SmartShop",
    emoji: "🏪",
    tagline: "Inventario y ventas para tiendas de barrio",
    description:
      "Backend de inventario, ventas y alertas WhatsApp para micronegocios LATAM. Pensado para el dueño de tienda que hoy lleva todo en cuaderno o un Excel desordenado. Pricing LATAM, no POS internacional caro.",
    status: "En desarrollo activo — abierta lista de espera",
    buyer:
      "Don Carlos: comerciante chico LATAM (tienda de barrio, abastos, ferretería pequeña, papelería). 30-55 años. Maneja inventario en cuaderno o Excel. Pierde stock por desorden, no sabe qué reponer.",
    pains: [
      "Inventario sin tracking — pierde productos, sobrestock o stockout",
      "Al cierre del día no sabe cuánto vendió ni qué",
      "Descubre que se quebró un producto cuando un cliente lo pide",
    ],
    features: [
      {
        icon: "📦",
        title: "Inventario en tiempo real",
        description: "Cada venta descuenta stock automático. Sin cuaderno paralelo.",
      },
      {
        icon: "💬",
        title: "Alertas WhatsApp",
        description: "Te avisa por WhatsApp cuando un producto baja del mínimo.",
      },
      {
        icon: "📈",
        title: "Forecasting de demanda",
        description: "Sugiere qué reponer según tu histórico de ventas.",
      },
      {
        icon: "🏪",
        title: "Multi-tenant",
        description: "Funciona para una tienda o varias bajo un solo backend.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "$0",
        features: [
          "1 tienda",
          "50 productos",
          "100 ventas / mes",
          "Sin alertas WhatsApp",
        ],
      },
      {
        name: "Pro",
        price: "30.000 - 50.000 COP / mes",
        highlight: true,
        features: [
          "Tienda ilimitadas",
          "Productos y ventas ilimitadas",
          "Alertas WhatsApp",
          "Forecasting demanda",
          "Soporte priority",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Únete a la lista de espera",
    waitlistDescription:
      "Te avisamos al lanzar y abrir cupos beta. Acceso temprano sin costo durante la beta.",
    techStack: ["FastAPI", "Next.js", "PostgreSQL", "Redis", "WhatsApp Business API"],
    accent: "#6d28d9",
  },

  mikit: {
    slug: "mikit",
    name: "MiKit",
    emoji: "📦",
    tagline: "El asistente de la vendedora por catálogo",
    description:
      "App para vendedoras por catálogo en LATAM (Avon, Yanbal, Natura, Tupperware). Reemplaza el cuaderno + WhatsApp + Excel con catálogo, clientes, pedidos y comisiones automáticas en un solo lugar.",
    status: "Roadmap-only — disponible tras validar Pagao",
    buyer:
      "Vendedora por catálogo independiente LATAM. Mujer 30-55 años. 5-50 clientes recurrentes. Vende 1-3 marcas a la vez. Hoy gestiona todo en cuaderno + WhatsApp + Excel mal hecho.",
    pains: [
      "El catálogo cambia cada 3 semanas y se vuelve un PDF pesado en WhatsApp",
      "Pedidos en cuaderno — olvida cantidades, errores en la entrega",
      "Comisiones a mano por cada marca — pierde dinero por errores de cálculo",
    ],
    features: [
      {
        icon: "📚",
        title: "Multi-marca real",
        description: "Avon + Yanbal + Tupperware en una sola vista. No tres apps abiertas.",
      },
      {
        icon: "💬",
        title: "Compartir pedido WhatsApp",
        description: "Un toque envía el pedido formateado al cliente.",
      },
      {
        icon: "🧮",
        title: "Comisiones automáticas",
        description: "Cálculo según campaña activa de cada marca, sin Excel.",
      },
      {
        icon: "📶",
        title: "Offline-first",
        description: "Trabaja en bus, mercado, sin Wi-Fi. Sincroniza después.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "$0",
        features: ["20 clientes max", "1 marca", "Comisiones básicas"],
      },
      {
        name: "Pro",
        price: "19.000 COP / mes",
        highlight: true,
        features: [
          "Clientes ilimitados",
          "Multi-marca",
          "Comisiones avanzadas",
          "Recordatorios cumpleaños",
          "Reportes mensuales",
        ],
      },
      {
        name: "Pro Anual",
        price: "190.000 COP / año",
        features: ["Todo lo Pro", "Ahorras 2 meses"],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Lista de espera MiKit",
    waitlistDescription:
      "Construcción real arranca después de Pagao Fase 2 (~jul-ago 2026). Te avisamos para acceso temprano.",
    techStack: ["Kotlin + Jetpack Compose", "FastAPI", "Firebase Auth", "Cloudflare R2", "Multi-tenant"],
    accent: "#be185d",
  },

  esfinge: {
    slug: "esfinge",
    name: "Esfinge",
    emoji: "🗳️",
    tagline: "Votaciones escolares sin papel ni Excel",
    description:
      "Plataforma multi-institución para gestionar votaciones escolares en LATAM. Personero, contralor, representante de curso. Auditable, multi-tenant, y gratis para escuelas. Tercera iteración del dominio — autoridad real.",
    status: "Pro-bono — abierta lista de espera para escuelas",
    buyer:
      "Rector o coordinador académico de institución educativa LATAM (Colombia primario). Públicos + privados pequeños-medianos (50-2000 estudiantes). Sin equipo IT dedicado. Anualmente organiza votaciones de personero, contralor y representantes.",
    pains: [
      "Votaciones en papel — costo, tiempo y errores de conteo",
      "Personero anual obligatorio (Colombia) exige proceso democrático verificable",
      "Resultados deben ser auditables ante autoridades educativas",
    ],
    features: [
      {
        icon: "🏫",
        title: "Multi-institución",
        description: "Cada colegio configura su propio espacio y roles.",
      },
      {
        icon: "🎓",
        title: "Niveles de votación",
        description: "Diferentes grados votan diferentes candidatos (general + por curso).",
      },
      {
        icon: "🔒",
        title: "Resultados auditables",
        description: "Trazabilidad completa para autoridades educativas.",
      },
      {
        icon: "🆓",
        title: "Pro-bono inicial",
        description: "Cero barrera de entrada para escuelas LATAM.",
      },
    ],
    pricing: [
      {
        name: "Free perpetuo",
        price: "$0",
        highlight: true,
        features: [
          "Escuelas <500 estudiantes",
          "Sin límite de votaciones / año",
          "Auditoría completa",
          "Soporte por email",
        ],
      },
      {
        name: "Pro",
        price: "30.000 - 80.000 COP / año",
        features: [
          "Escuelas grandes",
          "SSO institucional",
          "URL con marca propia",
          "Soporte prioritario",
        ],
      },
      {
        name: "Enterprise",
        price: "150.000 - 400.000 COP / año",
        features: [
          "Cadenas multi-sede",
          "Onboarding dedicado",
          "SLA",
          "Customizaciones",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Lista de espera escuelas",
    waitlistDescription:
      "Te avisamos cuando abramos beta para nuevas instituciones. Cupo limitado para soporte de calidad.",
    techStack: ["Multi-tenant", "Auditoría completa", "Roles institucionales"],
    accent: "#b45309",
  },

  "generador-horarios": {
    slug: "generador-horarios",
    name: "Generador de Horarios",
    emoji: "📅",
    tagline: "Optimizador de horarios académicos K-12",
    description:
      "Asigna profesores → grupos → aulas → bloques sin colisiones. Importa Excel docentes, exporta PDF + WhatsApp. Pensado para instituciones LATAM con jornada única + extendida (ley 115 Colombia). Constraint solver Python real, no fuerza bruta Excel.",
    status: "F0 idea — abierta lista de espera",
    buyer:
      "Coordinador académico K-12 LATAM. Colombia + LATAM amplio. Públicos + privados pequeños-medianos (50-2000 estudiantes). Hoy arma horarios manualmente en Excel: 1-2 semanas al inicio de año + ajustes constantes.",
    pains: [
      "Excel manual 1-2 semanas al inicio de año, sin garantía de cero colisiones",
      "Cambio de profesor a mitad de año = re-armar el horario manual",
      "Aulas compartidas (laboratorios, auditorios, canchas) generan conflictos invisibles",
    ],
    features: [
      {
        icon: "🧠",
        title: "Optimizador real",
        description: "Constraint solver con OR-tools. No fuerza bruta Excel.",
      },
      {
        icon: "📥",
        title: "Importa Excel",
        description: "Docentes y grupos en minutos, sin re-tipear.",
      },
      {
        icon: "🇨🇴",
        title: "Contexto LATAM",
        description: "Jornada única + extendida ley 115 Colombia + adaptable LATAM regional.",
      },
      {
        icon: "📤",
        title: "Export PDF + WhatsApp",
        description: "Distribuye horarios a profesores en un toque.",
      },
    ],
    pricing: [
      {
        name: "Free trial",
        price: "$0",
        features: ["1 horario completo gratis", "Validar antes de pagar"],
      },
      {
        name: "Pro institución pequeña",
        price: "30.000 - 80.000 COP / año",
        highlight: true,
        features: [
          "Horarios ilimitados",
          "Multi-jornada",
          "Soporte WhatsApp",
        ],
      },
      {
        name: "Pro mediana",
        price: "80.000 - 200.000 COP / año",
        features: ["Todo lo anterior", "Más estudiantes y profesores"],
      },
      {
        name: "Enterprise multi-sede",
        price: "150.000 - 400.000 COP / año",
        features: ["Cadenas educativas", "Multi-sede", "SLA", "Onboarding dedicado"],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Tu primer horario gratis",
    waitlistDescription:
      "Únete a la lista. Cuando lancemos beta tendrás el primer horario completo gratis para validar antes de pagar.",
    techStack: ["FastAPI", "Google OR-tools", "Next.js", "PostgreSQL"],
    accent: "#047857",
  },

  talentmatch: {
    slug: "talentmatch",
    name: "TalentMatch",
    emoji: "🎯",
    tagline: "Match dev LATAM ↔ empresas remotas",
    description:
      "Plataforma de matching entre developers LATAM y empresas US/EU contratando remoto. Verificación de inglés real con videos asíncronos, skills demostrables vía demos públicos y código verificable, pricing alineado con cliente — pago al placement, sin subscription engañoso.",
    status: "F1 — vitrina de validación. Build post-Pagao Q3 2026.",
    buyer:
      "Startups US/EU early-stage (10-50 empleados) contratando developer senior LATAM remoto. Stack Python, Node, Go. Hoy filtran 50-100 aplicantes por posición y 80% no califica.",
    pains: [
      "Verificar inglés hablado real (no claims tipo Duolingo) — necesitan video asíncrono demostrable, no quiz escrito",
      "Timezone overlap mayor a 4 horas con core hours del equipo, sin compromiso a medianoche",
      "Skill verificable importa más que CV claim — buscan demo deploy real, GitHub activo últimos 90 días, no tutorials",
    ],
    features: [
      {
        icon: "🌎",
        title: "Dataset LATAM curado",
        description:
          "Solo developers LATAM activos y verificados. Sin bases de datos globales con ruido.",
      },
      {
        icon: "🎤",
        title: "Verificación de inglés asíncrona",
        description:
          "Video corto respondiendo preguntas técnicas habladas. Verificable, no auto-claim.",
      },
      {
        icon: "🔓",
        title: "Verification challenges abiertos",
        description:
          "Cada perfil incluye link a demo deploy real y GitHub activo. Todo público y auditable.",
      },
      {
        icon: "💰",
        title: "Performance pricing",
        description:
          "Pago al placement (15% del salario del primer año). Sin subscription mensual engañoso si no contratas.",
      },
      {
        icon: "🤝",
        title: "Sin intermediario",
        description:
          "El developer firma contrato directo con la empresa. La plataforma facilita el match, no se interpone.",
      },
      {
        icon: "🧠",
        title: "Hybrid ranking",
        description:
          "Búsqueda semántica con embeddings vectoriales y BM25. Match dimensional por skill, no keyword Boolean.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "USD 0 / mes",
        features: [
          "3 búsquedas por mes",
          "Perfiles top 50%",
          "Sin tarjeta",
          "Para validar antes de pagar",
        ],
      },
      {
        name: "Pro",
        price: "USD 200 / mes",
        highlight: true,
        features: [
          "Búsquedas ilimitadas",
          "Perfiles top 25% verificados",
          "Preview de inglés directo",
          "Más 15% placement fee al contratar",
        ],
      },
      {
        name: "Pro+",
        price: "USD 500 / mes",
        features: [
          "Acceso prioritario al top 10%",
          "Intro directa al developer",
          "Sin placement fee si contratas en menos de 60 días",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Lista empresas — acceso anticipado al beta",
    waitlistDescription:
      "Lanzamos cuando Pagao Fase 2 valide. Las primeras 10 empresas reciben Pro 6 meses gratis y placement fee reducido para el primer hire.",
    techStack: ["FastAPI", "PostgreSQL + pgvector", "Next.js", "Stripe Connect"],
    accent: "#0369a1",
    notTarget: [
      "Empresas LATAM contratando localmente — no es nuestro foco",
      "Junior developers con menos de 2 años de experiencia — wedge mid-senior con inglés B2+",
      "Reclutamiento masivo donde cantidad pesa más que calidad",
    ],
  },

  conciliaya: {
    slug: "conciliaya",
    name: "ConciliaYa",
    emoji: "🏦",
    tagline: "Conciliación bancaria automática para contadores Colombia",
    description:
      "Sube el extracto de cualquier banco colombiano (Bancolombia, Davivienda, BBVA, Banco de Bogotá) en PDF o Excel y obtén una tabla unificada lista para importar a Siigo o Alegra. Sin macros, sin copiar columnas, sin reordenar fechas. La IA detecta el formato y normaliza automáticamente.",
    status: "F0 — abierta lista de espera",
    buyer:
      "Contador público o auxiliar contable Colombia con 5-20 clientes activos. Descarga extractos bancarios mensualmente y los concilia contra registros contables en Siigo, Alegra o World Office. Hoy gasta 2-3 días al mes en este proceso manual.",
    pains: [
      "Cada banco exporta un formato distinto — Davivienda en PDF, Bancolombia en XLS con columnas distintas según tipo de cuenta",
      "Reformatear columnas manualmente antes de importar a Siigo toma 1-2 horas por cliente",
      "Errores de importación por fechas mal formateadas o GMF sin etiquetar correctamente",
    ],
    features: [
      {
        icon: "🤖",
        title: "Detección automática de formato",
        description: "Reconoce Bancolombia, Davivienda, BBVA, Banco de Bogotá sin configuración manual.",
      },
      {
        icon: "📤",
        title: "Export listo para Siigo y Alegra",
        description: "Genera el Excel con las columnas exactas que cada software espera. Cero errores de importación.",
      },
      {
        icon: "🧠",
        title: "IA para casos especiales",
        description: "Identifica GMF (4x1000), notas débito cruzadas, transacciones de fechas límite.",
      },
      {
        icon: "📁",
        title: "Multi-cliente",
        description: "Procesa extractos de todos tus clientes en una sola sesión. Historial por cliente.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "$0",
        features: [
          "1 extracto por mes",
          "Bancolombia y Davivienda",
          "Export Excel básico",
        ],
      },
      {
        name: "Pro",
        price: "79.000 COP / mes",
        highlight: true,
        features: [
          "Extractos ilimitados",
          "Todos los bancos Colombia",
          "Export formato Siigo + Alegra",
          "Historial 12 meses",
          "Soporte por WhatsApp",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Únete a la lista de espera",
    waitlistDescription:
      "Te avisamos al lanzar beta. Los primeros 20 contadores reciben 3 meses Pro gratis.",
    techStack: ["FastAPI", "LLM (Claude Haiku)", "Next.js", "PostgreSQL"],
    accent: "#0891b2",
  },

  mapeocontable: {
    slug: "mapeocontable",
    name: "MapeoContable",
    emoji: "📊",
    tagline: "Normaliza cualquier Excel de cliente a formato Siigo o Alegra",
    description:
      "Tu cliente te envía sus ventas, gastos o inventario en un Excel con columnas en cualquier orden y cualquier nombre. MapeoContable detecta qué es cada columna, la mapea al formato de importación de tu software contable y entrega el archivo listo para subir. Sin tocar una sola celda.",
    status: "F0 — abierta lista de espera",
    buyer:
      "Contador o auxiliar contable Colombia que gestiona 5-15 clientes, cada uno enviando datos en su propio formato Excel. Gasta 30-60 minutos por cliente por mes solo en reformatear antes de poder contabilizar.",
    pains: [
      "10 clientes = 10 formatos Excel distintos — sin estándar, sin acuerdo previo",
      "Siigo rechaza importaciones si alguna columna no está en el orden exacto esperado",
      "Reformatear es trabajo mecánico que no aporta valor pero no se puede delegar fácilmente",
    ],
    features: [
      {
        icon: "🔍",
        title: "Detección semántica de columnas",
        description: "La IA lee los headers del Excel del cliente y entiende qué es 'Valor Neto', 'Monto', 'Importe' — todos son lo mismo.",
      },
      {
        icon: "🗺️",
        title: "Mapeo a plantilla contable",
        description: "Elige tu software (Siigo, Alegra, World Office) y exporta con las columnas exactas que espera cada uno.",
      },
      {
        icon: "⚡",
        title: "Batch multi-cliente",
        description: "Sube los Excels de todos tus clientes de una vez. Procesa en paralelo.",
      },
      {
        icon: "💾",
        title: "Guarda reglas de mapeo",
        description: "La primera vez configuras el mapeo de cada cliente. Las siguientes veces es automático.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "$0",
        features: [
          "3 archivos por mes",
          "1 plantilla de software",
          "Sin historial",
        ],
      },
      {
        name: "Pro",
        price: "59.000 COP / mes",
        highlight: true,
        features: [
          "Archivos ilimitados",
          "Siigo + Alegra + World Office",
          "Reglas de mapeo guardadas por cliente",
          "Historial 6 meses",
          "Soporte por WhatsApp",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Únete a la lista de espera",
    waitlistDescription:
      "Te avisamos al lanzar beta. Los primeros 20 contadores reciben 3 meses Pro gratis.",
    techStack: ["FastAPI", "LLM (Claude Haiku)", "Next.js", "PostgreSQL"],
    accent: "#059669",
  },

  ondina: {
    slug: "ondina",
    name: "Ondina",
    emoji: "🐟",
    tagline: "Cuidado delegado de acuarios, por voz",
    description:
      "El dueño carga cómo se cuida cada acuario; quien queda a cargo pregunta —por voz en la app o texto en el web— y recibe la instrucción exacta, anclada a esos datos. No una hoja genérica: la respuesta correcta para ESE acuario, cuando el dueño no está.",
    status: "Beta — asistente web en vivo, app en camino",
    buyer:
      "Dueño de acuario que viaja o se ausenta y deja el cuidado en manos de alguien no experto (pareja, familiar, vecino, cuidador). Y ese cuidador, que no sabe de peces pero no quiere matarlos.",
    pains: [
      "El error que más mata peces no es el hambre: es que un cuidador bien intencionado los sobrealimente",
      "El cuidador no sabe cuánto dar, cada cuánto, ni qué revisar — y el dueño no está para responder",
      "Las instrucciones a mano se pierden, quedan incompletas o no cubren la duda del momento",
    ],
    features: [
      {
        icon: "🐟",
        title: "Base por acuario",
        description: "El dueño carga peces, alimentación, cuidados y qué hacer ante problemas.",
      },
      {
        icon: "🎙️",
        title: "Pregunta por voz",
        description: "El cuidador aprieta un botón y pregunta en voz alta; la app le lee la respuesta.",
      },
      {
        icon: "🎯",
        title: "Respuesta anclada",
        description: "Contesta solo con los datos de ese dueño, no con teoría genérica de internet.",
      },
      {
        icon: "👥",
        title: "Acceso delegado",
        description: "El dueño le da acceso por correo a quien quiera, y se lo quita cuando termina.",
      },
    ],
    pricing: [
      {
        name: "Free",
        price: "$0",
        highlight: true,
        features: [
          "Carga tus acuarios y peces",
          "Preguntas por voz y texto",
          "Acceso para cuidadores",
          "Hoja de cuidado imprimible",
        ],
      },
    ],
    waitlistUuid: "72781dff-d178-441b-988a-e3857b540ee2",
    waitlistTitle: "Aviso de lanzamiento Ondina",
    waitlistDescription:
      "Te avisamos cuando esté lista la app de voz y cuando abramos cupos. Sin spam, solo el aviso.",
    techStack: ["FastAPI", "Kotlin", "Cloudflare Pages", "Neon", "Better Auth", "LLM provider-agnóstico"],
    accent: "#12a594",
    liveUrl: "https://ondina.geosdata.com",
    liveLabel: "Probar el asistente",
    toolUrl: "https://ondina.geosdata.com/kit",
    toolLabel: "Hoja de cuidado gratis",
    notTarget: [
      "Acuaristas expertos que quieren un log técnico de parámetros (esto es para delegar, no para medir)",
      "Tiendas o criaderos con gestión de inventario de peces",
    ],
  },
};

export const appSlugs = Object.keys(apps);
