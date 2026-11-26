---
title: "ARTEX: Microsoft alerta de que Salt Typhoon usa esta IA para atacar"
description: "Microsoft detecta a seis grupos, entre ellos los chinos Salt Typhoon y Crystal Typhoon, usando ARTEX, una IA que automatiza intrusiones en minutos. Cómo detectarla."
date: 2026-11-26T06:54:00+01:00
category: noticias
tags: [ARTEX, Microsoft, Salt Typhoon, inteligencia artificial, China, Corea del Norte, agentes de IA]
author: Redacción
photo: "File:Microsoft sign closeup.jpg"
imageAlt: "Letrero de Microsoft en su campus, empresa que ha publicado el análisis sobre ARTEX"
---

ARTEX, el marco de inteligencia artificial que automatiza ataques informáticos, ya forma parte del arsenal de grupos respaldados por estados. Microsoft Threat Intelligence publicó este miércoles 25 de noviembre un análisis en el que identifica a seis actores que lo usan, entre ellos los grupos chinos **Salt Typhoon** y **Crystal Typhoon** y los norcoreanos Onyx Sleet y Pearl Sleet. Según la compañía, la herramienta puede pasar "del reconocimiento a un acceso privilegiado y persistente en cuestión de minutos".

## Qué es ARTEX y por qué preocupa

ARTEX nació en julio de 2026 como un proyecto de código abierto para pruebas de penetración automatizadas, publicado en GitHub con una interfaz en chino. Su autor retiró el código en octubre, pero siguen circulando copias, y al menos una empresa china comercializa ya una versión de pago.

Por dentro funciona como varios agentes de IA coordinados: uno fija objetivos, otro planifica, otro ejecuta y otro redacta informes, todos compartiendo lo que van descubriendo. Puede conectarse a cualquier modelo de lenguaje y, si un proveedor falla, cambia a otro. Para atacar no inventa nada: encadena herramientas conocidas de auditoría para buscar fallos en aplicaciones web, probar contraseñas y moverse por la red. Lo nuevo es la velocidad y que reduce al mínimo el conocimiento necesario para lanzar una intrusión.

Microsoft señala además a dos actores con motivación económica, Storm-0940 y Storm-3358. En una campaña de Storm-0940 contó más de 151.000 inicios de sesión fallidos, con picos de 2.900 por minuto.

## Salt Typhoon y los ataques a agencias de EE. UU.

Salt Typhoon es conocido por haber espiado durante años a operadoras de telecomunicaciones de medio mundo. Que lo use ahora, según Microsoft, para reconocimiento de redes, ataques a credenciales y explotación de aplicaciones web confirma que los agentes de IA ofensivos han dejado de ser un experimento.

ARTEX también aparece en el [hackeo a la CIA y la ODNI](/hackeo-cia-odni-informacion-no-clasificada/): The New York Times informó de que se usó contra un sistema de análisis de fuentes abiertas de la CIA y contra otras agencias de inteligencia. Microsoft, sin embargo, no atribuye ese ataque a ninguno de los grupos de su informe. El FBI ya había publicado un aviso sobre la herramienta hace dos semanas, y las autoridades suizas e italianas alertaron recientemente de [los primeros ciberataques con agentes de IA](/ncsc-ciberataques-agentes-ia/) contra empresas e infraestructuras.

## Cómo detectar ARTEX en tu red

La buena noticia para los defensores es que ARTEX no usa técnicas desconocidas, así que las defensas clásicas siguen funcionando si están bien configuradas. Microsoft insiste en que la señal más fiable es el comportamiento: ráfagas de peticiones muy variadas lanzadas a velocidad de máquina desde un mismo origen en poco tiempo. Los atacantes pueden cambiar de IP y de agente de usuario, así que no basta con bloquear indicadores concretos. Entre sus recomendaciones:

- **Reducir la superficie expuesta a internet**: inventario de lo publicado, cortafuegos de aplicaciones web en modo bloqueo, limitación de peticiones y protección contra bots.
- **Proteger las identidades**: autenticación multifactor resistente al phishing, bloqueo inteligente tras intentos fallidos y prohibición de contraseñas débiles. Nuestra guía sobre [cómo proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/) resume lo básico.
- **No dejar secretos a la vista**: buscar claves y contraseñas en código y ficheros de configuración (como los `.env`) y rotarlas.
- **Vigilar los servidores web**: alertar si un proceso del servidor abre una consola, si aparecen scripts nuevos en carpetas públicas o si el servidor hace conexiones salientes inesperadas.
- **Conservar registros** de inicios de sesión, servidores web y del cortafuegos de aplicaciones para poder investigar.

Microsoft Defender ya detecta parte de esta actividad con firmas específicas, y la compañía ha añadido avisos de direcciones IP de actores verificados en Entra ID Protection.

La conclusión de fondo es incómoda: el tiempo entre que un atacante encuentra un fallo y lo aprovecha se ha reducido a minutos. Parchear rápido y tener alertas que salten a tiempo ya no es opcional.

## Fuentes

- [Microsoft Security Blog: What defenders need to know about ARTEX](https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/)
- [The Record: Microsoft: China's Salt Typhoon hackers are using Artex](https://therecord.media/microsoft-china-salt-typhoon-using-artex-ai-tool)
- [BleepingComputer: Hackers reportedly breached CIA intelligence analysis system](https://www.bleepingcomputer.com/news/security/hackers-reportedly-breached-cia-intelligence-analysis-system/)
