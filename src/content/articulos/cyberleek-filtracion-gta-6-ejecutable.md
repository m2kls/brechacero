---
title: "CyberLeek y el ejecutable filtrado de GTA 6: qué se sabe y por qué no debes descargarlo"
description: "Un filtrador anónimo ha publicado el ejecutable de una supuesta versión de Xbox de GTA 6. Repasamos el caso, la ofensiva legal de Take-Two y el malware que lo rodea."
date: 2026-11-24T13:20:00+01:00
category: noticias
tags: [GTA 6, CyberLeek, filtraciones, malware, Rockstar, Take-Two, videojuegos]
author: Redacción
featured: true
photo: "File:Xbox_Series_X_and_S_with_controllers.jpg"
imageAlt: "Consolas Xbox Series X y Series S con sus mandos"
---

El nombre de CyberLeek lleva tres meses persiguiendo a Rockstar Games. Lo que empezó en agosto con vídeos y recursos del mapa de *Grand Theft Auto VI* ha terminado esta semana con algo mucho más serio: el supuesto ejecutable de la versión de Xbox Series del juego, publicado el lunes 23 de noviembre en webs de piratería y foros. Es la pieza que faltaba en una compilación de unos 209 GB que el mismo filtrador había difundido días antes.

Detrás hay una historia que mezcla piratería, una criptomoneda creada al calor de la polémica, una investigación judicial que puede salpicar a miles de usuarios de Discord y, sobre todo, una ola de descargas falsas que están aprovechando los ciberdelincuentes. Esto es lo que se sabe, lo que no está confirmado y lo que conviene hacer si te cruzas con un enlace que promete GTA 6 "gratis".

## Quién es CyberLeek

Nadie lo sabe con certeza. CyberLeek es un alias anónimo que empezó a firmar filtraciones de GTA 6 a mediados de agosto. La mayoría de medios hablan de una sola persona; algún análisis lo describe como un grupo, pero no hay pruebas que lo confirmen. Su identidad sigue sin conocerse.

Lo que sí ha dejado claro es su discurso. En un archivo de texto que acompaña a las filtraciones, atribuido al propio CyberLeek, presenta su campaña como una protesta contra los lanzamientos solo digitales y lo que llama prácticas "anticonsumidor" de Take-Two, la matriz de Rockstar. También critica que la versión para PC llegue más tarde que la de consolas.

El otro elemento del caso es económico. El alias está vinculado a una criptomoneda tipo *memecoin* en la red Solana con su mismo nombre. Según Notebookcheck, la publicación del ejecutable se condicionó a que el token alcanzara una capitalización de mercado concreta: primero 15 millones de dólares y después 6 millones. Otras fuentes hablan de decenas de miles de dólares en comisiones cobradas, cifras que no hemos podido verificar. Que una filtración sirva para inflar una criptomoneda es, por sí solo, una señal de alarma para cualquiera que esté pensando en comprarla.

## Cronología: de los vídeos al ejecutable

![Cronología del caso CyberLeek, de agosto a noviembre de 2026](/img/articulos/cyberleek-cronologia.png)

- **18 de agosto.** Empiezan a circular vídeos de juego y recursos del mapa bajo el nombre CyberLeek. Para finales de mes ya se le atribuyen seis filtraciones.
- **20 de agosto.** Take-Two presenta ante un tribunal federal de Nueva York peticiones de información (*subpoenas*) dirigidas a Microsoft y a Discord para identificar al responsable.
- **26 de agosto.** Rockstar publica un mensaje en X en el que califica las filtraciones de "desoladoras", pide perdón por la espera y asegura que el juego está "casi listo".
- **19 de noviembre.** GTA 6 se lanza en PlayStation 5 y Xbox Series X/S. Ese mismo día, CyberLeek anuncia una compilación completa de Xbox de noviembre y aparecen alrededor de 209 GB de archivos, pero sin el ejecutable principal.
- **23 de noviembre.** El ejecutable se publica. Algunos medios dicen que llegó unas horas antes de lo prometido; otros, que apareció justo al expirar la cuenta atrás. KeenGamer lo identifica como la versión 1.0.2.1.

