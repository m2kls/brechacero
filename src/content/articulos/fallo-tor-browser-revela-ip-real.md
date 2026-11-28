---
title: "Fallo en Tor Browser: una cadena de ataques revela la IP real del usuario"
description: "Publican cómo un fallo de Tor Browser 15.0.22 (CVE-2026-92027) permitía revelar la IP real con un solo clic. Está corregido: comprueba tu versión y actualiza."
date: 2026-11-28T09:00:00+01:00
category: privacidad
tags: [Tor Browser, Tor, Firefox, CVE-2026-92027, anonimato, privacidad, Mozilla]
author: Redacción
photo: "File:The Tor Browser Showing The main Tor Project page.png"
imageAlt: "Ventana de Tor Browser con la página principal del proyecto Tor, navegador afectado por el fallo que revelaba la IP"
---

Un fallo en Tor Browser, el navegador que usan periodistas, activistas y millones de personas para navegar de forma anónima, permitía descubrir la dirección IP real del usuario con solo visitar una página y hacer un clic. Así lo ha demostrado el investigador Carlos Roque, de la empresa Calif, que publicó el 26 de noviembre el análisis completo y una prueba de concepto contra Tor Browser 15.0.22 en Linux con la configuración por defecto. La buena noticia es que el error de base, CVE-2026-92027, está corregido desde septiembre: quien tenga el navegador actualizado está protegido.

## Qué ha pasado con Tor Browser

Tor Browser se basa en Firefox ESR. El ataque descrito por Calif encadena cuatro pasos y empieza por CVE-2026-92027, un fallo de memoria del tipo *use-after-free* (uso de memoria ya liberada) en el componente de flujos de datos (Streams) del motor Gecko de Mozilla, con una puntuación CVSS de 8,8.

A partir de ahí, según el informe, el ataque consigue salir del aislamiento de la pestaña, engaña al navegador para que trate una entrada del historial como si fuera de máxima confianza y, por último, hace que el proceso principal abra una conexión directa a Internet sin pasar por la red Tor. Esa conexión llega al servidor del atacante con la IP pública real del usuario, que es precisamente lo que Tor debe ocultar.

Calif precisa que no llegó a ejecutar código en el proceso principal del navegador: el objetivo era romper el anonimato, no tomar el control del equipo. El trabajo forma parte de un programa de investigación de fallos en software de código abierto.

## ¿Estoy afectado?

Según el aviso recogido por Daily CyberSecurity, están afectados:

- Tor Browser 15.0.22 y anteriores.
- Firefox anterior a la versión 156 y las ramas ESR anteriores a 115.41, 140.16 y 153.3.
- Thunderbird anterior a 156, 140.16 y 153.3.

Mozilla corrigió el fallo el 15 de septiembre de 2026 en Firefox 156 y en Firefox ESR 140.16, y el proyecto Tor publicó ese mismo día Tor Browser 15.0.23. Por ahora ni Mozilla, ni el proyecto Tor ni la agencia estadounidense CISA han confirmado ataques reales con esta técnica, y el sistema de predicción EPSS le da una probabilidad baja de explotación. Pero ahora que los detalles son públicos, las copias sin actualizar son un blanco más fácil.

## Cómo protegerte

- **Actualiza Tor Browser**: en el menú, abre "Acerca de Tor Browser" para que busque actualizaciones. Debes tener la 15.0.23 o posterior (o la rama 16.0.3 en adelante). Ojo con las copias portables o que llevan meses sin abrirse: no se actualizan solas hasta que las ejecutas.
- **Actualiza Firefox y Thunderbird** a la versión 156 o a una ESR corregida.
- **Sube el nivel de seguridad a "El más seguro"** (icono del escudo > Configuración). Desactiva JavaScript en todas las webs y la cadena descrita depende de él.
- **Si tu anonimato es crítico**, no confíes solo en el navegador. Calif recomienda combinar Tor Browser con sistemas que fuerzan todo el tráfico por Tor, como Tails o Whonix, de modo que aunque el navegador falle no pueda salir una conexión directa.
- **No hagas clic en contenido de webs desconocidas** sin necesidad mientras navegas por Tor.

No es la primera vez este año que un fallo de Firefox pone en riesgo a usuarios de Tor: en julio, otro error en el compilador JavaScript (CVE-2026-10702) obligó a publicar Tor Browser 15.0.19. Si quieres entender cómo se puntúan y siguen estos fallos, lo explicamos en [qué es una CVE](/que-es-una-cve/). Y si te preocupa que tu IP se vincule a tu actividad, también contamos el reciente [fallo de privacidad en Bitcoin Core](/fallo-privacidad-bitcoin-core-direccion-ip/).

## Fuentes

- Calif: [TORtilla with Onion](https://calif.io/research/tortilla-with-onion)
- Daily CyberSecurity: [CVE-2026-92027: Tor Browser IP leak](https://securityonline.info/cve-2026-92027-tor-browser-ip-leak/)
- The Arabian Post: [Firefox flaw exposes unpatched Tor Browser users](https://thearabianpost.com/firefox-flaw-exposes-unpatched-tor-browser-users/)
