---
title: "Hackeo a Burger King: Inception dice tener datos de 126.000 clientes"
description: "El grupo Inception dice haber robado datos de 126.000 clientes de Burger King y de la atención al cliente de su matriz RBI. Qué se sabe y cómo protegerte."
date: 2026-11-26T16:58:00+01:00
category: noticias
tags: [Burger King, Restaurant Brands International, Inception, ransomware, filtración, Tim Hortons, Popeyes]
author: Redacción
photo: "File:Burger King in London.jpg"
imageAlt: "Restaurante de Burger King en Londres; su matriz RBI aparece en la web de filtraciones del grupo Inception"
---

El grupo de extorsión Inception asegura haber hackeado a Restaurant Brands International (RBI), la empresa canadiense propietaria de Burger King, Tim Hortons, Popeyes y Firehouse Subs. En la madrugada de este jueves 26 de noviembre añadió a RBI a su web de filtraciones y afirma tener datos de 126.038 clientes de Burger King en Estados Unidos, con nombres, datos de contacto, fechas de nacimiento y datos parciales de tarjeta. Da a la compañía 48 horas para negociar antes de publicarlo todo. RBI no ha confirmado el incidente.

## Qué dice haber robado Inception a Burger King

Según la ficha del grupo, recogida por el rastreador Ransomware.live a las 01:52 (hora UTC) y por Cybernews, el botín incluye:

- **126.038 clientes únicos de Burger King en EE. UU.**, extraídos "en directo", según los atacantes, de la herramienta interna de atención al cliente de la marca.
- **216.156 carpetas de incidencias** del servicio de atención al cliente de RBI (gestionado con ServiceNow), con correos, capturas de pantalla y datos de pedidos y pagos de clientes que presentaron quejas.
- Exportaciones de cuentas de OneDrive de empleados y de mensajes de Slack corporativos.

En total, el grupo habla de 234 GB, mientras que Cybernews menciona unos 800.000 archivos. Los atacantes dicen que el material abarca las cuatro marcas del grupo.

Hay que subrayar que **son afirmaciones de los delincuentes**. Inception no ha publicado muestras y el propio Ransomware.live advierte de que se trata de un grupo emergente cuyas reivindicaciones deben tomarse "con cautela hasta que se verifiquen de forma independiente". Cybernews pidió una valoración a RBI y no ha recibido respuesta.

## ¿Quién es Inception?

Inception es un grupo de extorsión de aparición reciente que en noviembre ha reivindicado ataques contra grandes empresas estadounidenses como PepsiCo, Paychex, Henry Schein, AutoZone o Lucid Motors. La semana pasada, Okta señaló posibles vínculos entre este grupo y ShinyHunters, conocido por sus campañas de [vishing para robar accesos a servicios en la nube](/okta-shinyhunters-inception-vishing/), algo que Inception niega. Si el robo es real, encajaría con ese patrón: los datos proceden sobre todo de plataformas SaaS de atención al cliente y colaboración, no de los sistemas de pago de los restaurantes.

## ¿Estoy afectado si he comprado en Burger King?

Por lo que se sabe, el robo afectaría a clientes de Estados Unidos que contactaron con el servicio de atención al cliente de Burger King (por ejemplo, para reclamar un pedido de la app o de entrega a domicilio). No hay ningún indicio de que afecte a clientes en España, donde Burger King opera mediante un franquiciado (Restaurant Brands Iberia) con sus propios sistemas.

Los "datos parciales de tarjeta" suelen ser los últimos cuatro dígitos y la caducidad, que no bastan para hacer compras. Su riesgo está en otro lado: combinados con nombre, fecha de nacimiento y el historial de una reclamación real, permiten fabricar engaños muy creíbles. Un correo del tipo "sobre su reclamación del pedido del día X, le devolvemos el importe, confirme su tarjeta" resulta mucho más convincente cuando el delincuente conoce los detalles.

## Cómo protegerte

- Desconfía de mensajes que digan venir de Burger King, Popeyes o Tim Hortons y ofrezcan reembolsos, cupones o "verificaciones" de tu tarjeta. Entra siempre por la app oficial, nunca por el enlace del mensaje. En nuestra guía sobre [cómo detectar el phishing](/como-detectar-phishing/) tienes las señales más habituales.
- Revisa los movimientos de la tarjeta que tengas guardada en la app y activa las notificaciones de pago del banco.
- Si usaste la misma contraseña en la app de Burger King y en otros servicios, cámbiala y activa la verificación en dos pasos donde puedas. Puedes comprobar si tu correo aparece en filtraciones conocidas con [estas herramientas](/saber-si-mi-contrasena-ha-sido-filtrada/).

## Un noviembre récord para la extorsión

El caso llega en un mes especialmente intenso: según los datos de Ransomware.live, la semana del 10 de noviembre fue la de más publicaciones en webs de filtraciones de todo 2026. Hace unos días otra cadena de comida rápida, McDonald's, reconoció una [filtración en su app en Japón](/filtracion-app-mcdonalds-japon/). Actualizaremos esta noticia si RBI confirma o desmiente el robo, o si el grupo publica los datos al vencer su plazo.

## Fuentes

- Cybernews: [Hackers claim Burger King, Tim Hortons, and Popeyes owner, some credit card data exposed](https://cybernews.com/security/burger-king-owner-ransomware-claims/)
- Ransomware.live: [Ficha de Restaurant Brands International (Inception)](https://www.ransomware.live/id/UmVzdGF1cmFudCBCcmFuZHMgSW50ZXJuYXRpb25hbCwgSW5jLkBJbmNlcHRpb24)
- QUE.com: [Burger King data published overnight: Inception ransomware leak caps a record November](https://que.com/burger-king-data-published-overnight-inception-ransomware-leak-caps-a-record-november/)
- SecurityWeek: [ShinyHunters claims comeback, new Inception group rejects alleged ties](https://www.securityweek.com/shinyhunters-claims-comeback-new-inception-group-rejects-alleged-ties/)
