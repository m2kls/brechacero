---
title: "Hackeo a la Fuerza Aérea de EE. UU.: entran en su nube Cloud One"
description: "Hackeo a la Fuerza Aérea de EE. UU.: intrusos accedieron al panel de control de Cloud One, su gran plataforma en la nube. Qué se sabe y qué datos están en riesgo."
date: 2026-11-27T14:58:00+01:00
category: noticias
tags: [Fuerza Aérea de EE. UU., Cloud One, hackeo, nube, Pentágono, Estados Unidos, ciberespionaje]
author: Redacción
photo: "File:The Pentagon January 2008.jpg"
imageAlt: "Vista aérea del Pentágono, sede del Departamento de Defensa y del mando de la Fuerza Aérea de EE. UU."
---

Unos atacantes han logrado entrar en **Cloud One**, la plataforma en la nube que la Fuerza Aérea de Estados Unidos usa como base para buena parte de sus aplicaciones. Lo ha publicado este viernes 27 de noviembre la agencia Reuters, que cita a varias fuentes con conocimiento del caso. El hackeo a la Fuerza Aérea se detectó durante el último mes, mientras se hacían trabajos de actualización del sistema, y podría afectar a datos tácticos, de personal y de logística. Ni la identidad de los atacantes ni el alcance real de la intrusión se conocen todavía.

## Qué es Cloud One y por qué importa este hackeo

Cloud One nació en 2017 como una especie de "ventanilla única" de informática para la Fuerza Aérea. Reúne recursos de los cuatro grandes proveedores de nube del país (Microsoft, Amazon, Oracle y Alphabet) y sobre ella funcionan aplicaciones de nóminas, gestión de personal, logística y mantenimiento de aeronaves.

Según Reuters, también aloja sistemas mucho más delicados. Uno de ellos es el mando y control en la nube que reúne datos de radares de defensa aérea de Norteamérica. Otro es el sistema que lleva el inventario de bombas y misiles en más de 200 instalaciones de la Fuerza Aérea. Hasta 2025 el contratista principal era SAIC; desde entonces la gestiona Leidos.

Por eso la noticia preocupa más que otras intrusiones en organismos públicos. Una sola plataforma concentra información muy variada, y quien la controle puede ver o tocar muchas aplicaciones a la vez.

## Cómo entraron los atacantes

Una de las fuentes de Reuters explica que los intrusos aprovecharon una vulnerabilidad de software para llegar al "plano de control" de la plataforma, la capa desde la que se administra todo lo demás. Esa fuente lo describió como un "mando a distancia universal". La agencia no ha podido identificar qué fallo se explotó ni si era ya conocido.

Tampoco está claro qué hicieron los atacantes una vez dentro. La misma fuente reconoce que no se sabe si llegaron a consultar el estado de los aviones o los movimientos de piezas de recambio, y Newsweek subraya que se desconoce qué datos, si es que hay alguno, se han robado.

## Efectos sobre la Fuerza Aérea

Aunque los datos sigan sin confirmarse, el incidente ya tiene consecuencias prácticas, siempre según las fuentes de Reuters:

- Se ha congelado la migración de aplicaciones administrativas a Cloud One.
- Se han bloqueado las actualizaciones de las aplicaciones que ya funcionan en la plataforma, lo que impide aplicar parches justo cuando se están publicando fallos nuevos.
- A algunos usuarios se les han retirado los permisos de administrador.
- El Mando Cibernético de EE. UU. (Cyber Command) participa en la evaluación de daños.

La Fuerza Aérea se limitó a responder que "no comenta la postura de seguridad, las vulnerabilidades ni el estado operativo" de redes y sistemas concretos. No es una confirmación, pero tampoco un desmentido. SAIC no respondió y Leidos remitió las preguntas al ejército.

## Otro golpe a la Administración estadounidense

El caso se suma a una racha de incidentes en organismos federales de EE. UU. En las últimas semanas hemos contado el [ataque al sistema NCIC del FBI](/ciberataque-fbi-ncic-usda/), el [acceso no autorizado a la red de FinCEN](/ciberataque-fincen-tesoro-eeuu/), dependiente del Tesoro, y el [hackeo a la CIA y la ODNI](/hackeo-cia-odni-informacion-no-clasificada/). Reuters cuenta al menos seis incidentes recientes además de este, entre ellos una filtración de datos de personal del Departamento de Seguridad Nacional.

Resulta llamativo que en 2023 los responsables de Cloud One presumieran de un "100 % de éxito" frente a un número "asombroso" de intentos de intrusión.

## Qué pueden aprender las empresas

Para el ciudadano de a pie no hay nada que hacer de momento: no se ha hablado de datos de civiles. Pero el caso deja lecciones útiles para cualquier organización que concentre sus servicios en una nube:

- **Proteger el plano de control como la joya de la corona.** Las consolas y API de administración de la nube deberían estar fuera de internet o tras accesos muy restringidos, con autenticación multifactor resistente al phishing y cuentas de administración separadas.
- **Parchear rápido lo que está expuesto.** Si la puerta fue un fallo de software, el tiempo entre la publicación de un parche y su instalación es decisivo. Nuestra guía sobre [qué es una CVE y cómo se mide su gravedad](/que-es-una-cve/) ayuda a priorizar.
- **Segmentar.** Que una sola credencial o un solo fallo no den acceso a todas las aplicaciones de la plataforma.
- **Registrar y revisar.** Guardar los registros de actividad del plano de control fuera de la propia nube permite reconstruir qué hizo un intruso, justo lo que ahora intenta averiguar la Fuerza Aérea.

Actualizaremos la noticia si el Pentágono o los contratistas aportan más datos.

## Fuentes

- [Reuters (vía ThePrint): Hackers breach US Air Force flagship Cloud One computing platform](https://theprint.in/world/exclusive-hackers-breach-us-air-force-flagship-cloud-one-computing-platform/3110997/)
- [CNBC: Hackers breach U.S. Air Force flagship Cloud One computing platform](https://www.cnbc.com/2026/11/27/hackers-breach-us-air-force-flagship-cloud-one-computing-platform.html)
- [Newsweek: US Air Force System Hacked—What Could Be At Risk?](https://www.newsweek.com/us-air-force-system-hacked-what-at-risk-12773327)
