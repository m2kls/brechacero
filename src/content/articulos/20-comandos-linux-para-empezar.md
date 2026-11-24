---
title: "20 comandos de Linux que todo aprendiz de ciberseguridad debe dominar"
description: "Los comandos de terminal que vas a usar a diario si estudias ciberseguridad: moverte, buscar, gestionar permisos, redes y procesos, con ejemplos."
date: 2026-11-27
category: linux
tags: [Linux, terminal, Bash, aprender, fundamentos]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

Casi todo en ciberseguridad pasa por una terminal de Linux: plataformas de práctica, servidores, herramientas de análisis... Si te sientes cómodo en ella, avanzarás el doble de rápido. Estos son los 20 comandos que más vas a usar, agrupados por tareas.

> Practica en tu propia máquina virtual. Si aún no la tienes, empieza por nuestra guía para [instalar Kali Linux en VirtualBox](/instalar-kali-linux-virtualbox/).

## Moverte por el sistema

### 1. `pwd`: dónde estoy
```bash
pwd
```
Muestra la carpeta en la que te encuentras.

### 2. `ls`: qué hay aquí
```bash
ls -la
```
Lista los archivos, incluidos los ocultos (los que empiezan por punto), con sus permisos y propietarios. En seguridad, los archivos ocultos importan.

### 3. `cd`: cambiar de carpeta
```bash
cd /var/log      # ir a una ruta
cd ..            # subir un nivel
cd ~             # volver a tu carpeta personal
```

## Ver y manipular archivos

### 4. `cat`, `less`, `head` y `tail`
```bash
cat archivo.txt
less /var/log/syslog
tail -f /var/log/auth.log
```
`tail -f` muestra en directo lo que se va escribiendo en un registro. Muy útil para ver intentos de acceso en tiempo real.

### 5. `cp`, `mv` y `rm`
```bash
cp origen destino
mv viejo.txt nuevo.txt
rm archivo.txt
```
Cuidado con `rm -rf`: borra sin preguntar y no hay papelera.

### 6. `mkdir` y `touch`
```bash
mkdir -p lab/notas
touch lab/notas/maquina1.md
```
Crear una estructura de carpetas para tus notas es el primer paso para ser ordenado.

## Buscar

### 7. `grep`: buscar texto
```bash
grep -i "failed" /var/log/auth.log
grep -rn "password" ./proyecto
```
Probablemente el comando que más usarás. `-i` ignora mayúsculas, `-r` busca en carpetas y `-n` muestra el número de línea.

### 8. `find`: buscar archivos
```bash
find / -name "*.conf" 2>/dev/null
find /home -type f -mtime -1
```
El segundo ejemplo lista los archivos modificados en el último día. `2>/dev/null` oculta los errores de permisos.

### 9. `which` y `whereis`
```bash
which python3
```
Te dice dónde está instalado un programa.

## Usuarios y permisos

### 10. `whoami` e `id`
```bash
whoami
id
```
Con qué usuario estás trabajando y a qué grupos perteneces.

### 11. `sudo`
```bash
sudo apt update
```
Ejecuta un comando como administrador. `sudo -l` muestra qué te está permitido ejecutar con `sudo`, algo que conviene revisar en tus propios sistemas.

### 12. `chmod`: cambiar permisos
```bash
chmod 600 clave_privada
chmod +x script.sh
```
Los permisos `rwx` (lectura, escritura, ejecución) para propietario, grupo y otros son la base de la seguridad en Linux.

### 13. `chown`: cambiar propietario
```bash
sudo chown usuario:grupo archivo
```

## Redes

### 14. `ip`: tu configuración de red
```bash
ip a
ip route
```
Muestra tus interfaces, direcciones IP y la puerta de enlace. Es lo primero que se mira en un laboratorio.

### 15. `ping`: ¿hay alguien ahí?
```bash
ping -c 4 192.168.56.101
```
Comprueba si un equipo responde. `-c 4` envía solo cuatro paquetes.

### 16. `ss`: conexiones y puertos
```bash
ss -tulpn
```
Qué puertos están a la escucha en tu equipo. Si no tienes claro qué es un puerto, lee [qué es un puerto en redes](/que-es-un-puerto-redes/).

### 17. `curl` y `wget`
```bash
curl -I https://ejemplo.com
wget https://ejemplo.com/archivo.zip
```
`curl -I` muestra solo las cabeceras HTTP de una web, muy útil para entender cómo responde un servidor.

### 18. `ssh`: conexión remota segura
```bash
ssh usuario@192.168.56.101
```

## Procesos y sistema

### 19. `ps` y `top`
```bash
ps aux
top
```
Qué programas se están ejecutando y cuántos recursos consumen.

### 20. `man`: el manual
```bash
man grep
```
El comando más infravalorado. Antes de buscar en Internet, mira el manual: casi siempre está la respuesta.

## Bonus: tuberías y redirecciones

La verdadera potencia de la terminal está en combinar comandos:

```bash
cat /var/log/auth.log | grep "Failed" | wc -l     # cuenta intentos fallidos
ls -la > listado.txt                              # guarda la salida en un archivo
```

- `|` (tubería) pasa la salida de un comando al siguiente.
- `>` guarda la salida en un archivo (sobrescribe) y `>>` la añade al final.

## Cómo practicar

- Dedica 15 minutos al día a hacer todo desde la terminal, aunque tardes más.
- Usa juegos como OverTheWire: Bandit, pensados para aprender comandos de Linux resolviendo retos.
- Cuando domines estos, pasa a nuestra lista de [comandos para revisar la seguridad de tu sistema](/comandos-linux-seguridad/).
