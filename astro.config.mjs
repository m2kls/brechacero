import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// CAMBIA ESTO por tu dominio real cuando lo tengas (también en src/config.ts)
export default defineConfig({
  site: 'https://brechacero.pages.dev',
  integrations: [sitemap()],
  build: { inlineStylesheets: 'auto' },
});
