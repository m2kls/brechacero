---
title: "VMware, Cisco y Apache: tres fallos críticos que ya se están explotando y cómo parchearlos"
description: "Un zero-day en vCenter usado por un grupo vinculado a China, credenciales fijas en Cisco Expressway y un fallo en Apache Roller. Cómo protegerte."
date: 2026-11-24
category: vulnerabilidades
tags: [VMware, vCenter, Cisco, Apache, zero-day, CISA KEV, parches]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
photo: "File:Front_of_server_racks_at_NERSC.jpg"
imageAlt: "Armarios de servidores en un centro de datos"
---

La agencia de ciberseguridad de Estados Unidos (CISA) añadió el 20 de noviembre tres vulnerabilidades críticas a su catálogo de fallos explotados activamente (KEV). Las tres tienen una puntuación CVSS de 9,8 y se pueden aprovechar sin credenciales. Si administras alguno de estos productos, esto va antes que cualquier otra tarea de la semana.

## 1. VMware vCenter: CVE-2026-123890

Es un fallo de omisión de autenticación: un atacante con acceso de red a vCenter puede saltarse el inicio de sesión. Era un zero-day, es decir, se estaba usando antes de que existiera parche.

Google Mandiant ha vinculado la explotación con Armory Castle, un grupo que se sospecha ligado a China (antes conocido como UNC5221). Según la revisión semanal de Senthorus, el grupo usó una herramienta propia llamada BONESAW para robar la base de datos de vCenter y el material de firma SAML. Con eso falsificó autenticaciones y llegó a la infraestructura ESXi. La explotación viene de septiembre. The Hacker News añade que se encadenó con un fallo de BeyondTrust Remote Support (CVE-2026-102764, CVSS 9,3), también corregido.

Qué hacer:

- Actualiza a vCenter 9.1.1.0200, 9.0.2.0200 u 8.0 U3m. Broadcom publicó los parches el 19 de noviembre.
- La versión 7.0 ya no tiene soporte general y no hay parche público: planifica la migración y, mientras tanto, limita al máximo quién puede llegar a vCenter por red.
- Revisa si hay cuentas de administrador SSO que nadie reconozca.

## 2. Cisco Expressway: CVE-2026-76466

Cisco Expressway incluía credenciales fijas en el código. Un atacante remoto con acceso de red puede ejecutar comandos como root en equipos en clúster a través del servicio de base de datos. La firma F6 informó de una intrusión real en una organización rusa después de que se publicara una prueba de concepto. No se ha atribuido a ningún grupo.

Qué hacer: aplica la actualización que Cisco publicó en octubre y no dejes expuestos a Internet los servicios de administración.

## 3. Apache Roller: CVE-2026-129448

Apache Roller es un motor de blogs en Java. El fallo está en la deserialización de datos que llegan por el endpoint XML-RPC antes de iniciar sesión, y permite ejecutar código en el servidor. Apache ha reconocido que se está explotando, sin dar detalles.

Qué hacer: actualiza a la versión 6.1.6 (afecta de la 4.0.0 a la 6.1.5). Si no usas XML-RPC, desactívalo.

## Otras actualizaciones importantes de la semana

- PHP publicó el 19 de noviembre las versiones 8.2.36, 8.3.37, 8.4.28 y 8.5.13, que corrigen siete fallos graves.
- NGINX corrigió el 18 de noviembre varios fallos en HTTP/2. Uno de ellos, CVE-2026-123007, tiene prueba de concepto pública.
- F5 publicó correcciones para seis fallos críticos en BIG-IP. No consta que se estén explotando.

Si no sabes cómo leer estos avisos ni cómo decidir qué parchear primero, te lo explicamos en [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [The Hacker News, 21 de noviembre de 2026](https://thehackernews.com/2026/11/hackers-exploit-critical-vmware-cisco.html)
- [Senthorus, revisión semanal del 16 al 22 de noviembre](https://blog.senthorus.ch/posts/weekly_reviews/23_11_2026)
- [Resumen de altas en el catálogo KEV de CISA, 16 a 22 de noviembre](https://dev.to/devaland/actively-exploited-this-week-9-new-cisa-kev-entries-16-november-to-22-november-2026-49al)
- [The Layman Security, 22 de noviembre de 2026](https://thelaymansecurity.com/cybersecurity-news-this-week-2026-11-22/)
