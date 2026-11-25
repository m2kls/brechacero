---
title: "Fallos de autenticación NTLM en Windows tras el parche de noviembre"
description: "Microsoft confirma fallos de autenticación NTLM tras las actualizaciones de noviembre de Windows: afectan a proxies y SSO. A quién afecta y cómo solucionarlo."
date: 2026-11-25T16:58:00+01:00
category: vulnerabilidades
tags: [Windows, NTLM, Microsoft, actualizaciones, CVE-2026-118737, Windows Server, autenticación]
author: Redacción
photo: "File:Windows 11 key.jpg"
imageAlt: "Tecla de Windows en un teclado, sistema afectado por los fallos de autenticación NTLM"
---

Microsoft ha confirmado que las actualizaciones de seguridad de noviembre de Windows provocan fallos de autenticación NTLM en algunas empresas. El problema afecta sobre todo a proxies de autenticación, soluciones de inicio de sesión único (SSO) y herramientas de empaquetado de aplicaciones de terceros que implementan NTLM de forma incorrecta. Microsoft lo ha documentado como problema conocido en el artículo KB5135557 y, por ahora, solo ofrece una solución temporal mediante el registro. Importa porque el cambio es la primera fase de un endurecimiento que en mayo de 2027 será obligatorio.

## Qué ha cambiado en NTLM con el parche de noviembre

Las actualizaciones publicadas a partir del 10 de noviembre corrigen la vulnerabilidad CVE-2026-118737, un fallo de ejecución remota de código en el entorno de llamadas a procedimientos remotos de Windows (RPC Runtime) de gravedad alta. Para cerrarlo, Microsoft ha empezado a reforzar la firma de mensajes NTLM, el viejo protocolo de autenticación que Windows mantiene por compatibilidad junto a Kerberos.

El plan tiene dos fases, según el propio artículo de soporte:

- **Fase 1 (10 de noviembre de 2026):** los equipos cliente ofrecen la firma NTLM por defecto. Los servidores siguen aceptando clientes que no firman, pero lo registran en el visor de eventos para que los administradores puedan detectarlos.
- **Fase 2 (mayo de 2027):** los servidores exigirán la firma por defecto y rechazarán a los clientes que no la usen.

## ¿Estoy afectado por los fallos de autenticación NTLM?

El cambio se aplica a Windows 11 (versiones 23H2 a 26H2), Windows 10 Enterprise LTSC 2021 y Windows Server 2016, 2019, 2022 y 2025. Un usuario doméstico normalmente no notará nada.

El fallo aparece en redes empresariales con productos de terceros que, al responder en el intercambio NTLM, envían el campo de información del destino (TargetInfo) vacío o incompleto. Con las nuevas protecciones, Windows exige que ese campo incluya el nombre del equipo y del dominio; si faltan, devuelve un error de inicio de sesión. Microsoft indica como pista que el evento 4021 del registro NTLM muestre "Target Information: Not Found" o que las capturas de red tengan una lista de información del destino vacía.

Este aviso se suma a otros problemas reconocidos tras el parche de noviembre, como errores de activación, problemas de impresión con documentos complejos y fallos de instalación, según BleepingComputer.

## Cómo solucionarlo

Microsoft no ha publicado todavía una corrección definitiva. Mientras tanto propone, en este orden:

1. **Solución temporal:** crear el valor `ClientAllowUnsignedNtlm` (tipo DWORD) con valor `1` en la clave `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0`. Hace que el cliente deje de ofrecer la firma NTLM, así que reduce la protección: úsalo solo en los equipos afectados y como medida provisional. Microsoft advierte de que podría eliminar esta opción en el futuro.
2. **Usar Kerberos** en el producto afectado si lo admite. Kerberos no se ve afectado por este cambio.
3. **Pedir al fabricante una actualización** que cumpla con NTLM. Según Microsoft, actualizar el producto o usar una configuración de autenticación compatible "es la solución recomendada a largo plazo".

Lo sensato es no desinstalar el parche: corrige una vulnerabilidad grave. Conviene además aprovechar los eventos 4022 y 4023 del registro Microsoft-Windows-NTLM/Operational para localizar ya qué equipos y aplicaciones no firman, antes de que la fase 2 los deje fuera en mayo. Si quieres entender cómo se clasifican estos fallos, lo explicamos en [qué es una CVE](/que-es-una-cve/). Y si tu empresa usa Outlook, recuerda que este mes también hubo que parchear [un fallo de Outlook que ya se estaba explotando](/outlook-zero-day-noviembre-2026/).

## Fuentes

- [Microsoft – KB5135557: NTLM signing security improvements in Windows](https://support.microsoft.com/en-us/help/5135557)
- [BleepingComputer – Microsoft confirms authentication issues after November updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-confirms-authentication-issues-after-november-updates/)
