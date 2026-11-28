---
title: "Hackeo a SAP: roban tokens de empleados y alteran código en GitHub"
description: "Hackeo a SAP: la empresa confirma un incidente activo en el que se robaron tokens de empleados para copiar y modificar código en GitHub. Qué se sabe y qué revisar."
date: 2026-11-27T04:54:00+01:00
updated: 2026-11-28T06:55:00+01:00
category: noticias
tags: [SAP, hackeo, GitHub, código fuente, cadena de suministro, tokens, Alemania]
author: Redacción
photo: "File:Sap-wdf.jpg"
imageAlt: "Sede de SAP en Walldorf (Alemania), empresa que ha confirmado el hackeo de su código en GitHub"
---

SAP, la mayor empresa de software de Europa y proveedor de los sistemas de gestión de buena parte de las grandes compañías del mundo, ha confirmado un incidente de seguridad en su entorno de desarrollo. Según publicó el semanario alemán Der Spiegel el 26 de noviembre, unos atacantes robaron tokens de autenticación de empleados de SAP y los usaron para copiar y modificar código fuente alojado en GitHub. La empresa de Walldorf asegura que, por ahora, no hay indicios de acceso a datos de negocio de sus clientes.

## Qué se sabe del hackeo a SAP

SAP ha reconocido que detectó "actividad sospechosa" y que tomó medidas de inmediato para proteger a sus clientes y la seguridad de sus servicios. No ha respondido a preguntas detalladas. La información más concreta procede de una comunicación interna a la plantilla a la que tuvo acceso Der Spiegel, según la cual el incidente seguía activo y se investiga bajo el nombre en clave "Project Granite". Fuentes citadas por el semanario apuntan a que los atacantes podrían haber utilizado agentes de inteligencia artificial para automatizar parte de la intrusión, algo que SAP no ha confirmado.

Lo que no se sabe todavía es importante:

- Cómo obtuvieron los atacantes los tokens de los empleados.
- Qué repositorios se vieron afectados y si eran públicos o privados.
- Qué cambios exactos se introdujeron en el código y si alguno llegó a versiones publicadas o a productos que usan los clientes.

## Actualización: medidas de emergencia y aviso del BSI

Según informaciones de agencias de prensa recogidas por SOCRadar y The Next Web el 27 de noviembre, SAP habría restringido el acceso a GitHub, detenido procesos automatizados de desarrollo y sustituido claves de firma de software. La empresa no ha confirmado públicamente estas medidas ni ha publicado todavía instrucciones específicas para clientes. Una carta interna citada por SOCRadar sitúa la actividad sospechosa en GitHub y pide a la plantilla que revise sus credenciales.

El cambio de claves de firma es relevante: esas claves sirven para que los clientes comprueben que una actualización viene realmente de SAP. Sustituirlas es una precaución lógica si existe la mínima duda de que hayan podido quedar expuestas, y conviene estar atento a cualquier aviso de SAP sobre nuevas firmas o certificados.

Por su parte, la Oficina Federal de Seguridad de la Información alemana (BSI) emitió el mismo jueves 26 una advertencia general sobre herramientas de ataque autónomas basadas en IA, entre ellas ARTEX, CAIRN y PentAGI. No es un comunicado sobre SAP, pero coincide con las informaciones que apuntan al uso de agentes de IA en la intrusión. Lo contamos también en [Suiza confirma ciberataques con agentes de IA](/suiza-ciberataques-agentes-ia-infraestructura-critica/).

## ¿Afecta a los clientes de SAP?

La respuesta oficial es que no hay pruebas de acceso a datos de negocio de clientes. Pero en un incidente de este tipo el riesgo principal no son los datos, sino la integridad del software: si un atacante consigue alterar código que luego se distribuye, puede colar una puerta trasera en miles de empresas a la vez. Es lo que se conoce como ataque a la cadena de suministro, el mismo patrón que vimos con los [paquetes NuGet maliciosos que suplantaban pruebas de empleo](/paquetes-nuget-maliciosos-falsas-pruebas-empleo/) o con el [hackeo a 1Password a través de GitHub](/hackeo-1password-github-datos-clientes/).

No es la primera vez este año que el código de SAP está en el punto de mira. A finales de abril, investigadores detectaron que varios paquetes oficiales de desarrollo de SAP habían sido manipulados con un malware llamado "Mini Shai Hulud", que robaba credenciales de servicios en la nube y plataformas de desarrollo. Por ahora no hay pruebas públicas que relacionen aquel episodio con el incidente actual.

## Qué deben hacer las empresas que usan SAP

Mientras SAP no publique más detalles, los equipos de seguridad y de desarrollo pueden tomar algunas medidas prudentes:

- Seguir los avisos oficiales de SAP (SAP Security Notes y el portal de soporte) y no actuar por rumores en redes sociales.
- Revisar si usáis librerías, SDK o paquetes de código abierto de SAP descargados de GitHub o npm en los últimos días, fijar versiones conocidas y comprobar sumas de verificación cuando estén disponibles.
- Vigilar comportamientos anómalos en los entornos de integración continua que descargan dependencias automáticamente.
- Rotar tokens y claves de acceso a GitHub y a la nube de vuestros propios desarrolladores si se reutilizan entre proyectos. El robo de tokens personales es una de las vías de entrada más habituales, y conviene que caduquen pronto y tengan los permisos mínimos.
- Exigir verificación en dos pasos resistente al phishing en las cuentas de desarrollo; repasa [cómo proteger tus cuentas con contraseñas y 2FA](/proteger-cuentas-contrasenas-2fa/).

Actualizaremos esta noticia cuando SAP aclare qué repositorios se vieron afectados y si algún componente distribuido a clientes llegó a modificarse.

## Fuentes

- SOCRadar: [SAP Security Incident: GitHub Tokens and Source Code](https://socradar.io/blog/sap-security-incident-github-tokens-source-code/)
- The Next Web: [SAP confirms security incident after reported GitHub breach](https://thenextweb.com/news/sap-security-incident-github-breach)

- Cyber Security News: [SAP Confirms Security Incident as Hackers Reportedly Steal GitHub Tokens and Alter Source Code](https://cybersecuritynews.com/sap-security-incident/)
- WPNews / osna.fm (a partir de Der Spiegel): [SAP confirms active cyberattack targeting GitHub source code and employee tokens](https://wpnews.pro/news/sap-confirms-active-cyberattack-targeting-github-source-code-and-employee-tokens)
- Börse Express (abril de 2026): [SAP: Schadcode in Repositories entdeckt](https://www.boerse-express.com/news/articles/sap-schadcode-in-1000-repositories-entdeckt-900007)
