---
title: "Ransomware Booba: ataca una planta de agua de EE. UU. y salta al ayuntamiento"
description: "El ransomware Booba entró por una potabilizadora de la costa este de EE. UU. y alcanzó la red del gobierno local. 48 equipos aislados y 3 cifrados. Qué se sabe."
date: 2026-11-28T16:55:00+01:00
category: noticias
tags: [Booba, ransomware, planta de agua, infraestructuras críticas, Estados Unidos, ThreatDown, administraciones locales]
author: Redacción
photo: "File:Water treatment plant in Saratoga Springs, New York.jpg"
imageAlt: "Planta de tratamiento de agua en Saratoga Springs, Nueva York, similar a la atacada por el ransomware Booba"
---

El **ransomware Booba** atacó este mes una planta de tratamiento de agua de la costa este de Estados Unidos y, desde ahí, llegó a la red del gobierno local que la gestiona. Lo ha contado ThreatDown, la división empresarial de Malwarebytes, cuyo equipo de detección y respuesta (MDR) frenó el cifrado en el lado municipal cuando ya había tres equipos afectados. El caso, recogido este sábado por Security Affairs, muestra un problema muy común: el punto exacto donde termina la vigilancia de seguridad.

## Qué ha pasado con el ransomware Booba en la planta de agua

La red estaba repartida entre dos proveedores. ThreatDown protegía la parte del gobierno local, donde están los expedientes y los datos personales de los vecinos. La parte de la planta potabilizadora la gestionaba otra empresa y no tenía su agente instalado.

Según ThreatDown, el ataque se preparó y se lanzó desde el lado de la planta. Lo primero que vio el equipo en la red municipal fue directamente el cifrado: dos o tres alertas casi seguidas de ransomware y cifrado de archivos, y un equipo con prácticamente todos sus ficheros renombrados con la extensión `.booba`. El cifrado procedía de una máquina sin agente, fuera de su cobertura.

La respuesta fue aislar de golpe **40 estaciones de trabajo y 8 servidores** desde la consola de gestión. Tres equipos ya estaban cifrados y se lanzaron órdenes para revertir los cambios, aunque no se ha detallado si funcionó. Los otros 45 se salvaron y no hubo más alertas. En la planta, el otro proveedor desconectó temporalmente todos los ordenadores para limpiarlos in situ.

ThreatDown dice que no hay pruebas de que el **suministro de agua** se viera afectado. Tampoco se sabe cómo entraron los atacantes ni cuál era su objetivo, porque la empresa no tuvo acceso forense a los sistemas de la planta.

## Quién está detrás de Booba

Booba es una marca de ransomware criminal que apareció este verano y que ha crecido muy deprisa:

- Supone el **44 %** de los casos de ransomware que han atendido los analistas de ThreatDown en los últimos 90 días.
- La firma SOCRadar, que lo sigue como "Booba Project", había contado 81 ataques reivindicados hasta el 17 de noviembre, varios de ellos contra ayuntamientos y condados de EE. UU.
- Uno de los analistas cree que su facilidad de uso explica parte de esa expansión.

No hay indicios de que se trate de un actor estatal, aunque grupos vinculados a gobiernos sí han atacado antes sistemas de agua estadounidenses.

## Por qué preocupa: las plantas de agua siguen en el punto de mira

El caso llega tras meses de avisos. CISA alertó este año de que más de 100 sistemas de agua y aguas residuales expuestos a internet habían sido atacados, Minnesota denunció una ofensiva coordinada contra más de 30 sistemas comunitarios, y la Asociación Nacional de Agua Rural dice que casi 100 operadores han pedido ayuda a su centro de vigilancia desde agosto. Son organizaciones pequeñas, con poco personal técnico y a menudo con la parte industrial externalizada, justo el escenario de este ataque.

En Europa la situación no es tan distinta: este mismo mes se han conocido ataques a [infraestructuras críticas en Suiza](/suiza-ciberataques-agentes-ia-infraestructura-critica/) y a la red eléctrica estadounidense con el [ransomware WhiteArmor contra Eversource](/ransomware-whitearmor-eversource-datos-red-electrica/).

## Cómo protegerse: saber dónde acaba tu vigilancia

La lección que saca ThreatDown es sencilla y aplicable a cualquier organización, también en España:

- **Inventario completo**: saber qué equipos hay en la red y cuáles no tienen protección. Los ataques empiezan cada vez más desde máquinas sin agente.
- **Cobertura en toda la cadena**: si la red está compartida con un proveedor o una entidad dependiente, acordar quién vigila qué y cómo se comunican los incidentes.
- **Segmentar** la red industrial de la ofimática, para que un problema en una no se propague a la otra.
- **No reconectar** redes aisladas hasta confirmar que el otro lado está limpio, como recomendó el equipo en este caso.
- Copias de seguridad desconectadas y probadas, que son las que permiten recuperarse sin pagar.

Si quieres entender mejor cómo se detectan y aprovechan los fallos que suelen abrir la puerta a estos ataques, repasa [qué es una CVE](/que-es-una-cve/).

## Fuentes

- [ThreatDown: Ransomware hit a US water plant, then spread to the local government behind it](https://www.threatdown.com/blog/ransomware-water-plant-local-government/)
- [Security Affairs: Booba ransomware attack on water plant reveals monitoring blind spot](https://securityaffairs.com/204166/cyber-crime/booba-ransomware-attack-on-water-plant-reveals-monitoring-blind-spot.html)
- [SOCRadar: Booba Project, ransomware intelligence](https://socradar.io/free-tools/ransomware-intelligence/groups/booba-project)
