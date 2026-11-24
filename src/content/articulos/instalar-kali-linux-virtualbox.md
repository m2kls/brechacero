---
title: "Cómo instalar Kali Linux en VirtualBox paso a paso (2026)"
description: "Guía para principiantes: descargar la imagen oficial, verificarla, importarla en VirtualBox y dejar Kali listo y seguro para practicar."
date: 2026-11-30
category: linux
tags: [Kali Linux, VirtualBox, laboratorio, máquinas virtuales]
author: Redacción
imageCredit: "Logotipo: Kali Linux (OffSec). Composición: Brecha Cero"
---

**Kali Linux** es la distribución más usada para aprender y trabajar en ciberseguridad: trae cientos de herramientas listas para usar. La forma más cómoda y segura de tenerla es en una máquina virtual, sin tocar tu sistema principal. En esta guía la instalamos en VirtualBox, gratis y en unos 20 minutos.

## Antes de empezar

**Requisitos recomendados:**
- 8 GB de RAM como mínimo (16 GB para ir cómodo).
- 40-80 GB de espacio libre en disco.
- Procesador con virtualización activada (Intel VT-x o AMD-V). Si VirtualBox se queja al arrancar, revisa esta opción en la BIOS/UEFI.
- Un ordenador con procesador x86/x64 (Intel o AMD). En Mac con chip Apple Silicon, usa la imagen ARM de Kali con UTM o VMware Fusion.

## Paso 1: instala VirtualBox

Descarga VirtualBox desde su web oficial (virtualbox.org) e instálalo con las opciones por defecto. Descarga también el Extension Pack de la misma versión: añade soporte para USB 3.0 y otras funciones útiles.

## Paso 2: descarga la imagen oficial de Kali

En la web oficial de Kali (kali.org), sección *Get Kali › Virtual Machines*, descarga la imagen preparada para VirtualBox. Es un archivo comprimido `.7z` que ya contiene la máquina configurada, así que te ahorras la instalación completa.

> ⚠️ Descarga Kali solo desde su web oficial. Las imágenes de otras fuentes pueden venir modificadas con malware.

## Paso 3: verifica que la descarga es auténtica

Es un buen hábito de seguridad desde el primer día. En la página de descarga aparece el hash SHA256 del archivo. Calcula el del tuyo y compáralos:

**En Windows (PowerShell):**
```powershell
Get-FileHash .\kali-linux-*-virtualbox-amd64.7z -Algorithm SHA256
```

**En Linux o macOS:**
```bash
sha256sum kali-linux-*-virtualbox-amd64.7z
```

Si los dos valores coinciden, el archivo no se ha alterado.

## Paso 4: descomprime e importa la máquina

1. Descomprime el `.7z` con 7-Zip (Windows) o `7z x archivo.7z` (Linux). Obtendrás una carpeta con un archivo `.vbox`.
2. Haz doble clic en el archivo `.vbox`, o en VirtualBox ve a Máquina › Añadir y selecciónalo.
3. La máquina aparecerá en la lista de la izquierda.

## Paso 5: ajusta los recursos

Antes de arrancar, entra en Configuración:

- **Sistema › Placa base**: asigna 4 GB de RAM (o 2 GB si vas justo).
- **Sistema › Procesador**: 2 núcleos o más.
- **Pantalla**: 128 MB de memoria de vídeo.

## Paso 6: configura la red de forma segura

En Configuración › Red:

- **Adaptador 1 – NAT**: para que Kali tenga Internet y pueda actualizarse.
- **Adaptador 2 – Red solo-anfitrión (Host-only)**: para comunicarte con las máquinas vulnerables de tu laboratorio, sin exponerlas a tu red de casa.

Evita el modo Adaptador puente cuando trabajes con máquinas vulnerables: las pondría en tu red doméstica real.

## Paso 7: arranca y cambia la contraseña

Inicia la máquina. Las credenciales por defecto de las imágenes oficiales son:

- Usuario: `kali`
- Contraseña: `kali`

Lo primero que debes hacer es cambiar esa contraseña:

```bash
passwd
```

Todo el mundo conoce la contraseña por defecto, así que no la dejes nunca así.

## Paso 8: actualiza el sistema

```bash
sudo apt update && sudo apt full-upgrade -y
```

Puede tardar un rato la primera vez. Reinicia al terminar.

## Paso 9: haz una instantánea

Con Kali recién instalada y actualizada, ve a Máquina › Tomar instantánea y llámala "Kali limpia". Si algún día rompes algo, volverás a este punto en segundos.

## Problemas frecuentes

- **"VT-x is not available"**: activa la virtualización en la BIOS. En Windows, desactiva también Hyper-V si da conflictos, o usa una versión reciente de VirtualBox compatible con él.
- **Pantalla pequeña**: cambia la resolución desde la configuración de pantalla de Kali o activa *Ver › Ajustar tamaño de pantalla automáticamente*.
- **Va muy lenta**: sube la RAM y los núcleos asignados, y cierra programas en tu equipo principal.

## Y ahora, ¿qué?

Con Kali lista, el siguiente paso es aprender a moverte por la terminal con nuestros [20 comandos de Linux para empezar](/20-comandos-linux-para-empezar/) y, después, a analizar tu propia red con [Nmap](/que-es-nmap-como-usarlo/).

*Usa estas herramientas solo en tus propios equipos o en entornos donde tengas permiso.*
