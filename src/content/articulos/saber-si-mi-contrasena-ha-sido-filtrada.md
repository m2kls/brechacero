---
title: "Cómo saber si tu contraseña ha sido filtrada (y qué hacer si es así)"
description: "Comprueba de forma segura si tu correo o tus contraseñas aparecen en filtraciones con Have I Been Pwned, tu navegador o tu gestor, y cómo reaccionar."
date: 2026-11-23
category: privacidad
tags: [contraseñas, filtraciones, Have I Been Pwned, privacidad]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

Cada año se filtran millones de contraseñas tras ataques a webs y servicios. Lo más probable es que alguna de las tuyas esté en una de esas listas sin que lo sepas. Comprobarlo es gratis, rápido y no obliga a exponer tu contraseña.

## Paso 1: comprueba tu correo en Have I Been Pwned

**Have I Been Pwned** (haveibeenpwned.com) es un servicio gratuito creado por el investigador de seguridad Troy Hunt que recopila filtraciones públicas.

1. Entra en la web y escribe tu dirección de correo.
2. Te dirá en qué filtraciones aparece y qué tipo de datos se expusieron en cada una (correo, contraseña, teléfono, dirección...).
3. Puedes suscribirte para recibir un aviso si tu correo aparece en futuras filtraciones.

> 💡 Que tu correo aparezca no significa que te hayan entrado en la cuenta. Fíjate en si la filtración incluía contraseñas y en qué servicio fue.

## Paso 2: comprueba tus contraseñas sin revelarlas

Además del correo, conviene saber si una contraseña concreta circula en listas filtradas. Tienes tres formas:

### Con tu navegador
- **Google Chrome**: *Configuración › Autocompletar y contraseñas › Gestor de contraseñas › Revisión*.
- **Firefox**: en *about:logins* avisa de contraseñas expuestas en filtraciones.
- **Safari / iPhone**: *Ajustes › Contraseñas › Recomendaciones de seguridad* (o la app Contraseñas).

### Con tu gestor de contraseñas
La mayoría de gestores (Bitwarden, 1Password, Proton Pass...) incluyen un informe de contraseñas expuestas, débiles o reutilizadas. Es la opción más cómoda porque revisa todas de golpe.

### Con Pwned Passwords
La sección *Passwords* de Have I Been Pwned te dice cuántas veces aparece una contraseña en filtraciones.

**¿No es peligroso escribirla ahí?** El servicio usa una técnica llamada *k-anonimato*: tu navegador calcula un resumen (hash) de la contraseña y solo envía los 5 primeros caracteres de ese resumen. El servidor devuelve todos los resúmenes que empiezan igual y la comparación final se hace en tu equipo. Tu contraseña nunca sale de tu ordenador. Aun así, si prefieres no escribirla en ninguna web, usa el navegador o el gestor.

## Paso 3: qué hacer si aparece

**Si se filtró una contraseña:**

1. **Cámbiala ya** en ese servicio.
2. **Cámbiala en cualquier otro sitio donde la hayas reutilizado.** Este es el paso más importante: los atacantes prueban automáticamente las contraseñas filtradas en otros servicios (*credential stuffing*).
3. Usa contraseñas largas y únicas, generadas y guardadas en un gestor.
4. Activa la [verificación en dos pasos](/proteger-cuentas-contrasenas-2fa/), sobre todo en tu correo.

**Si se filtraron otros datos (teléfono, dirección, DNI):**

- No se pueden "cambiar", pero sí puedes estar alerta: es muy probable que recibas phishing más creíble, que use tu nombre o datos reales.
- Revisa los movimientos de tu banco y activa las notificaciones de pagos.
- Si se filtró el DNI o datos bancarios, sigue los pasos de nuestra guía [tus datos aparecen en una filtración: qué hacer](/datos-en-filtracion-que-hacer/).

## Señales de que alguien ya ha usado tu contraseña

- Avisos de inicio de sesión desde dispositivos o países que no reconoces.
- Correos de "has cambiado tu contraseña" o "has añadido un nuevo correo" que no has pedido.
- Mensajes enviados desde tus redes sociales que no escribiste tú.
- Compras o suscripciones que no reconoces.

Si ves algo así, cambia la contraseña desde un dispositivo de confianza, cierra todas las sesiones abiertas (casi todos los servicios tienen esa opción en *Seguridad*) y revisa que no hayan cambiado tu correo o teléfono de recuperación.

## Cuidado con las estafas que se aprovechan de esto

Los delincuentes también usan el miedo a las filtraciones:

- Correos que dicen "tenemos tu contraseña y un vídeo tuyo, paga en bitcoin". Es una sextorsión genérica: a veces incluyen una contraseña antigua real sacada de una filtración para asustarte. No pagues. Cambia esa contraseña si aún la usas y denuncia.
- Webs o "servicios" que te piden tu contraseña para "comprobar si está filtrada". Usa solo los métodos de este artículo.

Si tienes dudas, en España puedes llamar gratis al 017, la línea de ayuda en ciberseguridad de INCIBE.

## Preguntas frecuentes

**¿Have I Been Pwned es fiable?**
Sí. Es un servicio muy conocido y usado en el sector, y lo utilizan incluso gestores de contraseñas y navegadores para sus propias comprobaciones.

**¿Cada cuánto debería comprobarlo?**
Suscríbete a los avisos de Have I Been Pwned y deja que tu gestor de contraseñas revise automáticamente. Así no tienes que acordarte.

**Mi correo aparece en muchas filtraciones, ¿debo cambiarlo?**
No necesariamente. Lo importante es que cada servicio tenga una contraseña distinta y que tu correo tenga verificación en dos pasos.
