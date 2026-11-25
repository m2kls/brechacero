---
title: "Volant Manticore: espías iraníes atacan aerolíneas y telecos de Chipre con KuboShell"
description: "Volant Manticore, grupo de espionaje iraní, usa CV falsos creados con IA y la puerta trasera KuboShell contra Chipre y hospitales saudíes. Cómo detectarlo."
date: 2026-11-25T06:54:00+01:00
category: noticias
tags: [Volant Manticore, Irán, KuboShell, MuddyWater, espionaje, Check Point, Chipre]
author: Redacción
photo: "File:LCA Terminal outside.jpg"
imageAlt: "Terminal del aeropuerto de Lárnaca, en Chipre, país cuyas aerolíneas y telecos ha atacado Volant Manticore"
---

Volant Manticore es el nombre que Check Point Research ha puesto a un grupo de ciberespionaje alineado con Irán que hasta ahora no estaba documentado. Según el análisis publicado el 24 de noviembre, el grupo lleva activo al menos desde finales de agosto de 2025 y ha atacado empresas de telecomunicaciones, aerolíneas e infraestructuras críticas de Chipre, además de entidades sanitarias de Arabia Saudí. Su herramienta principal es una puerta trasera nueva, KuboShell, que se comunica a través de la red descentralizada IPFS para pasar desapercibida.

## Quién está detrás de Volant Manticore

Check Point cree que el grupo está formado por antiguos operadores de MuddyWater, uno de los actores iraníes más conocidos, que se habrían separado para trabajar por su cuenta. Ambos se atribuyen al Ministerio de Inteligencia y Seguridad de Irán (MOIS). Esa herencia se nota en el código: además de KuboShell, usan Homa, un marco en JavaScript que reimplementa el cliente MuddyC2Go de MuddyWater.

Entre los objetivos citados están una aerolínea chipriota que opera vuelos entre Chipre e Israel y un organismo público chipriota relacionado con la defensa. En septiembre de 2026 el foco se desplazó a hospitales y entidades sanitarias de Arabia Saudí.

## Cómo engañan a sus víctimas

El grupo combina varias trampas, todas basadas en ingeniería social:

- **Currículos falsos con personajes creados por IA.** Los atacantes inventan candidatos con apariencia creíble y envían un enlace a su "currículum". Al abrirlo se instala KuboShell.
- **Documentos de Word con macros.** Un archivo llamado "MilitaryHeritageProposal.doc", dirigido al organismo de defensa chipriota, ejecutaba una puerta trasera en VBA si la víctima activaba las macros.
- **Seminarios ficticios sobre IA y sanidad.** En la campaña saudí enviaron archivos ZIP como "AI_Healthcare_Seminar.zip". Algunos correos salieron de la cuenta comprometida de un hospital privado saudí, lo que les daba credibilidad.
- **Robo de credenciales** de correo y corporativas haciéndose pasar por organizaciones legítimas.

Una vez dentro, instalan herramientas legítimas de administración remota (MeshCentral, NetLock RMM o N-able RMM) para mantener el acceso como si fueran técnicos de sistemas.

## Por qué KuboShell es difícil de ver

KuboShell es una puerta trasera para Windows que recibe órdenes a través de IPFS, el sistema de archivos distribuido, usando la pasarela del servicio Pinata. Para un cortafuegos, ese tráfico se parece al de un servicio web legítimo y no a un servidor de control clásico. El malware registra cada equipo por su dirección MAC, consulta nuevas órdenes cada 60 segundos y las ejecuta con PowerShell. También pide permisos de administrador mediante el aviso de Control de cuentas de usuario (UAC), un detalle que un usuario atento puede detectar.

## Cómo protegerse

Aunque es una campaña dirigida, sus técnicas son las mismas que usan muchos otros grupos:

- **Recursos humanos es un objetivo.** Los currículos que llegan como enlace a un servicio externo merecen la misma cautela que cualquier adjunto. Mejor pedirlos en PDF a través de un portal de empleo propio.
- **Bloquea las macros** de Office en documentos que vienen de internet mediante directivas de grupo.
- **Controla las herramientas de acceso remoto.** Mantén una lista de las RMM autorizadas y alerta de cualquier instalación nueva de MeshCentral, NetLock o similares.
- **Vigila el tráfico hacia pasarelas IPFS** si tu organización no las usa, y revisa ejecuciones de PowerShell lanzadas por procesos inusuales.
- **Forma a la plantilla** para que un correo de un remitente conocido no sea sinónimo de confianza: la cuenta puede estar comprometida.

Si quieres repasar las señales de alarma, tenemos una guía sobre [cómo detectar phishing](/como-detectar-phishing/) y otra sobre por qué [el phishing con IA ya no tiene faltas de ortografía](/phishing-con-ia/).

## Fuentes

- [Check Point Research: Volant Manticore, flying under the radar](https://research.checkpoint.com/2026/volant-manticore-flying-under-the-radar/)
- [The Hacker News: Iran-aligned Volant Manticore uses IPFS-based KuboShell backdoor in espionage campaigns](https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html)
