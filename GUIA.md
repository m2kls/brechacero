# Brecha Cero: guía para ponerla en marcha

Web de noticias de ciberseguridad hecha con **Astro** (sitio estático). Es rápida, gratis de alojar y no necesita base de datos ni mantenimiento de servidor.

> **Suposiciones que he hecho** (cámbialas cuando quieras):
> - Nombre provisional **Brecha Cero** y dominio de ejemplo `brechacero.es` (no he comprobado si está libre).
> - Público en España (textos legales según LSSI y RGPD).
> - Los 6 artículos incluidos son de ejemplo: puedes usarlos, editarlos o borrarlos.

---

## Qué hay en la carpeta

| Carpeta / archivo | Para qué sirve |
|---|---|
| `src/config.ts` | **El único archivo que tienes que tocar**: nombre, dominio, tus datos, IDs de AdSense |
| `src/content/articulos/` | Un archivo `.md` por artículo. Aquí escribes |
| `src/pages/` | Páginas: portada, categorías, legales, contacto… |
| `public/` | Imágenes, favicon, `ads.txt`, `robots.txt` |
| `dist/` | La web ya construida, lista para subir tal cual |

Secciones: Noticias, Vulnerabilidades, Guías, CTF y formación, Linux, Privacidad.
Incluye: portada tipo revista, páginas de categoría, artículos con índice y relacionados, Sobre nosotros, Contacto, Aviso legal, Privacidad, Cookies, 404, RSS, sitemap, datos estructurados para Google (NewsArticle), modo oscuro automático y 4 huecos de anuncio (cabecera, dentro del artículo, lateral y pie).

---

## Paso 1. Ver la web en tu ordenador (opcional)

1. Instala **Node.js** (versión LTS) desde nodejs.org.
2. Abre una terminal en esta carpeta y ejecuta:
   ```
   npm install
   npm run dev
   ```
3. Abre http://localhost:4321. Los cambios que hagas se ven al momento.

## Paso 2. Escribir un artículo

Crea un archivo nuevo en `src/content/articulos/`, por ejemplo `mi-noticia.md`. El nombre del archivo será la URL (`/mi-noticia/`).

```markdown
---
title: "Título del artículo (máx. 110 caracteres)"
description: "Resumen que sale en Google (máx. 170 caracteres)"
date: 2026-11-25
category: noticias        # noticias | vulnerabilidades | guias | ctf-formacion | linux | privacidad
tags: [ransomware, empresas]
author: Tu Nombre
image: /img/mi-foto.webp   # opcional, guarda la imagen en public/img/
imageAlt: "Descripción de la imagen"
featured: false            # true = sale grande en portada
---

Aquí el texto en Markdown. ## para subtítulos, **negrita**, [enlaces](https://...).
```

## Paso 3. Comprar el dominio (≈10-15 €/año)

Compra un dominio `.es` o `.com` en un registrador (Cloudflare Registrar, Namecheap, DonDominio…). **Lo necesitas para AdSense**: Google no aprueba subdominios gratuitos.
Después, cambia el dominio en `src/config.ts`, `astro.config.mjs` y `public/robots.txt`.

## Paso 4. Publicar gratis

**Opción recomendada: Cloudflare Pages** (gratis, sin límite de visitas, muy rápido).
1. Crea una cuenta en GitHub y sube esta carpeta a un repositorio nuevo.
2. En Cloudflare › Workers & Pages › Crear › Pages › Conectar con GitHub, elige el repositorio.
3. Configuración: framework **Astro**, comando `npm run build`, carpeta de salida `dist`.
4. En "Dominios personalizados", añade tu dominio.
Cada vez que subas un artículo a GitHub, la web se actualiza sola.

**Opción rápida sin GitHub: Netlify Drop.** Entra en app.netlify.com/drop y arrastra la carpeta `dist`. En un minuto la tienes online (luego conectas tu dominio en la configuración). Para actualizar tendrás que volver a construir (`npm run build`) y arrastrar de nuevo.

## Paso 5. Antes de pedir AdSense

- [ ] Rellena tus datos reales en `src/config.ts` (aviso legal) y personaliza **Sobre nosotros**.
- [ ] Ten **20-30 artículos originales** y útiles (no copiados ni reescritos con IA sin aportar nada).
- [ ] Registra la web en **Google Search Console** y envía `https://tudominio/sitemap-index.xml`.
- [ ] Publica con constancia (2-4 artículos por semana) durante unas semanas.

## Paso 6. Solicitar y activar AdSense

1. Ve a adsense.google.com, crea la cuenta (mayor de 18) y añade tu sitio.
2. Google te dará un código `ca-pub-XXXXXXXXXXXXXXXX`. Pégalo en `ADSENSE.client` en `src/config.ts` y publica. Esto pone el script de verificación en todas las páginas.
3. Sustituye el contenido de `public/ads.txt` por la línea que te indique AdSense.
4. **Consentimiento de cookies (obligatorio en Europa)**: en AdSense › Privacidad y mensajes › RGPD, crea y publica el mensaje de consentimiento de Google. No necesitas instalar otro banner.
5. Espera la revisión (de días a algunas semanas).
6. Cuando te aprueben, crea 4 bloques de anuncio (Anuncios › Por bloque de anuncios): uno *display* para cabecera, uno *en artículo*, uno *display* para el lateral y otro para el pie. Copia el número `data-ad-slot` de cada uno en `ADSENSE.slots`. Los recuadros grises se convertirán en anuncios.

## Cuidado con el contenido (muy importante en este nicho)

Las políticas de Google prohíben contenido que facilite el acceso no autorizado o el hacking malicioso. Para no perder la cuenta:
- Enfoca todo en **entender, detectar y defenderse**.
- Nada de credenciales filtradas, cracks, herramientas maliciosas ni pasos para atacar sistemas reales.
- Los writeups de CTF y laboratorios, siempre sobre entornos legales y con el aviso que ya incluye cada artículo.

## ¿Cuánto se puede ganar? (estimación orientativa)

En España, AdSense suele dar entre **1 y 6 € por cada 1.000 visitas** (la temática tecnológica está en la parte media-alta). Es decir:
- 10.000 visitas/mes → unos 10-60 €/mes
- 100.000 visitas/mes → unos 100-600 €/mes

Llegar a esas cifras normalmente lleva 6-12 meses de publicar con constancia y trabajar el SEO. Complementos que suelen rendir más que AdSense en este nicho: afiliados (cursos, VPN, gestores de contraseñas, libros), un canal de YouTube asociado y una newsletter.
