// Sitemap para Google News: solo artículos de las últimas 48 horas (requisito de Google).
import { getCollection } from 'astro:content';
import { SITE } from '../config';
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
export async function GET() {
  const now = new Date();
  const since = new Date(now.getTime() - 48 * 3600 * 1000);
  const posts = (await getCollection('articulos', ({ data }) => !data.draft && data.date <= now && data.date >= since))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  const items = posts.map((p) => `  <url>
    <loc>${SITE.url}/${p.id}/</loc>
    <news:news>
      <news:publication><news:name>${esc(SITE.name)}</news:name><news:language>es</news:language></news:publication>
      <news:publication_date>${p.data.date.toISOString()}</news:publication_date>
      <news:title>${esc(p.data.title)}</news:title>
    </news:news>
  </url>`).join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
${items}
</urlset>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
