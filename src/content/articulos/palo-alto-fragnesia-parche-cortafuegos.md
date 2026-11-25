---
title: "Palo Alto corrige Fragnesia, el fallo usado para tomar el control de sus cortafuegos"
description: "Palo Alto parchea Fragnesia (CVE-2026-46300) en PAN-OS: hackers ligados a China lo encadenaron con PHP2Shell para ser root en 24 cortafuegos. Qué actualizar."
date: 2026-11-25T10:53:00+01:00
category: vulnerabilidades
tags: [Palo Alto Networks, PAN-OS, Fragnesia, CVE-2026-46300, PHP2Shell, cortafuegos]
author: Redacción
photo: "File:Palo Alto Networks Headquarters South Side 2018.jpg"
imageAlt: "Sede de Palo Alto Networks, que ha corregido el fallo Fragnesia en sus cortafuegos PAN-OS"
---

Palo Alto Networks ha publicado los parches de Fragnesia para sus cortafuegos PAN-OS, el fallo del núcleo de Linux que unos atacantes vinculados a China usaron para hacerse con el control total (privilegios de root) de al menos 24 cortafuegos y un servidor de gestión. Las actualizaciones llegaron el martes 24 de noviembre, casi un mes después de que la empresa confirmara la cadena de ataque. Es una noticia relevante para cualquier organización que use estos equipos, muy extendidos en empresas y administraciones.

## Qué es Fragnesia y cómo se usó contra Palo Alto

Fragnesia, registrado como CVE-2026-46300, es una vulnerabilidad del núcleo de Linux conocida desde mayo. Afecta al subsistema que gestiona el tráfico IPsec encapsulado en TCP y permite a un usuario sin privilegios sobrescribir ficheros del sistema, es decir, escalar a administrador dentro de la máquina. PAN-OS, el sistema de los cortafuegos de Palo Alto, se basa en Linux, así que también estaba expuesto.

Por sí solo, Fragnesia necesita que el atacante ya esté dentro del equipo. Esa puerta la abrió PHP2Shell (CVE-2026-109618), un fallo de ejecución remota de código en la interfaz de gestión de PAN-OS. La empresa de seguridad Dream alertó el 26 de octubre de una campaña que encadenaba ambos fallos, y Palo Alto lo confirmó el 29 de octubre. Según SecurityWeek, los atacantes eran un grupo de habla china y la campaña estuvo asistida por herramientas de inteligencia artificial.

En total se vieron comprometidos 25 servidores: 24 cortafuegos y un servidor interno de gestión. Entre las víctimas había una organización vinculada al Gobierno de Estados Unidos.

## ¿Estoy afectado?

Palo Alto sostiene que la única vía de explotación conocida pasa por PHP2Shell, por lo que quien ya tenga instaladas las versiones que corrigen ese fallo (disponibles desde el 30 de octubre) está protegido frente a esta cadena concreta. Aun así, recomienda instalar también las correcciones de Fragnesia, porque cierran la escalada de privilegios por si aparece otra forma de entrar.

La compañía también indica que la explotación observada se dirigía a la interfaz de gestión expuesta a Internet. Si la consola de administración de tus cortafuegos se puede alcanzar desde fuera, el riesgo es mucho mayor.

Algunas de las versiones de PAN-OS con la corrección de Fragnesia son 12.2.4-h3, 12.1.10-h6, 11.2.16-h3, 11.1.16-h6 y 10.2.18-h15. La lista completa, con todas las ramas y revisiones, está en el aviso PAN-SA-2026-0015.

## Qué hacer

1. **Comprueba que tienes el parche de PHP2Shell** (CVE-2026-109618). Es el que corta la entrada.
2. **Instala la corrección de Fragnesia** que corresponda a tu rama de PAN-OS según el aviso oficial.
3. **Saca la interfaz de gestión de Internet**. Palo Alto insiste en que solo debe ser accesible desde una red de administración interna o a través de VPN.
4. **Revisa los registros** de los cortafuegos desde octubre en busca de accesos administrativos inesperados o cambios de configuración. Si hay indicios de compromiso, trata el equipo como no fiable y sigue el procedimiento de respuesta a incidentes.

No es el único caso reciente de ataques contra las consolas que gestionan cortafuegos: esta misma semana contamos el [hackeo de servidores Check Point por el grupo GT13](/hackeo-servidores-check-point-gt13/). Si necesitas repasar cómo se interpreta un identificador como CVE-2026-46300, lo explicamos en [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [Palo Alto Networks: aviso PAN-SA-2026-0015](https://security.paloaltonetworks.com/PAN-SA-2026-0015)
- [Palo Alto Networks: aviso CVE-2026-109618 (PHP2Shell)](https://security.paloaltonetworks.com/CVE-2026-109618)
- [SecurityWeek: Palo Alto Networks Patches Fragnesia Flaw Used to Root Firewalls](https://www.securityweek.com/palo-alto-networks-patches-fragnesia-flaw-used-to-root-firewalls/)