## ¿Es auténtico?

No está confirmado. Rockstar no ha autenticado ni el ejecutable ni el resto de la compilación. CyberLeek publicó sumas de verificación de los archivos, pero eso solo demuestra que lo que descargan distintas personas es idéntico, no que sea material real de Rockstar ni que esté completo. Tanto KeenGamer como TweakTown insisten en ese matiz.

Lo que sí parece claro es que la compilación de Xbox usa el kit de desarrollo de Microsoft (GDK), que comparte base con Windows. Por eso hay grupos de aficionados intentando adaptarla a PC con proyectos que se presentan como "ports" no oficiales. CyberLeek aseguró que estaría funcionando en ordenador "en una semana". Los desarrolladores consultados por la prensa son más prudentes: el archivo no se puede copiar sin más a un PC y ejecutarlo, faltan componentes del sistema, hay protecciones anti-manipulación y queda mucho trabajo de ingeniería inversa. A día de hoy no hay ninguna versión jugable verificada en PC.

## La ofensiva legal de Take-Two

La respuesta de Take-Two ha sido judicial y muy amplia. En las peticiones presentadas en agosto pidió a Microsoft todos los registros internos e investigaciones relacionados con el alias "cyberleek". A Discord le reclamó los datos de identificación de las cuentas de tres servidores desde el 1 de junio de 2026: identificador de cuenta, correo de registro, direcciones IP de alta y de último acceso, número de teléfono, cuentas de Google o Xbox vinculadas e identificadores del dispositivo.

Después llegaron peticiones similares a YouTube y a X. La de YouTube se retiró porque, según Take-Two, ya no necesitaba esa información. Y en septiembre la compañía pidió una segunda petición a Discord, esta vez bajo secreto, alegando que hacerla pública "podría comprometer" la investigación.

Malwarebytes señaló un efecto colateral importante: esa petición puede arrastrar los datos de cientos o miles de personas que simplemente estaban en esos servidores de Discord y no tienen nada que ver con la filtración. Uno de los servidores pertenece a un conocido *streamer* de GTA 5 que ha negado cualquier relación con el caso.

Hasta ahora no hay noticias de que se haya identificado a CyberLeek ni de acciones contra quienes descargan los archivos.

## El verdadero peligro: las descargas falsas

Para el usuario normal, el riesgo más inmediato no es legal sino técnico. Cada gran filtración de un videojuego atrae a ciberdelincuentes que se aprovechan del interés, y este caso no es una excepción. Desde agosto, varios análisis de seguridad han documentado campañas que usan el nombre de CyberLeek como cebo:

- **Webs que prometen una "versión jugable de CyberLeek".** Según las investigaciones publicadas, algunas muestran una falsa comprobación de "no soy un robot" que copia un comando en el portapapeles y pide al usuario que lo pegue y lo ejecute. Esa técnica, conocida como ClickFix, acaba instalando malware. Otras entregan directamente un ejecutable con Vidar, un troyano que roba contraseñas guardadas, cookies de sesión y carteras de criptomonedas.
- **Copias falsas en torrents, canales de Telegram y supuestas imágenes ISO.** Un análisis publicado en agosto describe webs que perfilan al visitante por su IP y ubicación y acaban instalando un programa legítimo de control remoto configurado para conectarse a los atacantes. Es decir, entregan el control del ordenador.
- **Cobros por "acceso premium".** Algunas de estas webs llegaron a pedir 100 dólares por un acceso anticipado que no existe.

Estas campañas se documentaron en la fase de agosto. Todavía no hay un análisis público sobre ejecutables falsos ligados a la publicación del 23 de noviembre, pero el patrón es predecible: cuanto más ruido hace una filtración, más trampas aparecen alrededor. Malwarebytes ya encontró anteriormente webs falsas de "demos" de GTA 6 que distribuían programas para robar contraseñas.

## Cómo protegerte

