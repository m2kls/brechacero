# Redacción automática de Brecha Cero

Instrucciones que sigue la tarea programada (cada 2 horas) para publicar noticias.
Cualquier persona que edite la web también puede usarlas como guía de estilo.

## 1. Decidir si hay algo que publicar

1. Mira qué se ha publicado ya: `ls src/content/articulos/` y los títulos de los últimos 3 días
   (`grep -h '^title:' src/content/articulos/*.md`). No repitas temas ya cubiertos.
2. Busca noticias de ciberseguridad de las **últimas 6 horas**, en este orden de prioridad:
   - España: INCIBE, CCN-CERT, AEPD, Policía Nacional / Guardia Civil, grandes empresas o administraciones españolas afectadas.
   - Mundo: CISA (catálogo KEV), avisos de Microsoft, Google, Apple, Cisco, Fortinet, etc.; grandes filtraciones; operaciones policiales contra ciberdelincuencia.
   - Fuentes de referencia: BleepingComputer, The Record, SecurityWeek, The Hacker News, Krebs on Security, Una al Día (Hispasec), medios españoles generalistas.
3. Publica **solo** si la noticia cumple al menos una de estas condiciones:
   - afecta a muchos usuarios en España o en el mundo,
   - es un fallo que se está explotando y hay que actualizar,
   - es una filtración o ataque a una organización conocida,
   - es una estafa activa que conviene avisar.
4. Máximo **2 artículos por ejecución** y **8 al día**. Si no hay nada que cumpla, **no publiques nada**:
   publicar relleno perjudica en Google y en AdSense.

## 2. Línea editorial (obligatoria)

- Enfoque **informativo y defensivo**: qué ha pasado, a quién afecta y cómo protegerse.
- **Nunca** incluir instrucciones de ataque, exploits, payloads, comandos para explotar fallos,
  enlaces a datos filtrados ni a foros de ciberdelincuentes. AdSense penaliza ese contenido.
- Contrastar con al menos **2 fuentes**, una de ellas oficial cuando exista. Si algo no está confirmado, decirlo.
- Redacción **original** en español de España. No copiar párrafos de las fuentes;
  como mucho una cita corta entre comillas y atribuida.
- Tono de periodista tecnológico: frases claras, sin exageraciones, sin "en el mundo actual",
  sin listas de emojis, pocas negritas.
- Extensión: 450–900 palabras. Estructura con `##`: qué ha pasado, a quién afecta,
  qué hacer / cómo protegerse, y al final `## Fuentes` con enlaces.
- Enlazar 1–2 artículos propios relacionados (p. ej. `/proteger-cuentas-contrasenas-2fa/`,
  `/como-detectar-phishing/`, `/saber-si-mi-contrasena-ha-sido-filtrada/`, `/que-es-una-cve/`).

## 2b. Posicionamiento en buscadores (obligatorio en cada noticia)

- **Palabra clave principal**: antes de escribir, decide cómo lo buscaría un lector en Google en español
  (p. ej. "filtración GTA 6", "hackeo LaLiga", "fallo Outlook"). Debe aparecer:
  - al principio del `title` (máx. ~65 caracteres visibles; el resto puede cortarse en Google),
  - en la `description` (140–160 caracteres, con el dato clave y una llamada a leer),
  - en el **primer párrafo** y en al menos un subtítulo `##`,
  - en el **slug** (corto, sin artículos ni fechas: `hackeo-laliga-datos-aficionados`).
- Usa nombres propios completos (empresa, producto, CVE, versión) tal y como se buscan.
- El primer párrafo responde a qué, quién, cuándo y por qué importa (Google lo usa como resumen).
- Subtítulos `##` que sean preguntas o frases que la gente busca ("¿Estoy afectado?", "Cómo protegerte").
- **Enlaces internos**: 2–3 enlaces a otros artículos de la web con texto descriptivo
  (nunca "pincha aquí"). Revisa `ls src/content/articulos/` para elegir los más relacionados.
- **Enlaces externos** solo a fuentes fiables, en la sección `## Fuentes`.
- `tags`: 4–7 etiquetas con los términos de búsqueda (empresa, producto, tipo de ataque, país).
- `imageAlt` describe la foto con la palabra clave si encaja de forma natural.
- Si una noticia anterior trata el mismo tema, **actualízala** (cambia el texto y pon `updated:` con la fecha) en lugar de crear otra casi igual.
- No repitas la palabra clave de forma forzada: escribe para personas.

La web ya genera sola el sitemap, el sitemap de Google News, los datos estructurados `NewsArticle`
y avisa a Bing (IndexNow) en cada publicación; no hace falta tocar nada de eso.

## 3. Formato del archivo

`src/content/articulos/<slug>.md` (slug en minúsculas, sin tildes, con guiones, 3–7 palabras):

```yaml
---
title: "Titular informativo de menos de 110 caracteres"
description: "Resumen de menos de 170 caracteres con el dato clave y por qué importa."
date: 2026-11-24T13:00:00+01:00   # hora real de publicación, zona Europe/Madrid
category: noticias                # o vulnerabilidades / privacidad
tags: [Etiqueta, Otra]
author: Redacción
image: "/img/fotos/<slug>.jpg"
imageAlt: "Descripción de la foto"
imageCredit: "Foto: Autor / Wikimedia Commons (CC BY-SA 4.0)"
imageCreditUrl: "https://commons.wikimedia.org/wiki/File:..."
---
```

`featured: true` solo para la noticia más importante del día (y quítalo de la anterior).

## 4. Foto real con licencia

Usa siempre `tools/foto.py` (Wikimedia Commons, solo licencias que permiten uso comercial):

```bash
python3 -I tools/foto.py buscar "nombre de la empresa sede" --hoja /tmp/hoja.jpg
# mira /tmp/hoja.jpg y elige el número que mejor encaje
python3 -I tools/foto.py bajar "nombre de la empresa sede" 2 <slug>
```

Copia en el frontmatter las líneas que imprime. Busca algo concreto y real de la noticia
(edificio o logotipo de la organización, el producto afectado, el lugar). Si no hay nada
concreto, una foto genérica pertinente (centro de datos, portátil, móvil…).
**Nunca** uses fotos de las webs de noticias ni de Google Imágenes: tienen copyright.
Si Commons no responde, deja el artículo sin `image` (se usa la portada ilustrada) y
no generes una portada nueva.

## 5. Comprobar y publicar

```bash
npm ci        # solo si no existe node_modules
npm run build # debe terminar sin errores
git add -A && git commit -m "Noticia: <titular corto>" && git push origin main
```

Al hacer push, GitHub Actions publica la web en Cloudflare Pages en 1–2 minutos.
