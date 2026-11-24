---
title: "Cómo proteger tus cuentas: contraseñas seguras, gestores y 2FA"
description: "Guía práctica para proteger tus cuentas: cómo crear contraseñas seguras, por qué usar un gestor de contraseñas y cómo activar la verificación en dos pasos."
date: 2026-11-17
category: guias
tags: ['contraseñas', '2FA', 'gestores']
author: Redacción
featured: false
imageCredit: "Ilustración: Brecha Cero"
video: "oFzKEogQEsI"
videoTitle: "Cómo proteger tu cuenta: activa la verificación en dos pasos"
videoSource: "Oficina de Seguridad del Internauta (INCIBE)"
---


La mayoría de cuentas robadas no caen por un ataque sofisticado de película. Caen por algo mucho más mundano: una contraseña débil, reutilizada o filtrada. Tres medidas sencillas se lo ponen muy difícil a cualquier atacante: contraseñas robustas, un gestor de contraseñas y la verificación en dos pasos.

## Por qué roban las cuentas

Entender cómo atacan te ayuda a entender por qué funcionan las defensas:

- **Filtraciones de datos:** una web donde te registraste sufre un robo y tu correo y contraseña acaban publicados.
- **Credential stuffing (relleno de credenciales):** los atacantes prueban automáticamente esas combinaciones filtradas en otros servicios (correo, redes sociales, banco). Si reutilizas contraseñas, caen todas a la vez.
- **Fuerza bruta y diccionario:** probar contraseñas comunes ("123456", "contraseña", "Madrid2024") hasta acertar.
- **Phishing:** engañarte para que escribas tu contraseña en una web falsa. Lo explicamos en [Phishing: cómo detectarlo](/como-detectar-phishing/).

## 1. Contraseñas seguras: qué funciona de verdad

Olvida las reglas de "una mayúscula, un número y un símbolo". Lo que más importa es la longitud y que sea única.

**Una buena contraseña:**
- Tiene al menos 14-16 caracteres.
- **No se repite** en ningún otro servicio.
- No contiene datos personales (nombre, fecha de nacimiento, mascota, equipo de fútbol).

**Truco de la frase de contraseña:** une varias palabras aleatorias, por ejemplo `tortuga-lámpara-viernes-cobre`. Es larga, fácil de recordar y muy difícil de adivinar. Úsala para las pocas contraseñas que tienes que memorizar (como la maestra de tu gestor).

> 💡 Para comprobar si tu correo aparece en alguna filtración conocida, puedes usar el servicio gratuito Have I Been Pwned.

## 2. Gestor de contraseñas: la herramienta que lo cambia todo

Nadie puede recordar 80 contraseñas largas y distintas. Para eso existen los gestores de contraseñas: una caja fuerte cifrada donde guardas todas tus claves y solo tienes que recordar una, la contraseña maestra.

**Ventajas:**
- Generan contraseñas largas y aleatorias por ti.
- Las rellenan automáticamente en webs y apps.
- **Protegen contra el phishing**: si la web es falsa, el gestor no reconoce el dominio y no rellena nada. Es una señal de alarma.
- Te avisan si alguna de tus contraseñas ha aparecido en una filtración.
- Se sincronizan entre móvil y ordenador.

**Tipos de gestores:**
- **Integrados en el navegador o el sistema** (Google, Apple, Microsoft): gratuitos y cómodos, buena opción para empezar.
- **Gestores dedicados** como Bitwarden (código abierto, con plan gratuito muy completo), 1Password o Proton Pass: más funciones, multiplataforma y opciones para compartir en familia.
- **Gestores locales** como KeePassXC: la base de datos se guarda en tu dispositivo; ideal si prefieres no depender de la nube, aunque exige más gestión.

> ⚠️ Tu contraseña maestra debe ser muy fuerte y única, y conviene activar la verificación en dos pasos también en el gestor.

## 3. Verificación en dos pasos (2FA)

La verificación en dos pasos añade una segunda prueba además de la contraseña. Así, aunque alguien consiga tu clave, no puede entrar sin ese segundo factor.

### Tipos de 2FA, de menos a más seguro

1. **SMS:** mejor que nada, pero vulnerable al robo del número de teléfono (*SIM swapping*) y al phishing.
2. **Aplicaciones de autenticación** (Google Authenticator, Microsoft Authenticator, Aegis, Ente Auth…): generan códigos de 6 dígitos que cambian cada 30 segundos. Mucho más seguras que el SMS.
3. **Notificaciones push** en la app del servicio: cómodas, pero no aceptes nunca una solicitud que no hayas iniciado tú.
4. **Llaves de seguridad físicas (FIDO2/U2F)**, como YubiKey: un pequeño dispositivo USB o NFC. Son resistentes al phishing y la opción más segura para cuentas críticas.
5. **Passkeys (llaves de acceso):** el sustituto moderno de las contraseñas. Usan tu huella, cara o PIN del dispositivo y no pueden ser robadas por una web falsa. Si un servicio te las ofrece, actívalas.

### Por dónde empezar

Activa la 2FA primero en estas cuentas, por orden de importancia:

1. **Correo electrónico principal** (es la llave para recuperar todas las demás).
2. Banca y pagos (PayPal, Bizum, etc.).
3. Gestor de contraseñas.
4. Redes sociales y WhatsApp (activa el PIN de verificación en dos pasos).
5. Cuentas de compras online y almacenamiento en la nube.

> 💡 Al activar la 2FA, guarda los códigos de recuperación en un lugar seguro (por ejemplo, dentro de tu gestor o impresos en casa). Si pierdes el móvil, son tu salvavidas.

## Plan de 30 minutos para blindar tus cuentas

1. Instala un gestor de contraseñas y crea una contraseña maestra fuerte (5 min).
2. Activa la 2FA en tu correo principal con una app de autenticación (5 min).
3. Comprueba tu correo en Have I Been Pwned (2 min).
4. Cambia las contraseñas de las cuentas filtradas o reutilizadas, guardándolas en el gestor (15 min).
5. Activa la verificación en dos pasos de WhatsApp (3 min).

## Preguntas frecuentes

**¿No es peligroso guardar todas las contraseñas en un solo sitio?**
Los gestores serios cifran los datos de forma que ni la propia empresa puede leerlos. El riesgo de reutilizar contraseñas es mucho mayor que el de usar un buen gestor con una contraseña maestra fuerte y 2FA.

**¿Cada cuánto debo cambiar mis contraseñas?**
Las recomendaciones actuales (por ejemplo, del NIST) indican que no hace falta cambiarlas periódicamente si son fuertes y únicas. Cámbialas cuando haya una filtración o sospecha de acceso.

**¿Qué pasa si pierdo el móvil con la app de autenticación?**
Por eso son importantes los códigos de recuperación. Algunas apps permiten también copias de seguridad cifradas.


Una contraseña larga y única, un gestor que las recuerde por ti y la verificación en dos pasos en tus cuentas importantes: con esas tres capas evitas la gran mayoría de robos de cuentas. Dedícale media hora hoy y ahorrarás muchos disgustos mañana.

*Este artículo tiene fines divulgativos. Algunos enlaces pueden ser de afiliado: si compras a través de ellos, recibimos una pequeña comisión sin coste adicional para ti.*
