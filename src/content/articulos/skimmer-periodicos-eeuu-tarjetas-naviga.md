---
title: "Skimmer en 80 periódicos de EE. UU.: robaban tarjetas al pagar la suscripción"
description: "Un skimmer de tarjetas se coló en el pago de suscripciones de 80 periódicos de EE. UU., como el Boston Herald o el Denver Post. Quién está afectado y qué hacer."
date: 2026-11-26T04:58:00+01:00
category: noticias
tags: [skimmer, Magecart, tarjetas de crédito, Naviga, Payway, Boston Herald, Denver Post]
author: Redacción
photo: "File:Newspaper boxes on Cambridge Street, Boston Downtown (53819130907).jpg"
imageAlt: "Cajas de periódicos en una calle de Boston, ciudad del Boston Herald, uno de los diarios afectados por el skimmer de tarjetas"
---

Un **skimmer de tarjetas** estuvo escondido durante casi una semana en la página de pago de suscripciones de unos **80 periódicos de Estados Unidos**, entre ellos el Boston Herald, el Denver Post, el New York Daily News, Newsday o el Sun Sentinel. Lo ha descubierto Guardio Labs, que ha bautizado el caso como «PaperCut»: el código malicioso se activaba cuando el lector tecleaba el número de su tarjeta, la fecha de caducidad y el CVV para suscribirse o renovar. Las webs de los diarios no fueron hackeadas una a una; el fallo estaba en un componente compartido por todas.

## Cómo funcionaba el skimmer de los periódicos

Los diarios afectados usan para cobrar las suscripciones una plataforma de Naviga, y el formulario de la tarjeta lo sirve Payway, su proveedor de pagos. Según el informe de Guardio, alguien añadió **una sola línea** a esa plantilla de pago la mañana del 13 de noviembre. Esa línea cargaba un archivo alojado en GitHub y distribuido por la red jsDelivr, disfrazado de una versión antigua de jQuery, una biblioteca muy común en la web.

Ese archivo no contenía el código que roba las tarjetas, lo que le ayudaba a pasar desapercibido ante los escáneres. Lo que hacía era abrir una conexión WebRTC, la tecnología que usan las videollamadas del navegador, con un servidor del atacante. Ese servidor enviaba a cada visitante el skimmer real, de unos 2,7 KB, que nunca llegaba a guardarse en ningún archivo.

El código solo se activaba en páginas con un campo de número de tarjeta. Cuando el usuario pasaba el ratón por encima del botón de pagar, enviaba lo escrito en el formulario por ese canal WebRTC. Al no ser una petición web normal, las protecciones habituales, como la política de seguridad de contenidos (CSP), no la bloqueaban.

Guardio calcula que el archivo se descargaba unas **15.000 veces al día**, aunque esa cifra mide cargas del formulario, no tarjetas robadas. La empresa aclara que no introdujo ninguna tarjeta, así que el robo final se deduce del código que devolvía el servidor. Risky Business News sitúa el periodo activo entre el 13 y el 22 de noviembre; el informe de Guardio indica que la línea maliciosa se retiró tras su aviso a Payway, Naviga y los diarios.

## ¿Estoy afectado por el robo de tarjetas?

Puede estarlo cualquier persona que **escribiera los datos de su tarjeta** en la página de suscripción o de gestión del pago automático de uno de estos periódicos desde el 13 de noviembre. Aunque los diarios son estadounidenses, muchos lectores de fuera, también en España y Latinoamérica, se suscriben a cabeceras de EE. UU.

Además de la tarjeta, el skimmer podía llevarse el nombre, el correo, el teléfono y la dirección si el formulario los pedía.

Quien pagó con **Apple Pay, Google Pay o PayPal** no está afectado: esos botones abren el formulario del propio proveedor, fuera de la página manipulada.

Ni Naviga ni Payway habían publicado un comunicado detallado en el momento de escribir esta noticia, ni se sabe cuántas tarjetas llegaron a robarse.

## Qué hacer si pagaste una suscripción con tarjeta

- **Pide a tu banco una tarjeta nueva.** Guardio recomienda tratar la tarjeta como robada. Cambiarla en la cuenta del periódico no sirve, porque el skimmer copia lo que escribes.
- **Revisa los movimientos** de las últimas semanas. Los delincuentes suelen probar primero con cargos pequeños.
- **Desconfía de correos y llamadas** que mencionen tu suscripción o tu banco: con el correo y el teléfono robados es fácil preparar un engaño creíble. Te lo explicamos en nuestra guía para [detectar un correo de phishing](/como-detectar-phishing/).
- Activa las **notificaciones de cada pago** en la app del banco y, si puedes, usa tarjetas virtuales o monederos como Apple Pay o Google Pay para compras por internet.

El caso recuerda al reciente [robo de tarjetas y CVV en Cleverbridge](/cleverbridge-filtracion-tarjetas-cvv/): cuando el fallo está en un proveedor de pagos, el daño se multiplica por todas las tiendas que lo usan. En plena campaña de compras navideñas, conviene repasar también las [estafas típicas del Black Friday](/estafas-black-friday/).

## Una lección para las empresas

Para las organizaciones, la conclusión de Guardio es que no basta con vigilar la propia web: hay que controlar qué cargan los formularios de pago alojados por terceros, incluidas conexiones poco habituales como WebRTC, y revisar quién puede modificar esas plantillas.

## Fuentes

- [Guardio Labs: «PaperCut» – 80 US newspaper websites served a credit card stealer](https://guard.io/labs/papercut---80-us-newspaper-websites-served-a-credit-card-stealer)
- [Risky Business News: Card stealer found on 80 major US news sites](https://news.risky.biz/risky-bulletin-card-stealer-found-on-80-major-us-news-sites/)
