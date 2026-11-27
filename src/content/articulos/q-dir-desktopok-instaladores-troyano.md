---
title: "Q-Dir y DesktopOK: instaladores de la web oficial traían un troyano"
description: "Los instaladores de Q-Dir y DesktopOK de la web oficial de SoftwareOK venían con un troyano en Python. Versiones afectadas y cómo comprobar si tu PC está limpio."
date: 2026-11-27T08:55:00+01:00
category: noticias
tags: [Q-Dir, DesktopOK, SoftwareOK, troyano, cadena de suministro, Windows, AhnLab]
author: Redacción
photo: "File:Tecla Windows (Windows 11).jpg"
imageAlt: "Tecla de Windows en un teclado, sistema en el que se instalan Q-Dir y DesktopOK"
---

Si usas **Q-Dir** o **DesktopOK** en Windows, conviene revisar el equipo. El equipo de análisis de AhnLab (ASEC) ha descubierto que varios instaladores de estas dos utilidades gratuitas, descargados desde la **web oficial de SoftwareOK**, venían manipulados para instalar un **troyano de acceso remoto escrito en Python**. El informe se publicó el 25 de noviembre y se ha difundido este 27 de noviembre. Lo más delicado es que el archivo malicioso no llegaba desde una web falsa, sino desde el sitio del propio desarrollador, e incluso durante la actualización de copias que ya estaban instaladas.

Q-Dir es un explorador de archivos con varios paneles y DesktopOK sirve para guardar y restaurar la posición de los iconos del escritorio. Las dos son del desarrollador alemán Nenad Hrg y tienen muchos usuarios entre administradores de sistemas y aficionados a personalizar Windows.

## Qué versiones de Q-Dir y DesktopOK están afectadas

ASEC ha confirmado instaladores manipulados en estas versiones:

- Q-Dir 12.85.0.0, 12.84.0.0 y 12.83.0.0
- DesktopOK 12.85.0.0 y 12.82.0.0

Los investigadores advierten de que no saben cómo se sustituyeron los archivos ni durante cuánto tiempo estuvieron disponibles, así que la lista puede no ser completa. Si descargaste o actualizaste alguno de los dos programas en las últimas semanas, trátalo como sospechoso aunque tu versión no aparezca.

## Cómo funcionaba el troyano

El truco estaba en que el usuario no notaba nada raro. El instalador ponía en marcha el programa legítimo, que funcionaba con normalidad, y mientras tanto descargaba en segundo plano una copia de 7-Zip y un archivo comprimido con un intérprete de Python completo. Así el malware no necesitaba que el equipo tuviera Python instalado. Después creaba una **tarea programada** con un nombre que imita a Microsoft Edge para arrancar en cada inicio.

Una vez dentro, el troyano permite al atacante ejecutar comandos y código Python, subir y bajar archivos, hacer capturas de pantalla y recopilar información del sistema. También compara los procesos en marcha con una lista de **1.206 nombres de productos de seguridad**, entre ellos antivirus y EDR conocidos como ESET, Kaspersky, CrowdStrike o SentinelOne, y envía el resultado a su servidor. Es la forma habitual de decidir si merece la pena seguir con un equipo o si hay riesgo de que los detecten.

Un detalle que complica la detección: los ejecutables legítimos que iban dentro del instalador coincidían con los hashes publicados y estaban firmados correctamente por el desarrollador. La firma cubría el programa, no el instalador que lo envolvía. Es un recordatorio de que ver una firma válida en un componente no garantiza que todo el paquete sea de fiar.

El código contiene comentarios en chino, lo que según ASEC apunta a un entorno de habla china, aunque no atribuye el ataque a ningún grupo concreto. El caso recuerda a otros secuestros de descargas oficiales, como el de las actualizaciones de Notepad++, y a la oleada de [malware escondido en repositorios y paquetes de código](/polinrider-malware-repositorios-github-python/).

## ¿Estoy afectado? Cómo comprobarlo

ASEC recomienda estos pasos a quien use Q-Dir o DesktopOK:

1. **Desinstala** el programa y vuelve a instalar la última versión. Antes de ejecutar el nuevo instalador, compara su huella SHA-256 con la que aparece en la página oficial. En Windows puedes calcularla en PowerShell con `Get-FileHash` seguido de la ruta del archivo.
2. **Desinstalar no elimina el troyano**. Abre el Programador de tareas y busca una tarea llamada `MicrosoftEdge_dcntel` dentro de una carpeta `UPnp`; Microsoft Edge no crea tareas con ese nombre.
3. Revisa si existen las carpetas `C:\ProgramData\Microsoft\DeviceSync\b2` o `C:\ProgramData\DeviceSync\b2`, que contienen el intérprete de Python del malware.
4. Actualiza el antivirus y haz un **análisis completo**.
5. Si encuentras rastros, desconecta el equipo de la red, cambia desde otro dispositivo las contraseñas que hayas usado en él (empezando por el correo y la banca) y activa la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/). En un ordenador de empresa, avisa al equipo de seguridad: el atacante pudo usarlo como puerta de entrada.

## Qué pueden hacer los desarrolladores

AhnLab aprovecha el caso para pedir a quienes publican software que firmen también los instaladores y comprueben los hashes en cada paso, desde la compilación hasta la subida al servidor de descargas. Para los usuarios, la lección es incómoda: descargar desde la web oficial sigue siendo lo correcto, pero no es una garantía absoluta. Comprobar el hash publicado y desconfiar de un programa que de repente se conecta a servidores extraños son hábitos que ayudan, igual que los que ya recomendábamos frente a las [falsas pruebas de empleo con paquetes maliciosos](/paquetes-nuget-maliciosos-falsas-pruebas-empleo/).

En el momento de escribir esta noticia, SoftwareOK no había publicado un comunicado sobre el incidente.

## Fuentes

- [AhnLab ASEC: Software Supply Chain Attack via the Official SoftwareOK Website](https://asec.ahnlab.com/en/96827/)
- [Cyber Security News: Hackers Turn Trusted Windows Software Downloads Into Tools for Secretly Controlling PCs](https://cybersecuritynews.com/hackers-turn-trusted-windows-software/)
