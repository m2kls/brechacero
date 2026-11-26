---
title: "Actualización de Joomla 6.2.1: corrige 58 fallos, cuatro de ellos críticos"
description: "Joomla 6.2.1 y 5.4.11 corrigen 58 fallos de seguridad, entre ellos una ejecución remota de código (CVE-2026-129393). Qué versiones están afectadas y cómo actualizar."
date: 2026-11-26T04:56:00+01:00
category: vulnerabilidades
tags: [Joomla, CMS, CVE-2026-129393, ejecución remota de código, XSS, actualización de seguridad]
author: Redacción
photo: "File:Joomla! 5.1.2 administrator dashboard.jpg"
imageAlt: "Panel de administración de Joomla 5, el gestor de contenidos que ha recibido la actualización de seguridad 6.2.1 y 5.4.11"
---

Joomla, uno de los gestores de contenidos más usados después de WordPress, ha publicado las versiones **Joomla 6.2.1 y 5.4.11**, una actualización de seguridad que corrige **58 fallos** de su núcleo. Cuatro son críticos, incluida una ejecución remota de código registrada como **CVE-2026-129393** que afecta a todas las versiones desde la 4.0.0. El proyecto recomienda actualizar cuanto antes a cualquier web que use Joomla 5 o 6.

## Qué fallos corrige la actualización de Joomla

Según el resumen publicado por Joomla Center a partir del anuncio oficial, los 58 fallos se reparten en 4 críticos, 23 altos, 29 medios y 2 bajos. Los críticos son:

- **CVE-2026-129393**: ejecución remota de código a través de los campos personalizados de tipo Media, por no escapar bien ciertos parámetros. Lo descubrió Alex Williams (Pellera Technologies) y lo comunicó VulnCheck el 26 de octubre.
- **CVE-2026-123214**: un salto de autenticación en el instalador web si la carpeta de instalación se ha dejado en la web en producción.
- **CVE-2026-126045**: inclusión de archivos locales mediante la selección de idioma.
- **CVE-2026-127297**: una condición de carrera en los registros que puede recrear un archivo de log sin su cabecera de protección; Joomla también la clasifica como ejecución remota de código.

Entre los de gravedad alta hay varios fallos de **XSS** en la búsqueda inteligente, los contactos y las fuentes de noticias (si no sabes qué es, lo explicamos en [qué es el XSS o cross-site scripting](/que-es-xss-cross-site-scripting/)), una comprobación incompleta de extensiones en el gestor multimedia y un recorrido de rutas en los registros del programador de tareas.

El aviso oficial de Joomla sobre CVE-2026-129393 califica su impacto como crítico, aunque la probabilidad de explotación como baja. Por ahora no hay constancia pública de que ninguno de estos fallos se esté aprovechando en ataques.

## ¿Qué versiones de Joomla están afectadas?

El fallo de ejecución remota de código afecta a **Joomla 4.0.0 a 5.4.10 y 6.0.0 a 6.2.0**. Las correcciones solo se publican para las ramas con soporte:

- Si usas **Joomla 6**, actualiza a la **6.2.1**.
- Si usas **Joomla 5**, actualiza a la **5.4.11**. La rama 5.4 seguirá recibiendo parches de seguridad hasta el 12 de octubre de 2027.
- **Joomla 3 y 4** no reciben paquete en esta ocasión. Si tu web sigue en ellas, tienes fallos conocidos sin corregir y conviene planificar la migración.

## Cómo actualizar Joomla de forma segura

1. Haz una **copia de seguridad completa** de archivos y base de datos.
2. Actualiza desde el panel en **Sistema > Actualizar > Joomla**.
3. Comprueba que **no queda la carpeta de instalación** en el servidor; es la condición que permite el salto de autenticación.
4. Revisa después lo básico: inicio de sesión y doble factor, edición de artículos y campos personalizados, gestor multimedia, búsqueda, tareas programadas y las extensiones principales.

La actualización llega en una semana especialmente movida para los gestores de contenidos: hay ataques activos contra el [fallo del instalador de Drupal](/fallo-drupal-instalador-explotado/) y WordPress.org ha tenido que bloquear [seis plugins de WP Connect con puerta trasera](/plugins-wordpress-wp-connect-puerta-trasera/). Los atacantes suelen aprovechar los fallos de los CMS pocos días después de que se publiquen los parches, así que no conviene dejarlo para más adelante.

## Fuentes

- [Joomla Security Centre: [20261156] Core – RCE through media custom field parameters](https://developer.joomla.org/security-centre/1154-20261156-core-rce-through-media-custom-field-parameters.html)
- [Joomla Center: Joomla 6.2.1 and 5.4.11, major security and bug fix releases](https://joomla.center/en/news/joomla-6-2-1)
- [Daily CyberSecurity: Joomla 6.2.1 fixes 58 flaws](https://securityonline.info/joomla-6-2-1-security-update-cve-2026-129393/)
