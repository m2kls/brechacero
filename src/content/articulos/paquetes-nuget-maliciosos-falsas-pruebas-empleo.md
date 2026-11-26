---
title: "Paquetes NuGet maliciosos: falsas pruebas de empleo infectan a programadores"
description: "13 paquetes NuGet maliciosos se escondían en falsas pruebas técnicas para desarrolladores .NET y robaban datos del navegador. Cómo evitar caer en la trampa."
date: 2026-11-26T10:59:00+01:00
category: noticias
tags: [NuGet, .NET, malware, ofertas de empleo falsas, cadena de suministro, Socket, GitHub]
author: Redacción
photo: "File:Programmer at work (Unsplash).jpg"
imageAlt: "Programador trabajando con un portátil, perfil al que se dirigen las falsas pruebas de empleo con paquetes NuGet maliciosos"
---

Una oferta de trabajo bien pagada, una prueba técnica para hacer en casa y un proyecto listo para compilar. Ese es el cebo de una campaña que ha colado **13 paquetes NuGet maliciosos** en el repositorio oficial de librerías de .NET para infectar los ordenadores de programadores que buscan empleo. La firma de seguridad Socket la ha documentado esta semana, y The Hacker News la ha recogido este 26 de noviembre. Al compilar o ejecutar el proyecto de la "prueba", el equipo descargaba programas que roban datos del navegador y abren una puerta trasera.

## Cómo funcionaba el engaño de los paquetes NuGet

NuGet es el gestor de paquetes de .NET, el equivalente a npm en JavaScript o PyPI en Python: los desarrolladores lo usan a diario para añadir librerías a sus proyectos sin revisarlas una a una. Los atacantes aprovecharon esa confianza.

Según Socket, la mayoría de los paquetes se hacían pasar por controles de botones para interfaces WinUI 3 y WPF, con nombres anodinos como WinUI.Button, StyledAppButton o SetButtonColor. Se publicaron desde cuatro cuentas distintas, con 28 versiones en total, entre julio y noviembre de 2026.

El anzuelo era un repositorio de GitHub con una supuesta prueba técnica, un pequeño gestor de archivos que había que compilar en Windows con Visual Studio. La oferta se anunció el 7 de noviembre en LaborX, una plataforma de trabajos para autónomos, con pagos de entre 8.500 y 10.000 dólares. El proyecto incluía como dependencias algunos de esos paquetes.

A partir de ahí, el código malicioso se activaba solo con el trabajo normal del candidato. Uno de los paquetes añadía una tarea que se ejecutaba después de cada compilación y descargaba un archivo desde GitHub, preparado para cargarse a través del Teclado en pantalla de Windows, un programa legítimo. Otro lanzaba la descarga de un ejecutable en cuanto se creaba el botón en la aplicación. Las cargas finales incluían un ladrón de perfiles de Chrome y un cargador controlado desde GitHub; una versión posterior apuntaba a ocho extensiones de carteras de criptomonedas.

## ¿Quién está detrás y a quién afecta?

Socket no atribuye la campaña a ningún grupo concreto. Señala parecidos con las operaciones de falsas entrevistas de trabajo vinculadas a Corea del Norte e Irán, pero no ha encontrado código compartido con familias de malware conocidas de esas campañas. La misma operación empezó en julio en npm, con repositorios falsos de la popular librería axios publicados por una cuenta que imitaba la de su mantenedor real.

NuGet ha retirado los paquetes. Socket indica que al menos uno, WinUI.Button, llegó a sumar unas 160 descargas. El riesgo es mayor para desarrolladores .NET en Windows que hayan hecho pruebas técnicas de origen desconocido en los últimos meses, y para las empresas cuyos equipos usan el mismo ordenador para trabajar y para buscar empleo.

## Cómo protegerte de las falsas pruebas técnicas

Estas son las recomendaciones de Socket y las que aplicaría cualquier equipo de seguridad:

1. **Trata cualquier prueba técnica como código no fiable.** Ábrela en una máquina virtual desechable, nunca en el ordenador donde tienes tus cuentas, claves SSH o carteras.
2. **Revisa el proyecto antes de compilar**: fuentes de paquetes añadidas en `NuGet.config`, archivos `.nupkg` incluidos en el repositorio o dependencias que no reconoces.
3. **Desconfía de las ofertas demasiado generosas** que llegan sin entrevista previa y con prisa por que ejecutes algo.
4. **Si ya ejecutaste un proyecto sospechoso**, reinstala el equipo y cambia contraseñas, tokens de GitHub y claves de la nube desde un dispositivo limpio. Activa la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/) en todas tus cuentas de desarrollo.
5. **Para empresas**: usar el mapeo de orígenes de NuGet (source mapping) para limitar de dónde se descargan paquetes y avisar a la plantilla de este tipo de engaños.

Es el mismo principio que en el [phishing clásico](/como-detectar-phishing/): la urgencia y una recompensa atractiva sirven para que bajes la guardia. La diferencia es que aquí el enlace malicioso es un proyecto de código. Hace solo unos días contábamos otro ataque a la cadena de suministro de software, el de los [plugins de WordPress con puerta trasera](/plugins-wordpress-wp-connect-puerta-trasera/).

## Fuentes

- [Socket: 13 Malicious NuGet Packages Target .NET Developers With Fake Job Assessments](https://socket.dev/blog/malicious-nuget-packages-fake-job-assessments)
- [The Hacker News: 13 Malicious NuGet Packages Turn Fake .NET Job Assessments Into Malware Delivery Traps](https://thehackernews.com/2026/11/13-malicious-nuget-packages-turn-fake.html)
