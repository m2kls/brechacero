---
title: "Phishing GoodGuys: falsas entrevistas pagadas para robar cuentas de Google y Okta"
description: "La campaña de phishing GoodGuys ofrece hasta 600 dólares por entrevistas falsas de Nvidia, Accenture o Spotify para robar cuentas corporativas de Google y Okta."
date: 2026-11-26T23:01:00+01:00
category: noticias
tags: [phishing, GoodGuys, Google, Okta, robo de credenciales, MFA, Push Security]
author: Redacción
photo: "File:Woman smiling and using laptop during video call in cozy wooden room.jpg"
imageAlt: "Persona en una videollamada con su portátil, el tipo de entrevista falsa que usa la campaña de phishing GoodGuys"
---

Una campaña de **phishing bautizada como GoodGuys** está ofreciendo dinero por participar en entrevistas de expertos y seminarios web que no existen, con un único objetivo: robar las cuentas corporativas de Google y Okta de quien pica. La ha descubierto la empresa de seguridad Push Security, que la sigue desde el 13 de octubre, y la ha detallado este 26 de noviembre junto con BleepingComputer. Los atacantes se hacen pasar por ocho marcas muy conocidas: Accenture, American Express, Coca-Cola, Culver's, Google Cloud, Nvidia, SpaceX y Spotify.

## Cómo funciona el phishing de las falsas entrevistas

El gancho es económico. Los mensajes prometen hasta 600 dólares por una entrevista de 45 minutos con "expertos del sector", 500 dólares por participar en un supuesto estudio de Nvidia sobre inteligencia artificial o una plaza en un seminario de Google Cloud sobre cómo llevar aplicaciones de IA a producción. Es una propuesta creíble para perfiles técnicos y directivos, que reciben este tipo de invitaciones de forma legítima con cierta frecuencia.

Para que los correos lleguen a la bandeja de entrada y parezcan reales, los delincuentes abusan de plataformas legítimas de envío y de gestión de eventos y selección, como HireVue, SendGrid, Mandrill o Cvent. El enlace lleva a dominios que imitan a la marca suplantada, con el nombre de la empresa delante y una palabra genérica detrás (del estilo "nvidia.feedback-study.com" o "spotify.interview-experts.com").

Una vez dentro, la víctima pasa por un CAPTCHA, ve una página de presentación con la imagen de la empresa y se le pide **iniciar sesión con Google** para "confirmar la plaza". El kit rechaza las direcciones personales de Gmail, Yahoo y Outlook: solo le interesan las cuentas de empresa. También incluye formularios falsos de Okta, el servicio de inicio de sesión único que usan muchas compañías.

## Por qué la verificación en dos pasos no basta

GoodGuys no usa la técnica más sofisticada del momento (los kits AiTM, que se colocan entre la víctima y el servicio real), sino formularios falsos alojados en servidores de los atacantes. Lo llamativo es lo que viene después de escribir la contraseña: la página pide el código SMS, el de la aplicación autenticadora, el número que hay que pulsar en el móvil con Google o la notificación de Okta Verify. Push Security cree que hay una persona al otro lado iniciando sesión a mano en tiempo real y trasladando a la víctima cada desafío de verificación.

Es decir, si el usuario aprueba lo que le aparece en pantalla, el atacante entra en su cuenta aunque tenga activada la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/). Solo los métodos resistentes al phishing, como las llaves de seguridad físicas o las passkeys, cortan este tipo de ataque, porque están ligados al dominio real y no funcionan en una web falsa.

Los investigadores relacionan las técnicas con las campañas de vishing contra cuentas de Okta atribuidas este año a grupos del entorno de ShinyHunters, de las que ya [informamos al hablar de INCEPTION](/okta-shinyhunters-inception-vishing/), aunque no hay una atribución firme. También han visto otra campaña parecida, con falsas entrevistas de Coca-Cola y el kit Evilginx, dirigida a cuentas de Google Ads, sin poder vincularla con certeza a los mismos autores. Por las etiquetas ocultas del código ("Sign-in simulation"), sospechan que el kit se construyó con ayuda de un asistente de programación con IA, una tendencia que ya describimos en nuestro artículo sobre el [phishing creado con inteligencia artificial](/phishing-con-ia/).

## Cómo protegerte de las falsas invitaciones a entrevistas

- **Desconfía del dinero fácil.** Una invitación no solicitada que paga cientos de euros por media hora de conversación merece una comprobación antes de hacer clic.
- **Mira el dominio completo**, no solo el principio. "nvidia.algo-distinto.com" no es Nvidia. Si dudas, entra en la web oficial de la empresa escribiendo tú la dirección.
- **No inicies sesión con la cuenta del trabajo** en una página a la que has llegado desde un correo de este tipo. Un estudio o seminario legítimo rara vez necesita tu cuenta corporativa de Google u Okta.
- **No apruebes notificaciones ni copies códigos** que no esperas. Si te piden un código justo después de meter la contraseña en una web dudosa, para y avisa al equipo de seguridad.
- **Empresas:** prioricen las passkeys o llaves FIDO2 para las cuentas con más acceso, limiten el inicio de sesión a dispositivos gestionados y revisen los inicios de sesión de Google Workspace y Okta desde ubicaciones nuevas.

Si ya has introducido tus datos, cambia la contraseña desde la web oficial, cierra todas las sesiones abiertas y comunícalo cuanto antes a tu empresa. Nuestra guía para [detectar un correo de phishing](/como-detectar-phishing/) repasa el resto de señales de alerta.

## Fuentes

- [Push Security: Meet the GoodGuys, a fake expert interview phishing campaign](https://pushsecurity.com/blog/goodguys-phishing-campaign-teardown)
- [BleepingComputer: Fake paid expert interviews impersonate brands to steal Google logins](https://www.bleepingcomputer.com/news/apple/fake-paid-expert-interviews-impersonate-brands-to-steal-google-logins/)
