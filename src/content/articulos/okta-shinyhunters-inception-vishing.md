---
title: "Okta vincula a los de ShinyHunters con INCEPTION, una nueva web de filtraciones"
description: "Okta cree que el grupo de vishing ligado a ShinyHunters publica ahora datos robados en INCEPTION. Llaman haciéndose pasar por soporte técnico. Cómo frenarlo."
date: 2026-11-25T04:53:00+01:00
category: noticias
tags: [Okta, ShinyHunters, INCEPTION, vishing, robo de cuentas, passkeys, filtración de datos]
author: Redacción
photo: "File:Concerned Phone Call (Unsplash).jpg"
imageAlt: "Persona hablando por el móvil con gesto preocupado, como en las llamadas de vishing del grupo ligado a ShinyHunters"
---

El grupo de vishing (estafas por llamada telefónica) que trabajaba para ShinyHunters no ha desaparecido: se ha mudado. El equipo de inteligencia de amenazas de **Okta** publicó el 24 de noviembre que el grupo, al que sigue desde marzo con el nombre O-UNC-053, parece estar publicando ahora los datos que roba en una nueva web de filtraciones llamada **INCEPTION**. La web de ShinyHunters dejó de funcionar a finales de septiembre tras la detención de tres presuntos miembros, pero según Okta "los operadores siguen activos atacando a organizaciones con llamadas de voz y robos de cuentas".

## Cómo funcionan los ataques de vishing de ShinyHunters

El método es sencillo y eficaz. Los atacantes llaman a empleados de una empresa haciéndose pasar por el soporte técnico interno, les convencen de que hay un problema con su cuenta y les guían hasta una página falsa que imita el inicio de sesión corporativo (a menudo el de Okta u otro proveedor de inicio de sesión único). Mientras la víctima teclea su contraseña y aprueba la notificación del segundo factor, el atacante la usa en tiempo real para entrar. Una vez dentro, descarga datos de aplicaciones en la nube como Salesforce o herramientas internas y después extorsiona a la empresa amenazando con publicarlos.

Okta ha observado que las empresas atacadas aparecían en la web de filtraciones entre 1 y 28 días después de que se registraran los dominios de phishing usados contra ellas. A 16 de noviembre, INCEPTION ya mostraba datos de varias organizaciones que habían sido objetivo de O-UNC-053.

## Nuevo cebo: dominios con la palabra "legal"

La unidad de inteligencia de Palo Alto Networks, Unit 42, ha detectado desde octubre más de 70 dominios .com que contienen "legal-" o "-legal", en una campaña de vishing con temática jurídica: llamadas que hablan de supuestos requerimientos o documentos legales para meter prisa a la víctima. Es una variante del mismo truco de siempre, la urgencia, que explicamos en [cómo detectar el phishing](/como-detectar-phishing/).

Okta advierte de que no está claro si todos los datos publicados en INCEPTION son auténticos ni si la web la gestionan exactamente las mismas personas que estaban detrás de ShinyHunters. Por eso conviene tomar con cautela las reivindicaciones concretas hasta que las empresas afectadas las confirmen.

## ¿Estoy afectado?

El objetivo son empresas, no usuarios particulares, aunque los datos robados suelen incluir información de clientes. Si trabajas en una organización que usa inicio de sesión único (Okta, Microsoft Entra, Google Workspace), eres un posible objetivo de estas llamadas.

## Cómo protegerse del vishing

- **Llaves de acceso (passkeys) o FastPass.** Okta subraya que su kit de phishing no consigue saltarse los métodos resistentes al phishing, como las passkeys o Okta FastPass, porque están ligados al dominio legítimo. Es la medida más eficaz. Lo explicamos en [cómo proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/).
- **El soporte técnico nunca te pide la contraseña ni que apruebes una notificación por teléfono.** Ante una llamada así, cuelga y llama tú al número interno conocido.
- **Desconfía de la urgencia**: requerimientos legales, cuentas a punto de bloquearse o auditorías inminentes son excusas habituales.
- **Para los equipos de seguridad**: vigilar dominios recién registrados que imiten el nombre de la empresa, limitar quién puede registrar nuevos dispositivos de autenticación y alertar de inicios de sesión desde ubicaciones o dispositivos nuevos justo después de un restablecimiento de credenciales.

## Fuentes

- [Okta Threat Intelligence: Former ShinyHunters cluster moves to new INCEPTION site](https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/)
- [Unit 42 (Palo Alto Networks): Legal-themed vishing activity, 23-11-2026](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt)
- [The Hacker News: Okta Links ShinyHunters-Associated Vishing Group to New INCEPTION Data Leak Site](https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html)
