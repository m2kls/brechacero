---
title: "OWASP Top 10 (2025) explicado para principiantes: los 10 riesgos web más importantes"
description: "Qué es el OWASP Top 10, las diez categorías de la edición 2025 explicadas con ejemplos sencillos y qué cambió respecto a la de 2021."
date: 2026-12-08
category: guias
tags: [OWASP, seguridad web, desarrollo seguro, aplicaciones web]
author: Redacción
imageCredit: "Logotipo: OWASP Top 10 (OWASP Foundation, CC BY-SA 4.0). Composición: Brecha Cero"
---

Si quieres dedicarte a la seguridad web, o simplemente programas aplicaciones, hay un documento que tienes que conocer: el OWASP Top 10. Es la lista de referencia de los riesgos de seguridad más importantes en aplicaciones web, y la usan desarrolladores, auditores y empresas de todo el mundo.

## Qué es OWASP

**OWASP** (*Open Worldwide Application Security Project*) es una fundación sin ánimo de lucro que publica herramientas, guías y documentación abierta sobre seguridad de aplicaciones. Su proyecto más conocido es el Top 10, que se actualiza cada pocos años a partir de datos reales de vulnerabilidades y de encuestas a profesionales del sector.

La edición más reciente es la 2025, la octava de la historia del proyecto.

## Las 10 categorías del OWASP Top 10:2025

### A01: Control de acceso roto
La aplicación no comprueba bien qué puede hacer cada usuario. Ejemplo clásico: cambias `/factura?id=1001` por `id=1002` en la URL y ves la factura de otra persona.
En 2025, esta categoría absorbe también el SSRF (*Server-Side Request Forgery*), cuando se engaña al servidor para que haga peticiones a sitios internos que no debería.

**Cómo se previene:** denegar por defecto y comprobar los permisos en el servidor en cada petición, nunca confiar en lo que oculta la interfaz.

### A02: Configuración de seguridad incorrecta
Contraseñas por defecto, paneles de administración expuestos, mensajes de error que muestran detalles internos, servicios innecesarios activados... Sube del puesto 5 al 2 respecto a 2021.

**Cómo se previene:** configuraciones mínimas y revisadas, procesos automáticos de despliegue y auditorías periódicas.

### A03: Fallos en la cadena de suministro de software (nueva)
Tu aplicación es tan segura como las librerías y herramientas de las que depende. Esta categoría amplía la antigua de "componentes vulnerables y desactualizados" para incluir dependencias comprometidas, sistemas de compilación y canales de distribución.

**Cómo se previene:** inventario de dependencias, actualizarlas, verificar su origen y vigilar avisos de seguridad (te explicamos cómo leerlos en [qué es una CVE](/que-es-una-cve/)).

### A04: Fallos criptográficos
Datos sensibles sin cifrar, algoritmos obsoletos, contraseñas guardadas sin un *hash* adecuado o claves escritas dentro del código.

**Cómo se previene:** HTTPS en todo, algoritmos actuales y funciones específicas para contraseñas (como Argon2 o bcrypt).

### A05: Inyección
La aplicación mezcla datos del usuario con órdenes (consultas SQL, comandos del sistema, código en el navegador...). Incluye la famosa [inyección SQL](/que-es-inyeccion-sql/) y el [Cross-Site Scripting (XSS)](/que-es-xss-cross-site-scripting/).

**Cómo se previene:** consultas parametrizadas, validación de entradas y codificación de salidas.

### A06: Diseño inseguro
Fallos que no son de código, sino de planteamiento. Por ejemplo, un sistema de recuperación de contraseña basado en preguntas cuya respuesta se encuentra en redes sociales.

**Cómo se previene:** pensar en la seguridad desde el diseño (modelado de amenazas) y no solo al final.

### A07: Fallos de autenticación
Permitir contraseñas débiles, no limitar los intentos de inicio de sesión, sesiones que no caducan o no ofrecer verificación en dos pasos.

**Cómo se previene:** limitar intentos, [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/), comprobar contraseñas contra listas filtradas y gestionar bien las sesiones.

### A08: Fallos de integridad de software o datos
Confiar en actualizaciones, *plugins* o datos sin verificar que no han sido alterados. Por ejemplo, una aplicación que descarga actualizaciones sin comprobar su firma.

**Cómo se previene:** firmas digitales, verificación de integridad y canales de distribución de confianza.

### A09: Fallos en el registro y las alertas de seguridad
Si no registras lo que pasa, o nadie revisa los avisos, un ataque puede durar meses sin que nadie lo note.

**Cómo se previene:** registrar inicios de sesión, errores y accesos sensibles, y configurar alertas que alguien revise.

### A10: Manejo incorrecto de condiciones excepcionales (nueva)
Qué hace la aplicación cuando algo sale mal: errores no controlados, fallos que dejan el sistema en un estado inseguro, o mensajes de error que revelan información interna.

**Cómo se previene:** gestionar todos los errores de forma explícita y "fallar de forma segura" (si algo falla, denegar el acceso en lugar de concederlo).

## Qué cambió respecto a 2021

| Cambio | Detalle |
|---|---|
| Se mantiene en el #1 | Control de acceso roto, que ahora incluye SSRF |
| Gran subida | Configuración incorrecta pasa del #5 al #2 |
| Nueva | Fallos en la cadena de suministro de software (#3) |
| Nueva | Manejo incorrecto de condiciones excepcionales (#10) |
| Bajadas | Criptografía (#2 → #4), Inyección (#3 → #5), Diseño inseguro (#4 → #6) |
| Cambios de nombre | Autenticación (#7) y Registro y alertas (#9) |

## Cómo practicar el OWASP Top 10 de forma legal

- **PortSwigger Web Security Academy:** gratuita, con laboratorios para casi todas las categorías.
- **OWASP Juice Shop:** una tienda online vulnerable a propósito que puedes ejecutar en tu equipo.
- **DVWA:** aplicación vulnerable clásica con niveles de dificultad.
- Las rutas de seguridad web de [TryHackMe y HackTheBox](/hackthebox-vs-tryhackme/).

> Practica siempre en estos entornos o en aplicaciones propias. Probar estas técnicas en webs ajenas sin permiso es ilegal.

## Preguntas frecuentes

**¿El OWASP Top 10 es una norma obligatoria?**
No es una ley, pero muchas empresas, auditorías y estándares lo usan como referencia mínima.

**¿Es solo para desarrolladores?**
No. Es igual de útil para pentesters, analistas y responsables de producto.

**¿Hay otras listas de OWASP?**
Sí, por ejemplo el OWASP API Security Top 10 o el Top 10 para aplicaciones con modelos de lenguaje (LLM).

**Fuente:** [OWASP Top 10:2025](https://owasp.org/Top10/2025/es/)
