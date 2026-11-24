import { getCollection, type CollectionEntry } from 'astro:content';
export type Post = CollectionEntry<'articulos'>;

// Artículos publicados: ni borradores ni con fecha futura (se publican solos al reconstruir la web)
export async function getPosts(): Promise<Post[]> {
  const now = new Date();
  const posts = await getCollection('articulos', ({ data }) => !data.draft && data.date <= now);
  return posts.sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());
}
export const cover = (p: Post) => p.data.image ?? `/img/covers/${p.id}.jpg`;
export const shortDate = (d: Date) => d.toLocaleDateString('es-ES', { day: 'numeric', month: 'short' }).replace('.', '');
export const longDate = (d: Date) => d.toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' });
export const readingTime = (p: Post) => Math.max(2, Math.round((p.body ?? '').split(/\s+/).length / 230));
export const initials = (name: string) => name.split(/\s+/).map((w) => w[0]).slice(0, 2).join('').toUpperCase();
