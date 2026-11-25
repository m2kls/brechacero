---
title: "Hackeo de Rackspace Spot: la nube cierra tras exponer secretos de Kubernetes"
description: "El hackeo de Rackspace Spot permitió leer secretos de Kubernetes de clientes. Rackspace cerrará el servicio el 8 de diciembre. Qué deben hacer los afectados."
date: 2026-11-25T20:58:00+01:00
category: noticias
tags: [Rackspace, Rackspace Spot, Kubernetes, nube, credenciales robadas, filtración]
author: Redacción
photo: "File:Front_of_server_racks_at_NERSC.jpg"
imageAlt: "Armarios de servidores en un centro de datos, como los de una plataforma de nube"
---

El hackeo de Rackspace Spot ha terminado de la forma más drástica posible: la compañía estadounidense va a cerrar el servicio. Un atacante entró el 17 de noviembre en esta plataforma de nube de bajo coste con credenciales robadas, creó contenedores en los clústeres de varios clientes y pudo leer los secretos de Kubernetes que guardaban dentro, es decir, contraseñas, claves de API y certificados. Rackspace ha avisado a los afectados y les ha dado hasta el 8 de diciembre para sacar sus datos antes de apagar Spot por completo.

## Qué es Rackspace Spot

Rackspace Technology es uno de los proveedores veteranos de alojamiento y servicios gestionados en la nube. Spot era su apuesta barata: servidores, máquinas virtuales y Kubernetes gestionado cuyo precio se fijaba mediante pujas, con descuentos de hasta el 90 % frente a la tarifa normal a cambio de aceptar que las cargas de trabajo se pudieran interrumpir. Lo usaban sobre todo desarrolladores, startups y equipos que buscaban potencia de cálculo a bajo precio.

## Cómo fue el hackeo de Rackspace Spot

Según la notificación que la empresa envió a sus clientes, recogida por BleepingComputer y TechRadar, el intruso accedió a partes de la plataforma en la madrugada del 17 de noviembre usando credenciales de acceso robadas. Rackspace no ha explicado cómo se obtuvieron. La empresa no lo detectó por sí misma: se enteró un día después gracias al aviso de un cliente.

Con ese acceso, el atacante:

- creó pods (contenedores) no autorizados en clústeres de clientes,
- leyó secretos de Kubernetes,
- y listó los nodos y volúmenes de almacenamiento.

En su aviso, Rackspace reconoce que el intruso "podría haber leído cualquier secreto" de los clústeres afectados. No ha dado una cifra de clientes perjudicados, más allá de decir que son varios, y por ahora ningún grupo ha reivindicado el ataque ni han aparecido los datos en foros de filtraciones.

Tras detectarlo, la compañía revocó los tokens y sesiones de Spot implicados, eliminó los pods creados por el atacante y rotó las claves de la plataforma y del almacenamiento afectadas.

## Rackspace cierra Spot el 8 de diciembre

Pocos días después llegó un segundo correo: "Tras revisar la situación, Rackspace ha decidido cerrar el servicio Rackspace Spot". La empresa lo justifica como la forma de dar a los clientes "un camino claro". Los usuarios tienen hasta el 8 de diciembre a las 17:00 (hora central de EE. UU., medianoche en España) para migrar sus datos; después, todas las cargas de trabajo que sigan en marcha se eliminarán.

Es una decisión poco habitual. Lo normal tras una intrusión es reforzar el servicio, no apagarlo, y algunos usuarios se han quejado en foros del poco margen para mudarse. Rackspace no ha respondido a esas peticiones.

## Por qué importa: los secretos de Kubernetes

Los secretos de un clúster son las llaves del resto de la infraestructura: contraseñas de bases de datos, tokens de servicios en la nube, claves de pasarelas de pago o de repositorios de código. Quien los tiene puede saltar del clúster a otros sistemas de la empresa aunque estos no estuvieran en Spot. Por eso el riesgo no termina con el cierre del servicio. Ya lo vimos esta semana con el [hackeo a Radware, que expuso claves de nube de clientes](/hackeo-radware-claves-nube-clientes/), y con el [fallo de Azure API Management usado para robar secretos](/fallo-azure-api-management-secretos/).

## Qué hacer si usabas Rackspace Spot

Rackspace recomienda, y conviene hacerlo aunque no se haya confirmado una fuga en tu cuenta:

1. **Rotar todos los secretos** guardados en los clústeres: contraseñas, claves de API, tokens y certificados. No basta con borrarlos; hay que revocarlos en el servicio que los emitió y generar otros nuevos.
2. Volver a emitir los tokens de API de Spot y sustituir los tokens de actualización guardados en scripts y automatizaciones.
3. Descargar kubeconfigs nuevos para cada cloudspace.
4. Revisar los registros de acceso desde el 17 de noviembre en adelante, también en los servicios externos a los que daban acceso esos secretos.
5. Planificar la migración antes del 8 de diciembre y no dejar copias de datos sensibles en la plataforma.

Para cualquier empresa, la lección es la de siempre: credenciales con el mínimo privilegio, [verificación en dos pasos en todas las cuentas de administración](/proteger-cuentas-contrasenas-2fa/) y secretos fuera del clúster, en un gestor dedicado que permita rotarlos rápido.

## Fuentes

- [TechRadar: Rackspace forced to shut down Spot cloud platform following security breach](https://www.techradar.com/pro/security/rackspace-forced-to-shut-down-spot-cloud-platform-following-security-breach)
- [BleepingComputer: Rackspace shuts down Spot cloud platform after security breach](https://www.bleepingcomputer.com/news/security/rackspace-shuts-down-spot-cloud-platform-after-security-breach/)
- [SC Media: Rackspace to shut down Spot cloud platform following security breach](https://www.scworld.com/brief/rackspace-to-shut-down-spot-cloud-platform-following-security-breach)
