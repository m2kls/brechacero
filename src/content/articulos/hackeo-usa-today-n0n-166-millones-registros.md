---
title: "Hackeo a USA Today: el grupo N0n dice tener 166 millones de registros"
description: "N0n, el grupo de extorsión ligado a los incidentes de JPMorgan y Visa, asegura haber robado 166 millones de registros de USA Today y señala a Mattel y otras 20 empresas."
date: 2026-11-26T16:57:00+01:00
category: noticias
tags: [USA Today, Gannett, N0n, extorsión, filtración, Mattel, ransomware]
author: Redacción
photo: "File:USA Today Newspaper Vending Machine.jpg"
imageAlt: "Máquina expendedora del periódico USA Today, cuyo editor aparece en la web de filtraciones del grupo N0n"
---

El grupo de extorsión N0n asegura haber hackeado a USA Today Co., el editor del diario estadounidense USA Today y de cientos de periódicos locales (la antigua Gannett). En su web de filtraciones afirma tener un "grafo de identidad" de suscriptores con 166 millones de registros, entre ellos unos 27 millones de direcciones de correo en texto plano. La empresa no ha confirmado el incidente y los atacantes no han publicado pruebas, pero el anuncio llega en plena ola de reivindicaciones de un grupo que en las últimas semanas ha apuntado a JPMorgan, Visa, Mastercard o Expedia.

## Qué dice haber robado N0n a USA Today

Según la ficha publicada por el grupo, recogida por Ransomware.live, BreachNews y Cybernews, el conjunto incluye:

- Un perfil unificado de unos 166 millones de usuarios y suscriptores.
- Registros de suscripción y facturación (números de cuenta y códigos de publicación).
- Quejas, bajas y rebotes de los boletines por correo electrónico.
- Resúmenes de visitas a la web con ciudad, región, código postal y tipo de dispositivo.
- Puntuaciones internas de riesgo de baja y de valor del cliente.
- Unos 27 millones de correos de consumidores, 7,7 millones de filas de registro en publicaciones y 58.704 filas con nombre y apellidos.

USA Today fue añadida el 25 de noviembre junto a otras 21 organizaciones, todas marcadas como "no han pagado" y con una cuenta atrás que vence hacia el 2 de diciembre. Ransomware.live calcula que el ataque se produjo hacia el 18 de noviembre, cuando el grupo publicó a una víctima anónima ("Company #230") que ahora identifica como Gannett.

## ¿Es creíble la cifra de 166 millones?

Hay motivos para la prudencia. USA Today Co. tenía al cierre de septiembre unos 1,4 millones de suscripciones solo digitales y unos 161 millones de visitantes únicos al mes, así que el total reclamado se parece más a una base de datos de marketing (con duplicados y visitantes anónimos) que a un listado de clientes. Ni la empresa ni sus registros ante la SEC mencionan un incidente, y Cybernews recuerda que estos grupos suelen inflar sus cifras. Por la descripción, los datos más sensibles serían nombres, correos y datos de facturación, sin contraseñas ni tarjetas completas.

## Quién es N0n y qué otras empresas señala

N0n apareció a mediados de septiembre y presume de 365 víctimas en tres meses. Su historial es irregular: JPMorgan, Expedia, Visa y Mastercard reconocieron incidentes en proveedores externos después de aparecer en su web, mientras que otras empresas negaron haber sido atacadas. Los investigadores de SOCRadar y Bitdefender han visto que el grupo entra sobre todo con credenciales débiles o robadas y que su servidor de archivos, expuesto en Internet, contenía datos de una veintena de víctimas, muy por debajo de las más de cien que anuncia.

En la misma tanda del 25 de noviembre figuran, entre otras:

- **Mattel**: un directorio de 29 empleados con acceso de administración a las tiendas online de sus marcas. No menciona datos de clientes.
- **Next**, la cadena británica de moda: más de 320.000 líneas de conversaciones de clientes con su asistente de compras con IA. Next ya informó el 23 de noviembre de un incidente en un proveedor y aseguró que no se vieron afectados datos personales de clientes.
- **hmv, Torrid y otras tiendas online**, con descripciones idénticas que apuntan a un mismo proveedor de búsqueda comercial.
- **Mobility ADO**, el gran operador de autobuses de México, y la fintech mexicana **PayClip**, con datos de venta de billetes y de vendedores.

El patrón, como en otros casos recientes, apunta a ataques contra proveedores tecnológicos compartidos más que contra la empresa principal. Es el mismo riesgo que se vio en el [hackeo a 1Password a través del GitHub de un empleado](/hackeo-1password-github-datos-clientes/): basta una credencial robada en una herramienta externa para llegar a datos de clientes.

## Qué hacer si eres suscriptor de USA Today

Aunque el robo no esté confirmado, con un correo y un historial de suscripción basta para montar un engaño creíble. Conviene:

- Desconfiar de correos sobre "renovaciones", "pagos fallidos" o "reembolsos" de USA Today o de periódicos del grupo, y entrar siempre a tu cuenta desde la web oficial. Repasa [las señales para detectar el phishing](/como-detectar-phishing/).
- Cambiar la contraseña si la reutilizas en otros servicios y activar la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/).
- Vigilar los cargos de la tarjeta asociada a la suscripción.

Actualizaremos esta información si USA Today Co. confirma o descarta el incidente o si el grupo publica los datos cuando venza su plazo.

## Fuentes

- Cybernews: [JPMorgan hackers claim USA Today breach revealed 166M records](https://cybernews.com/security/usa-today-hacker-data-breach/)
- BreachNews: [N0n extortion group names Mattel, Gannett and 20 other companies on leak site](https://breachnews.com/breaches/n0n-mattel-gannett-leak-site-claims/)
- Startup Fortune: [N0n says it holds 166 million USA Today records and sets a leak deadline](https://startupfortune.com/n0n-says-it-holds-166-million-usa-today-records-and-sets-a-leak-deadline/)
- Ransomware.live: [Ficha de Gannett Co., Inc. (USA TODAY Network)](https://www.ransomware.live/id/R2FubmV0dCBDby4sIEluYy4gKFVTQSBUT0RBWSBOZXR3b3JrKUBOMG4)
