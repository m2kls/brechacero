---
title: "Fallos en SolarWinds Serv-U: la versión 2026.4 corrige 9 críticos"
description: "SolarWinds Serv-U 2026.4 corrige 18 fallos, nueve críticos y dos que dan acceso root en Linux. Qué versiones están afectadas y cómo actualizar sin riesgos."
date: 2026-11-26T08:55:00+01:00
category: vulnerabilidades
tags: [SolarWinds, Serv-U, FTP, transferencia de archivos, parches, Linux]
author: Redacción
photo: "File:Wikimedia Foundation Servers-8055 35.jpg"
imageAlt: "Servidores en un centro de datos, como los que alojan servidores de transferencia de archivos Serv-U"
---

**SolarWinds** ha publicado **Serv-U 2026.4**, una actualización de su servidor de transferencia de archivos (FTP, FTPS, SFTP y HTTPS) que corrige **18 vulnerabilidades en Serv-U**, **nueve de ellas críticas** con una puntuación de 9,1 sobre 10. Dos de esos fallos críticos permiten llegar a **root en servidores Linux**. La versión salió el 24 de noviembre y, según las notas de la versión, no hay constancia de que ninguno de los fallos se esté explotando, pero conviene actualizar cuanto antes: Serv-U es un objetivo habitual de los atacantes.

## Qué corrige Serv-U 2026.4

Los nueve fallos críticos llegaron a SolarWinds a través del programa de recompensas por errores de **Intigriti**. La mayoría son escaladas de privilegios: alguien que ya tiene una cuenta con cierto nivel de administración puede acabar controlando el servidor entero.

- **CVE-2026-82322** (9,1): referencia directa insegura a objetos (IDOR). Un administrador de grupo de un dominio puede convertirse en administrador de todo el servidor Serv-U.
- **CVE-2026-123172** y **CVE-2026-123168** (9,1): escaladas de privilegios que acaban en **root en Linux**.
- **CVE-2026-123167** (9,1): recorrido de rutas (*path traversal*) que también permite elevar privilegios.
- **CVE-2026-82320** y **CVE-2026-82321** (9,1): confusiones de tipo que permiten escalar privilegios.
- **CVE-2026-82315**, **CVE-2026-82316** y **CVE-2026-82319** (9,1): condiciones de carrera al acceder a archivos.

Entre los fallos menos graves hay una inyección de comandos solo en Windows (CVE-2026-123166, 7,2), un error de lógica de negocio (CVE-2026-82313, 8,4), una lectura fuera de límites en el intercambio de claves SSH (CVE-2026-123173), un XSS almacenado, una denegación de servicio y varios problemas en el inicio de sesión: posibilidad de probar contraseñas por fuerza bruta, de adivinar y reutilizar códigos de verificación en dos pasos y de averiguar qué nombres de usuario existen. Si quieres saber cómo se leen estas puntuaciones, lo contamos en [qué es una CVE y cómo se mide su gravedad](/que-es-una-cve/).

La actualización trae otros cambios de seguridad: incorpora **OpenSSL 3.5 LTS** (y corrige con ello 11 fallos de esa biblioteca), restringe cifrados SSH antiguos en modo FIPS y deja de escribir los códigos de verificación en dos pasos en los registros.

## ¿A quién afecta?

A cualquier organización con Serv-U MFT o Serv-U FTP Server en una versión anterior a la 2026.4, tanto en Windows como en Linux. SolarWinds considera que el impacto es menor en Windows, pero recomienda actualizar en ambos sistemas.

Que haga falta una cuenta con privilegios para aprovechar la mayoría de los fallos no los convierte en poco importantes. En un ataque real, el delincuente suele entrar primero con credenciales robadas o reutilizadas y después busca escalones como estos para hacerse con el servidor. Por eso los fallos de inicio de sesión corregidos en esta versión, aunque tengan nota media, también cuentan.

Además, los servidores de transferencia de archivos son un blanco muy rentable: concentran documentos de clientes y suelen estar expuestos a internet. Serv-U ya sufrió en 2024 un fallo de recorrido de rutas (CVE-2024-28995) que la agencia estadounidense CISA añadió a su catálogo de vulnerabilidades explotadas, y este año SolarWinds ha publicado otras dos tandas de parches críticos para el producto, en febrero y en julio.

## Cómo actualizar Serv-U de forma segura

1. **Actualiza a Serv-U 2026.4**, empezando por los servidores Linux accesibles desde internet.
2. **Haz copia de seguridad** de la configuración antes de actualizar, siguiendo la guía de actualización de SolarWinds. Si te saltas versiones, revisa también las notas de las intermedias.
3. **Comprueba después** que el servidor indica la versión 2026.4 y que el inicio de sesión y las transferencias funcionan.
4. **Revisa la actividad reciente**: cambios de administradores, cuentas nuevas y archivos inesperados. Parchear no dice si el servidor ya estaba comprometido.
5. **Limita la exposición**: deja la consola de administración solo en la red interna, activa la verificación en dos pasos para todas las cuentas y usa contraseñas únicas. Tienes una guía en [cómo proteger tus cuentas con contraseñas fuertes y 2FA](/proteger-cuentas-contrasenas-2fa/).

Para quien gestione otros programas de alojamiento o transferencia, esta semana también hubo parches importantes en [WHMCS](/fallo-whmcs-inyeccion-sql/) y en [GeoServer](/fallos-geoserver-explotados-parche/).

## Fuentes

- [Serv-U 2026.4 release notes (SolarWinds)](https://documentation.solarwinds.com/en/Success_Center/servu/Content/release_notes/servu_2026-4_release_notes.htm)
- [Critical SolarWinds Serv-U Flaws Could Let Hackers Gain Root Access (Cyber Security News)](https://cybersecuritynews.com/critical-solarwinds-serv-u-flaws)
- [SolarWinds patches four critical Serv-U flaws enabling root access (Security Affairs, febrero de 2026)](https://securityaffairs.com/188454/hacking/solarwinds-patches-four-critical-serv-u-flaws-enabling-root-access.html)
