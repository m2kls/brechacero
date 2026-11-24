---
title: "Hackeo de routers GL.iNet: un fallo en GoodCloud instala malware"
description: "Atacantes usaron un fallo en GoodCloud, la nube de GL.iNet, para meter malware en routers de viaje y KVM Comet. Qué modelos actualizar y cómo comprobarlo."
date: 2026-11-25T00:55:00+01:00
category: vulnerabilidades
tags: [GL.iNet, GoodCloud, routers, KVM Comet, malware, firmware, IoT]
author: Redacción
photo: "File:GL-iNet Travel Router and Wyze Camera - Hotel Room Security.jpg"
imageAlt: "Router de viaje GL.iNet en la habitación de un hotel, uno de los modelos afectados por el hackeo de GoodCloud"
---

GL.iNet, el fabricante chino de los populares routers de viaje y de los KVM remotos Comet, ha confirmado que un atacante aprovechó una vulnerabilidad en **GoodCloud**, su servicio de gestión remota en la nube, para instalar malware en parte de sus dispositivos. La empresa detectó el fallo el 20 de noviembre, lo corrigió en sus servidores ese mismo día y ha publicado firmware de seguridad para limpiar los equipos ya infectados. Si tienes un router GL.iNet (Slate, Beryl, Flint, Brume…) o un KVM Comet y alguna vez activaste GoodCloud, conviene actualizarlo cuanto antes.

## Qué ha pasado con GoodCloud

GoodCloud permite administrar los routers y KVM de GL.iNet desde una web, sin estar en la misma red. Según el aviso de la compañía, alguien abusó de un fallo en ese servicio para enviar órdenes a los dispositivos conectados y descargar en ellos programas maliciosos. "Hemos corregido la vulnerabilidad de la nube y bloqueado el acceso usado en este incidente", explica GL.iNet, que aclara que ningún equipo puede infectarse ya por esa vía, pero que esas medidas "no eliminan el malware de los dispositivos que ya estaban infectados".

La empresa no ha dicho cuántos equipos se han visto afectados, desde cuándo duraba el ataque ni quién está detrás, y de momento no hay un identificador CVE asignado.

La consultora RemoteToHome, que gestiona flotas de estos routers, ha publicado un análisis independiente que GL.iNet no ha confirmado. Sostiene que el cliente de GoodCloud integrado en el firmware ejecutaba con permisos de administrador (root) valores recibidos desde la nube sin comprobarlos, un código presente desde al menos diciembre de 2024. De 183 routers que revisó, encontró actividad sospechosa en 152: 24 con una conexión remota oculta activa, 47 con una puerta trasera más antigua (instalada entre septiembre de 2025 y mayo de 2026, quizá sin relación con este ataque) y 81 con rastros de órdenes ejecutadas por el atacante.

El malware analizado por BleepingComputer se disfraza de un proceso del sistema, se reinstala al arrancar mediante tareas programadas, puede añadir claves SSH para volver a entrar y sustituye herramientas de diagnóstico para ocultar sus conexiones. Los comentarios en chino del código apuntan a un autor de habla china.

## ¿Estoy afectado?

Corres riesgo si tienes un router o KVM de GL.iNet con **GoodCloud activado**. Los que nunca se han vinculado a la nube no estaban expuestos por esta vía. En el caso de los KVM el problema es más serio, porque dan control del teclado, la pantalla y el arranque del ordenador al que están conectados: GL.iNet recomienda revisar también ese equipo en busca de programas, extensiones del navegador o cuentas de usuario desconocidas, tareas programadas nuevas y tráfico de red extraño.

GL.iNet indica como señal de infección un proceso que contiene el texto `/tmp/.log` (visible en el panel LuCI, en la lista de procesos). Los investigadores advierten de que esa marca no aparece en todos los casos, así que no encontrarla no garantiza que el equipo esté limpio. Haz la comprobación antes de reiniciar o actualizar, para no perder pistas.

## Qué versiones corrigen el problema

El firmware de seguridad elimina el malware detectado sin necesidad de restablecer el equipo, según el fabricante. Estas son las versiones mínimas que figuran en su aviso:

- **GL-MT3000 (Beryl AX), GL-MT6000 (Flint 2), GL-MG1300**: 4.11.1
- **GL-E5800**: 4.10.3
- **GL-BE3600, GL-BE9300**: 4.10.2
- **GL-BE14000**: 4.9.3
- **GL-BE6500, GL-MT3600BE, GL-MT5000**: 4.9.1
- **GL-BE10000**: 4.8.7
- **GL-AXT1800 (Slate AX), GL-AX1800, GL-SFT1200, GL-X3000, GL-XE3000**: 4.8.4
- **GL-MT2500 (Brume 2), GL-X2000**: 4.7.14
- **KVM Comet RM1, RM1V2, RM10, RM10RC, RM1PE y RM4PE**: 1.10.3; **RMQ1**: 1.8.7

GL.iNet recomienda instalarlo en todos sus dispositivos, también en los que no muestren síntomas.

## Cómo protegerte

1. **Actualiza el firmware** a la versión indicada para tu modelo desde el panel del router o la web oficial de GL.iNet.
2. **Si sospechas que estaba infectado, reinstala desde cero.** Los investigadores comprobaron que una actualización conservando la configuración puede arrastrar contraseñas, claves SSH y scripts de arranque del atacante. Lo más seguro es instalar el firmware sin mantener los ajustes y configurarlo a mano, sin restaurar copias de seguridad antiguas.
3. **Cambia todas las credenciales guardadas en el equipo**: contraseña de administración, claves Wi-Fi, claves de VPN (WireGuard u OpenVPN), cuentas en la nube y claves SSH. Un [gestor de contraseñas](/mejores-gestores-de-contrasenas/) facilita generar unas nuevas y fuertes.
4. **Desactiva GoodCloud si no lo necesitas**, después de asegurarte de que tienes otra forma de acceder al equipo. Desactivarlo no limpia un dispositivo ya infectado.
5. **Revisa los ordenadores conectados a un KVM** comprometido y activa la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/) en las cuentas a las que se haya accedido desde ellos.

El caso recuerda a otros ataques recientes contra dispositivos baratos conectados a Internet, como la [botnet BADBOX 3.0 en TV box Android](/badbox-3-botnet-android-tv-box/): los servicios de gestión remota son cómodos, pero si el servidor del fabricante falla, todos los equipos vinculados quedan expuestos a la vez.

## Fuentes

- [GL.iNet: aviso de seguridad de GoodCloud (20 de noviembre de 2026)](https://www.gl-inet.com/en-eu/blogs/blog/glinet-security-notice-2026-11-20)
- [BleepingComputer: Hackers exploit GL.iNet cloud flaw to infect routers, KVM devices](https://www.bleepingcomputer.com/news/security/hackers-exploit-glinet-cloud-flaw-to-infect-routers-kvm-devices/)
- [SecurityWeek: GL.iNet Routers, KVMs Compromised via Remote Management Service Flaw](https://www.securityweek.com/gl-inet-routers-kvms-compromised-via-remote-management-service-flaw/)
- [The Hacker News: Hackers Exploited GL.iNet Cloud Flaw to Install Malware on Routers and KVM Devices](https://thehackernews.com/2026/11/hackers-exploited-glinet-cloud-flaw-to.html)
