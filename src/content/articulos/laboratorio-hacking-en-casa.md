---
title: "Cómo montar tu laboratorio de hacking en casa (gratis y legal)"
description: "Aprende a montar un laboratorio de ciberseguridad en casa con máquinas virtuales gratuitas para practicar hacking ético de forma segura y legal."
date: 2026-11-21
category: ctf-formacion
tags: ['laboratorio', 'máquinas virtuales', 'práctica']
author: Redacción
featured: false
imageCredit: "Ilustración: Brecha Cero"
---


Si quieres aprender ciberseguridad de verdad, leer no basta: necesitas practicar. El problema es que no puedes practicar contra sistemas ajenos sin permiso. La solución es sencilla y no cuesta dinero: montar tu propio laboratorio con máquinas virtuales en tu ordenador.


## Qué es un laboratorio de hacking

Es un entorno aislado, normalmente dentro de tu propio ordenador, formado por:

- Una máquina atacante: el sistema desde el que lanzas las pruebas (por ejemplo, Kali Linux).
- Una o varias máquinas objetivo: sistemas deliberadamente vulnerables creados para aprender.
- Una red virtual privada que las conecta entre sí, pero no con tu red doméstica ni con Internet.

Todo funciona como si fueran ordenadores reales, pero si algo se rompe, simplemente restauras una copia y vuelves a empezar.

## Requisitos mínimos

| Componente | Mínimo | Recomendado |
|---|---|---|
| RAM | 8 GB | 16 GB o más |
| Procesador | 4 núcleos con virtualización (VT-x / AMD-V) | 6-8 núcleos |
| Disco | 100 GB libres | SSD con 250 GB libres |
| Sistema anfitrión | Windows, macOS o Linux | El que ya uses |

> 💡 Comprueba en la BIOS/UEFI que la virtualización está activada. Es el fallo más común cuando una máquina virtual no arranca.

## Paso 1: elige un programa de virtualización

- **VirtualBox:** gratuito, multiplataforma y con mucha documentación. Ideal para empezar.
- **VMware Workstation Pro:** actualmente gratuito para uso personal; muy estable.
- **Proxmox:** si tienes un ordenador viejo que puedas dedicar en exclusiva al laboratorio, es una opción excelente (más avanzada).

En Mac con chip Apple Silicon (M1 y posteriores), ten en cuenta que muchas máquinas vulnerables están hechas para procesadores x86 y pueden no funcionar; en ese caso, las plataformas online (paso 5) son tu mejor aliado.

## Paso 2: instala tu máquina atacante

Las dos distribuciones más usadas son:

- **Kali Linux:** la más popular, con cientos de herramientas preinstaladas. Ofrece imágenes ya preparadas para VirtualBox y VMware.
- **Parrot Security OS:** similar, algo más ligera y con un entorno de escritorio cuidado.

Descárgalas siempre desde su web oficial y verifica la suma de comprobación (hash) del archivo. Es un buen primer hábito de seguridad.

## Paso 3: configura la red de forma segura

Esta es la parte más importante. Las opciones típicas en VirtualBox son:

- **NAT:** la máquina sale a Internet pero no se ve desde fuera. Útil para actualizar Kali.
- **Red interna / Host-only:** las máquinas se ven entre ellas, pero no con tu red doméstica. Es la que debes usar para las máquinas vulnerables.
- **Adaptador puente (bridge):** la máquina aparece en tu red de casa como un dispositivo más. Evítalo con máquinas vulnerables, porque las expones a tu red real.

Una configuración sencilla y segura: Kali con dos adaptadores (NAT para actualizar + red interna para el laboratorio) y las máquinas vulnerables solo en la red interna.

## Paso 4: añade máquinas vulnerables

Algunas máquinas pensadas para aprender, gratuitas y descargables:

- **Metasploitable 2:** un clásico, lleno de servicios vulnerables. Perfecta para dar los primeros pasos.
- **DVWA (Damn Vulnerable Web Application):** una aplicación web vulnerable con niveles de dificultad para aprender seguridad web.
- **OWASP Juice Shop:** tienda online moderna repleta de fallos, con retos guiados.
- **VulnHub:** repositorio con cientos de máquinas creadas por la comunidad.

> ⚠️ Estas máquinas son inseguras a propósito. Nunca las conectes directamente a Internet ni a tu red doméstica.

## Paso 5: complementa con plataformas online

No todo tiene que estar en tu ordenador. Estas plataformas te dan máquinas listas para atacar de forma legal a través de una VPN:

- **TryHackMe:** muy guiada, ideal para principiantes. Tiene mucho contenido gratuito.
- **HackTheBox:** máquinas más realistas; su versión Academy incluye cursos estructurados.
- **PortSwigger Web Security Academy:** totalmente gratuita y centrada en seguridad web.

## Paso 6: buenas prácticas en tu laboratorio

- **Haz instantáneas (snapshots)** antes de cada práctica. Si algo se rompe, vuelves atrás en segundos.
- **Toma notas** de todo: comandos, errores y soluciones. Herramientas como Obsidian o CherryTree son muy populares.
- **Actualiza tu máquina atacante** con regularidad.
- **Apaga las máquinas vulnerables** cuando no las uses.

## Preguntas frecuentes

**¿Puedo montar el laboratorio en un portátil normal?**
Sí. Con 8 GB de RAM puedes tener Kali y una máquina objetivo a la vez; con 16 GB irás mucho más cómodo.

**¿Es legal tener herramientas de hacking instaladas?**
Tener y aprender a usar herramientas de seguridad en tus propios sistemas es habitual y legal en la mayoría de países. Lo ilegal es usarlas contra sistemas sin autorización.

**¿Necesito pagar algo?**
No. Todo lo que mencionamos en esta guía tiene opción gratuita.


Un laboratorio propio es la herramienta más valiosa para aprender ciberseguridad: te permite equivocarte sin consecuencias y practicar tanto como quieras. Empieza con VirtualBox, Kali y Metasploitable, y ve ampliando cuando lo domines.

¿Aún no tienes claro por dónde empezar? Lee nuestra guía [Qué es el hacking ético y cómo empezar desde cero](/que-es-hacking-etico-como-empezar/).

*Este artículo tiene fines educativos. Practica siempre en entornos propios o autorizados.*
