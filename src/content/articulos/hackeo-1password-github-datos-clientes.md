---
title: "Hackeo de 1Password: roban datos de clientes a través del GitHub de un empleado"
description: "El hackeo de 1Password expuso nombres, correos y tokens de recuperación de clientes, pero no las bóvedas de contraseñas. Qué se ha robado y qué debes vigilar."
date: 2026-11-25T23:00:00+01:00
category: noticias
tags: [1Password, gestor de contraseñas, GitHub, filtración, cadena de suministro, phishing]
author: Redacción
photo: "File:Code_on_computer_monitor_(Unsplash).jpg"
imageAlt: "Código fuente en un monitor, como el que se copió en el hackeo de 1Password"
---

El hackeo de 1Password, uno de los gestores de contraseñas más usados del mundo, se ha confirmado este 25 de noviembre. La empresa canadiense ha explicado que un atacante tomó el control de la cuenta corporativa de GitHub de un empleado, la usó para colar código malicioso en servicios internos y, con él, descargó datos administrativos de clientes y copió código fuente privado. Lo más importante para los usuarios: según 1Password, las bóvedas con las contraseñas y las claves que las cifran no se han visto afectadas.

## Qué ha pasado en el hackeo de 1Password

La compañía empezó a investigar el 19 de noviembre, cuando detectó indicios de que alguien había accedido a la cuenta de GitHub de uno de sus trabajadores. No es una cuenta cualquiera: desde ella se podía modificar código que acaba en los servicios de la empresa. El intruso aprovechó ese acceso para introducir código malicioso en sistemas de backend, es decir, los servidores que gestionan las cuentas, y esos servicios terminaron enviándole registros de clientes.

Además, el atacante copió código fuente de repositorios privados y obtuvo acceso al entorno de integración y despliegue continuo (CI/CD), la cadena que compila y publica el software. Ese tipo de acceso es delicado porque puede contener credenciales de infraestructura; 1Password asegura que ya las ha rotado o revocado.

## Qué datos se han robado

Según el comunicado oficial y la información publicada por BleepingComputer y Hackread, los datos copiados incluyen:

- nombres y direcciones de correo electrónico de clientes,
- identificadores de cuenta y de usuario,
- fechas de alta y del último inicio de sesión,
- claves criptográficas públicas y parámetros del protocolo SRP que usa el servicio para autenticar,
- tokens incluidos en algunos enlaces de correo de invitación, alta de cuentas (aprovisionamiento) y recuperación de cuenta.

1Password no ha dicho cuántos clientes están afectados. Sí ha indicado que un número pequeño de usuarios cuyos tokens de aprovisionamiento quedaron expuestos ha sido avisado directamente.

## ¿Están en peligro mis contraseñas?

Según la empresa, no. "Your vault data, the items in them, and the keys that protect them are safe and were not affected", dice el comunicado: los datos de las bóvedas, los elementos que contienen y las claves que los protegen están a salvo. Tampoco se vieron comprometidas las claves de recuperación ni las aplicaciones y extensiones del navegador, y la compañía afirma que no ha visto tomas de control de cuentas.

Esto encaja con el diseño de 1Password: las bóvedas se cifran en el dispositivo con la contraseña maestra y una Secret Key que la empresa no conoce. Por eso 1Password insiste en que los clientes no tienen que cambiar nada en su cuenta. La diferencia con el caso de LastPass en 2022 es clara: allí sí se llevaron copias de las bóvedas cifradas.

## Qué ha hecho 1Password

La compañía ha desactivado la cuenta de GitHub comprometida, ha revocado el token robado, ha restaurado versiones limpias del servicio afectado y ha rotado credenciales internas. También ha reforzado los controles de GitHub, del CI/CD y de los equipos de sus empleados, y ha contratado a expertos independientes para la investigación.

Un cambio visible: los códigos de verificación de invitaciones y recuperación pasan de seis dígitos a diez caracteres alfanuméricos, lo que hace mucho más difícil adivinarlos aunque alguien tenga los datos robados.

## El riesgo real: phishing muy creíble

Con nombres, correos y fechas de uso de cuenta en manos de un atacante, lo previsible es una campaña de correos o mensajes falsos haciéndose pasar por 1Password. Un correo que dice "detectamos un inicio de sesión el 14 de octubre" resulta mucho más convincente si la fecha es real.

## Cómo protegerte si usas 1Password

- **No hace falta cambiar la contraseña maestra ni la Secret Key**, según la empresa, aunque hacerlo no perjudica.
- **Desconfía de invitaciones o solicitudes de recuperación de cuenta que no hayas pedido**, lleguen por correo, SMS o llamada.
- **1Password nunca te pedirá tu contraseña maestra ni tu Secret Key.** Si alguien lo hace, es una estafa.
- **Entra siempre desde la app o tecleando la dirección oficial**, no desde enlaces de correos. Repasa nuestra guía para [detectar correos de phishing](/como-detectar-phishing/).
- **Activa la verificación en dos pasos** en 1Password y en tus cuentas importantes, como explicamos en [cómo proteger tus cuentas con contraseñas y 2FA](/proteger-cuentas-contrasenas-2fa/).
- Si notas algo raro, la empresa pide escribir a su soporte oficial.

Este incidente no cambia la recomendación general: un gestor de contraseñas sigue siendo mucho más seguro que reutilizar claves. Si estás valorando alternativas, tienes nuestra comparativa de los [mejores gestores de contraseñas](/mejores-gestores-de-contrasenas/).

## Fuentes

- [1Password: Update on a security incident involving 1Password's backend systems](https://1password.com/blog/update-on-nov-2026-security-incident)
- [BleepingComputer: 1Password customer data stolen after employee GitHub account breach](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/)
- [Hackread: 1Password says attacker copied customer account data, vaults unaffected](https://hackread.com/1password-attacker-copied-customer-account-data-vaults/)
