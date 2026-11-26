---
title: "Plugins de WordPress con puerta trasera: WordPress.org bloquea seis de WP Connect"
description: "Seis plugins de WordPress de WP Connect, con más de 3.600 webs, recibieron código con puerta trasera (CVE-2026-135202). Lista de versiones y qué revisar en tu web."
date: 2026-11-26T04:57:00+01:00
category: vulnerabilidades
tags: [WordPress, plugins, puerta trasera, WP Connect, CVE-2026-135202, cadena de suministro, Wordfence]
author: Redacción
photo: "File:WordPress Moleskine notebook - Flickr - Nikolay Bachiyski.jpg"
imageAlt: "Cuaderno con el logotipo de WordPress, el gestor de contenidos cuyos plugins de WP Connect recibieron una puerta trasera"
---

Seis **plugins de WordPress** desarrollados por WP Connect recibieron el pasado 22 de noviembre versiones con una **puerta trasera** capaz de dar al atacante el control total de las webs que los usaran. El equipo de plugins de WordPress.org bloqueó las publicaciones y cerró las seis fichas de forma permanente. Wordfence, que ha registrado el caso como **CVE-2026-135202** con la puntuación máxima práctica (9,8 sobre 10), calcula que los plugins estaban instalados en **más de 3.600 webs**.

## Qué plugins de WordPress están afectados

Estas son las extensiones y las versiones con código malicioso:

- **Air WP Sync** (Airtable a WordPress): versiones 2.9.1 a 2.9.4.
- **WP Sync for Notion** (Notion a WordPress): 1.7.4.
- **Add-on Brevo for Gravity Forms**: 2.6.3.
- **Add-On for Contact Form 7 to Airtable**: 2.5.4.
- **Add-On for Contact Form 7 to Notion**: 1.6.4.
- **Orders Sync to Airtable for WooCommerce**: 1.0.2.

No existe una versión corregida, y actualizar el núcleo de WordPress no resuelve nada.

## Qué hacía la puerta trasera

Según el análisis publicado por The Hacker News a partir de los datos de Wordfence, las versiones manipuladas añadían un archivo que se ejecutaba en cada visita a la web. Enviaba a un servidor del atacante la dirección del sitio y las versiones de PHP, WordPress y el sistema operativo, y ejecutaba el código PHP que el servidor le devolviera.

Con eso, el atacante podía lanzar comandos en el servidor, leer, modificar o borrar archivos, consultar la base de datos, **copiar la tabla de usuarios con los hashes de las contraseñas**, dejar *webshells* (pequeños programas de control remoto) y programar una tarea cada hora para mantener el acceso.

Chloe Chamberland, investigadora de Wordfence, atribuye el incidente a un probable **robo de la cuenta del desarrollador** en WordPress.org, no a un error de programación. Es un ataque a la cadena de suministro: no se ataca la web, sino el software de confianza que esta instala, como ocurrió esta misma semana con el [hackeo del repositorio de paquetes Hex.pm](/hackeo-hex-pm-elixir-erlang/).

## ¿Llegaron las versiones maliciosas a las webs?

Aquí las fuentes no coinciden. The Hacker News explica que las nuevas protecciones de WordPress.org, que retienen durante un tiempo las publicaciones antes de distribuirlas, frenaron las versiones maliciosas y que es **poco probable** que haya webs afectadas. En cambio, el boletín de Risky Business habla de plugins que distribuyeron la puerta trasera «durante varias horas» del domingo, y la firma Brandefense recomienda a todos los administradores revisar sus instalaciones. Ante la duda, conviene comprobarlo.

## Qué hacer si tu web usa estos plugins

1. **Revisa la lista de plugins**, también los desactivados y, en instalaciones multisitio, en todas las webs.
2. Si encuentras alguno de los nombres y versiones anteriores, **guarda una copia** de archivos, base de datos y registros antes de tocar nada: servirá para investigar.
3. **Desinstala el plugin** y busca una alternativa; las fichas no se van a reabrir.
4. Pasa un **análisis completo de malware** y revisa si han aparecido administradores nuevos, tareas programadas raras o archivos PHP en la carpeta de subidas.
5. **Cambia las contraseñas** de los usuarios y las claves de servicios conectados (Airtable, Notion, Brevo). Si no puedes asegurar que el sitio está limpio, reconstrúyelo desde una copia fiable.

El caso llega días después de que se confirmara que hay ataques activos contra el [fallo del instalador de Drupal](/fallo-drupal-instalador-explotado/), otra señal de que los gestores de contenidos están en el punto de mira. Si quieres entender cómo se clasifican estos fallos, te contamos [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [The Hacker News: WordPress Blocks Six Backdoored WP Connect Plugins Before Malicious Releases Go Live](https://thehackernews.com/2026/11/wordpress-blocks-six-backdoored-wp.html)
- [Brandefense: WP Connect Plugin Backdoors – removal steps](https://brandefense.io/security-news/wp-connect-plugin-backdoors-six-plugins-remove/)
- [Risky Business News: boletín del 25 de noviembre de 2026](https://news.risky.biz/risky-bulletin-card-stealer-found-on-80-major-us-news-sites/)
