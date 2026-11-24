---
title: "Fallo en Microsoft Entra Connect Health expone datos de administradores"
description: "Un fallo en Microsoft Entra Connect Health permitió leer correos de administradores, dominios e IDs de inquilinos. Qué se expuso y qué deben revisar las empresas."
date: 2026-11-24T19:00:00+01:00
category: vulnerabilidades
tags: [Microsoft, Entra ID, Entra Connect Health, Microsoft 365, filtración de datos, phishing]
author: Redacción
photo: "File:Microsoft building 17 front door.jpg"
imageAlt: "Entrada de un edificio del campus de Microsoft en Redmond"
---

Un fallo en Microsoft Entra Connect Health, el servicio que vigila la sincronización entre el Directorio Activo local de las empresas y Entra ID (el antiguo Azure AD), permitió a terceros leer información de los inquilinos de Microsoft 365 durante casi cuatro meses. Microsoft ha empezado a avisar a los clientes afectados desde el 20 de noviembre: se expusieron correos de administradores, identificadores de inquilino y dominios, aunque la compañía insiste en que no salieron contraseñas ni tokens. Para cualquier empresa que use Microsoft 365 con identidades híbridas, el riesgo inmediato es un aumento del phishing dirigido a sus administradores.

## Qué ha pasado con Entra Connect Health

Según la notificación que Microsoft ha enviado a través de Azure Service Health, y que varios administradores han compartido en foros como r/sysadmin, la función vulnerable estaba en una API alojada por la propia Microsoft. El fallo se introdujo el 23 de julio de 2026, la empresa lo detectó el 9 de noviembre y desplegó la corrección en sus servidores el 19 de noviembre. Un día después concluyó que había habido acceso no autorizado de solo lectura a metadatos de los inquilinos.

Microsoft afirma que no hubo cambios de configuración no autorizados. Al tratarse de un servicio en la nube, los clientes no tienen que instalar ningún parche: la corrección ya está aplicada. Lo que la compañía no ha dicho es cuántos inquilinos se han visto afectados ni quién accedió a los datos.

## ¿Qué datos se expusieron?

Con la información publicada por Microsoft y analizada por la firma Field Effect, los datos que pudieron leerse son:

- Direcciones de correo de los administradores y de los contactos técnicos del inquilino.
- Identificador y nombre del inquilino, y los dominios asociados.
- Estado de la sincronización y de la incorporación a Connect Health, información de licencias y región.
- Un certificado de un servicio interno de Microsoft que ya estaba retirado desde 2024.

Microsoft asegura que no se expusieron contraseñas, hashes de contraseñas, tokens de acceso, claves criptográficas activas, datos de suscripciones de Azure ni información de la infraestructura del Directorio Activo.

## Por qué importa aunque no haya contraseñas

Una lista de correos de administradores asociada a su dominio y a su inquilino es justo lo que necesita un atacante para preparar campañas de phishing muy creíbles: correos que imitan avisos de Microsoft, solicitudes de "verificar" la cuenta o falsas alertas de seguridad dirigidas a las personas con más permisos de la empresa. Si una de esas cuentas cae, el atacante tiene las llaves de todo el entorno de Microsoft 365.

Por eso los expertos coinciden en que el peligro no está en lo que se ha filtrado, sino en lo que se puede hacer después con ello. Ya explicamos en [phishing con IA](/phishing-con-ia/) por qué estos correos son cada vez más difíciles de distinguir.

## Qué deben revisar las empresas afectadas

Microsoft y los analistas consultados recomiendan:

1. **Comprobar el aviso en Azure Service Health**, no a través de enlaces recibidos por correo. Los propios atacantes pueden imitar la notificación.
2. **Ejecutar los scripts de revisión de solo lectura** que Microsoft ha publicado para ver qué contactos administrativos y técnicos tenía el inquilino y compararlos con los actuales.
3. **Exigir MFA resistente al phishing** (llaves FIDO2, Windows Hello para Empresas o certificados) en todas las cuentas con privilegios. Los códigos por SMS no bastan; lo contamos en nuestra guía sobre [cómo proteger tus cuentas con 2FA](/proteger-cuentas-contrasenas-2fa/).
4. **Reducir los permisos permanentes** con Privileged Identity Management, para que los administradores solo tengan privilegios cuando los necesitan.
5. **Revisar los registros** de inicio de sesión y de auditoría de Entra y los registros de actividad de Azure en busca de accesos raros desde julio.
6. **Avisar a los administradores y al personal de soporte** de que pueden recibir correos o llamadas que suplanten a Microsoft. Nuestra guía para [detectar phishing](/como-detectar-phishing/) sirve como repaso rápido.

## Un problema que no depende del cliente

Este caso se suma a la lista de incidentes en servicios en la nube en los que el cliente no puede hacer nada para evitar el fallo, solo reducir el daño. La lección práctica es la de siempre: tratar las direcciones de los administradores como información sensible, no usarlas para el día a día y blindar esas cuentas con la autenticación más fuerte disponible.

## Fuentes

- [Field Effect: Microsoft reports Entra Connect Health metadata exposure](https://fieldeffect.com/blog/microsoft-entra-connect-exposure)
- [Security Affairs: Microsoft Entra Connect Health breach exposes tenant metadata and admin details](https://securityaffairs.com/203820/data-breach/microsoft-entra-connect-health-breach-exposes-tenant-metadata-and-admin-details.html)
- [Notificación de Microsoft compartida por administradores en r/sysadmin](https://www.reddit.com/r/sysadmin/comments/1y1of2u/important_security_notification_regarding/)
