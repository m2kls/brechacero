---
title: "Filtración en Cleverbridge: roban números de tarjeta y CVV de clientes"
description: "Cleverbridge, la pasarela de pago de muchas tiendas de software, confirma el robo de números de tarjeta con su CVV. Quién está afectado y qué hacer ya."
date: 2026-11-24T17:20:00+01:00
category: noticias
tags: [Cleverbridge, filtración de datos, tarjetas de crédito, CVV, fraude, pagos online]
author: Redacción
photo: "File:Bunch of credit cards (49860171753).jpg"
imageAlt: "Varias tarjetas de crédito, el tipo de dato robado en la filtración de Cleverbridge"
---

La filtración en Cleverbridge es de las que conviene mirar con calma si has comprado software por internet en los últimos meses. La empresa alemana, que gestiona los pagos online de cientos de fabricantes de programas y servicios en la nube, ha confirmado que un tercero no autorizado copió datos de tarjetas de pago guardados en su plataforma: el número, la fecha de caducidad y el código de seguridad (CVV o CVC). Con esos tres datos se pueden hacer compras por internet, así que el riesgo de fraude es real.

## Qué ha pasado en Cleverbridge

Según la propia compañía, detectó actividad no autorizada en su plataforma el 4 de noviembre de 2026, cortó el acceso y volvió a poner sus sistemas en marcha ese mismo día. Cleverbridge asegura que no se trata de un ataque de ransomware, porque ninguno de sus sistemas llegó a cifrarse. Lo que no ha explicado es cómo entraron los atacantes ni cuánto tiempo estuvieron dentro.

Los avisos a las personas afectadas empezaron a enviarse el 20 de noviembre, más de dos semanas después de detectar el problema. La empresa dice que ha informado a las autoridades de protección de datos, a las marcas de tarjetas y a sus socios de pago, y que colabora con una unidad policial especializada en cibercrimen.

Hay un detalle que ha llamado la atención en el sector. Las normas de seguridad de la industria de tarjetas (PCI DSS) prohíben guardar el código CVV una vez autorizado el pago, ni siquiera cifrado. Cleverbridge no ha aclarado si esos códigos estaban almacenados o si se capturaron mientras se procesaban los pagos, como ocurre en los ataques de tipo *skimming* web.

## ¿Qué datos se han robado?

Según las notificaciones que han recibido los clientes:

- Número de la tarjeta de pago.
- Fecha de caducidad.
- Código de seguridad CVV/CVC.

Las fuentes no coinciden del todo en el resto. The Register, que ha visto uno de los correos, indica que también podrían estar expuestos datos de contacto como el correo electrónico, la dirección de facturación y el teléfono. Otras informaciones recogen que el aviso descarta el acceso a nombres o direcciones. Cleverbridge sí afirma que las contraseñas de las cuentas no se han visto afectadas. No ha dicho cuántas personas están afectadas.

## ¿Estoy afectado por la filtración de Cleverbridge?

Es difícil saberlo a simple vista, porque Cleverbridge actúa como intermediario: muchas veces el cargo aparece en el extracto con el nombre de Cleverbridge, pero tú compraste a otra marca. Entre los clientes que la empresa muestra en su web figuran fabricantes conocidos como Tenable, Jamf, Veeam, Red Hat o Sony, y algunos medios citan también a SUSE, Parallels o Plesk. Eso no significa que los compradores de todas esas marcas estén afectados: Cleverbridge no ha dicho qué tiendas concretas se vieron comprometidas.

La forma más fiable de saberlo es revisar si has recibido un correo de Cleverbridge sobre el incidente y buscar en tus extractos cargos con su nombre. La compañía opera en más de 240 países, así que también hay clientes europeos, aunque no ha dado cifras por país.

## Qué hacer si compraste a través de Cleverbridge

1. **Revisa los movimientos de tu tarjeta** de las últimas semanas y comunica a tu banco cualquier cargo que no reconozcas.
2. **Llama a tu banco** y cuéntale lo ocurrido. Lo más prudente es pedir que bloqueen la tarjeta y te envíen una nueva con otro número: con el número y el CVV robados, cambiar la contraseña no sirve de nada.
3. Activa las notificaciones de cada compra en la app del banco y, si es posible, usa tarjetas virtuales o de un solo uso para comprar online.
4. Desconfía de correos, SMS o llamadas que hablen de esta filtración y te pidan datos de la tarjeta, códigos o contraseñas. Las filtraciones suelen ir seguidas de campañas de phishing que se aprovechan del susto; repasa las señales en nuestra guía para [detectar el phishing](/como-detectar-phishing/).
5. Si en el aviso te ofrecen servicios de vigilancia, accede escribiendo tú la dirección oficial, nunca desde un enlace de un mensaje que no esperabas.

Si tus datos han aparecido en otras filtraciones, tienes más pasos en [qué hacer si tus datos están en una filtración](/datos-en-filtracion-que-hacer/). Y para cualquier duda, el 017 de INCIBE atiende gratis consultas de ciberseguridad.

## Lo que aún no se sabe

Faltan respuestas importantes: cuántas tarjetas se han robado, qué tiendas concretas estaban afectadas y por qué había códigos CVV accesibles para los atacantes. Actualizaremos esta noticia si Cleverbridge o las autoridades dan más datos.

## Fuentes

- [BleepingComputer: Cleverbridge warns hackers stole credit card numbers, CVVs in data breach](https://www.bleepingcomputer.com/news/security/cleverbridge-warns-hackers-stole-credit-card-numbers-cvvs-in-data-breach/)
- [The Register: Cleverbridge admits attackers stole customers' credit card and CVV numbers](https://www.theregister.com/cyber-crime/2026/11/23/cleverbridge-admits-attackers-stole-customers-credit-card-and-cvv-numbers-yep-you-read-that-right/5311573)
- [Infosecurity Magazine: Cleverbridge confirms customers' payment card data breached](https://www.infosecurity-magazine.com/news/cleverbridge-payment-card-breached/)
- [Cleverbridge: actualización sobre el incidente](https://grow.cleverbridge.com/incident-update)
