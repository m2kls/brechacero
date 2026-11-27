---
title: "Hackeo de pCloud Pass: el gestor de contraseñas confirma un ataque"
description: "pCloud confirma el hackeo de su gestor de contraseñas pCloud Pass tras una oleada de avisos de inicio de sesión sospechosos. Qué se ha expuesto y qué hacer ahora."
date: 2026-11-27T20:50:00+01:00
category: noticias
tags: [pCloud, pCloud Pass, gestor de contraseñas, filtración, phishing, Suiza]
author: Redacción
photo: "File:Reading_mail_at_night_(Unsplash).jpg"
imageAlt: "Persona leyendo el correo de noche, como los usuarios que recibieron avisos de acceso del gestor pCloud Pass"
---

El hackeo de pCloud Pass, el gestor de contraseñas de la empresa suiza de almacenamiento en la nube pCloud, está confirmado. Durante la noche del 26 al 27 de noviembre, muchos usuarios recibieron correos que avisaban de un inicio de sesión desde un "dispositivo nuevo" que no reconocían. Horas después, la compañía admitió en su cuenta oficial de Reddit que había sufrido un ataque contra pCloud Pass, que lo había "contenido rápidamente" y que se habían expuesto las direcciones de correo de un número pequeño de usuarios. Según pCloud, las contraseñas guardadas en las bóvedas siguen a salvo.

Es el segundo incidente en un gestor de contraseñas conocido en pocos días, después del [hackeo de 1Password a través del GitHub de un empleado](/hackeo-1password-github-datos-clientes/), y vuelve a poner el foco en los servicios que custodian las credenciales más sensibles.

## Qué ha pasado en pCloud Pass

Las primeras pistas llegaron de los propios usuarios. Varios publicaron en foros y redes que habían recibido avisos de acceso legítimos, enviados por pCloud, en los que aparecía un dispositivo llamado "pd" y direcciones IP situadas en Luxemburgo. Según recogen BleepingComputer y el medio francés Clubic, el botón del correo para revisar la configuración apuntaba a un dominio de pruebas de la propia empresa, algo poco habitual en un aviso dirigido a clientes.

Algunos detalles hicieron sospechar que no era una simple campaña de relleno de credenciales (probar contraseñas filtradas en otros servicios): recibieron el aviso personas con la verificación en dos pasos activada, clientes que solo usan el almacenamiento y no el gestor, e incluso direcciones de cuentas ya borradas. Clubic informó además de que el dominio de pCloud tuvo problemas con su correo durante la mañana del 27.

La empresa explicó después que la intrusión se limitó a pCloud Pass y que su servicio de almacenamiento pCloud Drive no se ha visto afectado. También aseguró que el contenido de las bóvedas, contraseñas y notas, no está comprometido gracias al cifrado de conocimiento cero: los datos se cifran en el dispositivo del usuario con su contraseña maestra, que la empresa no conoce.

## ¿Estoy afectado por el hackeo de pCloud?

pCloud no ha dicho cuántas cuentas se han visto afectadas, cómo entró el atacante ni por qué los avisos mostraban direcciones e infraestructura internas. Tampoco ha aclarado si el intruso llegó a descargar copias cifradas de bóvedas. Si usas pCloud Pass y recibiste uno de esos correos, da por hecho que tu dirección está en manos del atacante.

El riesgo inmediato es el phishing. Con una lista de correos de usuarios reales de un gestor de contraseñas, es fácil enviar mensajes que imiten a pCloud y pidan "verificar la cuenta", restablecer la contraseña maestra o introducir las palabras de recuperación. La propia empresa ha recordado que nunca pedirá la contraseña maestra ni las palabras de recuperación por correo, teléfono o chat.

## Qué hacer si usas pCloud Pass

- **No pulses enlaces de correos que digan venir de pCloud.** Abre la aplicación, la extensión del navegador o escribe pcloud.com a mano.
- **Revisa las sesiones activas** en los ajustes de seguridad de pCloud Pass y cierra cualquier dispositivo que no reconozcas, en especial uno llamado "pd".
- **Cambia la contraseña maestra** si viste un acceso extraño o si es corta o la usas en otro sitio. Una frase larga, de cuatro o cinco palabras, es mucho más difícil de romper.
- **Activa la verificación en dos pasos con app o llave física**, no solo por SMS. Te lo explicamos en nuestra guía para [proteger tus cuentas con contraseñas fuertes y 2FA](/proteger-cuentas-contrasenas-2fa/).
- **Guarda las palabras de recuperación fuera de línea** y desconfía de cualquier "soporte de pCloud" que te contacte sin que lo hayas pedido.

Si después de esto te planteas cambiar de servicio, en nuestra comparativa de los [mejores gestores de contraseñas](/mejores-gestores-de-contrasenas/) explicamos qué mirar: cifrado de extremo a extremo auditado, historial de incidentes y transparencia cuando algo sale mal. Ningún gestor es invulnerable; lo que marca la diferencia es que una brecha en la empresa no permita leer tus contraseñas.

## Fuentes

- [BleepingComputer: pCloud confirms password manager hack after suspicious login alerts](https://www.bleepingcomputer.com/news/security/pcloud-confirms-password-manager-hack-after-suspicious-login-alerts/)
- [Clubic: pCloud Pass a bien été victime d'une cyberattaque](https://www.clubic.com/actualite-641488-pcloud-pass-a-bien-ete-victime-d-une-cyberattaque-l-editeur-assure-que-vos-mots-de-passe-sont-en-securite.html)
- [Clubic: connexions suspectes à pCloud Pass](https://www.clubic.com/actualite-641377-connexions-suspectes-a-pcloud-pass-mails-rejetes-que-se-passe-t-il-chez-pcloud.html)
- [Dark Web Informer: pCloud confirms cyberattack on its password manager](https://darkwebinformer.com/pcloud-confirms-cyberattack-on-its-password-manager/)
