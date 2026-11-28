---
title: "Filtración en SafePal: el monedero cripto amplía a 37.542 pedidos más"
description: "SafePal amplía su filtración de datos: 37.542 pedidos más de su tienda, con nombres y correos expuestos. Qué datos hay en riesgo y cómo evitar el phishing que llega."
date: 2026-11-28T08:59:00+01:00
category: noticias
tags: [SafePal, filtración, criptomonedas, monedero hardware, phishing, datos personales]
author: Redacción
photo: "File:Trezor Model T.jpg"
imageAlt: "Monedero hardware de criptomonedas, el tipo de dispositivo que vende SafePal en la tienda afectada por la filtración"
---

La filtración de datos de SafePal, fabricante de monederos de criptomonedas, es más grande de lo que la empresa contó en agosto. SafePal actualizó el 28 de noviembre su informe del incidente para añadir 37.542 registros de pedidos pagados con criptomonedas entre el 6 de septiembre de 2022 y el 1 de marzo de 2025. Incluyen nombres, correos electrónicos, países, productos comprados e identificadores de pedido y de pago. La compañía insiste en que es el mismo incidente y en que no se han expuesto claves privadas ni frases de recuperación.

## Qué ha pasado en SafePal

Según el informe de SafePal, recogido por DeFi Prime, el origen fue un fallo de autorización en un complemento de seguimiento de pedidos de su tienda online: con él, una persona podía ver los datos de pedidos de otros clientes. La empresa recibió un primer aviso "compatible con el problema" a principios de mayo y lo hizo público en agosto. Aquel primer alcance cubría pedidos del 2 de marzo de 2025 al 11 de abril de 2026, de unos 39.798 clientes, y entonces sí incluía direcciones de envío y teléfonos.

La revisión posterior encontró un segundo problema: un error de configuración impidió que una tarea programada de borrado de datos antiguos funcionara entre septiembre de 2025 y abril de 2026. Por eso seguían almacenados, y expuestos, pedidos más antiguos que debían haberse eliminado. "Lamentamos sinceramente que este alcance adicional no se identificara durante nuestra investigación inicial", reconoce la empresa.

## ¿Qué datos se han filtrado y cuáles no?

En el nuevo grupo de 37.542 registros (son pedidos, no personas: hay devoluciones, compras repetidas y pedidos fallidos) aparecen:

- nombre y correo electrónico,
- país,
- número de pedido, producto comprado e identificador del pago.

No incluye dirección de envío ni teléfono, aunque sí estaban en la primera tanda. SafePal asegura que en ningún caso se expusieron credenciales del monedero, datos de tarjeta o cuenta bancaria, direcciones de pago en cripto, frases semilla ni claves privadas. La auditoría de la firma Cure53, publicada el 30 de octubre, no encontró vulnerabilidades en sus productos, según la empresa.

Hay un detalle incómodo: SafePal no puede avisar por correo a este grupo porque ya había borrado los datos de contacto de su sistema. Si compraste en su tienda en esas fechas pagando con criptomonedas, da por hecho que tus datos pueden estar afectados.

## El riesgo real: phishing dirigido a dueños de criptomonedas

Saber que alguien ha comprado un monedero de criptomonedas, con su nombre y su correo, es oro para los estafadores. SafePal ya avisó el 12 de noviembre de cartas de phishing con códigos QR enviadas a clientes. El objetivo de estas campañas es siempre el mismo: que la víctima escriba su frase de recuperación en una web falsa o instale un firmware manipulado.

## Cómo protegerte

- **Nunca escribas tu frase semilla ni tu clave privada** en una web, un formulario o un chat. SafePal recuerda que sus correos auténticos nunca la piden, ni exigen verificaciones urgentes ni actualizaciones de firmware mediante un enlace.
- **Desconfía de cartas, correos o SMS** que mencionen tu pedido o tu dispositivo y te pidan escanear un QR. Aprende a reconocerlos con nuestra guía sobre [cómo detectar el phishing](/como-detectar-phishing/).
- **Actualiza el firmware solo desde la app oficial** o el dispositivo, nunca desde un enlace recibido.
- **Si ya introdujiste la frase semilla en algún sitio sospechoso**, trata el monedero como comprometido: crea uno nuevo con un dispositivo de confianza o la app oficial, mueve tus fondos y contacta con el soporte oficial.
- Según SafePal, no hace falta mover los fondos solo porque se haya filtrado el pedido.
- Comprueba si tu correo aparece en otras filtraciones con nuestra guía para [saber si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/).

No es el primer caso de este tipo en el sector: esta semana contamos la [filtración en el exchange Bithumb](/filtracion-bithumb-pasaportes-cuentas-bancarias/), donde los atacantes estuvieron dentro durante dos semanas.

## Fuentes

- SafePal: [Security update](https://www.safepal.com/blog/security-update)
- SafePal: [Scam protection](https://www.safepal.com/scam-protection)
- DeFi Prime: [SafePal expands breach disclosure to 37,542 earlier order records](https://defiprime.com/safepal-expands-order-data-breach)
