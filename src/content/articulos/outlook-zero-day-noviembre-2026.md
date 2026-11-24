---
title: "Microsoft corrige un fallo de Outlook que ya se está explotando: actualiza Office cuanto antes"
description: "El parche de noviembre de 2026 corrige más de mil fallos, entre ellos un zero-day de Outlook que filtra tu hash de contraseña. Qué es y cómo protegerte."
date: 2026-11-24
category: vulnerabilidades
tags: [Microsoft, Outlook, zero-day, parches, Patch Tuesday]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
photo: "File:Microsoft_sign_closeup.jpg"
imageAlt: "Cartel de Microsoft en su sede de Redmond"
---

Microsoft publicó el pasado 10 de noviembre de 2026 su actualización mensual de seguridad, el conocido *Patch Tuesday*. Es una de las más grandes que se recuerdan: según CSO Online, corrige 1.094 vulnerabilidades, de las que 63 están calificadas como críticas. Pero la que más preocupa no es la que tiene la nota más alta, sino una de gravedad media que ya se está aprovechando en ataques reales.

## El fallo: CVE-2026-124194 en Outlook

La vulnerabilidad afecta a Outlook dentro de Microsoft 365 Apps for Enterprise y Office LTSC 2021 y 2024. Tiene una puntuación CVSS de 6,5 sobre 10, es decir, gravedad media. Entonces, ¿por qué tanta prisa?

Porque es un zero-day: los atacantes la estaban explotando antes de que existiera el parche. Si quieres entender qué significan estas cifras, te lo explicamos en [qué es una CVE y cómo leer su CVSS](/que-es-una-cve/).

### Qué permite hacer

Al abrir un archivo malicioso preparado por el atacante, Outlook se conecta a un servidor controlado por él sin mostrar el aviso habitual de contenido externo. En esa conexión, el equipo entrega el hash NTLMv2 del usuario, una versión cifrada de sus credenciales de Windows.

Con ese hash, el atacante puede:

- **Reenviarlo** a otros servicios de la red para iniciar sesión como la víctima (lo que se conoce como *relay*).
- **Intentar descifrarlo** sin conexión para recuperar la contraseña, algo mucho más fácil si es corta o común.

> Las fuentes difieren en el detalle: CSO Online habla de "un archivo de Office" y Malwarebytes de "un archivo de mensaje". En ambos casos, la clave es la misma: hace falta que la víctima abra un archivo enviado por el atacante.

## Por qué una nota de 6,5 merece prioridad

Este caso es un buen ejemplo de que el CVSS no lo es todo. A la hora de decidir qué parchear primero, pesa más que una vulnerabilidad se esté explotando activamente que su puntuación teórica. Un fallo "medio" usado en ataques reales es más urgente que uno "crítico" que nadie ha conseguido aprovechar todavía.

## Otros fallos destacados del mes

Entre los más de mil fallos corregidos hay varios con la puntuación máxima práctica de 9,8, según CSO Online y Malwarebytes:

- **CVE-2026-119958**: ejecución remota de código en LDAP de Windows.
- **CVE-2026-118207**: ejecución remota de código en Exchange.
- **CVE-2026-116928**: fallo en Windows Search que podría activarse cuando Exchange indexa adjuntos. Según Microsoft, no se ha visto explotado.

## Qué tienes que hacer

**Si usas Office en casa:**

1. Abre cualquier aplicación de Office (Word, Excel u Outlook).
2. Ve a Archivo › Cuenta (en Outlook, Cuenta de Office).
3. Pulsa Opciones de actualización › Actualizar ahora. Si no aparece, primero elige Habilitar actualizaciones.
4. Revisa también Windows Update e instala todo lo pendiente.

**Si gestionas equipos en una empresa:**

- Prioriza el despliegue del parche de Office en todos los puestos.
- Mientras tanto, refuerza el filtrado del correo entrante y recuerda a la plantilla que no abra adjuntos inesperados.
- Valora bloquear el tráfico SMB saliente hacia Internet (puerto 445) en el cortafuegos, una medida clásica contra la filtración de hashes NTLM.

## Lo que nos enseña este caso

Los ataques que dependen de "abrir un archivo" siguen funcionando porque combinan un fallo técnico con un engaño. La defensa también combina ambas cosas: actualizar rápido y desconfiar de adjuntos inesperados, aunque parezcan venir de alguien conocido. Te damos más pistas en nuestro artículo sobre [phishing con IA](/phishing-con-ia/).

**Fuentes:** [CSO Online](https://www.csoonline.com/article/4247015/november-2026-patch-tuesday-63-critical-microsoft-fixes-plus-an-outlook-zero-day-that-allows-theft-of-hashed-credentials.html) · [Malwarebytes](https://www.malwarebytes.com/es/blog/bugs/2026/11/microsoft-patch-tuesday-fixes-outlook-flaw-already-under-attack)
