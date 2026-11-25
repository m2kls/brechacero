---
title: "Hackeo de servidores Check Point: el grupo GT13 compromete a 22 organizaciones"
description: "Hackeo de servidores Check Point: GreyNoise detecta que el grupo GT13 tomó el control de consolas de gestión de cortafuegos en 22 organizaciones. Qué revisar ya."
date: 2026-11-25T08:55:00+01:00
category: vulnerabilidades
tags: [Check Point, GT13, GreyNoise, cortafuegos, CVE-2026-16232, SmartConsole, infraestructura crítica]
author: Redacción
photo: "File:Check Point offices.jpg"
imageAlt: "Oficinas de Check Point, cuyos servidores de gestión de cortafuegos han sido objetivo del grupo GT13"
---

El hackeo de servidores Check Point que ha documentado la empresa de inteligencia de amenazas GreyNoise afecta a una pieza especialmente delicada de cualquier red corporativa: los servidores de gestión desde los que se configuran y despliegan las políticas de los cortafuegos. Un grupo al que GreyNoise llama GT13 (GreyNoise Threat 13) logró entrar en estos servidores en al menos 22 organizaciones de sectores como la energía, la ingeniería, las finanzas, la administración pública, la industria, la minería y el transporte. La actividad confirmada va del 17 de octubre al 2 de noviembre, pero los investigadores creen que la campaña sigue en marcha.

## Qué ha pasado con los servidores de Check Point

Según el informe de GreyNoise, recogido por SecurityWeek el 24 de noviembre, los atacantes empezaron a moverse a principios de octubre. El 2 de octubre falsificaron una cookie de sesión de administrador firmada para acceder a un servidor de ficheros HFS (Rejetto HTTP File Server) que usaban como punto de apoyo, y desde ahí consiguieron acceso por SSH. Ese servidor les sirvió como relé para el resto de la operación.

La pieza central es CVE-2026-16232, un fallo de omisión de autenticación en Check Point SmartConsole que, según el análisis publicado por Aviatrix, permitía obtener tokens con privilegios de administrador. Con ellos, el grupo robó bases de datos de los cortafuegos, credenciales, configuraciones y ficheros de la autoridad de certificación interna. En algunos casos llegaron a descargar (desactivar) políticas y, al menos en un entorno, generaron certificados no autorizados.

Entre el 20 y el 26 de octubre lanzaron acciones masivas: una tarea de gestión de certificados enviada a 24 servidores de las 22 organizaciones. Esa tarea concreta falló, pero las respuestas de los servidores acabaron recogidas en el relé de los atacantes. GreyNoise contabiliza más de 1.400 sesiones de red, más de 800 rastros de línea de comandos y más de 1.200 ficheros asociados a la campaña, con tráfico desde 99 direcciones IP que eran salidas de una VPN comercial o equipos Check Point de víctimas ya comprometidas. SecurityWeek describe la operación como una campaña asistida por inteligencia artificial.

## ¿A quién afecta?

Las víctimas están repartidas por Estados Unidos, Reino Unido, Australia, Austria, China, Francia, Alemania, Hong Kong, Países Bajos, Corea del Sur y otros países; Aviatrix habla de 17 países en total. No se ha publicado ninguna víctima española, pero Check Point es uno de los fabricantes de cortafuegos más extendidos en empresas y administraciones de España, así que cualquier organización que use su gestión centralizada debería revisar sus sistemas.

El caso preocupa porque un servidor de gestión comprometido da al atacante algo más que un equipo: le da el mapa de la red, las reglas que la protegen y la capacidad de cambiarlas. Con los certificados de la CA interna, además, se pueden suplantar servicios legítimos.

## Otros fallos que usó el grupo

GreyNoise también vio a GT13 explotar o intentar explotar vulnerabilidades conocidas y antiguas en otros productos de la red de las víctimas. Entre ellas, Citrix Bleed (CVE-2023-4966) y CVE-2025-5777 en Citrix NetScaler, CVE-2024-21893 en Ivanti, ProxyLogon y ProxyShell en Exchange (CVE-2021-26855 y CVE-2021-34473), Zerologon (CVE-2020-1472) y dos fallos de VMware vCenter (CVE-2021-21972 y CVE-2023-34048). Las herramientas observadas son de uso común en auditorías: Nmap, Chisel, Impacket y Paramiko, entre otras.

Que aparezcan fallos de 2020 y 2021 en una campaña de 2026 es la lección habitual: los atacantes aprovechan lo que nadie ha parcheado. Si necesitas repasar cómo se leen estos identificadores, tenemos una guía sobre [qué es una CVE y cómo interpretar su gravedad](/que-es-una-cve/), y hace unos días contamos el [fallo crítico de VMware vCenter que permite saltarse el login](/fallo-vmware-vcenter-cve-2026-123903/).

## Qué hacer si usas Check Point

- **Aplica las actualizaciones de Check Point** para SmartConsole y el servidor de gestión (Security Management Server o Multi-Domain) y comprueba que no quedan versiones antiguas expuestas.
- **No expongas las interfaces de gestión a internet.** Deben estar en una red de administración separada, accesible solo desde equipos concretos y, si es posible, a través de VPN con doble factor.
- **Busca indicadores de compromiso**: sesiones de administrador desde IP inusuales, tareas masivas de certificados que no hayas lanzado, políticas desinstaladas y certificados nuevos en la CA interna.
- **Rota credenciales y certificados** si encuentras cualquier indicio, porque el grupo se llevó bases de datos y ficheros de la CA.
- **Repasa el resto del perímetro**: Citrix, Ivanti, Exchange, vCenter y controladores de dominio con los parches de los fallos citados.
- **Filtra el tráfico de salida** desde los servidores de gestión; un servidor de cortafuegos no debería conectar con servidores HFS desconocidos.

En el momento de publicar esta noticia, Check Point no había hecho una declaración pública específica sobre la campaña. La actualizaremos si el fabricante publica un aviso con versiones afectadas.

## Fuentes

- [SecurityWeek: Check Point Security Management Servers Hacked in AI-Assisted Campaign](https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/)
- [GreyNoise: Check Point Security Management Servers intrusion campaign](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)
- [Aviatrix: GT13 compromete servidores Check Point en 22 organizaciones](https://aviatrix.ai/threat-research-center/hackers-compromise-check-point-servers-22-organizations-gt13-cve-2026-16232/)
