import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://geosdata.com',
  output: 'static',
  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en'],
    routing: { prefixDefaultLocale: false },
  },
  build: {
    assets: 'assets'
  },
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()]
  }
});
