---
title: "Microsoft declara «Code Red» tras la caída de 24 horas de Outlook y Teams"
description: "Microsoft declara «Code Red» tras la peor caída de Exchange Online: 24 horas sin Outlook, Teams ni Copilot. Qué falló y por qué afecta a los parches de seguridad."
date: 2026-11-25T08:54:00+01:00
category: noticias
tags: [Microsoft, Code Red, Exchange Online, Outlook, Teams, Copilot, Microsoft 365]
author: Redacción
photo: "File:Building92microsoft.jpg"
imageAlt: "Edificio 92 del campus de Microsoft en Redmond, empresa que ha declarado «Code Red» tras la caída de Outlook y Teams"
---

Microsoft ha declarado un «Code Red» interno, su máxima prioridad de ingeniería, después de la caída de Exchange Online que dejó sin Outlook, Teams ni Copilot a millones de empresas durante unas 24 horas los días 12 y 13 de noviembre. Lo revelan memorandos internos a los que ha tenido acceso la agencia Reuters y que han recogido medios como The Next Web. La compañía asume que fue el incidente con más impacto para clientes en la historia de Exchange Online y se ha fijado un objetivo ambicioso: resolver cualquier incidente global en menos de una hora.

## Qué dicen los memorandos del «Code Red» de Microsoft

Jason Henderson, presidente de Microsoft 365 Core, escribió el viernes 20 de noviembre que se trataba del incidente «más impactante para los clientes» en la historia de Exchange Online. «Code Red significa que este es el trabajo de máxima prioridad para nuestro equipo», resumía. Henderson mantiene reuniones diarias con los responsables de Substrate, la plataforma que sostiene el correo y los datos de Microsoft 365, y revisiones semanales del avance.

Un segundo memorando, de Amanda Silver, vicepresidenta corporativa de M365 Core, describe la respuesta al incidente como una «niebla de guerra»: más de 11.000 mensajes repartidos en 11 chats de Teams y datos de diagnóstico dispersos en sistemas de seguimiento distintos. Silver cita además a Charles Lamanna, vicepresidente ejecutivo de Copilot, que reconoció que el componente que falló acumulaba «unos diez años de fallos aceptables».

## Qué provocó la caída de Outlook y Teams

Según Microsoft, el origen fue un defecto de escalabilidad en Windows introducido en julio que permaneció latente durante meses sin que nadie lo detectara. La empresa insiste en que no hubo ningún ciberataque ni intervino ningún agente de inteligencia artificial. Satya Nadella pidió disculpas públicamente.

El impacto fue global. Hubo administraciones afectadas en Australia, Japón y Estados Unidos, retrasos en empresas de inversión y problemas en las comunicaciones de aerolíneas. Para muchas organizaciones españolas, que dependen de Microsoft 365 para el correo y las reuniones, fue un día prácticamente sin herramientas de trabajo.

## Por qué importa para la seguridad

Aunque no fue un ataque, el «Code Red» tiene una lectura de ciberseguridad clara. Henderson admite en su memorando que los parches urgentes tardaron demasiado en llegar a los usuarios: una de las correcciones necesitó entre cinco y seis días. El objetivo ahora es que las correcciones de seguridad más urgentes se desplieguen en todo el mundo en una hora desde que se detecta el problema, y el propio directivo reconoce que Microsoft «todavía no está ahí».

Es un dato relevante en un mes en el que hemos visto [un zero-day explotado en Outlook](/outlook-zero-day-noviembre-2026/) y un [fallo en Microsoft Entra Connect Health que exponía datos de administradores](/fallo-microsoft-entra-connect-health/). Cuanto más tarda un parche en salir, más tiempo tienen los atacantes.

El plan se divide en cinco líneas de trabajo: reducción controlada de carga (load shedding) para que un fallo no tumbe todo el servicio, separación del tráfico por regiones, recuperación más rápida y nuevas herramientas, incluidos agentes de IA que ayuden a los ingenieros a interpretar los datos de salud del sistema.

## Qué pueden hacer las empresas

La caída de noviembre es un recordatorio de que la nube también falla, y de que la continuidad de negocio forma parte de la seguridad:

- **Ten un canal de comunicación alternativo** (teléfono, mensajería corporativa de otro proveedor) para avisar a la plantilla si Teams y el correo caen a la vez.
- **Sigue el estado oficial** en el Centro de administración de Microsoft 365 y en la página de estado del servicio, en vez de rumores en redes.
- **Desconfía de los correos que llegan justo después de una caída** pidiendo «volver a iniciar sesión» o «verificar la cuenta»: es un gancho clásico. Repasa [cómo detectar un phishing](/como-detectar-phishing/).
- **Documenta un plan de continuidad** que incluya cuánto tiempo puede trabajar la empresa sin correo.

## Fuentes

- [The Next Web: Microsoft declares 'Code Red' after its worst email outage, Reuters reports](https://thenextweb.com/news/microsoft-code-red-exchange-online-outage-memos-reuters)
- [Interesting Engineering: Microsoft declares Code Red after historic 24-hour outage](https://interestingengineering.com/culture/microsoft-code-red-24-hour-outage-engineering-overhaul)
- [Cybersecurity News: Microsoft Declares Code Red After Historic 24-Hour Outage](https://cybersecuritynews.com/microsoft-declares-code-red/)
