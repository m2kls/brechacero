---
title: "Qué es Nmap y cómo usarlo para revisar tu propia red"
description: "Nmap explicado para principiantes: para qué sirve, cómo descubrir qué dispositivos y puertos hay en tu red de casa y cómo interpretar los resultados."
date: 2026-12-01
category: guias
tags: [Nmap, redes, puertos, auditoría, defensa]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

**Nmap** (*Network Mapper*) es probablemente la herramienta más conocida del mundo de la ciberseguridad. Es gratuita, de código abierto y la usan tanto administradores de sistemas como auditores para responder a una pregunta muy simple: ¿qué hay en esta red y qué está expuesto?

En esta guía te enseñamos a usarla para revisar tu propia red, que es la mejor forma de aprender y de detectar dispositivos o servicios que no deberían estar ahí.

> ⚠️ Aviso legal: escanea solo redes y equipos que sean tuyos o para los que tengas permiso por escrito. Escanear sistemas ajenos puede considerarse un intento de intrusión. Para practicar, el proyecto Nmap ofrece el servidor `scanme.nmap.org`, autorizado expresamente para pruebas básicas (con moderación).

## Para qué sirve Nmap

- **Inventario de red**: descubrir todos los dispositivos conectados (ordenadores, móviles, cámaras, impresoras, televisores...).
- **Auditoría de puertos**: ver qué servicios tiene abiertos cada equipo.
- **Detección de versiones**: saber qué programa y qué versión hay detrás de cada puerto, para comprobar si está actualizado.
- **Comprobación del cortafuegos**: verificar que lo que crees que está cerrado lo está de verdad.

Si aún no tienes claro qué es un puerto, empieza por [esta guía](/que-es-un-puerto-redes/).

## Cómo instalarlo

- **Kali Linux**: viene preinstalado.
- **Debian/Ubuntu**: `sudo apt install nmap`
- **Windows y macOS**: descarga el instalador desde la web oficial, nmap.org. En Windows incluye Zenmap, una interfaz gráfica.

## Paso 1: averigua tu rango de red

En Linux:
```bash
ip a
```
En Windows:
```powershell
ipconfig
```

Si tu IP es, por ejemplo, `192.168.1.35`, tu red doméstica casi seguro es `192.168.1.0/24` (todas las direcciones de `192.168.1.1` a `192.168.1.254`).

## Paso 2: descubre los dispositivos conectados

```bash
sudo nmap -sn 192.168.1.0/24
```

La opción `-sn` solo comprueba qué equipos están encendidos, sin analizar puertos. El resultado es una lista de IP, a menudo con el fabricante del dispositivo.

**Ejercicio útil:** identifica cada dispositivo de la lista. Si aparece alguno que no reconoces, investígalo: puede ser un aparato olvidado o alguien usando tu WiFi.

## Paso 3: mira qué puertos tiene abiertos un equipo

```bash
nmap 192.168.1.1
```

Por defecto, Nmap revisa los 1.000 puertos TCP más comunes. El resultado será algo así:

```
PORT    STATE SERVICE
53/tcp  open  domain
80/tcp  open  http
443/tcp open  https
```

En este ejemplo, el router tiene abiertos DNS y su panel web.

## Paso 4: detecta las versiones de los servicios

```bash
nmap -sV 192.168.1.50
```

Con `-sV`, Nmap intenta identificar el programa y la versión que hay detrás de cada puerto. Esto te permite comprobar si algún servicio está desactualizado y buscar si tiene vulnerabilidades conocidas (te explicamos cómo en [qué es una CVE](/que-es-una-cve/)).

## Opciones básicas que conviene conocer

| Opción | Qué hace |
|---|---|
| `-sn` | Solo descubre equipos activos, sin escanear puertos |
| `-p 22,80,443` | Escanea solo los puertos indicados |
| `-p-` | Escanea los 65.535 puertos TCP (más lento) |
| `-sV` | Detecta la versión de los servicios |
| `-O` | Intenta adivinar el sistema operativo (requiere `sudo`) |
| `-sU` | Escanea puertos UDP (lento) |
| `-oN archivo.txt` | Guarda el resultado en un archivo de texto |
| `-T4` | Acelera el escaneo en redes locales |

## Cómo interpretar los resultados (y qué hacer)

- **`open` en un servicio que no usas**: desactívalo o ciérralo en el cortafuegos.
- **Telnet (23), FTP (21) o SMB (445) abiertos en dispositivos domésticos**: suelen ser señal de configuraciones antiguas o inseguras. Revisa el dispositivo y actualiza su firmware.
- **Paneles web en cámaras o impresoras**: cambia la contraseña por defecto y actualiza el firmware.
- **Versiones antiguas** detectadas con `-sV`: actualiza.
- **`filtered`**: un cortafuegos está bloqueando el puerto, lo que normalmente es buena señal.

## Revisión de seguridad de tu red en 10 minutos

1. Descubre todos los dispositivos con `nmap -sn`.
2. Escanea tu router y cualquier equipo que no reconozcas.
3. Anota los puertos abiertos y pregúntate si los necesitas.
4. Cierra lo que sobre, cambia contraseñas por defecto y actualiza firmware.
5. Repite la revisión cada pocos meses o cuando conectes un aparato nuevo.

## Preguntas frecuentes

**¿Es legal usar Nmap?**
La herramienta es legal y se usa a diario en empresas. Lo que importa es contra qué la usas: en tu red o con autorización, sin problema.

**¿Puede Nmap romper algo?**
Los escaneos básicos son inofensivos para la inmensa mayoría de equipos. Algunos dispositivos muy antiguos o industriales pueden comportarse de forma rara ante escaneos agresivos, por eso en entornos profesionales siempre se acuerdan los límites antes.

**¿Por dónde sigo aprendiendo?**
Practica en tu laboratorio con máquinas vulnerables a propósito. Si no lo tienes montado, empieza por [instalar Kali Linux en VirtualBox](/instalar-kali-linux-virtualbox/).
