---
title: "Fallo en .NET: un solo bit saltaba la integridad de código de Windows y VirtualBox"
description: "Project Zero detalla cómo cambiar un bit en un archivo .NET esquivaba la protección de Windows 11 en modo S y de VirtualBox (CVE-2026-108398). Qué actualizar."
date: 2026-11-25T06:53:00+01:00
category: vulnerabilidades
tags: [.NET Framework, VirtualBox, Windows 11, Project Zero, CVE-2026-108398, CVE-2026-87268]
author: Redacción
photo: "File:VirtualBox screenshot.png"
imageAlt: "Ventana de Oracle VirtualBox, uno de los programas afectados por el fallo en .NET que saltaba la integridad de código"
---

Un fallo en .NET Framework permitía saltarse dos protecciones de Windows cambiando un único bit de un archivo. James Forshaw, investigador de Google Project Zero, ha publicado esta semana el análisis completo de un comportamiento del cargador de .NET Framework 4 que le permitió ejecutar código no confiable dentro del proceso protegido de Oracle VirtualBox y esquivar la integridad de código en modo usuario (UMCI) de Windows 11 en modo S. Los dos fallos tienen ya parche, pero conviene comprobar que están aplicados.

## Qué ha descubierto Project Zero

Windows comprueba los programas y bibliotecas antes de cargarlos para asegurarse de que están firmados o permitidos. Forshaw encontró que, ante un error concreto al mapear un archivo, .NET Framework recurría a un plan B: cargaba una copia del ensamblado en memoria que se saltaba esas comprobaciones.

Para provocar ese error bastaba con desactivar un indicador de la cabecera del archivo (IMAGE_FILE_EXECUTABLE_IMAGE). Con ese cambio, la llamada de Windows que mapea la imagen la rechaza, pero .NET la acaba cargando igualmente. En palabras del investigador: "Este cambio de un solo bit es todo lo que necesitas para cargar un ensamblado .NET no confiable".

No es un fallo que se pueda explotar a distancia: el atacante necesita poder ejecutar código como usuario normal en el equipo. Su valor está en romper barreras diseñadas precisamente para contener a ese usuario.

## Los dos CVE: VirtualBox y Windows

- **CVE-2026-87268 (Oracle VirtualBox en Windows).** VirtualBox endurece su propio proceso para que otros programas no puedan inyectarle código. Con esta técnica, un usuario sin privilegios lograba ejecutar código dentro de ese proceso protegido. Oracle le da una puntuación CVSS de 7,8 y dice que puede acabar en la "toma de control de Oracle VM VirtualBox". No es una fuga de la máquina virtual al anfitrión: el atacante ya está en el anfitrión. Se corrigió en la actualización de septiembre de Oracle.
- **CVE-2026-108398 (integridad de código de Windows).** En Windows 11 en modo S, que solo permite ejecutar software aprobado, un error lógico en la comprobación de políticas de .NET dejaba cargar el archivo manipulado. Microsoft lo puntúa con 8,8, lo corrigió el 13 de octubre de 2026 y lo marca como divulgado públicamente pero sin explotación conocida. Forshaw lo presentó en la conferencia 44Con en septiembre.

El investigador también describe cómo ejecutar código en un proceso con protección PPL (Protected Process Light) sin ser administrador, secuestrando un objeto COM que carga WerSecureFault.exe. Según su análisis, el parche de octubre no cambia la carga en procesos protegidos, así que esa vía seguiría funcionando. No tiene CVE propio.

## ¿Estoy afectado? Qué actualizar

- **VirtualBox:** abre el programa, entra en *Ayuda > Acerca de VirtualBox* y comprueba la versión. Si usas una compilación anterior a la actualización de septiembre de 2026, descarga la última desde la web oficial. Si sigues nuestra guía para [instalar Kali Linux en VirtualBox](/instalar-kali-linux-virtualbox/), es buen momento para actualizar.
- **Windows y .NET Framework:** instala la actualización acumulativa de .NET Framework del 13 de octubre de 2026 que corresponda a tu versión de Windows (en Windows 11 26H2 es la KB5127694). Si tienes Windows Update al día, ya debería estar instalada; compruébalo en el historial de actualizaciones.
- **Empresas con listas blancas de aplicaciones** (App Control, WDAC o modo S): el caso recuerda que .NET es una superficie de ataque a vigilar. Conviene restringir qué ensamblados pueden cargarse y monitorizar procesos que carguen .NET de forma inesperada.

Si quieres entender mejor cómo leer estas puntuaciones, lo explicamos en [qué es una CVE y cómo leer un aviso de seguridad](/que-es-una-cve/).

## Fuentes

- [Google Project Zero: análisis técnico sobre el endurecimiento de procesos de VirtualBox](https://projectzero.google/2026/11/virtualbox-process-hardening.html)
- [Oracle: Critical Patch Update de septiembre de 2026](https://www.oracle.com/security-alerts/cspusep2026verbose.html)
- [Microsoft: notas de la actualización acumulativa de .NET Framework del 13 de octubre de 2026](https://learn.microsoft.com/en-us/dotnet/framework/release-notes/2026/10-13-october-cumulative-update)
- [The Hacker News: Google researcher shows how a single bit change in .NET files bypassed Windows Code Integrity](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html)
