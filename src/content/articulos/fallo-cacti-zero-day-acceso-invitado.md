---
title: "Fallo zero-day en Cacti 1.2.31: el acceso de invitado permite tomar el servidor"
description: "Un fallo zero-day en Cacti 1.2.31, aún sin parche ni CVE, permite ejecutar comandos sin contraseña si el usuario invitado está activo. Cómo protegerte hoy."
date: 2026-11-27T10:57:00+01:00
category: vulnerabilidades
tags: [Cacti, zero-day, vulnerabilidades, monitorización de redes, inyección SQL, servidores, Linux]
author: Redacción
photo: "File:Cacti (software) screenshot.png"
imageAlt: "Captura de Cacti, la herramienta de monitorización de redes afectada por un fallo zero-day"
---

Un investigador ha publicado los detalles y una prueba de concepto de un **fallo zero-day en Cacti 1.2.31**, la última versión de esta popular herramienta de código abierto para monitorizar redes. El error permite a un atacante sin usuario ni contraseña ejecutar comandos en el servidor, pero solo cuando el administrador ha activado la cuenta de invitado. Se hizo público el 26 de noviembre, todavía no tiene identificador CVE y, según las informaciones publicadas, no hay parche oficial.

## Qué es Cacti y por qué importa este fallo

Cacti se usa desde hace más de veinte años para dibujar gráficas del tráfico y el estado de routers, switches, servidores y enlaces. Es habitual en proveedores de internet, universidades, administraciones y departamentos de sistemas de todo tipo de empresas, también en España. Para hacer su trabajo, Cacti suele guardar credenciales SNMP y otros datos de acceso a los equipos de red que vigila, así que un servidor de Cacti comprometido es una muy buena puerta de entrada al resto de la infraestructura.

El investigador, que firma como "ek0ms savi0r", ha bautizado el problema con nombres como 4HTTP2ROOT, porque bastan cuatro peticiones web para llegar a ejecutar órdenes en el sistema. The Hacker News y la firma watchTowr se han hecho eco del hallazgo, y la empresa Previdian asegura haber reproducido el resultado en laboratorio.

## Cómo funciona el fallo de Cacti (sin entrar en detalles)

A grandes rasgos, se trata de una **inyección SQL de segundo orden**: el usuario invitado puede guardar en uno de sus ajustes un valor que debería ser un número y no lo es. Ese valor no se valida bien, acaba metido en una consulta a la base de datos y, más tarde, el proceso que recoge las métricas (el *poller*) ejecuta un comando almacenado en esa base de datos. La suma de varios descuidos pequeños termina en ejecución de código con los permisos del usuario con el que corre Cacti.

Si Cacti se ejecuta como root, el atacante obtiene control total del servidor. Si corre con un usuario sin privilegios, el daño es menor, pero sigue pudiendo leer las credenciales de los equipos monitorizados o alterar los datos para que no salten las alertas. Si quieres repasar en qué consiste este tipo de ataque, lo explicamos en [qué es una inyección SQL y cómo se previene](/que-es-inyeccion-sql/).

## ¿Estoy afectado?

Lo estás si se cumplen dos condiciones:

- Usas **Cacti 1.2.31** (el alcance en versiones anteriores todavía no está claro).
- Tienes **activado el acceso de invitado**, que permite ver gráficas sin iniciar sesión. Viene desactivado por defecto, pero muchos administradores lo encienden para compartir paneles con otros equipos o mostrarlos en una pantalla.

A día 27 de noviembre no se conocen ataques reales que aprovechen este fallo de Cacti, pero hay una prueba de concepto pública, y eso suele acelerar los intentos de explotación en cuestión de días. Por ahora no existe CVE ni puntuación oficial; cuando se asigne, te ayudará a medir la gravedad nuestra guía sobre [qué es una CVE y cómo leer su puntuación](/que-es-una-cve/).

## Cómo protegerte mientras no haya parche

1. **Desactiva la cuenta de invitado.** En la configuración de autenticación de Cacti, quita el usuario invitado y desactívalo también en la gestión de usuarios. Después abre una ventana privada del navegador y comprueba que ya no se puede ver nada sin iniciar sesión.
2. **No expongas Cacti a internet.** Limita el acceso a la interfaz web a la red de gestión o a una VPN con autenticación.
3. **No lo ejecutes como root.** Cacti y su *poller* deberían correr con un usuario sin privilegios.
4. **Revisa la configuración y los procesos.** Busca valores extraños en los ajustes de usuario y en la configuración del *poller*, y procesos inesperados lanzados por el usuario de Cacti.
5. **Si sospechas una intrusión**, cambia todas las credenciales SNMP, SSH o de otros servicios que Cacti tuviera guardadas y revisa los equipos de red a los que podía acceder.

Desactivar el invitado corta la vía de ataque demostrada, pero no corrige el error de fondo, así que conviene estar pendiente de los avisos de seguridad del proyecto en GitHub y actualizar en cuanto salga la versión corregida. Es la misma pauta que recomendábamos esta semana con [los fallos de GeoServer ya explotados](/fallos-geoserver-explotados-parche/): lo que está expuesto a internet, primero.

## Fuentes

- [The Hacker News: Unpatched Cacti Zero-Day Enables RCE in Just Four HTTP Requests via Guest Access](https://thehackernews.com/2026/11/unpatched-cacti-zero-day-enables-rce-in.html)
- [Cryptika: Cacti 4HTTP2ROOT Zero-Day Lets Hackers Execute Commands on Network Monitoring Servers Without Login](https://www.cryptika.com/cacti-4http2root-zero-day-lets-hackers-execute-commands-on-network-monitoring-servers-without-login/)
- [Cacti: avisos de seguridad del proyecto en GitHub](https://github.com/Cacti/cacti/security/advisories)
