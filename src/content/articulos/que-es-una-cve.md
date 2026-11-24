---
title: "Qué es una CVE y cómo leer un aviso de seguridad (explicado fácil)"
description: "Qué es una CVE, qué significa la puntuación CVSS y cómo interpretar un aviso de seguridad para saber si te afecta y qué hacer."
date: 2026-11-20
category: vulnerabilidades
tags: ['CVE', 'CVSS', 'parches']
author: Redacción
featured: false
imageCredit: "Ilustración: Brecha Cero"
---


Si sigues noticias de ciberseguridad, habrás visto titulares del tipo *"Corregida la vulnerabilidad CVE-2026-XXXXX con puntuación 9,8"*. Detrás de ese código hay un sistema que usa todo el sector para hablar el mismo idioma. Entenderlo te permitirá saber, en pocos minutos, si una noticia te afecta de verdad o es solo ruido.

## Qué es una CVE

**CVE** son las siglas de *Common Vulnerabilities and Exposures* (Vulnerabilidades y Exposiciones Comunes). Es un catálogo público donde cada fallo de seguridad conocido recibe un identificador único.

El formato es siempre el mismo:

```
CVE-AÑO-NÚMERO
```

Por ejemplo, `CVE-2021-44228` es el identificador de Log4Shell, una de las vulnerabilidades más famosas de los últimos años, que afectó a una librería de Java usada en miles de aplicaciones.

El programa CVE lo coordina la organización MITRE con financiación del gobierno de Estados Unidos, y los identificadores los asignan las llamadas CNA (*CVE Numbering Authorities*): grandes empresas tecnológicas, organismos como el INCIBE en España, y otros.

### Para qué sirve

Imagina que cinco empresas de seguridad descubren el mismo fallo y cada una le pone un nombre distinto. Sería un caos. Con la CVE, todo el mundo (fabricantes, administradores de sistemas, antivirus, periodistas) se refiere al mismo fallo con el mismo código.

## Qué es la puntuación CVSS

La CVE solo identifica el fallo. Para saber lo grave que es se usa el CVSS (*Common Vulnerability Scoring System*), una puntuación de 0 a 10:

| Puntuación | Gravedad |
|---|---|
| 0,0 | Ninguna |
| 0,1 – 3,9 | Baja |
| 4,0 – 6,9 | Media |
| 7,0 – 8,9 | Alta |
| 9,0 – 10,0 | Crítica |

La puntuación se calcula combinando factores como:

- **Vector de ataque:** ¿se puede explotar por Internet o hace falta acceso físico?
- **Complejidad:** ¿es fácil o requiere condiciones muy concretas?
- **Privilegios necesarios:** ¿el atacante necesita una cuenta previa?
- **Interacción del usuario:** ¿la víctima tiene que hacer clic en algo?
- **Impacto:** cuánto afecta a la confidencialidad, integridad y disponibilidad de los datos.

> 💡 Una puntuación alta no significa automáticamente que estés en peligro. Si el fallo está en un software que no usas, o en un servicio que no tienes expuesto a Internet, tu riesgo real es mucho menor.

## Otras siglas que verás junto a una CVE

- **CWE** (*Common Weakness Enumeration*): describe el tipo de error. Por ejemplo, CWE-89 es "inyección SQL". Muchas CVE distintas pueden compartir la misma CWE.
- **KEV** (*Known Exploited Vulnerabilities*): un catálogo de la agencia estadounidense CISA con vulnerabilidades que se están explotando activamente. Si una CVE aparece ahí, es prioridad absoluta parchear.
- **EPSS** (*Exploit Prediction Scoring System*): estima la probabilidad de que una vulnerabilidad se explote en los próximos 30 días. Complementa al CVSS.
- **Zero-day (día cero):** vulnerabilidad que se está explotando antes de que exista un parche.

## Cómo leer un aviso de seguridad paso a paso

Cuando veas una noticia sobre una vulnerabilidad, hazte estas preguntas en orden:

1. **¿Qué producto y qué versiones están afectados?** Es lo primero. Si no usas ese software, puedes respirar tranquilo.
2. **¿Cuál es la puntuación CVSS?** Te da una idea de la gravedad general.
3. **¿Se está explotando activamente?** Busca la CVE en el catálogo KEV de CISA o en los avisos del INCIBE-CERT.
4. **¿Existe parche o versión corregida?** Si existe, la respuesta casi siempre es actualizar cuanto antes.
5. **¿Hay medidas temporales (mitigaciones)?** Si no puedes actualizar ya, el fabricante suele indicar cómo reducir el riesgo mientras tanto.

## Dónde consultar CVE de forma fiable

- **cve.org:** el registro oficial del programa CVE.
- **NVD (National Vulnerability Database):** base de datos del NIST con puntuaciones CVSS y detalles técnicos.
- **INCIBE-CERT:** avisos en español, muy útiles para empresas y particulares en España.
- **Avisos del propio fabricante:** Microsoft, Apple, Google, Cisco, etc. publican boletines periódicos.

## Ejemplo práctico (simplificado)

Supón que lees: *"Vulnerabilidad crítica (CVSS 9,8) en el servidor web X, versiones 2.4.0 a 2.4.5. Corregida en la 2.4.6. Se está explotando activamente."*

- ¿Usas el servidor X? Si no, no te afecta.
- Si lo usas, ¿qué versión tienes? Si es la 2.4.6 o superior, estás protegido.
- Si tienes una versión afectada y está expuesta a Internet, actualiza inmediatamente: es crítica y ya se está explotando.

## Preguntas frecuentes

**¿Todas las vulnerabilidades tienen CVE?**
No. Solo las que se reportan y registran públicamente. Muchos fallos se corrigen sin llegar a tener identificador.

**¿Quién puede pedir una CVE?**
Cualquier investigador que descubra un fallo puede solicitarla a través de la CNA correspondiente o del propio programa CVE, normalmente tras coordinarse con el fabricante (divulgación responsable).

**¿Una CVE con puntuación baja se puede ignorar?**
No del todo. Varias vulnerabilidades "medias" combinadas pueden permitir un ataque serio. Pero sí sirve para priorizar.


Las CVE son el idioma común de la ciberseguridad. Saber leerlas te ayuda a separar las amenazas reales de los titulares alarmistas y a priorizar qué actualizar primero. La regla de oro sigue siendo la misma: mantén tu software actualizado.

*Este artículo tiene fines educativos.*
