# Redacción automática de Brecha Cero

Instrucciones que sigue la tarea programada (cada 2 horas) para publicar noticias.
Cualquier persona que edite la web también puede usarlas como guía de estilo.

## 1. Decidir si hay algo que publicar

1. Mira qué se ha publicado ya: `ls src/content/articulos/` y los títulos de los últimos 3 días
   (`grep -h '^title:' src/content/articulos/*.md`). No repitas temas ya cubiertos.
2. Busca noticias e historias de las **últimas 12 horas** sobre cualquier tema de la web:
   ciberseguridad, vulnerabilidades y parches, filtraciones y ataques, estafas, privacidad y protección de datos,
   hacking ético, CTF y formación, Linux y software libre (seguridad), seguridad e IA, nuevas herramientas,
   informes y estudios, regulación y operaciones policiales. Fuentes, por orden:
   - España: INCIBE, CCN-CERT, AEPD, Policía Nacional / Guardia Civil, empresas o administraciones españolas.
   - Mundo: CISA (catálogo KEV), avisos de Microsoft, Google, Apple, Cisco, Fortinet, etc.; Europol.
   - Medios: BleepingComputer, The Record, SecurityWeek, The Hacker News, Krebs on Security, Una al Día (Hispasec), medios españoles.
3. Ordena lo encontrado por importancia y publica **primero lo más importante**:
   - **Prioridad alta**: afecta a muchos usuarios en España o en el mundo, fallo explotado que hay que parchear,
     filtración o ataque a una organización conocida, estafa activa.
   - **Prioridad media**: parches importantes, nuevos informes o estudios relevantes, operaciones policiales,
     novedades de privacidad o regulación, herramientas o técnicas defensivas nuevas, noticias de la industria.
   - **Interesante**: historias curiosas o didácticas del sector que encajen con la web (formación, CTF, Linux, IA y seguridad).
4. Publica **varias noticias por ejecución** (lo normal, 2–5; hasta 6 si hay mucha actualidad). No hay límite diario.
   Cada artículo debe tener información nueva y real, fuentes y valor para el lector: si una franja solo tiene temas flojos o
   repetidos, publica menos o ninguno. Nunca dos artículos casi iguales ni "relleno": eso sí perjudica en Google y en AdSense.

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
category: noticias                # o vulnerabilidades / privacidad / linux / ctf-formacion / guias
tags: [Etiqueta, Otra]
author: Redacción
image: "/img/fotos/<slug>.jpg"
imageAlt: "Descripción de la foto"
imageCredit: "Foto: Autor / Wikimedia Commons (CC BY-SA 4.0)"
imageCreditUrl: "https://commons.wikimedia.org/wiki/File:..."
---
```

**Fecha (`date`)**: pon la hora real a la que haces el commit, en hora de Madrid (`TZ=Europe/Madrid date +%Y-%m-%dT%H:%M:00%:z`),
**nunca una hora posterior**. La web oculta los artículos con fecha futura hasta el siguiente build, así que una noticia
con fecha adelantada no aparecería. Si publicas varias a la vez, puedes separarlas un minuto hacia atrás, nunca hacia delante.
Antes del push comprueba que ningún `date:` de hoy es posterior a la hora actual.

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
