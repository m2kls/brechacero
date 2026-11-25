---
title: "Fallo en Drupal ya explotado: el instalador permite secuestrar webs"
description: "Fallo en Drupal explotado desde el 19 de noviembre: CVE-2026-132165 permite reinstalar la web y tomar el control. CISA da tres días. Versiones a instalar ya."
date: 2026-11-25T10:54:00+01:00
category: vulnerabilidades
tags: [Drupal, CVE-2026-132165, CMS, CISA KEV, parche, webs]
author: Redacción
photo: "File:Drupal logo.jpg"
imageAlt: "Logotipo de Drupal, el gestor de contenidos afectado por un fallo explotado en su instalador"
---

El fallo en Drupal que el proyecto corrigió el 18 de noviembre ya se está aprovechando en ataques reales. Se trata de CVE-2026-132165, una vulnerabilidad en el instalador del núcleo de Drupal que, en determinadas condiciones, permite a alguien sin cuenta volver a instalar el sitio y, a partir de ahí, secuestrarlo o ejecutar código en el servidor. El equipo de seguridad de Drupal ha confirmado explotación en webs en producción desde el 19 de noviembre, y la agencia estadounidense CISA la añadió el 24 de noviembre a su catálogo de vulnerabilidades explotadas.

Drupal es uno de los gestores de contenidos más usados por administraciones públicas, universidades, medios y grandes empresas, también en España, así que cualquier fallo de este tipo tiene un impacto potencial amplio.

## Qué es el fallo de Drupal CVE-2026-132165

El problema está en el instalador, el asistente que se usa una sola vez para montar un sitio nuevo. Según el aviso SA-CORE-2026-017, bajo ciertas condiciones ese instalador sigue siendo accesible en una web ya en marcha, y un atacante puede lanzar una reinstalación sin autenticarse. El resultado puede ser la toma del control del sitio o la ejecución de código arbitrario en el servidor.

Cuando se publicó el parche, Drupal ya advirtió de que los ataques podían llegar rápido. Así ha sido: el aviso se actualizó para indicar que el equipo de seguridad había recibido un informe de explotación "en sitios en producción desde el 19 de noviembre a las 19:00 UTC", menos de un día después del parche. Tras conocer los ataques, Drupal elevó la valoración del fallo a "altamente crítico", con una puntuación de 20 sobre 25 en su escala de riesgo.

Según SecurityWeek, la vulnerabilidad la encontró OSS Scanner, la herramienta de Anthropic que analiza proyectos de código abierto en busca de fallos. Es el tercer fallo de Drupal explotado este año, tras uno en mayo que afectó a miles de webs y otro en el módulo Commerce Core usado contra tiendas online a finales de octubre. No hay datos públicos sobre cuántos sitios han sido atacados esta vez.

## ¿Estoy afectado?

Están en riesgo las webs con Drupal 10 y 11 que no se hayan actualizado desde el 18 de noviembre. Las versiones corregidas son:

- Drupal 11.4.13
- Drupal 11.3.22
- Drupal 10.6.22

Las ramas que ya no tienen soporte no recibirán parche. Si tu web usa una versión antigua de Drupal, la única opción segura es migrar a una rama mantenida.

CISA ha dado a las agencias federales de Estados Unidos hasta el 27 de noviembre para corregirlo, un plazo de solo tres días que refleja la urgencia.

## Cómo proteger tu web Drupal

1. **Actualiza ya** a la versión corregida de tu rama. Es la medida principal.
2. **Bloquea el instalador** una vez montado el sitio, como recomienda el propio Drupal: no debe ser accesible desde Internet en una web en producción.
3. **Revisa los permisos de `settings.php`**. Drupal explica que algunas vías de explotación, aunque no todas, quedan neutralizadas si el servidor web no puede escribir ni cambiar permisos de ese fichero.
4. **Busca indicios de compromiso** si tu web estuvo sin parchear después del 19 de noviembre: usuarios administradores nuevos, cambios inesperados en la configuración, ficheros PHP desconocidos o una reinstalación que nadie pidió. Ante la duda, restaura desde una copia de seguridad anterior y cambia todas las credenciales.
5. Si la web la gestiona una agencia o proveedor, pregúntale hoy mismo si ya ha aplicado el parche.

Si quieres entender cómo se clasifican y priorizan estos fallos, lo explicamos en [qué es una CVE y cómo se mide su gravedad](/que-es-una-cve/). Y para el contexto de las vulnerabilidades web más habituales, en el [OWASP Top 10 explicado](/owasp-top-10-explicado/).

## Fuentes

- [Drupal: SA-CORE-2026-017, aviso de seguridad del núcleo](https://www.drupal.org/sa-core-2026-017)
- [CISA: CISA Adds Three Known Exploited Vulnerabilities to Catalog (24-11-2026)](https://www.cisa.gov/news-events/alerts/2026/11/24/cisa-adds-three-known-exploited-vulnerabilities-catalog)
- [SecurityWeek: Drupal Flaw Found by Anthropic Scanner Exploited in Attacks](https://www.securityweek.com/drupal-flaw-found-by-anthropic-scanner-exploited-in-attacks/)
- [The Hacker News: Drupal Patches Critical Installer Flaw](https://thehackernews.com/2026/11/drupal-patches-critical-installer-flaw.html)