Si eres jugador, o tienes en casa a alguien que lo es, estos son los consejos básicos:

1. **No descargues la filtración.** Además de ser material pirata, no hay forma de saber si el archivo que te llega es el original o una versión modificada con malware. Ejecutar un `.exe` de origen desconocido es la forma más rápida de infectar un ordenador.
2. **Desconfía de cualquier web que te pida pegar un comando.** Ninguna verificación legítima te pide abrir la ventana de Ejecutar de Windows o PowerShell y pegar algo. Si lo ves, cierra la página.
3. **No pagues por "accesos anticipados" ni versiones para PC.** A día de hoy GTA 6 solo existe oficialmente en PS5 y Xbox Series. Rockstar no ha anunciado fecha para PC.
4. **Cuidado con la criptomoneda asociada.** Los tokens creados al calor de una polémica son extremadamente volátiles y se prestan a estafas. No es una inversión, es una apuesta.
5. **Si ya ejecutaste algo**, desconecta el equipo de internet, pásale un análisis completo con tu antivirus y, desde otro dispositivo limpio, cambia las contraseñas de tu correo, redes sociales, banca y plataformas de juego (Steam, Xbox, PlayStation, Rockstar). Activa la verificación en dos pasos en todas ellas y revisa si hay sesiones abiertas que no reconoces. Te lo explicamos en nuestra guía sobre [cómo proteger tus cuentas con contraseñas y 2FA](/proteger-cuentas-contrasenas-2fa/).
6. **Comprueba si tus datos han aparecido en alguna filtración** con las herramientas que explicamos en [cómo saber si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/).

## Por qué importa más allá de GTA

El caso CyberLeek resume bien cómo funcionan hoy muchas filtraciones: un alias anónimo, una narrativa de protesta, un incentivo económico en forma de criptomoneda y un ecosistema de estafas que vive del interés generado. Y muestra también la otra cara: investigaciones judiciales tan amplias que pueden acabar exponiendo datos de miles de usuarios que solo estaban en el sitio equivocado.

Seguiremos el caso y actualizaremos esta información si Rockstar o Take-Two confirman la autenticidad de los archivos o hay novedades en la investigación.

## Fuentes

- Notebookcheck: [Cyberleek releases GTA 6 Xbox build .exe](https://www.notebookcheck.net/Cyberleek-releases-GTA-6-Xbox-build-exe-boosting-playable-PC-port-chances.1457977.0.html) (23 de noviembre de 2026)
- KeenGamer: [GTA 6 leaker Cyberleek releases Xbox executable file](https://www.keengamer.com/articles/news/gta-6-leaker-cyberleek-releases-xbox-executable-file-completing-alleged-leak/) (23 de noviembre de 2026)
- TweakTown: [The missing piece needed to get the leaked GTA 6 Xbox build running on PC](https://www.tweaktown.com/news/114831/the-missing-piece-needed-to-get-the-leaked-gta-6-xbox-build-running-on-pc-has-reportedly-surfaced-online/index.html) (23 de noviembre de 2026)
- VGC: [Take-Two files subpoenas to Microsoft and Discord in hunt for GTA 6 leaker](https://www.videogameschronicle.com/news/take-two-files-subpoenas-to-microsoft-and-discord-in-hunt-for-gta-6-leaker/) (21 de agosto de 2026)
- Notebookcheck: [Take-Two requests another Discord subpoena](https://www.notebookcheck.net/Take-Two-says-its-investigation-into-the-GTA-6-leaker-is-rapidly-evolving-as-it-requests-another-Discord-subpoena.1384292.0.html) (1 de septiembre de 2026)
- Malwarebytes: [GTA 6 leak hunt could expose data belonging to thousands of Discord users](https://www.malwarebytes.com/blog/privacy/2026/08/gta-6-leak-hunt-could-expose-data-belonging-to-thousands-of-discord-users) (25 de agosto de 2026)
- Intel Insights: [Behind the leak](https://intelinsights.substack.com/p/behind-the-leak) (26 de agosto de 2026)
