---
title: "Qué es un puerto en redes y qué significan los más comunes (22, 80, 443…)"
description: "Explicación sencilla de qué es un puerto, la diferencia entre TCP y UDP, los puertos más habituales y por qué importan para la seguridad."
date: 2026-11-26
category: guias
tags: [redes, puertos, TCP, UDP, fundamentos]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

Si estás empezando en ciberseguridad, vas a oír hablar de puertos constantemente: "el puerto 22 está abierto", "cierra el 3389", "escanea los puertos". Es uno de esos conceptos que conviene entender bien desde el principio, porque todo lo demás se apoya en él.

## La analogía del edificio

Imagina que la dirección IP de un ordenador es la dirección de un edificio. Dentro del edificio hay muchas oficinas, y cada una atiende un servicio distinto: una es la web, otra el correo, otra el acceso remoto. El puerto es el número de la puerta de cada oficina.

Cuando tu navegador visita una web, no solo va a la IP del servidor: llama a una puerta concreta, normalmente la 443, donde el servidor web está esperando.

Técnicamente, un puerto es un número entre 0 y 65.535 que permite a un mismo equipo ofrecer muchos servicios a la vez y saber a qué programa entregar cada conexión.

## Tipos de puertos según su número

| Rango | Nombre | Uso |
|---|---|---|
| 0 – 1023 | Puertos bien conocidos | Servicios estándar (web, correo, SSH…) |
| 1024 – 49151 | Puertos registrados | Aplicaciones concretas (bases de datos, juegos…) |
| 49152 – 65535 | Puertos dinámicos | Los usa tu equipo temporalmente como origen de sus conexiones |

## TCP y UDP: dos formas de hablar

Los puertos existen en dos protocolos de transporte distintos:

- **TCP**: establece una conexión antes de enviar datos y comprueba que todo llega completo y en orden. Lo usan la web, el correo o SSH.
- **UDP**: envía los datos sin establecer conexión ni confirmar la entrega. Es más rápido y se usa en DNS, videollamadas o juegos online.

El puerto 53 TCP y el 53 UDP son, en realidad, dos puertas distintas.

## Los puertos más comunes que debes conocer

| Puerto | Protocolo | Servicio | Comentario de seguridad |
|---|---|---|---|
| 20/21 | TCP | FTP | Transmite contraseñas sin cifrar. Mejor usar SFTP |
| 22 | TCP | SSH | Acceso remoto cifrado. Muy atacado por fuerza bruta |
| 23 | TCP | Telnet | Sin cifrar. No debería estar expuesto nunca |
| 25 | TCP | SMTP | Envío de correo entre servidores |
| 53 | TCP/UDP | DNS | Traduce nombres de dominio a IP |
| 80 | TCP | HTTP | Web sin cifrar |
| 110 / 143 | TCP | POP3 / IMAP | Lectura de correo (mejor sus versiones cifradas 995 / 993) |
| 443 | TCP | HTTPS | Web cifrada. El más usado de Internet |
| 445 | TCP | SMB | Compartir archivos en Windows. Nunca expuesto a Internet |
| 3306 | TCP | MySQL | Base de datos. No debería ser accesible desde fuera |
| 3389 | TCP | RDP | Escritorio remoto de Windows. Objetivo frecuente del ransomware |
| 8080 | TCP | HTTP alternativo | Paneles de administración y servidores de pruebas |

> 💡 Un servicio puede configurarse en cualquier puerto. Que SSH esté "normalmente" en el 22 no significa que siempre lo esté.

## Estados de un puerto

Cuando se analiza un equipo, cada puerto puede aparecer como:

- **Abierto**: hay un programa escuchando y aceptando conexiones.
- **Cerrado**: el equipo responde, pero no hay ningún servicio en esa puerta.
- **Filtrado**: un cortafuegos bloquea el paso y no se sabe qué hay detrás.

## Por qué los puertos importan para la seguridad

Cada puerto abierto es una puerta de entrada potencial. No es peligroso por sí mismo, pero el programa que hay detrás puede tener fallos o estar mal configurado. Por eso, en seguridad se aplica una regla muy sencilla: abre solo lo que necesites y cierra todo lo demás.

Algunos ejemplos clásicos de problemas:

- Un escritorio remoto (RDP) expuesto a Internet con una contraseña débil.
- Una base de datos accesible desde fuera sin contraseña.
- Un router con el panel de administración abierto hacia Internet.

## Cómo ver qué puertos tienes abiertos

En Linux:

```bash
sudo ss -tulpn
```

En Windows (PowerShell o símbolo del sistema):

```powershell
netstat -ano
```

Muestran qué puertos están a la escucha en tu propio equipo y qué programa los usa. Tienes más comandos útiles en [10 comandos de Linux para revisar la seguridad de tu sistema](/comandos-linux-seguridad/). Y para ver tu red "desde fuera", en nuestra guía de Nmap te enseñamos a [escanear tu propia red de forma segura](/que-es-nmap-como-usarlo/).

## Preguntas frecuentes

**¿Tener puertos abiertos es malo?**
No. Un servidor web necesita el 443 abierto para funcionar. Lo importante es que solo estén abiertos los que necesitas y que el software esté actualizado.

**¿Cambiar el puerto de un servicio lo hace seguro?**
Reduce el ruido de ataques automáticos, pero no es una medida de seguridad real. Lo que protege es una buena configuración, contraseñas fuertes o claves y las actualizaciones.

**¿Mi router tiene puertos abiertos?**
Puede. Revisa en su configuración que no tengas redirecciones de puertos (*port forwarding*) ni UPnP activados si no los necesitas.
