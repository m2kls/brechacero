---
title: "CISA alerta: fallos explotados en N-able Mail Assure y MONAI Label"
description: "CISA añade a su catálogo KEV dos fallos explotados en N-able Mail Assure y MONAI Label, este último atacado con agentes de IA en 11 minutos. Qué hacer."
date: 2026-11-25T04:54:00+01:00
category: vulnerabilidades
tags: [CISA KEV, N-able, Mail Assure, MONAI Label, IA, CVE-2026-134624, CVE-2026-133968]
author: Redacción
photo: "File:Cern datacenter.jpg"
imageAlt: "Filas de servidores en un centro de datos, como los que alojan servicios de correo y plataformas de IA afectados por los fallos"
---

La agencia de ciberseguridad de Estados Unidos (CISA) ha añadido a su catálogo de vulnerabilidades explotadas (KEV) dos fallos que ya se están usando en ataques: uno en **N-able Mail Assure**, el servicio de filtrado de correo que usan miles de proveedores de servicios gestionados (MSP), y otro en **MONAI Label**, una herramienta de código abierto para etiquetar imágenes médicas con inteligencia artificial. CISA lo anunció el 23 de noviembre y ha dado a las agencias federales hasta el 26 de noviembre para corregirlos, un plazo inusualmente corto que da idea de la urgencia.

## El fallo de N-able Mail Assure (CVE-2026-134624)

El fallo de N-able Mail Assure, con puntuación 9,3, es una falsificación de peticiones del lado del servidor (SSRF) en la función que comprueba la conexión de sincronización con LDAP. Un usuario autenticado de la API podía usarla para hacer que el servidor contactara con máquinas y puertos internos a los que no debería tener acceso.

Es el mismo problema que está detrás del incidente que N-able reconoció la semana pasada: el 16 de noviembre unos atacantes entraron en un servidor de su nube de Mail Assure y SpamExperts, lo que dejó sin paneles de gestión ni API a clientes de América, Asia-Pacífico y Europa durante varios días. El correo siguió filtrándose con normalidad y la empresa restableció el acceso el 21 de noviembre. N-able asegura que la explotación "se limitó a un único servidor alojado" y que no tiene pruebas de que se accediera a datos de clientes ni a buzones. Ha contratado a un equipo externo de respuesta a incidentes y promete un análisis de causa raíz en dos semanas.

Al ser un servicio en la nube, la corrección corre a cargo de N-able; los clientes no tienen que instalar nada, pero sí conviene revisar lo que se indica más abajo.

## El fallo de MONAI Label (CVE-2026-133968), explotado con IA

El segundo fallo es más grave en su puntuación (9,8). MONAI Label permite a un atacante **sin autenticar** escribir archivos fuera de la carpeta de datos mediante un recorrido de rutas (path traversal), lo que puede acabar en ejecución remota de código en el servidor.

Lo llamativo es cómo se ha explotado. Según los investigadores citados por The Hacker News, un grupo presuntamente vinculado a China usó una herramienta de ataque basada en agentes de IA, bautizada CAIRN, que aprovechó el fallo como zero-day y consiguió acceso como administrador (root) en unos 11 minutos. Amazon describe en un informe de su equipo de inteligencia cómo estos agentes planifican el ataque y cambian de táctica sobre la marcha. Es un ejemplo más de la tendencia de la que avisaba hace poco el [NCSC británico sobre ataques con agentes de IA](/ncsc-ciberataques-agentes-ia/).

## ¿A quién afecta?

- **Clientes de N-able Mail Assure y SpamExperts**, sobre todo MSP que gestionan el correo de otras empresas.
- **Hospitales, centros de investigación y startups de salud** que usen MONAI Label para preparar datos de entrenamiento de modelos de imagen médica, especialmente si el servidor está accesible desde internet.

## Qué hacer ahora

1. **MONAI Label:** actualiza a la última versión publicada por el proyecto, no expongas el servidor a internet y revisa si hay archivos extraños fuera del directorio de datos o procesos desconocidos.
2. **N-able Mail Assure:** cambia las credenciales de la API y de la conexión LDAP configuradas en el servicio, revisa los registros de acceso desde el 16 de noviembre y sigue la página de estado de N-able hasta que publique el análisis final.
3. **En general:** el catálogo KEV de CISA es una buena lista de prioridades para cualquier organización, no solo para la administración estadounidense. Si un producto tuyo aparece ahí, va primero. Explicamos cómo leer estos avisos en [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [CISA: CISA Adds Two Known Exploited Vulnerabilities to Catalog (23-11-2026)](https://www.cisa.gov/news-events/alerts/2026/11/23/cisa-adds-two-known-exploited-vulnerabilities-catalog)
- [N-able: página de estado del incidente de Mail Assure y SpamExperts](https://uptime.n-able.com/event/202672/)
- [Amazon Web Services: Threat actors running cybercrime campaigns with AI agents](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/)
- [The Hacker News: Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
- [The Hacker News: Hackers Breach N-able Cloud Server](https://thehackernews.com/2026/11/n-able-confirms-hackers-accessed-cloud.html)
