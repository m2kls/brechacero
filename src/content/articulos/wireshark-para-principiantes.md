---
title: "Wireshark para principiantes: captura y analiza el tráfico de tu propia red"
description: "Guía para empezar con Wireshark: instalarlo, capturar tráfico de tu equipo, usar filtros básicos y entender qué está pasando en tu red."
date: 2026-12-15
category: guias
tags: [Wireshark, redes, análisis de tráfico, herramientas, defensa]
author: Redacción
imageCredit: "Logotipo: Wireshark Foundation. Composición: Brecha Cero"
---

**Wireshark** es el analizador de tráfico de red más usado del mundo. Gratuito y de código abierto, te permite ver cada paquete que entra y sale de tu equipo, capa por capa. Es una herramienta imprescindible para entender cómo funcionan las redes, diagnosticar problemas y detectar comportamientos sospechosos.

> Captura solo el tráfico de tu propio equipo o de redes que administres. Interceptar comunicaciones ajenas sin autorización es delito.

## Para qué sirve

- **Aprender redes:** ver en directo el [modelo TCP/IP](/modelo-tcp-ip-explicado/), el saludo TCP, las consultas DNS...
- **Diagnosticar problemas:** por qué una web no carga, por qué una conexión es lenta.
- **Seguridad:** detectar tráfico extraño, comprobar si una aplicación envía datos sin cifrar o analizar capturas en ejercicios de CTF y análisis forense.

## Instalación

- **Windows y macOS:** descárgalo desde la web oficial, wireshark.org. En Windows, acepta instalar Npcap, el componente que permite capturar.
- **Kali Linux:** viene preinstalado.
- **Debian/Ubuntu:** `sudo apt install wireshark`. Durante la instalación te preguntará si los usuarios sin privilegios pueden capturar; responde que sí y añade tu usuario al grupo: `sudo usermod -aG wireshark $USER` (cierra sesión para que tenga efecto).

## Tu primera captura

1. Abre Wireshark. Verás una lista de interfaces de red con una pequeña gráfica de actividad.
2. Elige la que tenga movimiento (normalmente tu WiFi o Ethernet) y haz doble clic.
3. Abre una web en el navegador.
4. Pulsa el cuadrado rojo para detener la captura.

Verás cientos de líneas. No te agobies: los filtros están para eso.

## Entender la pantalla

Wireshark se divide en tres paneles:

1. **Lista de paquetes:** un paquete por línea, con hora, origen, destino, protocolo y un resumen.
2. **Detalle del paquete:** el paquete seleccionado desglosado por capas (Ethernet, IP, TCP/UDP, aplicación). Despliega cada una para ver sus campos.
3. **Bytes:** el contenido en bruto, en hexadecimal y texto.

Los colores ayudan: por defecto, el tráfico TCP, el UDP y los errores tienen tonos distintos.

## Filtros de visualización básicos

Escríbelos en la barra superior y pulsa Intro. La barra se pone verde si el filtro es válido.

| Filtro | Qué muestra |
|---|---|
| `dns` | Consultas y respuestas DNS |
| `http` | Tráfico web sin cifrar |
| `tls` | Tráfico cifrado HTTPS (verás el inicio de la conexión, no el contenido) |
| `ip.addr == 192.168.1.10` | Todo lo que va o viene de esa IP |
| `tcp.port == 443` | Tráfico por el puerto 443 |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | Inicios de conexión TCP |
| `icmp` | Pings y mensajes de control |
| `!(arp or dns)` | Todo excepto ARP y DNS (para quitar ruido) |

Puedes combinar filtros con `&&` (y), `||` (o) y `!` (no).

> No confundas los filtros de visualización (los de la barra, que ocultan paquetes ya capturados) con los filtros de captura (se ponen antes de empezar y deciden qué se guarda; usan otra sintaxis, por ejemplo `port 53`).

## Tres ejercicios para empezar

### 1. Mira una consulta DNS
Filtra por `dns`, abre una web nueva y busca la consulta con su nombre. Verás la pregunta ("¿qué IP tiene ejemplo.com?") y la respuesta. Así funciona la traducción de nombres que usas cada día.

### 2. Observa el saludo TCP
Filtra por `tcp.port == 443` y busca los tres primeros paquetes de una conexión: SYN, SYN-ACK, ACK. Es el saludo de tres vías que explicamos en el artículo de [TCP/IP](/modelo-tcp-ip-explicado/).

### 3. Comprueba la diferencia entre HTTP y HTTPS
En tu laboratorio, visita una página HTTP de una máquina vulnerable (por ejemplo, DVWA) e inicia sesión con sus credenciales de prueba. Filtra por `http` y usa *Clic derecho › Seguir › Flujo TCP*: verás el usuario y la contraseña en texto claro. Repite con una web HTTPS: solo verás datos cifrados. Es la mejor demostración de por qué el cifrado importa.

## Funciones útiles

- **Seguir flujo** (*Follow Stream*): reconstruye una conversación completa entre dos equipos.
- **Estadísticas › Conversaciones:** qué equipos han hablado más entre sí.
- **Estadísticas › Jerarquía de protocolos:** qué porcentaje del tráfico es de cada tipo.
- **Archivo › Guardar como:** guarda la captura en formato `.pcapng` para analizarla después.

## Qué puede revelar sobre tu seguridad

- Aplicaciones o dispositivos que envían información sin cifrar.
- Equipos que se conectan a destinos desconocidos de forma repetida.
- Un volumen de tráfico anormal a horas en las que nadie usa la red.
- Dispositivos del hogar (cámaras, enchufes inteligentes) que "hablan" más de lo esperado.

## Preguntas frecuentes

**¿Puedo ver las contraseñas de las webs que visito?**
No si usan HTTPS, que es la gran mayoría. Wireshark solo verá el tráfico cifrado.

**¿Wireshark es legal?**
Sí. Es una herramienta estándar de administración de redes. Lo ilegal es usarla para interceptar comunicaciones ajenas.

**¿Por qué no veo el tráfico de otros dispositivos de mi WiFi?**
En las redes actuales, tu equipo normalmente solo recibe su propio tráfico. Para analizar el de otros dispositivos de tu red hacen falta configuraciones específicas en el router o switch.

Para seguir aprendiendo, combina Wireshark con [Nmap](/que-es-nmap-como-usarlo/): verás exactamente qué paquetes envía cada tipo de escaneo.
