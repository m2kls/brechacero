import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const articulos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articulos' }),
  schema: z.object({
    title: z.string().max(110),
    description: z.string().max(170),
    date: z.coerce.date(),
    updated: z.coerce.date().optional(),
    category: z.enum(['noticias', 'vulnerabilidades', 'guias', 'ctf-formacion', 'linux', 'privacidad']),
    tags: z.array(z.string()).default([]),
    author: z.string().default('Redacción'),
    image: z.string().optional(),       // ruta en /public, p.ej. /img/mi-foto.webp
    imageAlt: z.string().optional(),
    imageCredit: z.string().optional(),   // p.ej. 'Foto: Ana López / Unsplash'
    video: z.string().optional(),         // ID de YouTube, p.ej. 'uhzV5-iFb5E'
    videoTitle: z.string().optional(),
    videoSource: z.string().optional(),   // canal, p.ej. 'INCIBE'
    featured: z.boolean().default(false),
    draft: z.boolean().default(false),
  }),
});

export const collections = { articulos };
