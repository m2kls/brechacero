---
title: "Fallos en GeoServer ya explotados: actualiza a 2.28.6, 2.27.7 o 3.0.2"
description: "Atacantes sondean dos fallos de GeoServer (CVE-2026-120705 y CVE-2026-129243) que encadenados permiten tomar el servidor sin contraseña. Qué versiones instalar."
date: 2026-11-26T00:55:00+01:00
category: vulnerabilidades
tags: [GeoServer, CVE-2026-120705, CVE-2026-129243, vulnerabilidades, parches, SIG, servidores]
author: Redacción
photo: "File:GeoServer logo.png"
imageAlt: "Logotipo de GeoServer, el servidor de mapas con fallos ya explotados"
---

Los fallos de GeoServer publicados esta semana ya están en el punto de mira. La firma watchTowr ha detectado el 25 de noviembre intentos de explotación de dos de ellos, **CVE-2026-120705** y **CVE-2026-129243**, apenas dos días después de que los responsables del proyecto publicaran los detalles. GeoServer es un servidor de código abierto muy usado por administraciones, ayuntamientos, empresas de energía y agua o universidades para publicar mapas y datos geográficos en internet, y no es la primera vez que los atacantes lo usan como puerta de entrada.

## Qué fallos de GeoServer se están explotando

Los dos fallos que se están sondeando son de gravedad alta y no requieren usuario ni contraseña:

- **CVE-2026-120705** (CVSS 8,6): una inyección en el servicio WFS, el que sirve datos vectoriales, permite leer ficheros del servidor y hacer peticiones a otras máquinas de la red interna (SSRF). Lo descubrió la empresa neerlandesa Eye Security.
- **CVE-2026-129243** (CVSS 8,8): un error de autorización permite llegar a operaciones que deberían estar reservadas a usuarios autenticados.

Por ahora, según watchTowr y SecurityWeek, lo observado son peticiones para comprobar qué servidores son vulnerables, no se ha confirmado ninguna toma de control completa. Pero el riesgo es real porque estos fallos forman parte de una cadena más larga.

## Por qué preocupa: una cadena que acaba en control total

Los mantenedores de GeoServer describen una cadena de cinco fallos que, combinados, permiten ejecutar código en el servidor sin autenticarse. Uno de los eslabones más delicados es **CVE-2026-129245** (CVSS 9,2): GeoServer usaba una clave fija y conocida para la función "recordarme" del inicio de sesión, lo que permite fabricar una sesión de administrador si se obtiene cierta información del servidor. Y esa información es justo la que puede filtrar la lectura de ficheros de CVE-2026-120705.

Eye Security demostró de forma independiente otra cadena con CVE-2026-120705, CVE-2026-129245 y CVE-2026-120704 que logra ejecución de código en Linux y en Windows. La empresa contó más de 3.000 instancias de GeoServer accesibles desde internet y reconoce que encontró los fallos con ayuda de inteligencia artificial: "un atacante decidido con buenos modelos podría hacer lo mismo", advierte en su informe. Los detalles técnicos y una prueba de concepto de Rapid7 ya son públicos, lo que suele acelerar los ataques.

Los propios responsables avisan de algo importante: cambiar a mano la clave en el fichero de configuración no basta si la misma fuga de ficheros permite leer la clave nueva. La solución es actualizar. Si quieres entender cómo se puntúan estos fallos, lo explicamos en [qué es una CVE y cómo leer su gravedad](/que-es-una-cve/).

## ¿Estoy afectado?

Están afectadas todas las ramas con soporte anteriores a las versiones corregidas. Las versiones que solucionan los fallos son:

- **GeoServer 3.0.2**
- **GeoServer 2.28.6**
- **GeoServer 2.27.7** (rama ya sin soporte oficial, pero con parche disponible)

Según Eye Security, estas versiones están disponibles desde el 19 de octubre, aunque los detalles de las vulnerabilidades no se publicaron hasta el 23 de noviembre. Quien actualizó en octubre ya está protegido. La versión instalada se puede ver en la consola de administración, en "Acerca de GeoServer", dentro de la información de compilación.

Esto importa también en España: GeoServer está detrás de muchos visores de mapas de comunidades autónomas, diputaciones, confederaciones hidrográficas y proyectos de datos abiertos, y suele instalarse una vez y olvidarse.

## Cómo protegerte

1. **Actualiza ya** a 3.0.2, 2.28.6 o 2.27.7. Si usas GeoServer dentro de otro producto o imagen de contenedor, comprueba que el proveedor ha publicado la versión corregida.
2. **No expongas la consola de administración** a internet. Restringe `/geoserver/web` por VPN o lista de direcciones IP.
3. **Revisa los registros** en busca de peticiones extrañas al servicio WFS y a consultas almacenadas desde el 23 de noviembre.
4. **Si no puedes actualizar hoy**, saca temporalmente el servidor de internet o colócalo detrás de un cortafuegos de aplicaciones web.
5. **Si sospechas una intrusión**, trátala como compromiso completo: cambia todas las contraseñas de GeoServer y las credenciales de las bases de datos que usa, y revisa el resto de la red.

Es la segunda vez este año que GeoServer da un susto: en agosto ya se explotó un fallo previo antes de que existiera parche, y en 2025 un fallo de este servidor sirvió para entrar en una agencia federal de Estados Unidos. Para el resto de servidores expuestos, conviene seguir la misma pauta que con [los fallos de VMware, Cisco y Apache que ya se explotan](/vmware-cisco-apache-fallos-explotados/): parchear primero lo que está en internet.

## Fuentes

- [SecurityWeek: Two Newly Disclosed GeoServer Vulnerabilities Under Attack](https://www.securityweek.com/two-newly-disclosed-geoserver-vulnerabilities-under-attack/)
- [The Hacker News: Hackers Exploit Two GeoServer Flaws as Researchers Warn of Unauthenticated RCE Chains](https://thehackernews.com/2026/11/hackers-exploit-two-geoserver-flaws-as.html)
- [Eye Security: Unauthenticated remote code execution vulnerability in GeoServer](https://labs.eye.security/unauthenticated-remote-code-execution-vulnerability-in-geoserver/)
- [GeoServer: aviso de seguridad CVE-2026-120705 (GHSA-39mw-5chv-jh47)](https://github.com/geoserver/geoserver/security/advisories/GHSA-39mw-5chv-jh47)
- [GeoServer: aviso de seguridad CVE-2026-129243 (GHSA-rv5g-g2r9-58rj)](https://github.com/geoserver/geoserver/security/advisories/GHSA-rv5g-g2r9-58rj)
