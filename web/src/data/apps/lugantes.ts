export interface LugantesConfig {
  name: string;
  tagline: string;
  description: string;
  longDescription: string;
  packageId: string;
  domain: string;
  primaryColor: string;
  accentColor: string;
  iconLetter: string;
  features: Array<{ icon: string; title: string; description: string }>;
  playStoreUrl: string;
  playStoreReady: boolean;
  contactEmail: string;
  privacyEffectiveDate: string;
  thirdParties: string[];
  dataCollected: Array<{ type: string; purpose: string; optional: boolean }>;
  publisher: string;
  publisherUrl: string;
}

export const config: LugantesConfig = {
  name: 'Lugantes',
  tagline: 'Lugares antes — historia LATAM en tu bolsillo',
  description:
    'Reconstrucciones IA + relatos curados de plazas, iglesias y rincones históricos de ciudades intermedias LATAM.',
  longDescription:
    'Lugantes es una guía cultural geo-localizada. Cada lugar tiene reconstrucción artística IA del pasado, foto del presente, narración en audio y mapa. Curaduría humana, no Wikipedia.',
  packageId: 'com.geosdata.lugantes',
  domain: 'geosdata.com/apps/lugantes',
  primaryColor: '#d97706',
  accentColor: '#fbbf24',
  iconLetter: 'L',
  features: [
    { icon: '🏛️', title: 'Reconstrucciones IA', description: 'Cómo se veía el lugar hace 50, 100 o 200 años. Generado con IA + referencias históricas.' },
    { icon: '🎧', title: 'Narración audio', description: 'Relato corto del lugar contado en español neutro LATAM. Manos libres, mientras caminas.' },
    { icon: '🗺️', title: 'Mapa interactivo', description: 'Encuentra lugares cercanos. Ruta sugerida para visita a pie.' },
    { icon: '📖', title: 'Relatos curados', description: 'Historias humanas verificadas, no auto-generadas. Equipo curatorial revisa cada lugar.' },
    { icon: '🌎', title: 'Ciudades intermedias LATAM', description: 'Foco en ciudades que no aparecen en guías globales. Empieza por Montería, Cartagena, Cali.' },
    { icon: '📡', title: 'Funciona offline', description: 'Descarga ciudad completa. Sin datos en zonas sin señal.' },
  ],
  playStoreUrl: 'https://play.google.com/store/apps/details?id=com.geosdata.lugantes',
  playStoreReady: false,
  contactEmail: 'contacto@geosdata.com',
  privacyEffectiveDate: 'Mayo 2026',
  thirdParties: [
    'Firebase (Auth + Crashlytics)',
    'Google AdMob',
    'Cloudflare R2',
    'Minimax (TTS)',
    'OpenStreetMap',
  ],
  dataCollected: [
    { type: 'Identificador publicitario (AdMob ID)', purpose: 'Mostrar anuncios relevantes', optional: false },
    { type: 'Datos de fallo (Crashlytics)', purpose: 'Detectar y corregir errores', optional: false },
    { type: 'Ubicación GPS aproximada', purpose: 'Mostrar lugares cercanos', optional: true },
  ],
  publisher: 'GeosData',
  publisherUrl: 'https://geosdata.com',
};
