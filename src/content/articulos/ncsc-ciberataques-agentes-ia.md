---
title: "Ciberataques con agentes de IA: el NCSC británico alerta de un fuerte aumento"
description: "El NCSC de Reino Unido ve un fuerte aumento de ciberataques con agentes de IA desde septiembre: explotan fallos conocidos en minutos. Así puedes defenderte."
date: 2026-11-24T20:58:00+01:00
category: noticias
tags: [inteligencia artificial, NCSC, Reino Unido, agentes de IA, ciberataques, defensa]
author: Redacción
photo: "File:Aerial of GCHQ, Cheltenham, Gloucestershire, England 24May2017 arp.jpg"
imageAlt: "Vista aérea de la sede del GCHQ en Cheltenham, organismo del que depende el NCSC británico"
---

Los ciberataques con agentes de IA ya no son una hipótesis de laboratorio. El Centro Nacional de Ciberseguridad de Reino Unido (NCSC), dependiente del GCHQ, ha publicado este 24 de noviembre un aviso en el que asegura haber visto desde septiembre "un marcado aumento" de ataques asistidos por inteligencia artificial. Los delincuentes usan herramientas que automatizan todo el proceso, desde encontrar un servicio expuesto hasta explotarlo, y lo hacen en minutos. La buena noticia, según el propio NCSC, es que no aprovechan fallos nuevos: los que tienen los deberes hechos están mucho mejor protegidos.

## Qué ha detectado el NCSC

El organismo británico describe lo que llama "marcos ofensivos agénticos": programas pensados originalmente para equipos de *red team* (los que simulan ataques para mejorar la defensa) que ahora se usan fuera de ese fin. En su aviso cita varios por su nombre, entre ellos ARTEX, Cairn, PentAGI, RedAmon, Xalgorix y Darkmoon. Según CyberScoop, los atacantes los combinan con modelos abiertos baratos o con revendedores ilegales de acceso a API de IA, lo que abarata mucho una campaña.

Estos agentes repasan todo lo que una organización tiene expuesto a internet y pasan "del descubrimiento a la explotación en minutos", explica el NCSC. Las consecuencias que ha visto van desde caídas de servicio hasta el compromiso completo de sistemas.

CyberScoop recoge además un caso contado por CrowdStrike en la conferencia CYBERWARCON: en un ataque a una organización sanitaria de Argentina, un agente encontró y explotó una inyección SQL en unos 90 minutos a partir de una instrucción mínima.

## Qué fallos aprovechan los agentes de IA

Aquí está el matiz importante. El NCSC insiste en que "ninguna de las debilidades explotadas es nueva". Los agentes van a por lo de siempre, solo que más rápido y a más escala:

- Credenciales olvidadas dentro de repositorios de código.
- Errores de configuración en la infraestructura como código.
- Servicios con contraseñas por defecto o sin autenticación.
- Abuso de API sin límites de uso.
- Parches pendientes en sistemas expuestos.

Dicho de otra forma: la IA no ha inventado un tipo de ataque, ha reducido el tiempo que una empresa tiene entre que algo queda expuesto y que alguien lo aprovecha. Es la misma lógica que ya vimos en las campañas de [phishing con IA](/phishing-con-ia/): técnicas conocidas, más volumen y más velocidad.

## Cómo protegerse de los ataques con agentes de IA

El NCSC plantea sus recomendaciones como ocho preguntas que cualquier equipo de seguridad debería poder responder. Resumidas:

1. **Saber qué está expuesto**: un inventario real de todo lo que se ve desde internet.
2. **Sacar de internet lo que no necesite estar ahí**, o protegerlo con un proxy con control de identidad, restricciones de cortafuegos o TLS mutuo.
3. **Detectar la actividad de agentes en los registros**: patrones de peticiones rápidos y sistemáticos.
4. **Parchear antes** y corregir los permisos que se han ido acumulando con el tiempo.
5. **Poner retos anti-bots** en los puntos más abusados, con una alternativa accesible para las personas.
6. **Limitar la frecuencia de peticiones a las API** por cuenta, token o sesión, no solo por dirección IP.
7. **Frenar la creación masiva de cuentas.**
8. **Usar señuelos** como *honeytokens* (credenciales falsas que avisan si alguien las usa) y *tarpits* que ralentizan a los atacantes automatizados.

Para una pyme o un usuario particular, la traducción es sencilla: actualizar pronto, no reutilizar contraseñas y activar la [verificación en dos pasos en todas las cuentas](/proteger-cuentas-contrasenas-2fa/). Un agente automático busca la puerta abierta más fácil; cerrar las obvias le obliga a buscar en otro sitio.

## Un aviso que llega en plena oleada

El aviso coincide con otros casos recientes en los que la IA aparece en el centro de un incidente y con el [robo de secretos en Azure API Management](/fallo-azure-api-management-secretos/), donde la autoridad noruega también alertó de que el uso creciente de IA eleva el riesgo de nuevas explotaciones. El propio NCSC ya había publicado a principios de noviembre una evaluación sobre la IA y las intrusiones. Su conclusión de fondo se repite: la defensa que funciona contra los agentes es la misma higiene básica de siempre, aplicada con más prisa.

## Fuentes

- [NCSC: Familiar weaknesses, exploited faster: defending against agentic cyber attacks](https://www.ncsc.gov.uk/blogs/familiar-weaknesses-exploited-faster-defending-against-agentic-cyber-attacks)
- [CyberScoop: UK cyber agency, threat companies tracking rise in AI-assisted hacks](https://cyberscoop.com/uk-ncsc-ai-assisted-cyberattacks)
