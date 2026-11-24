---
title: "Fallo en Azure API Management: roban secretos de clientes y llega a Equinor"
description: "Un fallo en Azure API Management Classic se usó para robar claves y secretos, con Equinor y Skagerak Energi entre las víctimas. Qué versiones afecta y qué rotar ya."
date: 2026-11-24T20:59:00+01:00
category: vulnerabilidades
tags: [Microsoft, Azure, Azure API Management, Equinor, Noruega, robo de credenciales, nube]
author: Redacción
photo: "File:Wenatchee washington azure datacenter aerial 1.jpg"
imageAlt: "Vista aérea de los centros de datos de Microsoft Azure en Wenatchee, Washington"
---

Un fallo en Azure API Management, el servicio de Microsoft que hace de puerta de entrada a las API de miles de empresas, ha sido aprovechado para robar claves, tokens y otros secretos guardados por los clientes. Microsoft detectó el problema el 18 de noviembre y cerró la vía de acceso al día siguiente, pero el arreglo no invalida lo que ya se hubiera llevado el atacante. La autoridad de seguridad noruega (NSM) relaciona el fallo con los ciberataques de la semana pasada contra las energéticas Equinor y Skagerak Energi, y avisa de que también hay víctimas fuera de Noruega. Si tu organización usa las versiones Classic del servicio, toca revisar y rotar credenciales.

## Qué ha pasado con Azure API Management

Según el aviso que Microsoft ha enviado a sus clientes a través del portal de Azure, citado por The Hacker News y Help Net Security, el 18 de noviembre la compañía identificó un "problema de seguridad" en los niveles Classic de API Management. Un tercero sin autorización podía llegar a funciones de administración y leer los secretos almacenados en las instancias que no estuvieran configuradas según las buenas prácticas documentadas por Microsoft. El 19 de noviembre Microsoft cerró ese acceso y, donde hizo falta, renovó las claves que gestiona ella misma.

Lo que podía quedar expuesto es justo lo más delicado de una pasarela de API: los llamados *named values* (variables que a menudo guardan contraseñas), los secretos de clientes OAuth y OpenID Connect, las claves de suscripción y tokens de la API de gestión. Con ellos, un atacante puede llamar a los servicios internos que hay detrás de la pasarela con los mismos permisos que la propia empresa.

Microsoft no ha publicado un identificador CVE ni ha dicho cuántos clientes están afectados. The Register, que tuvo acceso al aviso, señala que la compañía lo calificó como crítico.

## La conexión con los ataques a Equinor y Skagerak Energi

Equinor, la petrolera estatal noruega, anunció el 17 de noviembre que había detectado un ciberataque que afectó a servicios internos, sin impacto en la producción ni indicios de robo de datos. Un día después, Skagerak Energi, una eléctrica del sureste del país, informó de un intento de ataque contra sus sistemas informáticos.

Ahora la NSM ha atribuido ambos incidentes a este fallo y explica que fue el propio sector energético noruego el que dio la voz de alarma. En palabras del organismo, "un actor desconocido ha estado buscando activamente tokens de acceso, secretos y named values en APIM", y "todavía no está claro hasta dónde llega la explotación". Nadie ha atribuido de momento la campaña a ningún grupo o país.

## ¿Estoy afectado?

- **Afectados**: los niveles Developer, Basic, Standard y Premium de API Management Classic.
- **No afectados**: el nivel Consumption de Classic y todos los niveles v2.
- **Más expuestas**: las instancias sin la integración de red que recomienda Microsoft y las que guardan los secretos dentro de APIM en lugar de en Azure Key Vault.

Microsoft asegura que sus instancias ya están corregidas y que el cliente no tiene que instalar nada. La NSM recomienda aun así comprobar que la instancia ejecuta la versión de runtime 0.52.31936 o superior, o 0.53.31938 o superior, y contactar con Microsoft si no es así.

## Qué hacer: rotar secretos en Azure API Management

La recomendación de Microsoft y de la NSM coincide: dar por comprometido lo que estuviera guardado en la instancia y actuar en consecuencia.

1. **Rotar todos los secretos**: claves de suscripción, named values con contraseñas, credenciales de backends, secretos OAuth/OpenID Connect y cadenas de conexión (por ejemplo, las de Event Hubs).
2. **Hacerlo en el orden correcto**: crear la credencial nueva en el servicio que la emite, actualizarla en API Management, probar las API y solo entonces revocar la antigua. Microsoft recuerda que cambiar el valor en APIM no revoca la credencial vieja en su origen.
3. **Revisar los registros** de API Management y de los sistemas a los que daban acceso esas credenciales desde mediados de noviembre.
4. **Buscar cambios que no reconozcas**: suscripciones, usuarios, políticas o backends que nadie de tu equipo haya creado.
5. **Reducir el riesgo a futuro**: usar identidades administradas donde se pueda y guardar los secretos en Azure Key Vault, referenciados desde APIM.

Las organizaciones noruegas comprometidas deben avisar a la NSM. En España, las empresas pueden notificar el incidente a INCIBE-CERT y, si es una administración o un operador esencial, al CCN-CERT.

## Una semana complicada para la nube de Microsoft

Es el segundo problema de seguridad en servicios gestionados de Microsoft en pocos días, después del [fallo en Microsoft Entra Connect Health](/fallo-microsoft-entra-connect-health/) que expuso datos de administradores de inquilinos. En los dos casos el cliente no podía evitar el fallo, solo limitar el daño, lo que refuerza una idea básica: los secretos deben tener los mínimos permisos posibles y caducar pronto. Si quieres repasar cómo se catalogan y priorizan estos fallos, lo explicamos en [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [The Hacker News: Microsoft fixes Azure API Management Classic flaw as actor targets customer secrets](https://thehackernews.com/2026/11/microsoft-fixes-azure-api-management.html)
- [Help Net Security: Azure API Management vulnerability exploited to steal customers' secrets](https://www.helpnetsecurity.com/2026/11/24/azure-apim-vulnerability-credential-theft/)
- [The Register: Norway links energy firm cyberattacks to critical Azure API Management flaw](https://www.theregister.com/security/2026/11/23/norway-links-energy-firm-cyberattacks-to-critical-azure-api-management-flaw/5311598)
- [NSM: medidas frente a la vulnerabilidad de Azure API Management (en noruego)](https://nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management)
- [Microsoft Tech Community: Rotating credentials in Azure API Management](https://techcommunity.microsoft.com/blog/integrationsonazureblog/rotating-credentials-in-azure-api-management/4575478)
- [The Record: Cyberattack hits Norwegian energy giant Equinor](https://therecord.media/norway-equinor-cyberattack-energy)
