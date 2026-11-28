---
title: "Ransomware LostTrust y Eclipse: un agente de IA guía sus intrusiones"
description: "El ransomware LostTrust reaparece ligado a Eclipse: SOCRadar halla 17 víctimas, entre ellas una agencia federal de EE. UU., y un agente de IA conectado por MCP."
date: 2026-11-28T14:58:00+01:00
category: noticias
tags: [LostTrust, Eclipse, ransomware, SOCRadar, Microsoft Defender, IA, MCP]
author: Redacción
photo: "File:SOC Security Monitors.jpg"
imageAlt: "Pantallas de un centro de operaciones de seguridad, donde se vigilan amenazas como el ransomware LostTrust"
---

El **ransomware LostTrust** ha vuelto, y con novedades. La empresa de inteligencia de amenazas **SOCRadar** ha publicado una investigación sobre una banda de habla rusa ligada a la plataforma de extorsión MetaEncryptor/LostTrust y, con "alta confianza", al programa de ransomware como servicio **Eclipse**. Los investigadores encontraron en la infraestructura de los atacantes material sobre **17 organizaciones** de cuatro países, 14 de ellas en Estados Unidos, entre las que hay una agencia federal, tres cooperativas energéticas y un proveedor sanitario. Lo más llamativo: el servidor de mando de la banda conecta sus implantes a un **agente de inteligencia artificial** mediante el protocolo MCP.

## Qué ha descubierto SOCRadar sobre LostTrust y Eclipse

SOCRadar sigue a LostTrust desde marzo de 2023 y lo considera una continuación de MetaEncryptor. En esta nueva fase, los operadores no solo cifran y publican datos: mantienen un laboratorio propio donde **prueban sus implantes contra Microsoft Defender for Endpoint** antes de lanzarlos contra las víctimas.

Los investigadores documentan un ejemplo. Entre el 13 y el 16 de octubre, una versión del implante (un programa escrito en Rust que se carga aprovechando un ejecutable firmado de Microsoft) generó una alerta de severidad alta y fue aislada. El 21 de octubre, una versión retocada y renombrada como si fuera un componente de otro producto de seguridad se conectó a su servidor **sin disparar ninguna alerta**. Defender sí registró cientos de eventos de enumeración de cuentas y preparación de datos, pero como simples eventos, sin convertirlos en aviso para el equipo de seguridad.

El análisis de GBHackers, que se basa en el informe, recoge que la banda recurre también a fallos antiguos y muy conocidos para entrar o escalar privilegios, como **ZeroLogon (CVE-2020-1472)**, ProxyLogon y ProxyShell en Exchange, además de un fallo de 2024 en el software IDURAR ERP/CRM. Si no sabes cómo leer estos identificadores, te lo contamos en [qué es una CVE](/que-es-una-cve/).

## Un agente de IA conectado por MCP

El servidor de control de LostTrust expone las funciones del implante a un modelo de lenguaje a través del **Model Context Protocol (MCP)**, el estándar que usan muchos asistentes de IA para manejar herramientas externas. SOCRadar recuperó una sesión del 14 de julio contra el laboratorio de los atacantes: en 136 minutos, con ocho instrucciones del operador en ruso, el agente hizo **329 llamadas a 57 herramientas distintas**.

Los investigadores subrayan que el agente no es infalible: inventa nombres de herramientas, hace llamadas mal formadas y, cuando lo lanzaron el 29 de octubre contra un proveedor sanitario real, se quedó en tareas de reconocimiento porque había un EDR vigilando. Los operadores siguen eligiendo a las víctimas y ejecutando cada paso que lleva a la extorsión. Encaja con lo que han advertido esta semana las autoridades suizas sobre [ciberataques asistidos por agentes de IA](/suiza-ciberataques-agentes-ia-infraestructura-critica/) y con el aviso de Microsoft sobre [el uso de IA por parte de Salt Typhoon](/microsoft-artex-ia-salt-typhoon/).

## ¿Quiénes son las víctimas?

SOCRadar ha retirado los nombres, pero detalla los sectores. El caso más grave es una **agencia federal estadounidense**, donde los atacantes abrieron túneles hacia servidores de directorio internos, probaron contraseñas de forma masiva y robaron archivos de repositorios de código y un certificado con su clave privada. En una **cooperativa eléctrica rural** lograron acceso de administrador y a bases de datos, y en otras dos cooperativas energéticas obtuvieron credenciales y registros de clientes. La lista incluye también un ministerio de Colombia, un sistema judicial de Taiwán, empresas de gestión de residuos, medios de comunicación, una teleco, un proveedor de servicios informáticos y un fabricante sueco de dispositivos médicos.

Según la empresa, las organizaciones afectadas y las autoridades ya han sido avisadas. Ninguna de las 17 coincide con las 19 víctimas que la web de filtraciones de LostTrust mostraba el 17 de noviembre, lo que apunta a que varios afiliados trabajan en paralelo con la misma plataforma. Eclipse, por su parte, recluta afiliados en foros criminales, se queda con el 10–20 % de cada rescate, exige un mínimo de 70.000 dólares por caso y permite atacar gobiernos, infraestructuras críticas y hospitales.

## Cómo protegerse

La conclusión de SOCRadar es que "la reputación de archivos y las alertas aisladas son controles débiles" frente a este tipo de banda. Sus recomendaciones para equipos de seguridad:

- **Buscar comportamientos, no solo alertas**: ejecutables firmados que cargan DLL desde carpetas donde el usuario puede escribir, consultas masivas al directorio activo o servidores que abren conexiones salientes poco habituales.
- **Revisar la telemetría del EDR** más allá de las alertas: los eventos de enumeración de cuentas o preparación de datos pueden ser la única pista.
- **Parchear fallos antiguos** como ZeroLogon y los de Exchange, que siguen dando acceso años después.
- **Controlar las herramientas de soporte remoto** con una lista de permitidas y vigilar el tráfico a OneDrive o Microsoft Graph desde procesos que no deberían usarlo.
- **No repetir credenciales de administrador** entre clientes cuando se trabaja con un proveedor de TI compartido, y reforzar las cuentas con [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/).

## Fuentes

- SOCRadar: [LostTrust revival: Eclipse ransomware targets the US](https://socradar.io/blog/losttrust-revival-eclipse-ransomware-targets-us/)
- GBHackers: [LostTrust ransomware revival linked to Eclipse as hackers target U.S. government and energy firms](https://gbhackers.com/losttrust-ransomware/)
