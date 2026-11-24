import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE } from '../config';
export async function GET(context) {
  const posts = (await getCollection('articulos', ({ data }) => !data.draft && data.date <= new Date()))
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
  return rss({
    title: SITE.name, description: SITE.description, site: context.site,
    items: posts.map((p) => ({ title: p.data.title, description: p.data.description, pubDate: p.data.date, link: `/${p.id}/` })),
    customData: '<language>es-es</language>',
  });
}
