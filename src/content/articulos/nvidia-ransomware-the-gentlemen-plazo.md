---
title: "NVIDIA y el ransomware The Gentlemen: hoy vence el plazo de extorsión"
description: "Ransomware The Gentlemen contra NVIDIA: el grupo amenaza con publicar datos hoy, 28 de noviembre. NVIDIA dice que sus sistemas no están afectados. Lo que se sabe."
date: 2026-11-28T02:59:00+01:00
category: noticias
tags: [NVIDIA, ransomware, The Gentlemen, Storm-2697, extorsión, proveedores, cadena de suministro]
author: Redacción
photo: "File:NVIDIA Headquarters.jpg"
imageAlt: "Sede de NVIDIA en Santa Clara (California), empresa a la que el ransomware The Gentlemen amenaza con filtrar datos"
---

El grupo de ransomware The Gentlemen ha puesto a NVIDIA en su web de filtraciones y fija para hoy, 28 de noviembre, el final de la cuenta atrás tras la cual dice que publicará los datos supuestamente robados. El fabricante de chips, el más valioso del mundo por capitalización bursátil, asegura que no ha encontrado indicios de que sus propios sistemas hayan sido comprometidos y que investiga un posible incidente en un socio externo. Hasta ahora, los delincuentes no han mostrado ninguna prueba.

## Qué ha pasado con NVIDIA y The Gentlemen

La entrada apareció el 18 de noviembre en el portal que el grupo mantiene en la red Tor, donde exhibe a sus víctimas para presionarlas a pagar. A diferencia de otros casos, no incluye muestras de archivos, descripción de lo robado ni volumen de datos. Solo el nombre de la empresa y un contador.

NVIDIA respondió a BleepingComputer con un mensaje breve: "No hemos encontrado indicios de que los sistemas o las redes de NVIDIA se hayan visto afectados. Seguimos vigilando la situación". La compañía añadió que analiza un incidente "que puede haber afectado a un socio externo", sin identificarlo.

Ese matiz es importante. Los grupos de ransomware a menudo atribuyen a una gran marca los datos que han robado a un proveedor, un distribuidor o un fabricante de componentes, porque el nombre conocido da más visibilidad y aumenta la presión. En octubre, The Gentlemen ya reivindicó el robo de más de 9 TB a Jentech Precision Industrial, una empresa taiwanesa que se presenta como socia del ecosistema de servidores MGX de NVIDIA. No hay confirmación de que ambos casos estén relacionados.

## ¿Quién es The Gentlemen?

Microsoft sigue a sus operadores con el nombre de Storm-2697. Según el análisis que publicó en mayo su equipo de inteligencia de amenazas, el grupo apareció a mediados de 2025 como una banda cerrada y en septiembre de ese año empezó a funcionar como ransomware como servicio: alquila su programa a afiliados que hacen los ataques a cambio de una parte del rescate. Ofrece hasta el 90 % del botín, por encima del 70-80 % habitual, y se ha asociado con el foro BreachForums para reclutar intrusos y vendedores de accesos.

Practica la doble extorsión: cifra los equipos y, además, roba datos para amenazar con publicarlos. Dice tener más de 1.100 víctimas en sectores como la industria, la sanidad, el transporte, la energía, la educación y la banca, una cifra que no se ha verificado de forma independiente.

Su cifrador, escrito en Go, intenta desactivar Microsoft Defender, borra las instantáneas de volumen y los registros de eventos, y tiene un modo de propagación que recorre la red con herramientas legítimas de administración como PsExec, WMI o WinRM. Microsoft lo describe como un programa que pasa de cifrar un equipo a comportarse como "un gusano que se propaga solo".

## ¿Corren riesgo los usuarios de NVIDIA?

Con la información disponible, no hay motivo para que los usuarios de tarjetas gráficas, controladores o servicios como GeForce NOW cambien nada. NVIDIA niega que sus redes estén afectadas y el grupo no ha dado detalles. Si hoy se publican datos, habrá que ver de quién son realmente: si pertenecen a un proveedor, lo previsible son documentos técnicos o comerciales y no cuentas de clientes.

Lo que sí conviene es desconfiar de correos que aprovechen el ruido mediático, por ejemplo falsos avisos de "actualización urgente de controladores" o de "restablecimiento de cuenta NVIDIA". Los controladores solo deben descargarse desde la web oficial o la aplicación de NVIDIA. Si tienes dudas sobre un mensaje, repasa [cómo detectar un correo de phishing](/como-detectar-phishing/).

## Qué deben revisar las empresas

El caso vuelve a poner el foco en la cadena de suministro: una gran empresa puede tener sus sistemas en orden y aun así ver datos suyos expuestos a través de un socio. Las recomendaciones de Microsoft frente a este ransomware sirven para cualquier organización:

- Activar la protección contra manipulación del antivirus, para que el atacante no pueda apagarlo.
- Usar reglas de reducción de la superficie de ataque que bloqueen la creación de procesos desde PsExec y WMI.
- Activar el acceso controlado a carpetas y el EDR en modo bloqueo.
- Revisar qué datos se comparten con proveedores y exigirles autenticación multifactor y avisos rápidos en caso de incidente.

Si tu empresa ha sufrido un incidente, en Brecha Cero explicamos [qué hacer si tus datos aparecen en una filtración](/datos-en-filtracion-que-hacer/).

Actualizaremos esta noticia si el grupo publica datos o NVIDIA da más información.

## Fuentes

- [BleepingComputer: NVIDIA investigating Gentlemen ransomware breach claims](https://www.bleepingcomputer.com/news/security/nvidia-investigating-gentlemen-ransomware-breach-claims/)
- [Microsoft Threat Intelligence: The Gentlemen ransomware, dissecting a self-propagating Go encryptor](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/)
- [Wccftech: NVIDIA faces ransomware extortion threat](https://wccftech.com/nvidia-faces-ransomware-extortion-threat-as-hackers-threaten-to-leak-stolen-data-on-november-28-company-investigates-possible-partner-breach/)
