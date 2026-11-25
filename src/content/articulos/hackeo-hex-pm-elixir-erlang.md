---
title: "Hackeo de Hex.pm: atacan el repositorio de paquetes de Elixir y Erlang"
description: "Un fallo de gravedad 10 (CVE-2026-129514) permitió atacar Hex.pm, el repositorio de Elixir y Erlang. No se alteraron paquetes, pero hay que cambiar contraseña y 2FA."
date: 2026-11-26T00:54:00+01:00
category: noticias
tags: [Hex.pm, Elixir, Erlang, CVE-2026-129514, cadena de suministro, repositorio de paquetes, filtración]
author: Redacción
photo: "File:Official Elixir logo.png"
imageAlt: "Logotipo de Elixir, el lenguaje cuyo repositorio Hex.pm ha sufrido un hackeo"
---

El hackeo de Hex.pm, el repositorio oficial de paquetes de los lenguajes Elixir y Erlang, se ha confirmado esta semana. Un atacante aprovechó el lunes 23 de noviembre una vulnerabilidad de gravedad máxima, **CVE-2026-129514** (CVSS 10), para ejecutar órdenes en seis servidores web del servicio. El equipo de Hex.pm asegura que ningún paquete fue modificado, pero no puede descartar que se accediera a la base de datos con correos, hashes de contraseñas y secretos de verificación en dos pasos, así que pide a todos los usuarios que cambien sus credenciales.

## Qué ha pasado en el hackeo de Hex.pm

Según el informe del propio proyecto, el ataque duró apenas trece minutos: entre las 18:16 y las 18:29 (hora UTC) del lunes llegaron 69 peticiones maliciosas desde dos direcciones IP, y a las 18:31 la corrección ya estaba desplegada en todos los servidores. El atacante consiguió crear archivos en seis servidores web, con los permisos de la cuenta de servicio del registro. Su identidad no se conoce.

Lo llamativo es el origen del fallo. Estaba en el servidor de Hex.pm (no en la herramienta `hex` que usan los programadores) y procedía de un cambio de febrero de 2016 que eliminó una comprobación de seguridad al procesar ciertos datos. Durante casi diez años, el servicio aceptó estructuras que podían convertirse en ejecución de órdenes sin autenticarse. Curiosamente, un aviso independiente sobre el mismo fallo llegó por correo a las 19:07, cuando el ataque ya había terminado.

## ¿Se han manipulado paquetes de Elixir o Erlang?

Es la gran pregunta en cualquier ataque a la cadena de suministro de software, y aquí la respuesta, por ahora, es tranquilizadora. Durante la ventana del ataque se publicaron 23 versiones de paquetes y todas coinciden con el registro de auditoría, según Hex.pm. La clave con la que se firma el registro es la única credencial que el equipo no ha cambiado, porque no estaba al alcance del atacante.

Lo que sí puede haberse expuesto, según el propio equipo, es:

- direcciones de correo de los usuarios,
- hashes de contraseñas y de claves de API,
- secretos de la verificación en dos pasos (2FA),
- datos de sesión,
- y el contenido de paquetes privados, que podría haberse leído sin dejar rastro.

Hex.pm ha cerrado la sesión de todos los usuarios, ha rotado las claves de sesión y de tokens y ha sustituido todas las credenciales a las que el atacante pudo llegar. También ha notificado el incidente a la autoridad sueca de protección de datos, a la CISA estadounidense y a ENISA.

## A quién afecta

A cualquier persona u organización con cuenta en Hex.pm, que es el gestor de paquetes por defecto de Elixir y de muchos proyectos de Erlang. Quien solo descarga paquetes públicos no tiene que hacer nada especial, pero quien publica paquetes o tiene paquetes privados debe actuar. Las copias autoalojadas del servidor hexpm siguen siendo vulnerables hasta que se actualicen.

## Qué hacer si usas Hex.pm

1. **Cambia la contraseña** de tu cuenta en hex.pm, y si la reutilizabas en otro sitio, cámbiala también allí. Te explicamos cómo hacerlo bien en nuestra guía para [proteger tus cuentas con contraseñas fuertes y 2FA](/proteger-cuentas-contrasenas-2fa/).
2. **Restablece la verificación en dos pasos**, ya que el secreto podría haberse copiado.
3. **Vuelve a iniciar sesión** en la herramienta de línea de órdenes (`mix hex.user auth` en Elixir o `rebar3 hex user auth` en Erlang). Según el equipo, las claves de API no hace falta sustituirlas.
4. **Descarga paquetes solo desde repo.hex.pm** hasta que se publique la nueva versión del cliente.
5. **Desconfía de correos** que hablen del incidente y pidan credenciales: tras una filtración de direcciones es habitual el phishing. Repasa [cómo detectar un correo de phishing](/como-detectar-phishing/).
6. **Si alojas tu propio hexpm**, aplica el parche (commit 379b0a29) cuanto antes.

En paralelo, el ecosistema ha corregido otros fallos en librerías populares de Elixir que no tienen relación con el ataque: ash (CVE-2026-124283, corregido en 3.38.0), db_connection (CVE-2026-133555, en 2.10.3) y flop (CVE-2026-130411). Conviene revisar las dependencias del proyecto y actualizar las afectadas.

## Fuentes

- [Hex.pm: Security incident on hex.pm](https://hex.pm/blog/security-incident-on-hexpm)
- [GitHub: aviso de seguridad de hexpm GHSA-9pmm-hf4r-27pg](https://github.com/hexpm/hexpm/security/advisories/GHSA-9pmm-hf4r-27pg)
- [The Hacker News: Hackers Exploited CVSS 10.0 Hex.pm RCE Flaw to Compromise 6 Package Registry Servers](https://thehackernews.com/2026/11/hackers-exploited-cvss-100-hexpm-rce.html)
- [Elixir Forum: Hex.pm security incident](https://forum.elixirforum.com/t/hex-pm-security-incident/77503)
