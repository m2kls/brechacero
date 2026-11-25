---
title: "Fallo en WHMCS: una inyección SQL expone datos de clientes sin iniciar sesión"
description: "WHMCS corrige tres fallos, uno de inyección SQL sin login que expone datos de clientes y hashes de administradores. Versiones 9.0.10 y 8.13.8: actualiza ya."
date: 2026-11-25T04:52:00+01:00
category: vulnerabilidades
tags: [WHMCS, inyección SQL, hosting, CVE-2026-82981, CVE-2026-93700, parches]
author: Redacción
photo: "File:NOIRLab HQ Server Racks (6V6A0402-CC).jpg"
imageAlt: "Armarios de servidores en un centro de datos, como los de las empresas de hosting que usan WHMCS"
---

**WHMCS**, el programa de facturación y gestión de clientes que usan miles de empresas de alojamiento web y revendedores de dominios en todo el mundo, ha publicado actualizaciones para tres vulnerabilidades. La más preocupante, **CVE-2026-82981**, es una inyección SQL que se puede explotar **sin iniciar sesión** y que permite leer registros de clientes y los hashes de las contraseñas de los administradores. WHMCS lo comunicó el 23 de noviembre junto con las versiones corregidas 9.0.10 y 8.13.8.

## Los tres fallos de WHMCS

- **CVE-2026-82981** (8,7 sobre 10 en CVSS 4.0): inyección SQL sin autenticación. Un atacante puede consultar la base de datos y sacar datos de clientes (nombres, correos, direcciones, a veces información de facturación) y los hashes de contraseña de los administradores, que después puede intentar descifrar.
- **CVE-2026-82979** (7,1): inyección SQL en el área de cliente. Requiere una cuenta de cliente con permiso para ver y gestionar contactos.
- **CVE-2026-93700** (9,0 en CVSS 3.1): fallo en las campañas de correo electrónico. Un cliente con sesión iniciada podría leer archivos de configuración, incluidas las credenciales de la base de datos, y ejecutar código en el servidor, aunque requiere cierta interacción.

Si no sabes cómo funciona una inyección SQL, la idea es que el programa mezcla lo que escribe el usuario con las consultas a la base de datos sin filtrarlo bien, de modo que un texto preparado cambia la consulta. Es una de las familias de fallos más antiguas y frecuentes en aplicaciones web.

## ¿A quién afecta?

A cualquier empresa que tenga instalado WHMCS en su propio servidor con una versión anterior a las corregidas, y de rebote a sus clientes, cuyos datos son los que están en juego. Si contratas hosting o dominios con un proveedor pequeño o mediano, es probable que su área de cliente funcione con WHMCS.

Las instalaciones de WHMCS Cloud se actualizan solas. WHMCS no ha informado de ataques que aprovechen estos fallos, pero el software ya ha sido objetivo en el pasado y un fallo sin autenticación en una aplicación expuesta a internet suele atraer intentos rápidamente.

## Qué hacer si usas WHMCS

1. **Actualiza** a WHMCS 9.0.10 o 8.13.8. Para la rama 9.1, el aviso menciona la 9.1.2. Si sigues en las ramas 8.0 a 8.12, tienes que pasar a una versión corregida: no habrá parche para ellas.
2. **Para CVE-2026-93700**, el aviso de WHMCS pide además borrar todas las campañas de correo programadas o en curso (Utilities > Email Campaigns) y vaciar la caché de plantillas (Utilities > System > System Cleanup > Empty Template Cache).
3. **Cambia las contraseñas de los administradores** si tu instalación ha estado expuesta sin actualizar, y activa el segundo factor en el panel de administración.
4. **Revisa los registros** del servidor web en busca de peticiones extrañas a WHMCS en los últimos días y limita el acceso al directorio de administración por IP.

Si eres cliente de un hosting, no tienes que hacer nada técnico, pero sí conviene que tu contraseña del área de cliente sea única. Puedes comprobar si tus datos aparecen en filtraciones con nuestra guía para [saber si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/). Y si tu proveedor te avisa de una brecha, repasa [qué hacer si tus datos aparecen en una filtración](/datos-en-filtracion-que-hacer/).

## Fuentes

- [WHMCS: CVE-2026-82981 Security Update 2026-11-23](https://help.whmcs.com/m/125386/l/2151347-cve-2026-82981-whmcs-security-update-2026-11-23)
- [WHMCS: CVE-2026-93700 Security Update 2026-11-23](https://help.whmcs.com/m/125386/l/2151351-cve-2026-93700-whmcs-security-update-2026-11-23)
- [WHMCS: notas de la versión 9.0](https://docs.whmcs.com/releases/9-0/9-0-release-notes/)
- [The Hacker News: WHMCS SQL Injection Could Expose Customer Data and Admin Password Hashes without Login](https://thehackernews.com/2026/11/whmcs-sql-injection-flaw-could-expose.html)
