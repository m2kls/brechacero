---
title: "Hackeo de Todoist: roban correos y contraseñas cifradas del 6 % de usuarios"
description: "Hackeo de Todoist: un atacante robó correos y hashes de contraseñas antiguos del 6 % de usuarios, y tokens y datos de Outlook. Qué hacer si te llega el aviso."
date: 2026-11-26T02:55:00+01:00
category: noticias
tags: [Todoist, filtración, contraseñas, SHA1, Outlook, Slack, credenciales robadas]
author: Redacción
photo: "File:Todoist logo.png"
imageAlt: "Logotipo de Todoist, la aplicación de tareas que ha sufrido un hackeo"
---

El hackeo de Todoist, una de las aplicaciones de listas de tareas más usadas del mundo, ha dejado expuestos datos de aproximadamente el **6 % de sus usuarios**. La empresa, Doist, ha confirmado que un atacante entró en sus sistemas de producción los días 22 y 23 de noviembre y descargó direcciones de correo, fechas de creación de cuenta y hashes de contraseñas calculados con un método antiguo. En un grupo mucho más pequeño de cuentas también se llevó tokens de integración, buscó claves dentro de las tareas y leyó parte del correo de Outlook conectado a la aplicación.

## Cómo fue el hackeo de Todoist

Según el aviso oficial publicado por la compañía, todo empezó con una credencial robada de su sistema de control de versiones, el lugar donde se guarda el código. Desde las 14:04 (hora UTC) del 22 de noviembre, el atacante modificó flujos automatizados en tres repositorios y consiguió más credenciales. Pudo leer código fuente, aunque Todoist asegura que no se modificó ni una línea de la aplicación.

La madrugada del 23, una de esas credenciales le permitió cambiar la configuración de acceso de un empleado y entrar en la infraestructura en la nube con su cuenta de trabajo. Creó cuentas adicionales para no perder el acceso y, a partir de las 9:08, empezó a consultar las bases de datos de producción. Entre las 12:45 y las 12:51 exportó los registros de cuentas. Los sistemas de monitorización detectaron una cuenta de administrador inesperada a las 17:01 y, en menos de una hora, el equipo cortó el acceso.

La empresa todavía no sabe cómo se robó la primera credencial. Su principal hipótesis, sin confirmar, es que el dispositivo de un empleado estaba comprometido.

## ¿Qué datos se han robado en Todoist?

El aviso divide a los afectados en cuatro grupos, con poco solapamiento entre ellos:

- **Alrededor del 6 % de los usuarios**: correo electrónico, fecha de alta y hash de la contraseña. Son cuentas antiguas cuya contraseña seguía guardada con SHA1 con sal, un método que Todoist dejó de usar hace más de diez años pero que mantenía para quien nunca cambió la clave. La empresa reconoce que ese sistema es vulnerable a ataques de adivinación de contraseñas y que "debería haberlo retirado antes". No ha encontrado inicios de sesión del atacante en estas cuentas.
- **Un 0,003 %**: tokens de la API de Todoist y de la integración con Slack. En parte de esos casos, el atacante usó el token para leer proyectos, tareas y comentarios.
- **Un 0,001 %**: búsquedas en tareas, comentarios y nombres de adjuntos de cosas que parecieran credenciales, como frases de recuperación de monederos de criptomonedas, claves privadas, contraseñas o claves de servicios en la nube.
- **Otro 0,001 %**: usuarios del complemento Todoist para Outlook. Con las credenciales robadas del complemento, el atacante vio asuntos, remitentes, los primeros 255 caracteres de algunos mensajes y los nombres de los adjuntos, y lanzó búsquedas por palabras relacionadas con contraseñas y servicios.

Las cuentas que entran con Google o Apple no han visto afectadas sus contraseñas de esos servicios.

## Qué ha hecho la empresa

Todoist desactivó las contraseñas de las cuentas afectadas, revocó sus tokens de API, desconectó las aplicaciones enlazadas y cerró las sesiones abiertas. También retiró el complemento para Outlook el 24 de noviembre, revocó los tokens de Slack, rotó sus credenciales internas y endureció los permisos de sus automatizaciones. El consejero delegado, Amir Salihefendić, pidió disculpas públicamente. "Proteger tu información es responsabilidad nuestra y hemos fallado", dice el comunicado.

Los avisos a los afectados se enviaron entre el 24 y el 25 de noviembre. Si no has recibido ninguno, según la empresa no tienes que hacer nada.

## Cómo protegerte si usas Todoist

1. **Revisa tu correo** buscando el aviso oficial, que llega desde `no-reply@notify.todoist.com`. Todoist no te pedirá la contraseña ni que instales nada: cualquier correo que lo haga es **phishing** aprovechando la noticia. Repasa [cómo detectar un correo de phishing](/como-detectar-phishing/).
2. **Cambia la contraseña** si te lo piden. Si la usabas en otros servicios, cámbiala también allí: un hash SHA1 puede romperse con relativa facilidad si la clave era corta o común. Puedes [comprobar si tu contraseña ha sido filtrada](/saber-si-mi-contrasena-ha-sido-filtrada/).
3. **Activa la verificación en dos pasos** en Todoist y en tus cuentas importantes. Aquí tienes [cómo proteger tus cuentas con contraseñas fuertes y 2FA](/proteger-cuentas-contrasenas-2fa/).
4. **Revoca cualquier secreto** que guardaras en tareas o comentarios (claves de API, tokens, frases de recuperación). Borrar la tarea no sirve: hay que anular la clave en el servicio correspondiente y crear otra.
5. Si usabas scripts con la API, actualiza el token; y si tenías conectado Slack u Outlook, vuelve a enlazarlos.

La lección va más allá de Todoist: una aplicación de tareas acaba guardando información muy sensible, y un [gestor de contraseñas](/mejores-gestores-de-contrasenas/) es mucho mejor sitio para claves y frases de recuperación.

## Fuentes

- [Todoist: Security incident in November 2026 (aviso oficial)](https://www.todoist.com/help/todoist/get-started/security-incident-in-november-2026-cG0EIACNU)
- [TechCrunch: Todoist confirms 6% of customers' details were stolen in data breach](https://techcrunch.com/2026/11/25/todoist-confirms-6-of-customers-details-were-stolen-in-data-breach/)
- [tbreak: Todoist breach exposed password hashes for 6% of users](https://tbreak.com/todoist-breach-password-hashes/)
