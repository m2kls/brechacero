---
title: "El modelo TCP/IP explicado fácil: cómo viajan tus datos por Internet"
description: "Las cuatro capas del modelo TCP/IP con ejemplos cotidianos, su relación con el modelo OSI y por qué entenderlas es clave en ciberseguridad."
date: 2026-12-03
category: guias
tags: [redes, TCP/IP, OSI, fundamentos, protocolos]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

Cada vez que abres una web, envías un WhatsApp o ves un vídeo, tus datos atraviesan decenas de equipos hasta llegar a su destino. Todo eso funciona gracias a un conjunto de reglas llamado modelo TCP/IP. Entenderlo es imprescindible en ciberseguridad: casi todos los ataques y defensas se explican según la "capa" en la que actúan.

## La idea clave: capas que se reparten el trabajo

Enviar datos por Internet es un problema enorme, así que se divide en partes más pequeñas. Cada capa se ocupa de una tarea y se apoya en la de abajo, sin preocuparse de cómo lo hace.

Piensa en enviar un paquete por mensajería:

1. Tú escribes la carta (el contenido).
2. La metes en un sobre con el nombre del destinatario y el departamento (a qué servicio va).
3. La empresa de mensajería pone la dirección postal completa y decide la ruta (a qué equipo va y por dónde).
4. El repartidor la lleva físicamente en una furgoneta (el medio físico).

El modelo TCP/IP hace exactamente eso, en cuatro capas.

## Las 4 capas del modelo TCP/IP

### 1. Capa de aplicación
Es la que "ve" el usuario. Aquí están los protocolos que usan los programas para hablar entre sí:

- **HTTP/HTTPS**: la web.
- **DNS**: traduce nombres como `ejemplo.com` a direcciones IP.
- **SMTP, IMAP**: el correo electrónico.
- **SSH**: acceso remoto seguro.

### 2. Capa de transporte
Decide a qué programa del equipo de destino van los datos (mediante los [puertos](/que-es-un-puerto-redes/)) y cómo se entregan:

- **TCP**: fiable. Establece una conexión, numera los fragmentos, confirma que llegan y reenvía los perdidos.
- **UDP**: rápido. Envía sin confirmar. Ideal para videollamadas, juegos o DNS.

**El saludo de tres vías de TCP.** Antes de enviar datos, TCP establece la conexión en tres pasos:

```
Cliente  →  SYN       →  Servidor   "¿Hablamos?"
Cliente  ←  SYN-ACK   ←  Servidor   "Sí, hablamos"
Cliente  →  ACK       →  Servidor   "Perfecto, empiezo"
```

Este "apretón de manos" es la base de muchas técnicas de escaneo, como las de [Nmap](/que-es-nmap-como-usarlo/), y también de algunos ataques de denegación de servicio que lo abusan.

### 3. Capa de Internet (o de red)
Se encarga de la dirección del equipo y de la ruta:

- **IP** (IPv4 e IPv6): cada paquete lleva una IP de origen y otra de destino.
- Los routers leen esa dirección y deciden por dónde enviar cada paquete, salto a salto.
- **ICMP**: mensajes de control, como los que usa `ping`.

### 4. Capa de acceso a la red (o de enlace)
Mueve los datos por el medio físico de la red local: cable Ethernet, WiFi, fibra...

- Aquí se usan las direcciones MAC, el identificador de cada tarjeta de red.
- **ARP** traduce una IP de tu red local a la MAC correspondiente.

## Encapsulación: la muñeca rusa de los datos

Cuando envías algo, cada capa añade su propia "etiqueta" (cabecera) a lo que recibe de arriba:

```
[ Datos de la aplicación ]
[ Cabecera TCP | Datos ]                         → segmento
[ Cabecera IP | Cabecera TCP | Datos ]           → paquete
[ Cab. Ethernet | IP | TCP | Datos | Cola ]      → trama
```

Al llegar al destino, el proceso se invierte: cada capa quita su cabecera y pasa el resto hacia arriba. Con herramientas como Wireshark puedes ver todas estas capas en tu propio tráfico.

## TCP/IP frente al modelo OSI

Seguramente también oirás hablar del modelo OSI, de 7 capas. Es más teórico, pero se usa mucho como referencia ("es un ataque de capa 7"). Así se corresponden:

| Modelo OSI | Modelo TCP/IP | Ejemplos |
|---|---|---|
| 7. Aplicación | Aplicación | HTTP, DNS, SSH |
| 6. Presentación | Aplicación | Cifrado TLS, codificación |
| 5. Sesión | Aplicación | Gestión de sesiones |
| 4. Transporte | Transporte | TCP, UDP |
| 3. Red | Internet | IP, ICMP |
| 2. Enlace | Acceso a la red | Ethernet, WiFi, MAC, ARP |
| 1. Física | Acceso a la red | Cables, señales de radio |

## Por qué esto importa en ciberseguridad

Muchas amenazas y defensas se entienden mejor por capas:

| Capa | Ejemplo de amenaza | Ejemplo de defensa |
|---|---|---|
| Aplicación | Inyección SQL, phishing | Actualizaciones, validar entradas, WAF |
| Transporte | Inundación de conexiones SYN | Limitación de conexiones, protección anti-DDoS |
| Internet | Suplantación de IP | Filtrado en routers y cortafuegos |
| Acceso a la red | Envenenamiento ARP en una red WiFi pública | Redes cifradas, VPN, segmentación |

Un cortafuegos clásico trabaja sobre todo en las capas de Internet y transporte (IP y puertos), mientras que un WAF (cortafuegos de aplicaciones web) inspecciona el contenido de la capa de aplicación.

## Prueba esto en tu ordenador

```bash
ip a                    # tu IP y tu MAC (capas de Internet y enlace)
ip neigh                # la tabla ARP: IP ↔ MAC de tu red local
ping -c 3 ejemplo.com   # DNS + ICMP en acción
traceroute ejemplo.com  # los routers por los que pasan tus paquetes
```

(En Windows: `ipconfig /all`, `arp -a`, `ping` y `tracert`.)

Si los comandos de terminal aún te cuestan, repasa nuestros [20 comandos de Linux para empezar](/20-comandos-linux-para-empezar/).

## Preguntas frecuentes

**¿TCP/IP es un solo protocolo?**
No. Es un conjunto de protocolos que toma su nombre de los dos más importantes: TCP e IP.

**¿Tengo que aprenderme el modelo OSI?**
Sí, al menos a nivel básico. Aparece en entrevistas, certificaciones y en el lenguaje del día a día del sector.

**¿HTTPS en qué capa está?**
HTTP es de aplicación; el cifrado TLS que lo convierte en HTTPS se sitúa entre la aplicación y el transporte (en OSI se suele asociar a las capas 5-6).
