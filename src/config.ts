// ===============================================
//  AJUSTES DEL SITIO: edita solo este archivo
// ===============================================
export const SITE = {
  name: 'Brecha Cero',                       // Nombre provisional
  tagline: 'Ciberseguridad y hacking ético, explicado claro',
  url: 'https://brechacero.pages.dev',          // Tu dominio (también en astro.config.mjs)
  description:
    'Noticias, análisis y guías de ciberseguridad, hacking ético, Linux y privacidad en español. Divulgación con enfoque defensivo.',
  lang: 'es',
  // Datos del titular para el aviso legal (OBLIGATORIO rellenar antes de publicar)
  owner: {
    name: '[TU NOMBRE COMPLETO]',
    nif: '[TU NIF/DNI]',
    address: '[TU DIRECCIÓN O LOCALIDAD]',
    email: 'contacto@brechacero.es',
  },
  social: {
    x: '',        // p.ej. https://x.com/brechacero
    youtube: '',
    github: '',
  },
};

// Google AdSense. Con solo el client activo funcionan los "anuncios automáticos"
// (se activan en AdSense > Anuncios). Los slots son opcionales: si creas bloques
// manuales en AdSense, pega aquí su ID numérico y aparecerán en esos huecos.
export const ADSENSE = {
  client: 'ca-pub-9276111079167887',
  slots: {
    header: '',             // ID de bloque de anuncio (números) para cabecera
    inArticle: '',          // dentro del artículo
    sidebar: '',            // barra lateral
    footer: '',             // pie de la portada
  },
};

// Google Analytics 4 (opcional). Ej: 'G-XXXXXXXXXX'
export const ANALYTICS_ID = '';

export const CATEGORIES = [
  { slug: 'noticias', name: 'Noticias', description: 'Lo último en ciberseguridad: brechas, ataques, parches y la industria.' },
  { slug: 'vulnerabilidades', name: 'Vulnerabilidades', description: 'CVEs explicadas: qué afectan, por qué importan y cómo protegerte.' },
  { slug: 'guias', name: 'Guías', description: 'Tutoriales para proteger tus equipos, redes y cuentas paso a paso.' },
  { slug: 'ctf-formacion', name: 'CTF y formación', description: 'Cómo aprender hacking ético de forma legal: plataformas, certificaciones y retos.' },
  { slug: 'linux', name: 'Linux', description: 'Sistemas, terminal y herramientas para quien quiere dominar Linux.' },
  { slug: 'privacidad', name: 'Privacidad', description: 'Protege tus datos: navegadores, VPN, contraseñas y derechos digitales.' },
] as const;

export type CategorySlug = (typeof CATEGORIES)[number]['slug'];
export const categoryName = (slug: string) =>
  CATEGORIES.find((c) => c.slug === slug)?.name ?? slug;
