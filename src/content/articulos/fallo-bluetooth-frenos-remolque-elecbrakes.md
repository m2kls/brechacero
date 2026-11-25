---
title: "Fallo Bluetooth en frenos de remolque Elecbrakes: podían activarse a distancia"
description: "Tres fallos en los controladores de freno Bluetooth de Elecbrakes permitían frenar o soltar un remolque a 100 metros sin contraseña. Qué modelos tienen parche y cuál no."
date: 2026-11-25T12:54:00+01:00
category: vulnerabilidades
tags: [Elecbrakes, Bluetooth, remolques, vehículos conectados, CISA, IoT]
author: Redacción
photo: "File:Mustang & Caravan.jpg"
imageAlt: "Coche remolcando una caravana, el tipo de remolque que usa controladores de freno Bluetooth como los de Elecbrakes"
---

Un fallo Bluetooth en los controladores de freno de remolque de la marca australiana Elecbrakes permitía a cualquiera que estuviera a menos de unos 100 metros activar o soltar los frenos de un remolque, o cambiar su fuerza de frenado, sin necesidad de contraseña ni de que el conductor hiciera nada. Los investigadores de Element Digital encontraron tres vulnerabilidades en los modelos EB2, VM1 y ELBC 2000, y la agencia estadounidense CISA publicó un aviso el 19 de noviembre. Dos de los modelos ya tienen parche; el ELBC 2000, todavía no.

Estos dispositivos se usan sobre todo en Australia y Nueva Zelanda para caravanas y remolques pesados, pero el caso es un buen ejemplo de lo que pasa cuando se añade conectividad a un sistema de seguridad física sin protegerla bien.

## Qué fallos tienen los frenos Bluetooth de Elecbrakes

Los controladores de freno de remolque regulan la fuerza con la que frena el remolque en función de cómo frena el coche. Los de Elecbrakes se configuran y manejan desde una aplicación móvil por Bluetooth o con un mando.

Element Digital, que contó con ayuda de herramientas de inteligencia artificial en su análisis, identificó tres problemas:

- **Falta de autenticación** (crítico): el controlador aceptaba órdenes de cualquier dispositivo cercano, sin comprobar que fuera el teléfono del propietario.
- **Protección insuficiente frente a ataques de repetición** (crítico): una orden legítima capturada por radio podía reenviarse más tarde.
- **Debilidad en el mecanismo de actualización del firmware** (gravedad media): los propios investigadores reconocen que su impacto es teórico y no lo demostraron por completo.

Combinados, los dos primeros permitían a un atacante dentro del alcance del Bluetooth bloquear los frenos del remolque mientras el coche sigue acelerando. Los investigadores lo resumen con crudeza: es "la receta exacta" para que el conjunto haga la tijera, uno de los accidentes más peligrosos con remolque.

No hay constancia de que nadie haya aprovechado estos fallos fuera del laboratorio.

## ¿Estoy afectado?

Si tienes un controlador de freno Elecbrakes, depende del modelo:

- **EB2 y VM1**: Elecbrakes publicó actualizaciones de firmware a principios de julio. Una vez instaladas, el control remoto exige un emparejamiento inicial que requiere acceso físico al equipo. La empresa dice que avisó a unos 40.000 usuarios de su aplicación y que entre el 60 y el 70 % de los controladores que se usan a diario ya tienen la actualización.
- **ELBC 2000**: no hay solución todavía. El fabricante recomienda mantener el controlador conectado al teléfono o al mando mientras se usa, para que otro dispositivo no pueda tomar el control.

Los investigadores han criticado que el proceso de corrección fue lento (avisaron a la empresa a mediados de mayo) y que Elecbrakes tardó en reconocer que el ELBC 2000 también estaba afectado.

## Cómo protegerte si usas dispositivos conectados en el coche

Más allá de esta marca, cualquier accesorio Bluetooth que toque la seguridad del vehículo merece algo de atención:

1. Actualiza el firmware desde la aplicación oficial del fabricante y comprueba la versión instalada.
2. Mantén la conexión emparejada mientras conduces y no dejes el dispositivo en modo de emparejamiento abierto.
3. Desconfía de aplicaciones de terceros que prometan controlar el equipo.
4. Revisa los avisos de seguridad del fabricante, igual que harías con el móvil o el router. Si no sabes interpretar uno, te lo explicamos en [qué es una CVE y cómo leer un aviso de seguridad](/que-es-una-cve/).

El caso se suma a otros fallos en sistemas de frenado conectados, como los dispositivos de cola de tren sobre los que CISA ya alertó en 2025, y a la lista de equipos del internet de las cosas que llegan al mercado con la seguridad como asunto secundario, como los [TV box Android de la botnet BADBOX 3.0](/badbox-3-botnet-android-tv-box/).

## Fuentes

- [CISA: aviso ICSA-26-323-02 sobre Elecbrakes EB2, VM1 y ELBC2000](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-02)
- [Element Digital: Brake check, trailer brakes over Bluetooth](https://elementdigital.com.au/blog/brake-check-trailer-brakes-over-bluetooth/)
- [Elecbrakes: actualización de seguridad para sus controladores de freno](https://www.elecbrakes.com/news-and-articles/security-update-for-elecbrakes-brake-controllers)
- [SecurityWeek: Elecbrakes Bluetooth Vulnerabilities Expose Trailers to Forced Braking](https://www.securityweek.com/elecbrakes-bluetooth-vulnerabilities-expose-trailers-to-forced-braking/)
