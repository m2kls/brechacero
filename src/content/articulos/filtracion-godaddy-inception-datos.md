---
title: "Filtración de GoDaddy: Inception publica 37,5 GB de datos internos"
description: "El grupo Inception publica 37,5 GB que atribuye a GoDaddy, con vídeos de reuniones y código. Es la segunda reclamación en un mes. Qué se sabe y cómo protegerte."
date: 2026-11-27T18:58:00+01:00
category: noticias
tags: [GoDaddy, Inception, filtración, extorsión, ShinyHunters, vishing, dominios]
author: Redacción
photo: "File:Godaddy Logo.jpg"
imageAlt: "Logotipo de GoDaddy, el registrador de dominios que aparece en la web de filtraciones de Inception"
---

El grupo de extorsión Inception ha publicado en su web de filtraciones unos **37,5 GB de archivos que atribuye a GoDaddy**, uno de los mayores registradores de dominios y proveedores de alojamiento web del mundo. La publicación apareció el 26 de noviembre y la han analizado este viernes 27 los investigadores de Cybernews. Según ese análisis, la mayor parte son grabaciones de reuniones internas y documentos corporativos con fechas de entre 2020 y 2024. GoDaddy no ha confirmado ningún incidente ni ha publicado comunicado alguno.

Es la segunda vez en menos de un mes que un grupo criminal dice tener datos de la compañía: el 1 de noviembre otro actor, Whitearmor, aseguró haber robado registros de empleados de una plataforma de centro de llamadas que usa GoDaddy.

## Qué contiene la supuesta filtración de GoDaddy

Según Cybernews, el paquete publicado por Inception tiene unos 10.800 archivos y se reparte así:

- **Unos 25 GB de vídeos** de reuniones internas y de encuentros generales de plantilla (*all hands*).
- Documentos de Office y PDF, en su mayoría protegidos con cifrado de gestión de derechos (IRM), lo que limita su lectura.
- Configuraciones internas de su *data lake* y unos **570 archivos de código** en Go y TypeScript.
- **9,6 GB de fotos y vídeos personales**.
- De acuerdo con los atacantes, nombres de empleados, conversaciones de chat y datos de retribuciones.

Los investigadores apuntan que el material trata sobre todo de estrategia de marca y podría proceder de una copia de seguridad antigua y cifrada. Esa antigüedad reduce el impacto, aunque advierten de que sigue siendo una exposición potencialmente relevante para la empresa. Inception no ha indicado cuándo entró en los sistemas ni cuánto dinero pedía.

## La otra reclamación: Whitearmor y el centro de llamadas

El portal especializado WebHosting.Today recuerda que el 1 de noviembre el grupo Whitearmor publicó una ficha titulada "AmplifAI (GoDaddy instance)". AmplifAI vende software de gestión del rendimiento y formación para centros de atención al cliente. Whitearmor dice tener una base de datos con **13.565 usuarios**, registros de inicio de sesión, listados de personal, 227 programas del centro de llamadas y detalles de cómo esa plataforma se conecta con el inicio de sesión único (SSO) de GoDaddy. Su anuncio no menciona datos de clientes.

Ninguna de las dos reclamaciones está verificada de forma independiente y, a 27 de noviembre, el apartado de prensa de GoDaddy no recoge ninguna de ellas.

## ¿Quién es Inception?

La web de filtraciones de Inception apareció a mediados de noviembre y ya acumula alrededor de una docena de supuestas víctimas, entre ellas AMD, PepsiCo, Cigna o McDonald's. En Brecha Cero ya contamos su ataque a [Burger King y su matriz RBI](/hackeo-burger-king-rbi-inception-datos-clientes/).

El equipo de inteligencia de Okta relaciona el grupo con un clúster que, con mucha probabilidad, procede del entorno de ShinyHunters y que se especializa en el *vishing*: llamadas en las que se hacen pasar por el soporte técnico para robar credenciales y códigos de un solo uso. Inception lo niega. Lo explicamos con detalle en [el informe de Okta sobre ShinyHunters e Inception](/okta-shinyhunters-inception-vishing/).

## ¿Estoy afectado si tengo un dominio o una web en GoDaddy?

Con lo publicado hasta ahora, **no hay indicios de que se hayan expuesto datos de clientes**, contraseñas de cuentas ni información de pago. El material parece interno y antiguo. Aun así, GoDaddy gestiona decenas de millones de dominios, y cualquier noticia sobre la empresa es un buen anzuelo para los estafadores.

Lo razonable si eres cliente:

- **Desconfía de correos o llamadas "de GoDaddy"** que hablen de esta filtración, de renovar un dominio con urgencia o de verificar tu cuenta. Entra siempre escribiendo tú la dirección en el navegador. Repasa las señales en nuestra guía para [detectar un correo de phishing](/como-detectar-phishing/).
- **Activa la verificación en dos pasos** en tu cuenta y, si es posible, usa una llave de seguridad o una *passkey*, que son las que resisten este tipo de engaños. Tienes los pasos en [cómo proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/).
- **Activa el bloqueo de transferencia del dominio** y revisa que el correo de contacto del registro sea uno que controlas.
- Si eres empresa, recuerda a tu plantilla que el soporte técnico real no pide códigos por teléfono.

Actualizaremos esta noticia si GoDaddy confirma o desmiente el incidente.

## Fuentes

- Cybernews: [Hackers post alleged GoDaddy data leak, including hours of internal meeting videos](https://cybernews.com/security/godaddy-data-leak-inception-ransomware/)
- WebHosting.Today: [GoDaddy faces two extortion claims, one with a 37.5 GB leak](https://webhosting.today/2026/11/27/godaddy-faces-two-extortion-claims-one-with-a-37-5-gb-leak/)
- The IT Nerd: [Hackers leak alleged GoDaddy data, including 25GB of internal meeting recordings](https://itnerd.blog/2026/11/27/hackers-leak-alleged-godaddy-data-including-25gb-of-internal-meeting-recordings/)
- Ransomware.live: [ficha de GoDaddy en la web de Inception](https://www.ransomware.live/id/R29EYWRkeUBJbmNlcHRpb24)
