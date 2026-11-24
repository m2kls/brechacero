---
title: "10 comandos de Linux para revisar la seguridad de tu sistema"
description: "Comandos básicos para ver quién está conectado, qué puertos tienes abiertos y qué está pasando en tu máquina Linux."
date: 2026-11-20
category: linux
tags: [Linux, terminal, sysadmin, defensa]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

Saber qué está pasando en tu equipo es el primer paso para protegerlo. Estos comandos vienen en la mayoría de distribuciones y te ayudan a revisar tu propio sistema.

## 1. Quién está conectado: `who` y `w`

```bash
w
```
Muestra los usuarios con sesión abierta y qué están ejecutando.

## 2. Últimos accesos: `last`

```bash
last -n 20
```
Lista los últimos inicios de sesión. Un acceso a una hora rara merece una revisión.

## 3. Puertos a la escucha: `ss`

```bash
sudo ss -tulpn
```
Muestra qué programas esperan conexiones. Cualquier servicio que no reconozcas es candidato a desactivarse.

## 4. Procesos: `ps` y `top`

```bash
ps aux --sort=-%cpu | head
```
Los procesos que más CPU consumen. Útil para detectar algo que no debería estar ahí.

## 5. Registros del sistema: `journalctl`

```bash
sudo journalctl -p warning --since today
```
Avisos y errores de hoy.

## 6. Intentos de acceso SSH fallidos

```bash
sudo journalctl -u ssh --since "1 hour ago" | grep -i failed
```

## 7. Actualizaciones pendientes

```bash
sudo apt update && apt list --upgradable   # Debian/Ubuntu
```

## 8. Cortafuegos: `ufw`

```bash
sudo ufw status verbose
```
Si está inactivo, plantéate activarlo permitiendo solo lo que necesitas.

## 9. Permisos sospechosos

```bash
find / -perm -4000 -type f 2>/dev/null
```
Lista binarios con el bit SUID. Compáralo con una instalación limpia de tu distribución.

## 10. Integridad de paquetes

```bash
sudo debsums -s   # Debian/Ubuntu, requiere instalar debsums
```
Avisa si algún archivo de un paquete instalado ha sido modificado.

Con estos diez comandos ya puedes hacer una revisión básica en pocos minutos. En próximas guías veremos cómo automatizarla.
