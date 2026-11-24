---
title: "Fallo crítico en Idunno.AntiCsrf para ASP.NET explotado: no tiene parche"
description: "Atacan webs ASP.NET que usan la librería Idunno.AntiCsrf (CVE-2026-131914, CVSS 9,3). No habrá parche: cómo saber si la usas y cómo sustituirla."
date: 2026-11-24T22:55:00+01:00
category: vulnerabilidades
tags: [ASP.NET, Idunno.AntiCsrf, CVE-2026-131914, IIS, Mandiant, ejecución remota, Windows Server]
author: Redacción
photo: "File:NOIRLab HQ Server Racks (6V6A0402-CC).jpg"
imageAlt: "Armarios de servidores en un centro de datos, como los que alojan aplicaciones ASP.NET"
---

Un fallo crítico en Idunno.AntiCsrf, una vieja librería de protección contra ataques CSRF para aplicaciones ASP.NET, se está explotando ya en Internet y no va a tener parche: el proyecto está abandonado desde diciembre de 2008. La vulnerabilidad, registrada como CVE-2026-131914 y con una puntuación CVSS de 9,3, permite ejecutar código en el servidor web sin necesidad de usuario ni contraseña. Mandiant, el equipo de respuesta a incidentes de Google, ha confirmado la explotación, y la firma watchTowr ha visto sondeos masivos en busca de webs vulnerables. Si mantienes aplicaciones ASP.NET WebForms antiguas, conviene revisarlas hoy.

## Qué es Idunno.AntiCsrf y qué falla

Idunno.AntiCsrf es un módulo HTTP de terceros (el archivo `Idunno.AntiCsrf.dll`) que se añadía a aplicaciones ASP.NET para frenar ataques de falsificación de petición en sitios cruzados (CSRF). Fue popular a finales de los 2000, antes de que Microsoft incluyera sus propias defensas, y sigue presente en aplicaciones heredadas que nadie ha tocado en años.

El problema está en el orden en que trabaja: la librería deserializa datos que envía el visitante antes de comprobar si el token es válido. Es un caso clásico de deserialización insegura, uno de los fallos web más peligrosos porque convierte una petición manipulada en código que se ejecuta en el servidor. Según Mandiant, basta una única petición POST, sin autenticación y sin token válido. El código se ejecuta con los permisos del proceso de trabajo de IIS (`w3wp.exe`), lo que da al atacante acceso a la aplicación, a sus ficheros de configuración y, a menudo, a las credenciales de la base de datos.

Están afectadas las versiones hasta la 0.9.1 Beta, incluida la DLL 0.9.1.0. El fallo está en esta librería opcional, no en ASP.NET ni en WebForms.

## ¿Estoy afectado?

Solo si alguna de tus aplicaciones carga esta librería. Para comprobarlo:

- Busca `Idunno.AntiCsrf.dll` en las carpetas `bin` de tus aplicaciones web.
- Revisa los `Web.config` en busca de referencias a `AntiCsrfModule`.
- Prioriza las aplicaciones expuestas a Internet, que son las que se están sondeando.

watchTowr ha detectado que los atacantes envían peticiones que provocan una redirección para comprobar si el ataque funcionó. Una redirección extraña en los registros no prueba por sí sola que te hayan comprometido, pero sí que alguien lo ha intentado.

## Cómo protegerte del fallo de Idunno.AntiCsrf

Como no habrá actualización, la única solución real es quitar la librería y usar las defensas actuales:

1. **Sustituirla** por `System.Web.Helpers.AntiForgery` en ASP.NET clásico, por ViewState con MAC y cifrado junto a `ViewStateUserKey`, o por `IAntiforgery` si la aplicación está en ASP.NET Core.
2. **Restringir el acceso** a las aplicaciones afectadas (VPN, lista de IP permitidas o desconexión temporal) mientras se hace el cambio.
3. **Guardar los registros** de IIS y del proxy inverso antes de tocar nada, por si hay que investigar.
4. **Buscar señales de intrusión**: peticiones POST anómalas a páginas `.aspx` que devuelven 302 o 500, ficheros nuevos en la carpeta web y procesos inesperados lanzados por `w3wp.exe`.
5. **Si sospechas que te han atacado**, cambia los secretos de `Web.config` y `applicationHost.config` (claves `machineKey`, claves de cifrado y credenciales de bases de datos).

Hay un matiz importante que recuerdan los investigadores: cambiar las claves no elimina la librería, y eliminar la librería no te dice si ya ejecutaron código. Hacen falta las dos cosas, más la revisión de registros.

## Un problema que va más allá de esta librería

El caso recuerda el riesgo de las dependencias olvidadas. Un componente que dejó de mantenerse hace casi dos décadas sigue en producción y ahora es una puerta abierta. Tener un inventario de librerías y vigilar los avisos de vulnerabilidades es la mejor defensa; si no tienes claro cómo leer uno, te lo contamos en [qué es una CVE y cómo interpretar su gravedad](/que-es-una-cve/). Esta misma semana vimos otros fallos explotados en productos empresariales en nuestro repaso a [VMware, Cisco y Apache](/vmware-cisco-apache-fallos-explotados/).

## Fuentes

- [The Hacker News: Hackers exploit critical ASP.NET anti-CSRF library flaw allowing unauthenticated RCE](https://thehackernews.com/2026/11/hackers-exploit-critical-aspnet-anti.html)
- [Cyber Security News: Critical ASP.NET AntiCsrf flaw exploited in attacks](https://cybersecuritynews.com/critical-asp-net-anticsrf-flaw-exploited/)
