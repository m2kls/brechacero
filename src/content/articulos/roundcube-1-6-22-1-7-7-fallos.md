---
title: "Roundcube 1.6.22 y 1.7.7: 12 fallos corregidos y fin de la rama 1.6"
description: "Roundcube corrige 12 fallos de seguridad en su webmail y anuncia que la 1.6.22 es la última versión de la rama 1.6. Qué cambia y cómo actualizar tu correo web."
date: 2026-11-26T08:54:00+01:00
category: vulnerabilidades
tags: [Roundcube, webmail, correo electrónico, parches, hosting, Sieve]
author: Redacción
photo: "File:Roundcube 1.6.0 screenshot.png"
imageAlt: "Bandeja de entrada del webmail Roundcube 1.6"
---

**Roundcube**, el webmail de código abierto que usan universidades, administraciones y miles de empresas de hosting (viene incluido en paneles como cPanel, Plesk y DirectAdmin), ha publicado las versiones **Roundcube 1.6.22 y 1.7.7** para corregir **12 fallos de seguridad**. El proyecto, que lo anunció el 23 de noviembre, añade un aviso importante: **la 1.6.22 es la última versión de la rama 1.6**. A partir de ahora solo la 1.7 recibirá parches.

## Qué fallos corrige Roundcube

Las notas oficiales no dan identificadores CVE ni puntuaciones de gravedad, y no mencionan ataques en curso. Los fallos, comunicados por investigadores independientes, se agrupan así:

- **Contenido de los mensajes**: varias formas de saltarse el aislamiento de los estilos CSS de un correo (con comentarios HTML, con varios enlaces de estilo o accediendo directamente al proxy de CSS), un fallo que dejaba ver respuestas del proxy de CSS y una vía para colar atributos con prefijo de espacio de nombres en el filtro HTML con PHP anterior a 8.4. Son problemas que un atacante podría usar en correos preparados.
- **Bloqueo de imágenes remotas**: un SVG con comentarios CSS podía cargar recursos externos aunque el usuario tuviera desactivado el contenido remoto, lo que sirve para saber si alguien ha abierto un mensaje.
- **Adjuntos**: los archivos PDF, PostScript y SVG peligrosos seguían llegando a ImageMagick para generar miniaturas (era un fallo que ya se había intentado corregir) y un adjunto TNEF de Outlook podía provocar una denegación de servicio.
- **Filtros Sieve**: dos inyecciones que permitían meter instrucciones no autorizadas en las reglas de filtrado del correo.
- **Otros**: una inyección de peticiones HTTP en el corrector ortográfico ATD (de nuevo), una inyección XML en el complemento de cambio de contraseña con el conector XIMSS y un caso en el que Roundcube se conectaba **sin cifrar** a los servidores IMAP, SMTP o ManageSieve aunque se hubiera configurado TLS, si el servidor no anunciaba esa capacidad.

Es la segunda tanda de parches de este mes: el 9 de noviembre Roundcube ya había corregido 17 fallos en las versiones 1.6.21 y 1.7.6.

## ¿Por qué importa?

Los webmails son un objetivo clásico del espionaje y del cibercrimen porque dan acceso directo al correo de la víctima. Grupos patrocinados por Estados han aprovechado fallos de Roundcube en otras ocasiones para robar correos de gobiernos y organismos europeos, y la agencia estadounidense CISA ha incluido varios de ellos en su catálogo de vulnerabilidades explotadas. Aunque esta vez no se conocen ataques, la mayoría de los fallos se activan con un correo, y eso los hace atractivos.

El fin de la rama 1.6 afecta sobre todo a empresas de hosting y administradores que la mantienen por compatibilidad: la 1.6 solo soporta oficialmente hasta PHP 8.3, y cPanel y Plesk todavía distribuyen esa rama.

## Qué hacer si usas Roundcube

1. **Actualiza ya** a Roundcube 1.7.7 o, si todavía no puedes migrar, a la 1.6.22. Haz antes copia de seguridad.
2. **Planifica el salto a la 1.7**: la 1.6 no recibirá más parches de seguridad.
3. Si tu correo lo gestiona tu proveedor de hosting, **pregunta** cuándo aplicará la actualización.
4. Como usuario, desconfía de correos inesperados aunque solo los abras en el navegador, y no abras adjuntos que no esperas. Repasa [cómo detectar un correo de phishing](/como-detectar-phishing/) y [cómo saber si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/).

## Fuentes

- [Security updates 1.6.22 and 1.7.7 released (Roundcube)](https://roundcube.net/news/2026/11/23/security-updates-1.6.22-and-1.7.7)
- [Roundcube Webmail Flaws Could Let Hackers Execute Malicious Code (Cyber Security News)](https://cybersecuritynews.com/roundcube-webmail-flaws)
- [Roundcube fixes 17 flaws and warns that 1.6 will be discontinued soon (Webhosting Today)](https://webhosting.today/2026/11/10/roundcube-fixes-17-flaws-and-warns-that-1-6-will-be-discontinued-soon/)
