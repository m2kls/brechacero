---
title: "BADBOX 3.0: la botnet escondida en TV box Android baratos bate récords"
description: "BADBOX 3.0 usa TV box y tablets Android sin marca para un fraude publicitario récord y para convertirlos en proxies. Cómo saber si tu dispositivo es seguro."
date: 2026-11-24T18:58:00+01:00
category: noticias
tags: [BADBOX 3.0, Android, TV box, botnet, fraude publicitario, malware, HUMAN Security]
author: Redacción
photo: "File:DroidBOX Android Kodi TV Box.JPG"
imageAlt: "TV box Android con Kodi, el tipo de aparato que usa la botnet BADBOX 3.0"
---

BADBOX 3.0 es la nueva versión de una botnet que vive dentro de reproductores multimedia Android baratos, los TV box sin marca conocida que se venden por pocos euros en tiendas online. El equipo de investigación Satori, de la empresa HUMAN Security, ha publicado esta semana un informe que la describe como la mayor operación de fraude publicitario conocida: en su pico llegó a generar unos 40.000 millones de peticiones de anuncios al día. Además, los aparatos infectados se alquilan como proxies residenciales, lo que puede poner la conexión de tu casa al servicio de terceros.

## Qué es BADBOX 3.0

BADBOX afecta sobre todo a dispositivos con Android de código abierto (AOSP) fabricados por marcas poco conocidas: TV box, tablets, móviles económicos y proyectores. En muchos casos el malware viene instalado de fábrica o llega con la primera actualización, así que el comprador no hace nada mal: simplemente enchufa el aparato.

Según HUMAN, la versión 3.0 incorpora módulos que imitan los kits de anuncios de vídeo de las aplicaciones de streaming legítimas. El aparato reproduce anuncios en ventanas ocultas, sin que el usuario vea nada, y se hace pasar por apps reales para cobrar a los anunciantes. En su momento de mayor actividad supuso más del 4 % de todo el tráfico de televisión conectada que analiza la empresa, más de tres veces el anterior récord, el de la operación VASTFLUX.

## Tu TV box como proxy de otros

La otra parte del negocio es menos visible y más preocupante para el usuario. Los dispositivos infectados se inscriben en once redes de proxies residenciales. Eso significa que otras personas pueden navegar a través de tu conexión a internet: si alguien la usa para cometer fraudes o ataques, la dirección IP que aparecerá será la de tu casa.

Los investigadores han relacionado el catálogo de malware con TXCZ, un fabricante chino de electrónica, aunque aclaran que eso no demuestra que la empresa sepa o participe en la operación. Los operadores reparten sus módulos a través de repositorios públicos y redes de distribución de contenido para resistir los intentos de cierre.

## Un problema que vuelve una y otra vez

No es la primera vez. En 2025, Google, HUMAN y otros socios desmantelaron parte de BADBOX 2.0, que había infectado más de 10 millones de dispositivos en todo el mundo, y el FBI llegó a pedir a los usuarios que desconectaran los aparatos sospechosos. Otra operación liderada por Google acabó con la red XCPE, con más de un millón de equipos. Cada vez que se tumba la infraestructura, el malware sigue en los aparatos vendidos y los operadores lo reactivan con otra versión.

## ¿Cómo saber si mi TV box Android está infectado?

No es fácil, porque el fraude publicitario es invisible. Algunas señales que deben hacerte sospechar:

- El aparato **no tiene certificación Google Play Protect**. Puedes comprobarlo en Play Store > tu perfil > Ajustes > Información > "Certificación de Play Protect".
- Viene con una **tienda de aplicaciones alternativa** o pide desactivar protecciones para instalar apps.
- Se calienta, va lento o consume datos **aunque no lo estés usando**.
- La marca o el modelo no aparecen en ninguna web oficial, y el precio es sospechosamente bajo para lo que promete.

## Cómo protegerte

1. **Compra dispositivos de marcas conocidas** y, en el caso de los TV box, prefiere modelos con Android TV o Google TV certificados.
2. **Instala aplicaciones solo de la tienda oficial**. Las apps "piratas" para ver fútbol o series son una vía de entrada habitual.
3. **Si tienes un aparato sin certificar que se comporta de forma rara, desconéctalo** y deja de usarlo. Formatearlo no sirve si el malware viene en el firmware.
4. **Separa los dispositivos del hogar** en la red de invitados del router, para que un aparato infectado no vea tu ordenador ni tu móvil.

Si quieres entender mejor qué pasa dentro de tu red, puedes empezar por nuestra guía de [Wireshark para principiantes](/wireshark-para-principiantes/) o por saber [qué es un puerto en redes](/que-es-un-puerto-redes/).

## Fuentes

- [HUMAN Security (Satori): BADBOX 3.0 hides the largest ad fraud operation ever disclosed inside infected TV boxes](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-3-0-hides-the-largest-ad-fraud-operation-ever-disclosed-inside-infected-tv-boxes/)
- [Security Affairs: BADBOX 3.0 exposed, massive botnet hides ad fraud inside Android TV boxes](https://securityaffairs.com/203767/malware/badbox-3-0-exposed-massive-botnet-hides-ad-fraud-inside-android-tv-boxes.html)
- [HUMAN Security: disrupción de BADBOX 2.0](https://www.humansecurity.com/learn/blog/satori-threat-intelligence-disruption-badbox-2-0/)
