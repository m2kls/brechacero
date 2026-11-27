---
title: "WeaveLotus: espionaje a militares y gobiernos de Tailandia y Filipinas"
description: "El grupo WeaveLotus robó documentos militares y del poder legislativo de Tailandia y Filipinas usando fallos conocidos y contraseñas por defecto. Qué se sabe."
date: 2026-11-27T08:54:00+01:00
category: noticias
tags: [WeaveLotus, ciberespionaje, Tailandia, Filipinas, GeoServer, JasperReports, SOCRadar]
author: Redacción
photo: "File:Sappaya-Sapasathan (I).jpg"
imageAlt: "Sappaya-Sapasathan, sede del Parlamento de Tailandia, país afectado por el espionaje de WeaveLotus"
---

Un grupo de **ciberespionaje** al que la empresa SOCRadar llama **WeaveLotus** ha robado miles de documentos de organismos militares, gubernamentales y legislativos de **Tailandia** y **Filipinas**. La campaña, bautizada como RedOps, se desarrolló entre agosto y septiembre de 2026 y se ha dado a conocer este 27 de noviembre. Los investigadores han confirmado cinco intrusiones y han visto tareas de reconocimiento contra más de 30 organismos públicos de Indonesia, aunque en ese país no encontraron pruebas de que llegaran a entrar.

Lo llamativo del caso no es una técnica sofisticada, sino lo contrario: casi todas las puertas que usaron los atacantes estaban abiertas por **fallos conocidos sin parchear** y **contraseñas por defecto**.

## Qué robó WeaveLotus en Tailandia

Según el informe, la primera víctima tailandesa fue una organización vinculada al ejército. Los atacantes entraron aprovechando **CVE-2024-36401**, un fallo de GeoServer (un servidor de mapas muy usado por administraciones) que lleva parcheado desde 2024 y que CISA incluyó en su catálogo de vulnerabilidades explotadas. Además, un gestor de contenidos Directus permitía descargar archivos sin iniciar sesión. De ahí salieron unos **31.418 archivos** (575 MB) sobre logística, respuesta a emergencias y operaciones militares.

La mayor fuga verificada procede de un **órgano legislativo** tailandés que tenía expuesto a internet un servidor de informes JasperReports con las **credenciales de fábrica**. Los investigadores han confirmado unos **19 GB** de datos, con órdenes del día de reuniones, registros de gastos y resultados de declaraciones de bienes.

En otro organismo, los atacantes capturaron credenciales de administrador que les dieron acceso a un servidor Keycloak, el sistema que gestiona los inicios de sesión. Copiaron más de 40.000 registros de usuarios y casi 350.000 documentos sobre políticas, presupuestos y finanzas.

## Y en Filipinas

En Filipinas, una instalación vulnerable del sistema de soporte osTicket dejó al descubierto nombres de usuario, correos y hashes de contraseñas del personal. Una aplicación web hecha con Laravel funcionaba en **modo de depuración** en producción, lo que mostraba rutas internas del servidor y fragmentos de código fuente a cualquiera que provocara un error.

## ¿Quién está detrás?

SOCRadar atribuye la campaña, con **confianza moderada**, a un actor patrocinado por el Estado vietnamita. Se basa en comentarios en vietnamita dentro de los scripts y en que la actividad coincide con el horario laboral de la zona UTC+7. También ve una posible relación con **OceanLotus (APT32)**, un grupo de espionaje vietnamita conocido, pero con confianza baja: no se ha observado ninguna de sus herramientas habituales. Ningún gobierno de los afectados ha confirmado públicamente las intrusiones, así que la atribución debe tomarse con cautela.

El caso encaja con lo que se ve cada vez más en el espionaje entre Estados: en lugar de gastar vulnerabilidades desconocidas, los atacantes recorren internet buscando servidores olvidados y mal configurados. Es la misma lógica que ya vimos con los [fallos de GeoServer explotados este mes](/fallos-geoserver-explotados-parche/) o con la campaña iraní [Volant Manticore](/volant-manticore-iran-espionaje-kuboshell/).

## Cómo protegerse: la lección para cualquier organización

Aunque las víctimas están en el sudeste asiático, las recomendaciones del informe sirven para cualquier ayuntamiento, empresa o universidad en España:

- **Parchea los servidores expuestos a internet**, sobre todo GeoServer, osTicket y gestores de contenidos. Un fallo de 2024 sigue abriendo puertas en 2026.
- **Cambia las contraseñas por defecto** de cualquier herramienta antes de publicarla. Es la medida más barata y la que habría evitado la mayor fuga. Si necesitas ideas, repasa nuestra guía para [proteger cuentas con contraseñas robustas y 2FA](/proteger-cuentas-contrasenas-2fa/).
- **Desactiva el modo de depuración** de las aplicaciones web en producción (en Laravel, `APP_DEBUG=false`).
- Comprueba que las API de archivos **no permiten acceso anónimo** a documentos internos.
- Vigila conexiones SSH salientes por el puerto 443 y transferencias de datos inusualmente grandes, dos señales que SOCRadar observó en esta campaña.
- Revisa también los sistemas compartidos de informes y las relaciones de confianza entre servicios de identidad como Keycloak: una sola credencial de administrador abrió el acceso a cientos de miles de registros.

## Fuentes

- [SOCRadar: RedOps / WeaveLotus targets Southeast Asian governments](https://socradar.io/blog/redops-weavelotus-southeast-asian-governments/)
- [Cyber Security News: Hackers Breach Military and Government Networks Across Southeast Asia](https://cybersecuritynews.com/military-and-government-networks/)
- [NVD: CVE-2024-36401 (GeoServer)](https://nvd.nist.gov/vuln/detail/CVE-2024-36401)
