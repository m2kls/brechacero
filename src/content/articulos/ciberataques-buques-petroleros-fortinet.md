---
title: "Ciberataques a buques: EE. UU. investiga hasta 50 petroleros y gaseros"
description: "Ciberataques a buques: EE. UU. investiga intrusiones en hasta 50 barcos con carga peligrosa. Apuntan a cortafuegos Fortinet y a Irán, sin confirmar. Lo que se sabe."
date: 2026-11-25T14:55:00+01:00
category: noticias
tags: [ciberataques a buques, transporte marítimo, Fortinet, FortiBleed, Irán, Guardia Costera, OT]
author: Redacción
photo: "File:Oil tanker moored off Rotterdam.jpg"
imageAlt: "Petrolero fondeado frente a Rotterdam, imagen ilustrativa de los ciberataques a buques investigados en EE. UU."
---

Los ciberataques a buques mercantes se han convertido en una investigación de primer nivel en Estados Unidos. Según publicó el lunes The Wall Street Journal, las autoridades estadounidenses examinan intrusiones informáticas en hasta 50 barcos que transportan petróleo, gas licuado, productos químicos y otras cargas peligrosas. Irán aparece como principal sospechoso y Rusia también está bajo la lupa, aunque un alto cargo de la Administración ha dicho al mismo periódico que no hay pruebas de participación iraní. La noticia importa porque toca el punto débil de un sector que mueve la mayor parte del comercio mundial y que todavía conecta muchos sistemas de a bordo a internet sin la protección adecuada.

## Qué se sabe de los ciberataques a buques

Los incidentes descritos son variados: accesos a las redes de a bordo, amenazas de bomba, peticiones de rescate y mensajes que pedían a las tripulaciones no transportar productos estadounidenses. Algunos barcos podrían haber estado comprometidos sin que la tripulación lo supiera.

Equipos de ciberprotección de la Guardia Costera de EE. UU. se han desplegado en al menos cuatro buques que se acercaban a puertos del país, según la agencia Anadolu. En agosto, el FBI y la Guardia Costera ya habían abordado dos mercantes en el golfo de México tras detectar señales de que sus redes estaban comprometidas. Bloomberg, citando a fuentes oficiales, informó además de que los investigadores hallaron indicios de acceso al sistema de propulsión de un superpetrolero que se acercaba a la costa de Texas este verano.

Hay casos con nombre propio, como los petroleros VL Prosperity y Kohaku, inspeccionados por la Guardia Costera, o el metanero Vivit Africa, cuya tripulación no pudo acceder a algunos sistemas de control frente a Italia y acabó volviendo hacia Algeciras. En este último caso, la empresa Dragos dice no haber podido corroborar que se tratara de un ataque.

Conviene leer todo esto con cautela. Reuters no pudo verificar de inmediato la información del WSJ, Washington no ha atribuido públicamente los ataques y Security Affairs subraya que los informes no demuestran que nadie llegara a controlar la navegación o la propulsión de un barco. Un responsable citado por el WSJ calificó cuatro de los incidentes de "menores".

## ¿Por dónde entran? Cortafuegos Fortinet y contraseñas débiles

La principal sospecha apunta a cortafuegos y pasarelas VPN de Fortinet, los equipos que conectan el barco con tierra. Varios medios vinculan la actividad con una campaña bautizada como FortiBleed. El FBI y el Servicio Secreto la describieron en octubre como una campaña global de robo de credenciales con más de 86.000 dispositivos comprometidos en 194 países, cuyos accesos se revenden después a bandas de ransomware.

Fortinet sostiene que FortiBleed no explota fallos nuevos, sino contraseñas reutilizadas o débiles en equipos sin verificación en dos pasos. La alerta conjunta de la Guardia Costera y el FBI menciona, aun así, dos vulnerabilidades conocidas entre las más atacadas: CVE-2026-24858 y CVE-2025-25252. La firma de ciberseguridad marítima Cydome asegura que más de 250 empresas del sector aparecen en los datos de FortiBleed, aunque eso no significa necesariamente que hayan sido comprometidas.

## A quién afecta

El riesgo principal es para navieras, gestores de flota y operadores portuarios, también en España: Algeciras, Valencia o Barcelona reciben a diario buques de estas características. Un ataque que alcance los sistemas de carga o de propulsión de un petrolero o un gasero no es solo un problema informático, sino de seguridad física y medioambiental. Ya lo vimos en otros sectores industriales, como en el reciente [ciberataque a la mina de uranio de Peninsula Energy](/ciberataque-mina-uranio-peninsula-energy/).

## Cómo protegerse: recomendaciones para el sector

La alerta de la Guardia Costera y el FBI resume las medidas básicas, válidas para cualquier empresa con equipos expuestos a internet:

- Aplicar los parches pendientes en cortafuegos y VPN, y sustituir los equipos sin soporte. Si no sabes cómo priorizarlos, repasa [qué es una CVE y cómo leer su gravedad](/que-es-una-cve/).
- Revisar los registros de cortafuegos y VPN en busca de accesos extraños.
- Separar de verdad la red de oficina (IT) de los sistemas de control del barco (OT).
- Cambiar las contraseñas que puedan estar comprometidas y activar la verificación en dos pasos en todos los accesos remotos; te explicamos por qué en [cómo proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/).

En Estados Unidos, una nueva norma de la Guardia Costera obligará a buques con bandera estadounidense e instalaciones portuarias a designar un responsable de ciberseguridad y presentar un plan antes de julio de 2027.

## Fuentes

- [Tech Times: WSJ Says US Eyes Iran in Up to 50 Ship Hacks; Official Sees No Iranian Link](https://www.techtimes.com/articles/331483/20261125/tanker-cyberattacks-wsj-says-us-eyes-iran-50-ship-hacks-official-sees-no-iranian-link.htm)
- [Security Affairs: Maritime industry faces growing cyber threats as 50 ships targeted](https://securityaffairs.com/203918/intelligence/maritime-industry-faces-growing-cyber-threats-as-50-ships-targeted.html)
- [heise online: Up to 50 ships: U.S. suspects Iran behind cyberattacks on cargo vessels](https://www.heise.de/en/news/Up-to-50-ships-U-S-suspects-Iran-behind-cyberattacks-on-cargo-vessels-11535487.html)
