---
title: "Hackeo a Radware: expuestas claves de nube de clientes de su Cloud WAF"
description: "Una API interna de Radware quedó abierta en internet sin contraseña y expuso claves de AWS, Azure y SFTP de clientes de su Cloud WAF. Qué rotar y qué revisar."
date: 2026-11-25T02:58:00+01:00
category: noticias
tags: [Radware, Cloud WAF, AWS, Azure, filtración de datos, credenciales, API]
author: Redacción
photo: "File:Radware tlv.jpg"
imageAlt: "Sede de Radware en Tel Aviv, empresa afectada por el hackeo que expuso claves de nube de clientes"
---

El hackeo a Radware afecta a una empresa cuyo negocio es precisamente proteger a otras. La compañía israelí, conocida por sus soluciones contra ataques DDoS y su cortafuegos de aplicaciones web en la nube (Cloud WAF), ha comunicado a sus clientes que un atacante accedió el 19 de noviembre a una API de gestión interna que estaba expuesta en internet sin pedir ningún tipo de autenticación. Por ese hueco salieron datos de contacto de clientes y, en una parte de las cuentas, las credenciales que Radware usa para enviar los registros (logs) del WAF a los almacenamientos en la nube de cada cliente: Amazon S3, Azure Blob Storage o servidores SFTP.

## Qué ha pasado en Radware

Según el análisis de causa raíz que Radware ha enviado a sus clientes y que ha publicado BleepingComputer, el origen fue "una API de gestión del Cloud WAF de uso interno que era accesible desde internet sin requerir autenticación". El acceso no autorizado se produjo el 19 de noviembre y la empresa lo detectó unas diez horas después. Desde entonces asegura haber bloqueado la dirección IP del atacante, cortado el acceso a esa API y cambiado sus credenciales internas.

Radware dice que no se vieron afectados la inspección del tráfico del WAF, los certificados SSL de los clientes, los datos de los usuarios finales que pasan por el servicio ni los datos de su protección DDoS. Lo delicado son las claves de exportación de logs: con ellas un tercero puede leer o escribir en los buckets o contenedores donde los clientes guardan esos registros, que a menudo incluyen direcciones IP, rutas y cabeceras de peticiones web.

Algunos clientes han contado que recibieron alertas de AWS por accesos desde una IP desconocida a sus buckets de logs, lo que indica que las claves llegaron a usarse. La empresa no ha dicho cuántas cuentas están afectadas; da servicio a más de 12.500 clientes en todo el mundo, pero esa cifra es su base total, no el número de afectados. A fecha de esta noticia no había un aviso público en su web ni una comunicación al regulador bursátil estadounidense.

## ¿Estoy afectado si uso Radware Cloud WAF?

Si tu organización usa el Cloud WAF de Radware y tiene configurada la exportación de logs a S3, Azure Blob o SFTP, debes tratar esas credenciales como comprometidas aunque no hayas recibido aviso directo. Los clientes que solo usan otros productos de Radware, o que no exportan registros, no aparecen como afectados en la información disponible, aunque sus datos de contacto sí pueden haber quedado expuestos. Eso abre la puerta a correos de phishing muy creíbles que se hagan pasar por el soporte de Radware.

## Cómo protegerte: claves que rotar y registros que revisar

Radware recomienda "encarecidamente" rotar las credenciales de exportación y revisar los registros de acceso al almacenamiento. En la práctica:

- **Haz inventario** de todos los buckets de S3, contenedores de Azure o servidores SFTP que reciben logs de Radware.
- **Rota las claves sin cortar el servicio**: en AWS crea una segunda clave de acceso, cámbiala en Radware, comprueba que siguen llegando registros y después desactiva y borra la antigua. En Azure, usa la rotación entre key1 y key2 y, si usabas tokens SAS, regenera la clave con la que se firmaron.
- **Revisa los registros de acceso** al almacenamiento desde al menos el 19 de noviembre: lecturas, borrados o escrituras desde IPs que no sean las de Radware.
- **Reduce permisos**: la clave de exportación solo debería poder escribir en una ruta concreta, nunca listar ni leer todo el bucket.
- **Desconfía de correos** que pidan "verificar" la cuenta de Radware o cambiar credenciales desde un enlace.

El caso recuerda al [robo de secretos en Azure API Management](/fallo-azure-api-management-secretos/) de hace unos días: cuando un proveedor de nube guarda credenciales en nombre de sus clientes, un fallo suyo se convierte en un problema de todos. Si tu empresa se ve afectada, nuestra guía sobre [qué hacer si tus datos aparecen en una filtración](/datos-en-filtracion-que-hacer/) te ayuda a ordenar los siguientes pasos.

## Una lección sobre APIs internas

Que una API "solo para uso interno" acabe publicada en internet sin contraseña es uno de los errores más repetidos en seguridad en la nube, y figura entre los riesgos del [OWASP Top 10](/owasp-top-10-explicado/). Ninguna interfaz debería depender de que "nadie sepa que existe": toda API debe exigir autenticación y estar inventariada, aunque su intención sea no salir nunca de la red de la empresa.

## Fuentes

- [BleepingComputer: Radware discloses breach exposing customer cloud access keys](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)
- [Windows Forum: Radware Cloud WAF breach exposes Azure and AWS log-export credentials](https://windowsforum.com/news/radware-cloud-waf-breach-exposes-azure-and-aws-log-export-credentials-rotation-guide.453957/)
- [TheTechHacker: Radware breach, what customers should do](https://thetechhacker.com/news/radware-breach-cloud-access-keys-what-customers-should-do/)
