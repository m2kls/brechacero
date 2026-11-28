---
title: "Windows Server 2028 elimina WSUS, SMBv1, VBScript y WMIC"
description: "Windows Server 2028 dejará de incluir WSUS, SMBv1, VBScript, WMIC y PPTP. Qué desaparece, qué lo sustituye y cómo preparar tus servidores con tiempo."
date: 2026-11-28T02:56:00+01:00
category: noticias
tags: [Windows Server 2028, Microsoft, WSUS, SMBv1, VBScript, WMIC, administración de sistemas]
author: Redacción
photo: "File:Servers in a Rack.jpg"
imageAlt: "Servidores en un rack, como los que tendrán que adaptarse a los cambios de Windows Server 2028"
---

Windows Server 2028 no incluirá el rol de servidor WSUS, la herramienta con la que miles de empresas distribuyen desde hace casi veinte años las actualizaciones de Windows en sus redes. Microsoft lo ha confirmado en su documentación de funciones retiradas, que también anuncia la desaparición de SMBv1, VBScript, la utilidad WMIC, los protocolos de VPN PPTP y L2TP, y el arranque BIOS heredado. La lista corresponde a la versión preliminar, presentada en Ignite 2026, y todavía puede cambiar.

## Qué desaparece en Windows Server 2028

La tabla publicada por Microsoft en Learn incluye estos elementos y sus sustitutos recomendados:

- **WSUS**: sigue disponible y con soporte en Windows Server 2025 y anteriores. Microsoft recomienda pasar a Windows Autopatch, Intune o Azure Update Manager y promete dar más detalles sobre cómo parchear entornos desconectados de internet.
- **SMBv1**: se sustituye por SMBv2 o SMBv3. Es la versión del protocolo de compartición de archivos que aprovechó WannaCry en 2017.
- **VBScript**: se sustituye por PowerShell para scripts de administración y JavaScript en la web.
- **WMIC**: desaparece la utilidad de línea de comandos, no WMI. Las consultas pasan a PowerShell.
- **PPTP y L2TP** para acceso remoto: se sustituyen por IKEv2 o SSTP. DirectAccess también se retira en favor de Always On VPN.
- **Arranque BIOS heredado**: será obligatorio UEFI y las máquinas virtuales de Hyper-V deberán ser de generación 2.
- También salen el servidor WINS (reemplazado por DNS), las VM blindadas (sustituidas por las nuevas Trusted VMs), el comando `at.exe` (reemplazado por `schtasks`) y .NET Framework 3.5 como componente integrado, que seguirá disponible con un instalador aparte.

Además, quedan marcados como obsoletos, aunque aún se incluyen, BranchCache, Windows Deployment Services con PXE y Windows PowerShell 5.1, que debe dar paso a PowerShell 7.

## Por qué es una buena noticia para la seguridad

Varios de los componentes eliminados llevan años en la lista de recomendaciones para desactivar. SMBv1 no tiene cifrado moderno y fue la puerta de entrada de gusanos como WannaCry y NotPetya. PPTP usa un cifrado roto desde hace más de una década. VBScript y WMIC son herramientas que los atacantes usan con frecuencia para moverse por una red sin instalar nada nuevo, una técnica conocida como *living off the land*; el ransomware The Gentlemen, por ejemplo, usa WMIC para borrar las copias de seguridad de Windows antes de cifrar.

El propio WSUS ha dado problemas recientes: en 2025 Microsoft tuvo que publicar un parche de emergencia para una vulnerabilidad de ejecución remota de código explotada activamente en este servicio (CVE-2025-59287). Si quieres entender qué significan estos identificadores, lo explicamos en [qué es una CVE](/que-es-una-cve/).

## ¿A quién afecta y qué hacer ya?

El cambio no obliga a nada inmediato: Windows Server 2025 mantiene WSUS y el resto de componentes durante su ciclo de soporte. Pero las organizaciones que planean migrar en los próximos años deberían empezar a revisar dependencias:

- Inventariar scripts `.vbs` y tareas programadas que usen `wmic` o `at`, y reescribirlos en PowerShell.
- Comprobar qué equipos siguen usando SMBv1 (impresoras y NAS antiguos suelen ser los culpables) y desactivarlo ya en los servidores actuales.
- Migrar las VPN con PPTP o L2TP a IKEv2 o SSTP.
- Planificar la alternativa a WSUS, sobre todo en redes aisladas o industriales, donde las soluciones en la nube no siempre son viables.

Hacer estos deberes ahora reduce la superficie de ataque hoy, no solo cuando llegue la nueva versión. Si gestionas parches de Windows, también te interesa nuestro análisis de los [fallos de autenticación NTLM tras el parche de noviembre](/fallo-autenticacion-ntlm-windows-noviembre/).

## Fuentes

- [Microsoft Learn: Features removed or no longer developed in Windows Server (Windows Server 2028 preview)](https://learn.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server?tabs=ws28-preview)
- [BleepingComputer: Microsoft removes WSUS server role in Windows Server 2028](https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-wsus-server-role-in-windows-server-2028/)
- [Microsoft Threat Intelligence: The Gentlemen ransomware](https://www.microsoft.com/en-us/security/blog/2026/05/28/the-gentlemen-ransomware-dissecting-a-self-propagating-go-encryptor/)
