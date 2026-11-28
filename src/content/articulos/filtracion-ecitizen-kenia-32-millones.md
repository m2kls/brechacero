---
title: "Filtración de eCitizen en Kenia: publican datos de 32 millones de personas"
description: "Los atacantes de eCitizen, el portal de trámites de Kenia, empiezan a difundir documentos de identidad, huellas y PIN fiscales de hasta 32 millones de personas."
date: 2026-11-28T10:56:00+01:00
category: privacidad
tags: [Kenia, eCitizen, filtración, ByteToBreach, documentos de identidad, robo de identidad]
author: Redacción
photo: "File:Nyayo House (2123739963).jpg"
imageAlt: "Nyayo House en Nairobi, sede del Departamento de Inmigración de Kenia, responsable de eCitizen"
---

La **filtración de eCitizen**, el portal desde el que los kenianos hacen casi cualquier trámite con su Administración, ha pasado de ser una reivindicación sin confirmar a un problema muy real. Según la revisión de los archivos publicados que ha hecho el diario keniano *Nation*, los atacantes tuvieron acceso a datos de identidad de **32.128.394 personas**, y desde este fin de semana han empezado a difundir parte de ellos en foros de la web oscura. Kenia tiene unos 55 millones de habitantes, así que hablamos de la mayoría de su población adulta.

El Gobierno keniano todavía no ha confirmado esa cifra ni que haya habido un acceso indebido, pero ya ha abierto una investigación forense y ha pedido a los ciudadanos que cambien sus contraseñas.

## Qué ha pasado con eCitizen

Todo empezó el **22 de noviembre**, cuando un actor que firma como **ByteToBreach** publicó en un foro clandestino un mensaje firmado con PGP en el que aseguraba haber robado unos **740 GB** de la plataforma. Según su propio reparto, serían unos 600 GB de documentos de verificación de identidad (KYC), 100 GB de registros de bases de datos y 40 GB de código fuente del portal. El atacante afirma que entró a través de un fallo en la subida de archivos, que le permitió instalar una *webshell*, y que llegó a comprometer los sistemas de identidad federada y OAuth con los que eCitizen da acceso a otros servicios públicos.

El medio ITWeb Africa señaló que algunos archivos tienen marcas de tiempo del 14 y 15 de noviembre, lo que apuntaría a que la intrusión se produjo una semana antes del anuncio. La firma de inteligencia VECERT, que detectó la publicación, la catalogó entonces como "presunta y no confirmada".

Lo que ha cambiado ahora es que los datos han empezado a circular. *Nation* asegura que en los archivos aparecen **números de documento nacional de identidad, copias de pasaportes, fechas de nacimiento, huellas dactilares y PIN de la Agencia Tributaria keniana (KRA)**. También figuran números de identificación sanitaria digital de la Autoridad de Salud Social (SHA), aunque eso no significa que se hayan llevado historiales médicos. No todos los registros se han publicado todavía.

## Qué dice el Gobierno de Kenia

El Departamento de Estado de Inmigración y Servicios al Ciudadano, dependiente del Ministerio del Interior, reconoció el 24 y 25 de noviembre que estaba al tanto de las informaciones y que sus equipos técnicos y de seguridad trabajan con otras agencias en una investigación forense. "Proteger los datos personales confiados al Departamento de Estado es una prioridad y se informará al público cuando concluyan las investigaciones", señaló en su comunicado.

Las autoridades insisten en que eCitizen sigue funcionando con normalidad. *Nation* no ha encontrado pruebas de que la Autoridad de Salud Social, la policía judicial (DCI) o el Servicio Nacional de Policía, que el atacante mencionaba como posibles afectados, hayan sido comprometidos.

Queda en el aire si el Gobierno ha avisado a la Oficina del Comisionado de Protección de Datos (ODPC). La Ley de Protección de Datos de Kenia obliga a notificar una brecha en un plazo de 72 horas cuando existe un riesgo real para los afectados, y los responsables no han aclarado si lo han hecho. No es el primer susto del portal: en julio de 2023 sufrió un ataque de denegación de servicio que lo dejó fuera de juego varios días, aunque entonces el Gobierno aseguró que no se habían tocado datos.

## Por qué es tan grave esta filtración

eCitizen ha crecido muchísimo en poco tiempo: según el Gobierno, ha pasado de unos 500 servicios en 2022 a unos 24.000 en 2026, desde pasaportes y certificados de buena conducta hasta registros de empresas o pagos de tasas. Eso lo convierte en un punto único de fallo. Una contraseña se puede cambiar; un número de identidad, una fecha de nacimiento o una huella dactilar no.

Con esos datos, los delincuentes pueden suplantar a una persona para pedir créditos, abrir líneas de móvil o cuentas de dinero móvil (muy extendidas en Kenia a través de M-PESA) y, sobre todo, montar estafas muy creíbles. Un estafador que te llama sabiendo tu número de identidad y tu fecha de nacimiento parece mucho más legítimo. Es el mismo patrón que vimos con la reciente [filtración del registro civil CPR de Dinamarca](/filtracion-registro-civil-dinamarca-cpr/): cuando cae una base de datos estatal, el daño dura años.

## ¿Estoy afectado? Cómo protegerse

Si tienes cuenta en eCitizen, lo más prudente es dar por hecho que tus datos pueden estar expuestos. Las recomendaciones del propio Gobierno keniano y de los expertos son:

- **Cambia la contraseña de eCitizen** y la de cualquier otro servicio en el que la reutilizaras. Si puedes, activa la verificación en dos pasos; te lo explicamos en nuestra guía para [proteger tus cuentas con contraseñas seguras y 2FA](/proteger-cuentas-contrasenas-2fa/).
- **Entra siempre escribiendo la dirección del portal** en el navegador, nunca desde enlaces que lleguen por SMS, correo o WhatsApp.
- **No compartas nunca códigos de verificación ni el PIN de M-PESA**, aunque quien te llame conozca tus datos personales.
- Desconfía de llamadas y mensajes que se presenten como eCitizen, la KRA o la policía y que metan prisa. Repasa las señales típicas en nuestra guía sobre [cómo detectar el phishing](/como-detectar-phishing/).
- Vigila movimientos extraños en tus cuentas bancarias y de dinero móvil, y denuncia cualquier actividad sospechosa.

Para las instituciones que usan eCitizen como sistema de inicio de sesión, los expertos recomiendan revisar los registros de acceso en busca de tokens usados de forma anómala, ya que el atacante asegura haber comprometido la parte de OAuth.

Conviene recordar que cambiar la contraseña no deshace la exposición de un documento de identidad. Si tus datos aparecen en la filtración, la vigilancia frente al robo de identidad tendrá que mantenerse en el tiempo.

## Fuentes

- [Kenya eCitizen Data Breach – Hackers Reportedly Leak Identity Records of 32 Million Kenyans (Cyber Security News)](https://cybersecuritynews.com/kenya-ecitizen-data-breach)
- [Kenyan Government is investigating unverified claims of a 740GB eCitizen data breach (HapaKenya)](https://hapakenya.com/2026/11/25/kenyan-government-is-investigating-unverified-claims-of-a-740gb-ecitizen-data-breach/)
- [Kenya probes 740GB eCitizen data breach claim (Biometric Update)](https://www.biometricupdate.com/202611/kenya-probes-740gb-ecitizen-data-breach-claim)
- [Kenya's eCitizen platform faces fresh security concerns (TechTrends KE)](https://techtrendske.co.ke/2026/11/25/ecitizen-data-breach/)
