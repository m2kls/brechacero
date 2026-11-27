---
title: "Fallo de privacidad en Bitcoin Core: vincular tu dirección a tu IP cuesta 35 céntimos"
description: "Un fallo de privacidad en Bitcoin Core permite ligar una dirección de Bitcoin a la IP del nodo que la vigila por menos de 35 céntimos. Quién está afectado."
date: 2026-11-27T06:56:00+01:00
category: privacidad
tags: [Bitcoin, Bitcoin Core, privacidad, criptomonedas, Tor, monederos]
author: Redacción
photo: "File:Bitcoin, Wroclaw (P1180334).jpg"
imageAlt: "Logotipo de Bitcoin en un cajero de criptomonedas en Breslavia, en una noticia sobre un fallo de privacidad de Bitcoin Core"
---

Un desarrollador de **Bitcoin Core** ha demostrado que es posible relacionar una dirección de Bitcoin con la **dirección IP** del nodo que la vigila gastando menos de **35 céntimos de dólar**. El fallo de privacidad lo ha descrito Abubakar Sadiq Ismail, colaborador del proyecto, en el foro técnico Delving Bitcoin el 25 de noviembre, y afecta al programa de referencia de la red y a muchos monederos que lo usan por debajo. No pone en riesgo los fondos, pero sí el anonimato de quien gestiona su propio nodo, algo especialmente delicado para periodistas, activistas o cualquier persona que guarde cantidades importantes.

## Qué ha descubierto el investigador

El problema está en una función pensada para ayudar: la **retransmisión del monedero**. Cuando una transacción del monedero lleva entre 12 y 36 horas sin confirmarse, Bitcoin Core vuelve a anunciarla a la red para que no se pierda. Lo hace también con los **pagos entrantes**, aunque el dueño del nodo no los haya enviado.

Ismail aprovecha ese comportamiento: un observador envía un pago diminuto, con comisión baja para que tarde en confirmarse, a una dirección que ya sospecha que pertenece a alguien. Después se conecta a los nodos candidatos y espera. El nodo que vuelva a anunciar esa transacción concreta es el que vigila la dirección, y con él queda al descubierto su IP pública.

En una red de pruebas privada, el método acertó **30 de 30 veces**. El coste estimado de cada intento, sumando el pago y la comisión, va de 18 a 34 céntimos según el tipo de dirección y el precio del bitcoin, aunque no incluye el gasto de vigilar la red. Todavía no se ha medido en la red real. El autor también simula que, por el orden en que se reciben los anuncios, se puede adivinar con alta probabilidad a qué otro nodo está conectado el afectado.

## ¿Estoy afectado por el fallo de Bitcoin Core?

Afecta a quien usa un **monedero conectado a su propio nodo de Bitcoin Core** (o de Bitcoin Knots), incluidos los monederos de solo lectura que únicamente vigilan direcciones. También pueden heredarlo programas que usan Core como motor, y el investigador cita Sparrow, Specter, Liana, Electrum Personal Server o JoinMarket como potencialmente afectados en esa configuración.

No afecta a quien usa un monedero móvil o de una plataforma de intercambio que no depende de un nodo propio. Y conviene matizar el alcance: una coincidencia identifica el **nodo que vigila la dirección**, no necesariamente a su dueño. Una IP por sí sola no identifica a una persona, aunque sí puede ser el primer paso para hacerlo con otros datos.

Tampoco basta con usar Tor a medias. Si el nodo se conecta a la vez por Tor y por la red normal, la IP pública puede quedar expuesta. Un nodo que solo use Tor evita mostrar la IP, pero la dirección sigue quedando ligada a su identidad en Tor.

## Cómo proteger tu privacidad

- **Desactiva la retransmisión** con la opción `-walletbroadcast=0`. El inconveniente es que el monedero deja de anunciar también tus propios pagos, así que tendrás que enviarlos a mano.
- **Usa solo Tor o I2P** (`-onlynet=onion` o `-onlynet=i2p`) si quieres que tu IP no aparezca, sabiendo que no rompe del todo el vínculo.
- **No reutilices direcciones**. El ataque necesita una dirección ya conocida, y usar una nueva para cada cobro reduce mucho el margen.
- **Estate atento a las próximas versiones**. Los desarrolladores debaten un cambio para que solo se retransmitan transacciones recién añadidas y otro, más completo, para que la retransmisión de pagos entrantes pase a ser opcional. Ninguno ha llegado aún a una versión publicada.

Si guardas criptomonedas, recuerda también que el mayor riesgo suele estar fuera de la red: estafas como el [timo rip deal con criptomonedas](/estafa-rip-deal-criptomonedas-barcelona/) o el robo de credenciales. Puedes comprobar si tus datos han aparecido en alguna brecha con nuestra guía para [saber si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/).

## Fuentes

- Delving Bitcoin: [Exploiting Wallet Rebroadcast to Link Addresses to Node IPs and More](https://delvingbitcoin.org/t/exploiting-wallet-rebroadcast-to-link-addresses-to-node-ips-and-more/3123)
- Cybersecurity News: [Bitcoin Privacy Flaw Could Let Hackers Trace Wallet Addresses to IP Addresses for Just 35 Cents](https://cybersecuritynews.com/bitcoin-privacy-flaw)
