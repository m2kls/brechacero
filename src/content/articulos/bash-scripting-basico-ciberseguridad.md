---
title: "Bash scripting básico para ciberseguridad: automatiza tus primeras tareas"
description: "Aprende lo esencial de Bash (variables, condiciones, bucles y argumentos) con scripts útiles para revisar tu sistema y tu laboratorio."
date: 2026-12-16
category: linux
tags: [Bash, scripting, Linux, automatización, terminal]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

En ciberseguridad repites muchas tareas: revisar registros, comprobar qué equipos responden, ordenar resultados... Bash te permite convertir esas tareas en scripts que se ejecutan con un solo comando. No hace falta ser programador: con cinco o seis conceptos ya puedes hacer cosas muy útiles.

> Antes de empezar, conviene que te muevas con soltura por la terminal. Repasa nuestros [20 comandos de Linux para empezar](/20-comandos-linux-para-empezar/).

## Tu primer script

Crea un archivo:

```bash
nano hola.sh
```

Escribe:

```bash
#!/bin/bash
echo "Hola, $USER. Hoy es $(date +%d/%m/%Y)."
```

Guarda (Ctrl+O, Intro) y sal (Ctrl+X). Dale permisos de ejecución y lánzalo:

```bash
chmod +x hola.sh
./hola.sh
```

- La primera línea, `#!/bin/bash` (el *shebang*), indica qué programa debe interpretar el script.
- `$USER` es una variable del sistema con tu nombre de usuario.
- `$(...)` ejecuta un comando e inserta su resultado.

## Los conceptos básicos

### Variables
```bash
nombre="laboratorio"
red="192.168.56"
echo "Analizando la red $red.0/24 del $nombre"
```
Sin espacios alrededor del `=`. Para usar la variable, se antepone `$`.

### Argumentos
Lo que escribes después del nombre del script llega en `$1`, `$2`... y `$#` indica cuántos argumentos hay:

```bash
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Uso: $0 <archivo>"
    exit 1
fi
echo "Vas a analizar: $1"
```

### Condiciones
```bash
if [ -f "/var/log/auth.log" ]; then
    echo "El registro existe"
else
    echo "No encuentro el registro"
fi
```
Comprobaciones habituales: `-f` (existe el archivo), `-d` (existe la carpeta), `-z` (texto vacío), `-eq` / `-ne` / `-gt` (comparar números).

### Bucles
```bash
for i in 1 2 3; do
    echo "Vuelta $i"
done

for i in $(seq 1 5); do
    echo "Número $i"
done
```

### Leer un archivo línea a línea
```bash
while read -r linea; do
    echo "Procesando: $linea"
done < lista.txt
```

## Scripts útiles para tu sistema y tu laboratorio

### 1. Descubrir equipos activos en tu laboratorio
Un "barrido de ping" sencillo para la red interna de tu laboratorio virtual:

```bash
#!/bin/bash
# Uso: ./barrido.sh 192.168.56
# Úsalo solo en tu propia red o laboratorio.
red=$1
if [ -z "$red" ]; then
    echo "Uso: $0 <red, ej. 192.168.56>"
    exit 1
fi

for host in $(seq 1 254); do
    ping -c 1 -W 1 "$red.$host" > /dev/null 2>&1 && echo "Activo: $red.$host" &
done
wait
```

El `&` lanza cada ping en paralelo y `wait` espera a que terminen todos. Es una versión casera de lo que hace `nmap -sn` (te lo explicamos en [la guía de Nmap](/que-es-nmap-como-usarlo/)).

### 2. Resumen de intentos de acceso SSH fallidos
```bash
#!/bin/bash
# Muestra las IP con más intentos fallidos de SSH hoy en tu equipo.
sudo journalctl -u ssh --since today 2>/dev/null \
  | grep "Failed password" \
  | grep -oE "from [0-9.]+" \
  | awk '{print $2}' \
  | sort | uniq -c | sort -rn | head -10
```

Combina varios comandos con tuberías: filtra las líneas, extrae la IP, cuenta las repeticiones y ordena. (En algunas distribuciones el servicio se llama `sshd` en lugar de `ssh`.)

### 3. Comprobar actualizaciones y espacio en disco
```bash
#!/bin/bash
echo "== Espacio en disco =="
df -h / | tail -1

echo "== Actualizaciones pendientes =="
sudo apt update -qq 2>/dev/null
pendientes=$(apt list --upgradable 2>/dev/null | grep -c upgradable)
if [ "$pendientes" -gt 0 ]; then
    echo "Tienes $pendientes paquetes por actualizar."
else
    echo "Sistema al día."
fi
```

### 4. Crear la carpeta de notas para una nueva máquina
Muy útil cuando practicas en [HackTheBox o TryHackMe](/hackthebox-vs-tryhackme/):

```bash
#!/bin/bash
# Uso: ./nueva_maquina.sh nombre
maquina=$1
[ -z "$maquina" ] && { echo "Uso: $0 <nombre>"; exit 1; }
mkdir -p "$HOME/lab/$maquina"/{escaneos,notas,archivos}
echo "# $maquina - $(date +%F)" > "$HOME/lab/$maquina/notas/notas.md"
echo "Carpeta creada en $HOME/lab/$maquina"
```

## Buenas prácticas desde el principio

- **Pon siempre las variables entre comillas** (`"$var"`) para evitar problemas con espacios.
- Añade `set -euo pipefail` al principio de scripts importantes: el script se detiene ante errores en lugar de seguir como si nada.
- **Comenta** lo que hace cada parte. Tu yo del futuro te lo agradecerá.
- Revisa tus scripts con ShellCheck (`sudo apt install shellcheck`), que detecta errores comunes.
- **Nunca ejecutes scripts descargados de Internet sin leerlos** antes, y menos con `sudo`.

## Siguiente paso

Cuando domines Bash, aprende Python: es más potente para tareas complejas y es el otro gran lenguaje de la ciberseguridad. Pero para automatizar lo del día a día en Linux, Bash seguirá siendo tu herramienta más rápida.
