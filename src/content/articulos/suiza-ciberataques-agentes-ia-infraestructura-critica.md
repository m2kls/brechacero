---
title: "Suiza confirma ciberataques con agentes de IA a infraestructuras críticas"
description: "Ciberataques con agentes de IA en Suiza: cinco casos confirmados, cuatro con intrusión y dos en operadores críticos. Qué se sabe y cómo protegerse."
date: 2026-11-28T04:58:00+01:00
category: noticias
tags: [Suiza, inteligencia artificial, agentes de IA, ARTEX, infraestructura crítica, NCSC, CyberStrikeAI]
author: Redacción
photo: "File:Federal Palace of Switzerland in Bern.jpg"
imageAlt: "Palacio Federal de Berna, sede del Gobierno suizo, que ha confirmado ciberataques con agentes de IA"
---

Suiza ha confirmado oficialmente los primeros ciberataques con agentes de IA contra organizaciones del país. Según explicó Florian Schütz, director de la Oficina Federal de Ciberseguridad (BACS, antes NCSC), en una entrevista con la radiotelevisión pública SRF, se conocen cinco casos: en cuatro los atacantes llegaron a entrar en los sistemas, y tres iban dirigidos contra operadores de infraestructura crítica, de los que dos fueron comprometidos. No se han comunicado interrupciones graves de servicio.

Es una de las primeras veces que una agencia gubernamental europea pone cifras concretas a un fenómeno del que se venía hablando en informes técnicos: herramientas de ataque que encadenan reconocimiento, explotación y movimiento dentro de la red con muy poca intervención humana.

## Qué ha pasado en Suiza con los ataques de agentes de IA

La agencia suiza publicó un primer aviso el martes 24 de noviembre, en el que decía haber recibido "en los últimos días" las primeras denuncias de ataques asistidos por un agente de IA, con víctimas en al menos dos sectores de infraestructura crítica. En aquel texto afirmaba que, en todos los casos conocidos hasta entonces, los atacantes habían logrado comprometer los sistemas. En la entrevista posterior, Schütz habló de cinco casos y cuatro intrusiones; ninguna de las dos fuentes explica el cambio de cifra.

Las víctimas no se han identificado. Son pequeñas y medianas empresas y operadores de servicios esenciales como electricidad, agua potable y telecomunicaciones, que comunicaron los incidentes de forma voluntaria. Tampoco se sabe quién está detrás.

El aviso menciona como ejemplos de estas herramientas ARTEX y CyberStrikeAI, dos marcos de ataque "agéntico" accesibles en internet, aunque no afirma que fueran los usados en los cinco casos. Según la agencia, el número de herramientas de este tipo disponibles libremente casi se ha duplicado desde octubre.

## ¿Por qué preocupa a toda Europa?

Lo llamativo no es que la IA descubra fallos nuevos, sino la velocidad. Estos agentes atacan lo de siempre: contraseñas débiles o por defecto, vulnerabilidades conocidas sin parchear y servicios expuestos a internet. La diferencia es que lo hacen de forma automática y en paralelo contra muchos objetivos. Una alerta del FBI sobre ARTEX describía intrusiones en las que se pasó del primer contacto a privilegios de administrador en menos de tres horas.

Suiza no es un caso aislado. El CSIRT de Italia ha publicado un boletín sobre campañas automatizadas con agentes de IA que comprometieron muchos sistemas en pocas horas, y cita ARTEX, CyberStrikeAI, PentAGI y DeepSeek Harness. El NCSC británico ha advertido de que desde septiembre ve "un aumento notable de los ciberataques asistidos por IA". Y la Comisión Europea confirmó en octubre una intrusión mediante ARTEX que afectó a varios sistemas internos. Microsoft ya alertó hace unos días de que actores estatales y criminales están adoptando este marco, como contamos en [nuestra noticia sobre ARTEX y Salt Typhoon](/microsoft-artex-ia-salt-typhoon/).

Raphael Reischuk, del Instituto Nacional de Pruebas de Ciberseguridad suizo, prevé una oleada mayor y cree que muchas empresas siguen subestimando el riesgo.

## Cómo protegerse de los ataques con agentes de IA

Las recomendaciones de la agencia suiza son, sobre todo, higiene básica aplicada con más urgencia:

- **Parchear en 24 horas.** Las actualizaciones críticas de sistemas accesibles desde internet deben instalarse "lo antes posible, pero no más tarde de 24 horas" tras su publicación. Lo que no se pueda parchear, aislarlo.
- **Reducir lo expuesto.** Limitar el acceso a paneles, VPN y correo web con geobloqueo, listas de IP permitidas y autenticación previa.
- **MFA o passkeys en todo.** Especialmente en accesos remotos y correo web. Te explicamos cómo hacerlo en [nuestra guía para proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/).
- **Mínimo privilegio.** Que una cuenta comprometida no abra toda la red.
- **Vigilar lo anómalo.** Comportamientos fuera de lo normal, volúmenes de datos inusuales y ráfagas de peticiones automáticas; los desafíos antibots y los honeytokens ayudan a detectar a un agente que explora.
- **Probar la propia infraestructura** de forma periódica e incorporar los indicadores de compromiso publicados por el CSIRT italiano.

Para entender por qué un fallo ya publicado se convierte en el primer objetivo de estas herramientas, puede servir nuestro artículo sobre [qué es una CVE](/que-es-una-cve/). El caso suizo confirma que el tiempo entre que se conoce una vulnerabilidad y que alguien la usa contra tu empresa se ha reducido a horas.

## Fuentes

- [BACS (Suiza): aviso sobre ataques con agentes de IA](https://www.bacs.admin.ch/en/26-ki-agenten-1-en)
- [SRF: cinco casos confirmados de ciberataques con agentes de IA en Suiza](https://www.srf.ch/news/schweiz/fuenf-bestaetigte-faelle-erstmals-cyberangriffe-mit-ki-agenten-in-der-schweiz)
- [NCSC (Reino Unido): defensa frente a ciberataques agénticos](https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks)
- [CSIRT Italia: agentes de IA en campañas de compromiso automatizadas](https://csirt.regione.toscana.it/impiego-di-agenti-di-ia-in-campagne-di-compromissione-automatizzate-bl01-261123-csirt-ita/)
- [The Hacker News](https://thehackernews.com/2026/11/switzerland-confirms-ai-assisted.html)
- [Security Affairs](https://securityaffairs.com/204004/hacking/switzerland-confirms-first-ai-agent-cyberattacks-on-local-organisations.html)
