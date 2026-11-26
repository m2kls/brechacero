---
title: "Fallos explotados en Mitel, Xen Orchestra y Juniper: CISA avisa de 10"
description: "CISA añade 10 fallos explotados a su catálogo KEV: cinco de Mitel MiCollab, Xen Orchestra, Juniper Session Smart y Danfoss. Versiones afectadas y cómo protegerte."
date: 2026-11-26T02:54:00+01:00
category: vulnerabilidades
tags: [CISA, KEV, Mitel MiCollab, Xen Orchestra, Juniper, Danfoss, vulnerabilidades explotadas]
author: Redacción
photo: "File:Datacenter Server Racks (22370909788).jpg"
imageAlt: "Armarios de servidores en un centro de datos, el tipo de infraestructura que gestionan Xen Orchestra y Juniper"
---

La Agencia de Ciberseguridad de Estados Unidos (CISA) añadió el 25 de noviembre **diez fallos explotados** a su catálogo de vulnerabilidades conocidas y aprovechadas (KEV). La lista incluye cinco errores de **Mitel MiCollab**, la plataforma de comunicaciones unificadas de muchas empresas; una puerta trasera en el inicio de sesión de **Xen Orchestra**, la consola que administra servidores virtuales XCP-ng; un fallo crítico en **Juniper Session Smart Router**; y tres más en controladores de refrigeración **Danfoss**. Entrar en el KEV significa que hay pruebas de ataques reales, así que la prioridad es parchear ya.

## Qué fallos explotados ha añadido CISA

Ninguno de estos productos es de consumo, pero todos están en redes de empresas y administraciones también en España. Estos son los grupos de vulnerabilidades:

- **Mitel MiCollab** (CVE-2026-133275, CVE-2026-133303, CVE-2026-133311, CVE-2026-133323 y CVE-2026-133324). Afectan al componente de audio, web y videoconferencia (AWV) de la versión 10.3 (10.3.0.18) y anteriores. Hay una inyección de órdenes con gravedad máxima (CVSS 10), una inyección XML de nivel 9.0 y otros tres fallos de subida de archivos, acceso a información y salto de autenticación. Mitel advierte de que todos se pueden aprovechar sin credenciales y de que, combinados, "pueden amplificar significativamente su impacto".
- **Xen Orchestra** (CVE-2026-133469, aviso VSA-2026-062 del fabricante, Vates). Permite saltarse el inicio de sesión y entrar con permisos de administrador. Vates confirmó ataques desde el 10 de noviembre.
- **Juniper Session Smart Conductor y Router** (CVE-2026-103406, CVSS 9.8). Una inyección de órdenes en el componente de aprovisionamiento automático que permite ejecutar comandos como root. Juniper lo corrigió a finales de octubre.
- **Danfoss AK-SM 800A** (CVE-2023-25914, CVE-2023-25915 y CVE-2025-41450). Controladores de sistemas de frío muy usados en supermercados, con fallos de lectura de archivos y salto de autenticación ya conocidos.

## El caso más delicado: Xen Orchestra

El fallo de Xen Orchestra preocupa por dos motivos. El primero, que quien entra obtiene el control de toda la plataforma de virtualización: puede llegar a ejecutar código en los servidores XCP-ng y en las máquinas virtuales que alojan. El segundo, que **el acceso no deja rastro en los registros** de la aplicación, según el propio fabricante. Para saber si te han atacado hay que revisar el tráfico HTTP en bruto o buscar indicios en los servidores, como una máquina virtual llamada `pivot2` o tareas programadas con nombres `zz-ustar` que Vates ha publicado como indicadores.

Además, los atacantes lo combinaron con un segundo problema (VSA-2026-063) que permite a usuarios con permiso de importar máquinas virtuales colar una maliciosa y comprometer el servidor. Según SecurityOnline, este segundo fallo seguía sin parche a mediados de noviembre.

## ¿Estoy afectado? Cómo protegerte

Si tu organización usa alguno de estos productos:

1. **Mitel MiCollab**: aplica el parche descrito en el artículo KB000129195 para la 10.3 o actualiza a una versión posterior. Mientras tanto, corta el acceso desde Internet al componente AWV.
2. **Xen Orchestra**: actualiza a la versión 6.9.2 (rama estable) o 6.10.1 (rama más reciente), también en el appliance XOA. Sácala de Internet y déjala en una red de gestión separada. Hasta que se corrija VSA-2026-063, desactiva a los usuarios que puedan importar máquinas virtuales o crear redes. Si encuentras indicios de intrusión, Vates recomienda cambiar todas las contraseñas y secretos guardados y reinstalar desde cero.
3. **Juniper Session Smart**: instala las versiones 7.0.5-14-lts, 7.1.7-15-sts o 7.2.3-8r2 o posteriores (aviso JSA112183). CISA ha dado a las agencias federales hasta el 28 de noviembre.
4. **Danfoss AK-SM 800A**: actualiza el firmware y no expongas nunca la interfaz del controlador a Internet.

Como regla general, las consolas de administración (de virtualización, de cortafuegos o de telefonía) no deberían ser accesibles desde fuera. Es el mismo patrón que ya vimos en el [hackeo de servidores de Check Point](/hackeo-servidores-check-point-gt13/). Si no tienes claro qué significan los códigos CVE o la puntuación CVSS, lo explicamos en [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [CISA: CISA Adds 10 Known Exploited Vulnerabilities to Catalog (25-11-2026)](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog)
- [Mitel Product Security Advisory MISA-2026-0012](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)
- [SecurityOnline: Xen Orchestra authentication bypass exploited](https://securityonline.info/xen-orchestra-authentication-bypass-exploited/)
- [Brandefense: Xen Orchestra VSA-2026-062, active exploitation and fixes](https://brandefense.io/security-news/xen-orchestra-vsa-2026-062-active-exploitation/)
