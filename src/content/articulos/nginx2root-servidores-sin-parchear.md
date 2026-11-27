---
title: "NGINX2Root: millones de servidores NGINX siguen sin parchear una semana después"
description: "Fallos NGINX2Root: unos 10 millones de servidores NGINX siguen expuestos a cinco bugs críticos corregidos el 18 de noviembre. Cómo saber si te afecta y protegerte."
date: 2026-11-27T12:57:00+01:00
category: vulnerabilidades
tags: [NGINX, NGINX2Root, CVE-2026-123007, servidores web, HTTP/2, parches, Linux]
author: Redacción
photo: "File:Servers in a Rack.jpg"
imageAlt: "Servidores en un rack, como los que ejecutan NGINX afectados por los fallos NGINX2Root"
---

Más de una semana después de que se publicaran los parches, los fallos **NGINX2Root** siguen siendo un problema enorme. Según datos de Censys recogidos el 26 de noviembre por The Hacker News, **más de 10 millones de servicios NGINX expuestos a internet** ejecutan todavía una versión afectada con HTTP/2 activado. NGINX es el servidor web más usado del mundo: está detrás de cientos de millones de webs, como servidor principal, proxy inverso o balanceador. Si administras uno, esta es la noticia que te interesa hoy.

## Qué son los fallos NGINX2Root

NGINX2Root es el nombre que la empresa de seguridad Xint dio a **cinco vulnerabilidades críticas** de corrupción de memoria (en su mayoría *use-after-free*) que se corrigieron el 18 de noviembre en **nginx 1.30.7 (estable) y 1.31.9 (mainline)**. En el peor caso, permiten a un atacante sin credenciales ejecutar código en el servidor con los permisos del proceso de NGINX:

- **CVE-2026-123007**: el más grave. Afecta al control de flujo de HTTP/2 y está presente desde la versión 1.9.5, de 2015, cuando NGINX incorporó HTTP/2. Basta con que HTTP/2 esté activo en un puerto accesible.
- **CVE-2026-123633**: afecta a HTTP/2 cuando NGINX hace de proxy hacia un servidor interno (versiones 1.19.7 en adelante).
- **CVE-2026-121810**: afecta a HTTP/3 al hacer de proxy (desde 1.25.0). Desactivar HTTP/2 no protege de este.
- **CVE-2026-123634**: en el resolvedor DNS interno, con configuraciones concretas de subpeticiones y *mirror*.
- **CVE-2026-113425**: en el proxy de correo, cuando se usa autenticación por `auth_http`.

Las puntuaciones de gravedad varían según la fuente (F5, el fabricante de NGINX, las sitúa en 9,2 sobre 10 con CVSS 4.0 en sus avisos), pero todas coinciden en tratarlas como críticas. Si no tienes claro qué significa una CVE o cómo se mide su gravedad, lo explicamos en [qué es una CVE](/que-es-una-cve/).

Lo llamativo del caso es cómo se descubrieron. Xint encontró el primer fallo preparando una competición de hacking y el resto con un análisis automatizado apoyado en IA. Otras firmas (Wiz, Rapid7, Ikotas Labs y Metnir) encontraron de forma independiente los dos fallos de HTTP/2. Además, Xint mostró que podían encadenarse con un fallo del núcleo Linux en el módulo SCTP para llegar a root en el equipo, incluso desde dentro de un contenedor Docker; de ahí el nombre.

## ¿Se están explotando ya?

A fecha de publicación no hay ataques confirmados. F5, Wiz y Rapid7 aseguran no tener constancia de explotación real, y Bitsight tampoco la ha detectado. Pero hay motivos para no relajarse: Rapid7 ha publicado una prueba de concepto que ejecuta código contra NGINX en un entorno de laboratorio, y la experiencia dice que entre la prueba pública y los ataques masivos suelen pasar pocos días.

## ¿Estoy afectado?

Si usas NGINX y no has actualizado desde el 18 de noviembre, muy probablemente sí. Ten en cuenta dos detalles:

- **Las distribuciones Linux aplican parches sin cambiar el número de versión.** Un Ubuntu 22.04 actualizado puede seguir mostrando nginx 1.18.0 aunque ya tenga la corrección. Consulta el aviso de seguridad de tu distribución en lugar de fiarte solo de `nginx -v`.
- **Recargar no basta.** Un `reload` mantiene el binario antiguo en memoria; hay que reiniciar el servicio o desplegar contenedores nuevos.

Los recuentos de servidores vulnerables se basan en la versión que anuncian, así que son una estimación. Censys contaba el 19 de noviembre unos 8,8 millones de servicios potencialmente expuestos al fallo principal y más de medio millón ya corregidos; la cifra posterior supera los 10 millones al incluir todos los fallos.

## Cómo proteger tu servidor NGINX

1. **Actualiza** a nginx 1.30.7 o 1.31.9, a NGINX Plus 37.0.8.1 o 37.3.0.1, o al paquete corregido de tu distribución, y reinicia el servicio.
2. Empieza por los servidores expuestos a internet, sigue por los proxies internos y termina por los que solo sirven ficheros estáticos: el fallo principal no necesita ninguna aplicación detrás.
3. Si no puedes actualizar ya, como **medida temporal** desactiva HTTP/2 y HTTP/3 en los puertos públicos y, si no usas el proxy de correo, cierra sus puertos. F5 advierte de que esto reduce el riesgo pero no corrige el fallo, y que puede romper servicios como gRPC.
4. En equipos que no lo necesiten, impide la carga del módulo SCTP del núcleo, que es la pieza que convierte el fallo en acceso root.
5. Revisa los registros de NGINX en busca de caídas inesperadas de procesos *worker*, que pueden indicar intentos de explotación.

Si estás empezando a administrar servidores, nuestra guía de [comandos de Linux básicos](/20-comandos-linux-para-empezar/) te ayudará a comprobar versiones y servicios.

## Fuentes

- [The Hacker News – ThreatsDay: 10M NGINX Services at Risk](https://thehackernews.com/2026/11/threatsday-250-rogue-extensions-10m.html) (26/11/2026)
- [BleepingComputer – Critical NGINX "NGINX2Root" bugs let attackers hijack servers](https://www.bleepingcomputer.com/news/security/critical-nginx-nginx2root-bugs-let-attackers-hijack-servers/)
- [Bitsight – NGINX2Root: five nginx vulnerabilities](https://www.bitsight.com/blog/nginx2root-cve-2026-123007-five-nginx-vulnerabilities)
- [F5 – Aviso K000164058 (CVE-2026-123007)](https://my.f5.com/manage/s/article/K000164058)
