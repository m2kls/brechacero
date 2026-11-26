---
title: "Fugas de prompts en proveedores de IA: OpenRouter expulsa a tres tras el aviso de Dragos"
description: "Dragos sembró claves falsas en dos millones de prompts y detectó fugas de datos en proveedores de IA. OpenRouter expulsa a tres y retira 125 endpoints sin retención."
date: 2026-11-26T22:59:00+01:00
category: noticias
tags: [OpenRouter, Dragos, inteligencia artificial, fuga de datos, prompts, Together AI, Zero Data Retention]
author: Redacción
photo: "File:Datacenter Server Racks (22370909788).jpg"
imageAlt: "Armarios de servidores en un centro de datos, como los que usan los proveedores de IA implicados en las fugas de prompts"
---

Las **fugas de prompts en proveedores de IA** han dejado de ser una hipótesis. OpenRouter, uno de los servicios más usados para acceder a cientos de modelos de inteligencia artificial a través de una sola API, ha expulsado de su plataforma a tres proveedores (Together AI, Phala y Novita) y ha retirado la etiqueta de "Zero Data Retention" (cero retención de datos) a 125 endpoints. Lo ha hecho después de que la empresa de seguridad Dragos demostrara que lo que los usuarios escribían a esos modelos, incluidas contraseñas y claves, acababa en manos de terceros.

## Qué descubrió Dragos con sus claves trampa

El jefe de investigación de Dragos, HD Moore, conocido por crear Metasploit, envió unos dos millones de prompts a distintos servicios de IA entre julio y noviembre. Cada uno llevaba "canarios": direcciones web únicas y credenciales falsas de AWS que no existían en ningún otro sitio. Si alguien las usaba, solo podía haberlas sacado de ese prompt concreto.

El resultado, publicado el 19 de noviembre, es preocupante. Dragos detectó que atacantes estaban robando datos de tres proveedores de alojamiento de modelos desde mediados de julio, sin que ninguno lo supiera hasta que la empresa les avisó. En el caso más grave, se copiaron un par de centenares de claves de AWS en unas pocas ventanas de finales de octubre, algunas de peticiones que ni siquiera llegaron al modelo. Con esas claves trampa, los atacantes lanzaron decenas de miles de llamadas a la API de AWS para listar almacenamiento, buscar secretos, activar modelos en Bedrock o crear usuarios nuevos. Una clave sembrada el 21 de octubre se usó al día siguiente y seguía usándose tres semanas después.

Uno de los atacantes empleaba ARTEX, la plataforma de ataque automatizado con IA sobre la que [Microsoft alertó esta semana](/microsoft-artex-ia-salt-typhoon/). Dragos también vio que algunos revendedores de un mercado de inferencia podían leer y guardar los prompts con sus registros normales, sin necesidad de hackear nada, y que peticiones enviadas a proveedores estadounidenses acababan siendo consultadas desde China. Como resume Moore, "los prompts y las respuestas suelen valer más que la propia GPU".

## Qué ha hecho OpenRouter y qué dicen los proveedores

OpenRouter afirma que sus propios sistemas no fueron atacados, pero el 22 de noviembre anunció la salida de los tres proveedores, la retirada de la etiqueta de cero retención a 125 endpoints hasta que demuestren que la cumplen y el aviso directo a todos los clientes que pudieron verse afectados. A partir de ahora repetirá las pruebas de Dragos de forma periódica y verificará por dónde viajan las peticiones que reenvía.

Cada proveedor da su versión. Together AI atribuye la fuga a que OpenRouter no activó la cero retención en su tráfico y la sitúa en peticiones de junio y julio. Phala reconoce que un atacante comprometió un servidor que procesaba peticiones y obtuvo credenciales de las máquinas afectadas. Novita explica que un error de configuración desvió algunas peticiones a la API de MiniMax.

## ¿A quién afecta y qué hacer?

El problema afecta sobre todo a empresas y desarrolladores que usan modelos a través de intermediarios, en especial si sus agentes o aplicaciones meten en los prompts claves, contraseñas, código interno o datos de clientes. Es el mismo tipo de riesgo de cadena de suministro que ya vimos en ataques con [agentes de IA contra organizaciones](/ncsc-ciberataques-agentes-ia/).

- **Da por expuesto todo secreto que haya pasado por un prompt** enviado a estos proveedores y rótalo: claves de nube, tokens de API, contraseñas.
- **No metas credenciales en los prompts.** Usa filtros que eliminen secretos antes de enviarlos, aunque no lo detectan todo.
- **Elige tú el proveedor final** en los enrutadores de IA en lugar de dejar que el servicio decida, y evita los mercados de reventa.
- **Siembra tus propios canarios**: una clave falsa en un prompt que nunca debería usarse es una alarma barata y muy eficaz.
- Para datos sensibles, valora un modelo autoalojado o el contrato directo con el fabricante del modelo.

La etiqueta de "cero retención" es una promesa contractual, no una garantía técnica. Este caso demuestra que hay que comprobarla.

## Fuentes

- [Dragos: Three breaches, endless leaks: Your AI supply chain needs canaries](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)
- [OpenRouter: Data Processing Incidents on Inference Providers](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/)
- [Together AI: Security event, prompt leakage for requests in June and July of 2026](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)
- [Phala: November preliminary incident report](https://phala.com/posts/phala-november-preliminary-incident-report)
- [BankInfoSecurity: Breach Roundup, OpenRouter suspends AI providers over leaks](https://www.bankinfosecurity.com/breach-roundup-openrouter-suspends-ai-providers-over-leaks-a-33535)
