---
title: "Fallo crítico en Danfoss AK-SM sin parche: CISA alerta a los supermercados"
description: "CISA avisa de CVE-2026-129713, un fallo crítico sin parche en los controladores de frío Danfoss AK-SM 800A de supermercados. A quién afecta y cómo protegerse."
date: 2026-11-26T19:01:00+01:00
category: vulnerabilidades
tags: [Danfoss, AK-SM 800A, CVE-2026-129713, CISA, sistemas industriales, supermercados, refrigeración]
author: Redacción
photo: "File:Area with freezer displays near meat and poultry section and product aisles in Lotte Plaza Market, Tampa, Florida, on 15 January 2025.jpg"
imageAlt: "Congeladores en un supermercado, el tipo de instalación que gestionan los controladores Danfoss AK-SM con fallo crítico"
---

La Agencia de Ciberseguridad de Estados Unidos (CISA) ha publicado un aviso sobre un **fallo crítico en los controladores Danfoss AK-SM 800A** que todavía no tiene parche. La vulnerabilidad, registrada como **CVE-2026-129713**, permite a un atacante sin credenciales provocar un desbordamiento de memoria en el servidor web del equipo, reiniciarlo y, potencialmente, ejecutar código. Estos controladores gestionan las cámaras frigoríficas, congeladores y vitrinas de miles de supermercados en todo el mundo, y llevan semanas en el punto de mira tras los sabotajes sufridos por tiendas europeas desde octubre.

## Qué es el fallo CVE-2026-129713 de Danfoss

Se trata de un desbordamiento de búfer en la pila (*stack overflow*) que se puede activar a distancia sin iniciar sesión. Las referencias públicas lo sitúan en la franja crítica, con una puntuación CVSS superior a 9. Afecta a la serie **AK-SM 8xxA** (modelos 820A, 850A y 880A, entre otros), y las agencias citan también como productos relacionados los AK-SC y el sistema Dixell XWEB.

Danfoss dijo el 20 de noviembre que la corrección llegará con la **versión 5.5.x** del firmware, que además eliminará la opción de desactivar el modo estricto (*Strict mode*). A día de hoy esa versión no está disponible y no hay fecha pública. Por ahora no hay confirmación oficial de que este fallo concreto se esté explotando, aunque el contexto preocupa.

## Seis fallos más sin parche y una ola de sabotajes

El aviso llega diez días después de que la empresa neerlandesa Midnight Blue revelara **otros seis fallos** en el mismo AK-SM 800A que permiten tomar el control del equipo sin contraseña. Según los investigadores, cinco están en partes de la web del controlador que no piden autenticación y se ejecutan como *root*; afectan a las versiones hasta la 5.3.2, y la 5.4.0 publicada en noviembre no los corrige. Estos fallos aún no tienen CVE ni detalles técnicos públicos.

El BSI alemán, el CCB belga y el NCSC irlandés han pedido actuar ya por los incidentes registrados desde el 11 de octubre en Francia, con una segunda oleada en otros países europeos: alguien entró en sistemas de refrigeración de supermercados y cambió consignas y ciclos de descongelación, lo que obligó a tirar producto. Las agencias no vinculan por ahora esos ataques con los seis fallos nuevos. CISA, por su parte, añadió el 25 de noviembre otros tres fallos antiguos de Danfoss a su catálogo de vulnerabilidades explotadas, como contamos en [nuestra noticia sobre Mitel, Xen Orchestra y Juniper](/fallos-explotados-mitel-xen-orchestra-juniper/).

## ¿A quién afecta?

Sobre todo a cadenas de supermercados, tiendas de alimentación, almacenes frigoríficos, logística en frío y empresas de mantenimiento de refrigeración comercial. El riesgo es mayor cuando la interfaz web del controlador está expuesta a Internet, algo habitual porque los técnicos la usan para revisar las instalaciones a distancia, a veces a través de un módem 4G o 5G que nadie recuerda que existe. Un atacante podría alterar temperaturas, desactivar alarmas o romper la cadena de frío.

## Qué hacer mientras no hay parche

Las recomendaciones de CISA, el BSI, el CCB y el NCSC irlandés coinciden:

1. **Saca el controlador de Internet.** Ninguna interfaz de gestión debería ser accesible desde fuera, tampoco a través de módems móviles. Empieza por una revisión de [los puertos que tienes abiertos en tu red](/que-es-un-puerto-redes/).
2. **Acceso remoto solo por VPN** actualizada o por una red interna protegida. Permitir solo la IP de la empresa de mantenimiento es un apaño temporal.
3. **Separa la red de control** de la red de oficinas y de la wifi de la tienda con un cortafuegos.
4. **Revisa la configuración**: consignas de temperatura, programas de descongelación, alarmas, usuarios y opciones de acceso remoto. Cualquier cambio inesperado es una señal de alarma.
5. Si sospechas una intrusión, **cambia todas las credenciales** y avisa al fabricante y al CERT de tu país (en España, INCIBE-CERT para empresas).
6. Instala la versión 5.5.x en cuanto Danfoss la publique. Actualizar el firmware actual, cambiar contraseñas o activar el modo estricto ayuda, pero no basta por sí solo.

Si gestionas sistemas industriales y quieres entender cómo leer estos avisos, tenemos una guía sobre [qué es una CVE y cómo interpretar su gravedad](/que-es-una-cve/).

## Fuentes

- BleepingComputer: [CISA warns of critical unpatched flaw in Danfoss refrigeration controllers](https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-unpatched-flaw-in-danfoss-refrigeration-controllers/)
- The Hacker News: [Six unpatched Danfoss refrigeration controller flaws could allow remote takeover without login](https://thehackernews.com/2026/11/six-unpatched-danfoss-refrigeration.html)
- Security Affairs: [CISA adds HPE, Danfoss, Mitel MiCollab and Vates Xen Orchestra flaws to its KEV catalog](https://securityaffairs.com/204014/hacking/u-s-cisa-adds-hpe-juniper-session-smart-conductor-and-session-smart-router-flaw-to-its-known-exploited-vulnerabilities-catalog.html)
- Danfoss: [Avisos de seguridad](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/)
