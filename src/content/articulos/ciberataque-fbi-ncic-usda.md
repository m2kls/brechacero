---
title: "Ciberataques al Gobierno de EE. UU.: qué se sabe del FBI y del Departamento de Agricultura"
description: "EE. UU. investiga una posible intrusión en la base de datos criminal del FBI y un ataque confirmado al sistema de pagos agrícolas. Lo confirmado y lo que no."
date: 2026-11-28
category: noticias
tags: [FBI, Estados Unidos, ciberataque, administración pública, integridad de datos]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

La semana del 16 al 20 de noviembre de 2026 terminó con dos incidentes de ciberseguridad en organismos federales de Estados Unidos. Uno de ellos está confirmado oficialmente; el otro, por ahora, solo se conoce por fuentes anónimas. Como suele pasar en las primeras horas de un incidente, la información es parcial, así que vamos a separar con cuidado lo que se sabe de lo que no.

## 1. Departamento de Agricultura (USDA): ataque confirmado

**Qué ha pasado.** Según NBC News, que cita a dos antiguos altos cargos del organismo, unos atacantes accedieron durante esa semana a un sistema de pagos a agricultores del Departamento de Agricultura. Los empleados fueron avisados el jueves 19 y la noticia se hizo pública el viernes 20.

**Sistemas afectados.** Según Meganoticias, el incidente afectó a herramientas de préstamos y ayudas de la Farm Service Agency (FSA) y al programa ProTracts del Servicio de Conservación de Recursos Naturales (NRCS). Varias aplicaciones tuvieron que apagarse y reiniciarse para restablecer el servicio.

**Qué dice el Gobierno.** Richard Fordyce, subsecretario de Agricultura para Producción y Conservación, confirmó que el departamento se enfrentó a una "amenaza cibernética". Según su versión, las medidas de protección funcionaron, no se perdieron datos y no se comprometieron datos personales identificables.

**Lo que no se sabe.** No se ha identificado públicamente a los responsables, ni se ha detallado cómo entraron.

## 2. FBI: posible intrusión en el NCIC, sin confirmar

**Qué se ha publicado.** CNN informó, citando a dos personas conocedoras de la investigación, de que el FBI investiga un posible acceso no autorizado al NCIC (*National Crime Information Center*), la base de datos que usan miles de cuerpos policiales de todo el país para consultar órdenes de búsqueda y detención, antecedentes y otros registros.

**Lo que no se sabe (que es casi todo).** A fecha de publicación de este artículo:

- El FBI no ha confirmado la intrusión ni ha hecho declaraciones; tampoco respondió a Reuters ni a la BBC, según Infobae.
- No se sabe qué alcance tuvo el acceso, ni si los atacantes leyeron, copiaron o modificaron datos.
- Nadie ha reivindicado el ataque. Algún medio ha mencionado al grupo ShinyHunters, pero sin una fuente que lo respalde, así que conviene tomarlo como especulación.

> ℹ️ Fallos que NO eran ciberataques: en esas mismas fechas hubo una caída de servicios de Microsoft y un fallo en el control del tráfico aéreo de la FAA. Según las autoridades, citadas por la BBC, ninguno de los dos fue un ciberataque.

## Por qué este caso es interesante: la integridad de los datos

Cuando pensamos en un ciberataque, solemos pensar en robo de datos (confidencialidad). Pero un antiguo responsable de ciberdelincuencia del FBI, citado por CNN, apuntó a otra preocupación: que los atacantes hubieran podido alterar la exactitud de la información en la que confían los agentes.

Es un buen ejemplo de la llamada tríada CIA de la seguridad de la información:

- **Confidencialidad:** que solo quien debe pueda leer los datos.
- **Integridad:** que los datos no se puedan modificar sin autorización.
- **Disponibilidad:** que los sistemas funcionen cuando se necesitan.

En una base de datos policial, un registro manipulado (una orden de detención falsa o borrada) puede ser tan grave como una filtración. Y en el caso del USDA, aunque no se hayan perdido datos, el impacto en la disponibilidad fue real: hubo que interrumpir servicios a agricultores.

Estos tres pilares son también los que mide la puntuación CVSS de una vulnerabilidad, como explicamos en [qué es una CVE](/que-es-una-cve/).

## Cómo leer noticias de ciberataques sin caer en el sensacionalismo

Este incidente es un buen ejercicio para cualquier lector:

1. **Busca la confirmación oficial.** "Fuentes conocedoras" no es lo mismo que un comunicado del organismo afectado.
2. **Distingue acceso, robo y manipulación.** Que alguien haya "accedido" no significa que haya sacado o cambiado datos.
3. **Desconfía de las atribuciones tempranas.** Saber quién está detrás de un ataque suele llevar semanas o meses.
4. **Mira de dónde viene la información.** Varios medios en español contaron esta historia citando a CNN y NBC de segunda o tercera mano.

¿Te afecta como ciudadano europeo? Directamente, no. Pero si en algún momento recibes un correo o una llamada aprovechando el tirón de una noticia así ("tus datos aparecen en la filtración del FBI, paga para borrarlos"), es una estafa. Te contamos [qué hacer si tus datos aparecen en una filtración](/datos-en-filtracion-que-hacer/).

Actualizaremos este artículo si el FBI o el USDA publican más información.

**Fuentes:** [Infobae](https://www.infobae.com/estados-unidos/2026/11/21/hackeo-al-fbi-un-ciberataque-habria-comprometido-la-base-de-datos-criminal-con-ordenes-de-arresto-y-antecedentes-penales/) · [Meganoticias](https://www.meganoticias.cl/mundo/536942-ciberataque-gobierno-estados-unidos-hackers-departamento-agricultura-20-11-2026.html) · [Moncloa.com](https://www.moncloa.com/2026/11/21/ciberataque-fbi-base-datos-criminal-3472262/) (que a su vez citan a CNN y NBC News)
