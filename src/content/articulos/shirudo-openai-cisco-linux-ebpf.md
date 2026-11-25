---
title: "Shirudo: OpenAI y Cisco lanzan escudos con IA para Linux antes del parche"
description: "Shirudo, de OpenAI y Cisco, usa agentes de IA para crear reglas eBPF que bloquean exploits en Linux mientras llega el parche. Qué es y cómo funciona."
date: 2026-11-25T04:51:00+01:00
category: linux
tags: [Shirudo, OpenAI, Cisco, Isovalent, eBPF, Tetragon, Linux, IA]
author: Redacción
photo: "File:Tux.jpg"
imageAlt: "Peluche de Tux, el pingüino de Linux, sistema para el que OpenAI y Cisco han lanzado Shirudo"
---

**OpenAI y Cisco** han presentado **Shirudo**, una herramienta de código abierto para Linux que usa agentes de inteligencia artificial para fabricar "escudos": pequeñas reglas que bloquean la forma concreta de explotar una vulnerabilidad mientras el servicio sigue funcionando y hasta que se puede instalar el parche oficial. El anuncio, del 24 de noviembre, llega en plena avalancha de fallos críticos y con los atacantes usando también la IA para explotarlos cada vez más rápido.

## Qué es Shirudo y cómo funciona

Shirudo se apoya en **eBPF**, una tecnología del núcleo de Linux que permite ejecutar pequeños programas dentro del kernel de forma segura para observar o bloquear lo que hacen los procesos. En concreto, está construido sobre **Tetragon**, la plataforma de seguridad basada en eBPF que Isovalent (hoy parte de Cisco) liberó en 2022.

El flujo, según la documentación del proyecto, es este:

1. Unos agentes de IA revisan código abierto y avisos de los fabricantes para detectar vulnerabilidades que afectan a lo que tienes instalado.
2. Para cada una, generan un escudo: una política eBPF que corta el camino que usaría el exploit (por ejemplo, impedir que un proceso concreto lance una shell o escriba en cierta ruta).
3. El escudo se **valida contra el exploit** y un operador humano tiene que aprobarlo antes de que empiece a bloquear.
4. Los escudos van firmados criptográficamente, se comprueban con el chip TPM antes de cargarse y se distribuyen como paquetes desde un registro compatible con OCI, el mismo estándar de las imágenes de contenedores.
5. Cuando llega el parche de verdad, el escudo se retira.

OpenAI cuenta que, en un experimento controlado, un escudo generado con su modelo Codex bloqueó un intento de explotar Java4Shell contra un servicio Elasticsearch en marcha, sin reiniciarlo. En palabras de la propia OpenAI, la herramienta "permite a los agentes escribir controles eBPF dinámicos para proteger los sistemas de exploits".

## Por qué importa: la ventana entre el fallo y el parche

El problema que intenta resolver es real. Entre que se publica una vulnerabilidad y que una empresa puede parchear todos sus servidores pasan días o semanas: hay que probar, programar ventanas de mantenimiento y reiniciar servicios. Mientras tanto, los atacantes ya automatizan la explotación, en algunos casos con agentes de IA que tardan minutos, como en el caso de MONAI Label que ha llevado a CISA a lanzar una alerta esta semana.

Cisco lo enmarca como "ampliar la ventana del defensor". La idea no es sustituir el parche, sino ganar tiempo con una mitigación más precisa que un cortafuegos genérico.

## Lo que conviene tener en cuenta

- **No es magia.** Un escudo bloquea una forma concreta de explotar el fallo; variantes distintas podrían esquivarlo. El parche sigue siendo imprescindible.
- **Supervisión humana.** El diseño exige la aprobación de un operador antes de bloquear, un punto importante para no tumbar servicios en producción por una regla mal hecha.
- **Requisitos.** Hace falta un kernel con soporte de eBPF moderno y, para la verificación, TPM. OpenAI y Cisco no han detallado aún licencia ni versión estable en los primeros anuncios.

Para quien administra servidores Linux, es una herramienta a seguir de cerca. Si estás empezando con el sistema, te puede servir nuestra lista de [comandos Linux útiles para seguridad](/comandos-linux-seguridad/), y para entender el contexto, el aviso del [NCSC sobre ataques con agentes de IA](/ncsc-ciberataques-agentes-ia/).

## Fuentes

- [OpenAI: Introducing Shirudo](https://openai.com/index/introducing-shirudo/)
- [Cisco: Expanding the defender's window with self-defending infrastructure](https://blogs.cisco.com/news/expanding-the-defenders-window-with-self-defending-infrastructure)
- [Shirudo: documentación, cómo funciona](https://docs.shirudo.dev/start/how-it-works.html)
- [The Hacker News: OpenAI and Cisco Unveil AI-Assisted Linux Security Tool](https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html)
