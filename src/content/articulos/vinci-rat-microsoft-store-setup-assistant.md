---
title: "Vinci RAT: una app de la Microsoft Store instalaba un troyano en Windows"
description: "La app «Setup Assistant» de la Microsoft Store abría la puerta a Vinci RAT, un troyano que controla el PC a distancia. Cómo llegaba y cómo comprobar tu equipo."
date: 2026-11-27T18:57:00+01:00
category: noticias
tags: [Vinci RAT, Microsoft Store, Windows, troyano, eSentire, Setup Assistant, malware]
author: Redacción
photo: "File:Microsoft Windows 11.jpg"
imageAlt: "Portátil con Windows 11, el sistema en el que la app de la Microsoft Store instalaba Vinci RAT"
---

Investigadores de la empresa canadiense eSentire han descubierto que una aplicación publicada en la **Microsoft Store**, llamada **"Setup Assistant"**, servía para instalar **Vinci RAT**, un troyano de acceso remoto hasta ahora desconocido que permite a los atacantes controlar el PC. La app estuvo disponible al menos desde el 1 de junio de 2026, es decir, más de cinco meses. eSentire la denunció a Microsoft el 10 de noviembre y, según su informe, la respuesta fue que no infringía sus condiciones. Este 27 de noviembre la app ya no aparece en la tienda.

El caso importa porque mucha gente, y muchas empresas, consideran la tienda oficial de Microsoft una fuente segura por defecto.

## Cómo llegaba Vinci RAT a los equipos

La cadena empezaba con una búsqueda tan corriente como "herramienta de recortes". Según eSentire y The Hacker News, el proceso era este:

1. La víctima acababa en una web falsa de descargas, alojada en el dominio *codes-team[.]com*, que imitaba la página de la herramienta de recortes de Windows. Ese mismo dominio tenía subdominios que imitaban las descargas de **Microsoft Teams** y **Roblox**.
2. La web entregaba un archivo llamado "Snipping-Tool.exe". Era un instalador legítimo de la Microsoft Store, firmado por Microsoft, lo que no levanta sospechas.
3. Ese instalador descargaba de la tienda la app "Setup Assistant", del editor "ETPS Ltd". Es una aplicación Electron con el código ofuscado.
4. Setup Assistant contactaba con un servidor de los atacantes y ejecutaba las órdenes que recibía. Con ellas creaba una tarea programada que se repetía cada diez minutos, desactivaba la protección AMSI de Windows (la que permite al antivirus revisar los scripts) y descargaba el troyano.

Vinci RAT es un programa en PowerShell de unas 800 líneas. Recopila información del equipo, detecta qué antivirus o EDR hay instalado (Defender, ESET, Kaspersky, Bitdefender, CrowdStrike y otros), abre una consola remota y puede descargar y ejecutar otros programas, incluso directamente en memoria. En la práctica, deja el ordenador en manos de los atacantes para lo que quieran instalar después.

## ¿Por qué no lo frenó la Microsoft Store?

eSentire critica que Microsoft considerara que la app no violaba sus condiciones, pese a que su propio documento de criterios de malware incluye el código ofuscado y el comportamiento de puerta trasera. Tampoco está claro si la retirada de la tienda la hizo Microsoft o los propios atacantes. Microsoft no ha hecho declaraciones públicas.

No es el primer caso este mes de software aparentemente legítimo que esconde un troyano: hace unos días contamos que [los instaladores oficiales de Q-Dir y DesktopOK](/q-dir-desktopok-instaladores-troyano/) también venían manipulados.

## Cómo saber si tu PC con Windows está afectado

Revisa estos puntos si has buscado y descargado alguna herramienta para Windows en los últimos meses:

- Abre **Configuración > Aplicaciones > Aplicaciones instaladas** y busca **"Setup Assistant"**. Si aparece y no sabes de dónde viene, desinstálala.
- Mira en el **Programador de tareas** si hay tareas desconocidas que se ejecutan cada pocos minutos y lanzan PowerShell.
- Pasa un análisis completo con un antivirus actualizado. Si el equipo es del trabajo, avisa al departamento de TI: un troyano de acceso remoto obliga a revisar el equipo a fondo y a cambiar las contraseñas usadas en él.

Y para el futuro:

- **Descarga las herramientas desde la web oficial del fabricante** o abriendo tú la Microsoft Store, nunca desde enlaces de resultados patrocinados o webs que "ayudan" a instalar. La herramienta Recortes ya viene incluida en Windows.
- En empresas, eSentire recomienda **limitar qué apps de la tienda se pueden instalar** (con directivas de grupo, AppLocker, WDAC o Intune) y vigilar el uso anómalo de PowerShell.
- Que una aplicación esté en una tienda oficial no garantiza que sea segura. Lo mismo aplica a las extensiones del navegador, como vimos con [la falsa extensión de Google Sheets que leía Gmail](/malware-remus-extension-falsa-google-sheets-gmail/).

## Fuentes

- eSentire: [Vinci RAT Lives in the Microsoft Store](https://www.esentire.com/blog/vinci-rat-lives-in-the-microsoft-store)
- The Hacker News: [Microsoft Store App Found Delivering Vinci RAT Capable of Remote System Control](https://thehackernews.com/2026/11/microsoft-store-app-found-delivering.html)
