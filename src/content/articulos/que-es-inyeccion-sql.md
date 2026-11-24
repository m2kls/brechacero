---
title: "Qué es una inyección SQL y cómo se previene (explicado con ejemplos)"
description: "Cómo funciona la inyección SQL, por qué sigue siendo tan peligrosa y cómo evitarla con consultas parametrizadas y otras buenas prácticas."
date: 2026-12-09
category: guias
tags: [inyección SQL, seguridad web, OWASP, bases de datos, desarrollo seguro]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
video: "ciNHn38EyRc"
videoTitle: "Running an SQL Injection Attack (en inglés)"
videoSource: "Computerphile"
---

La inyección SQL es una de las vulnerabilidades web más antiguas y conocidas, y sin embargo sigue apareciendo en aplicaciones reales. Forma parte de la categoría A05: Inyección del [OWASP Top 10](/owasp-top-10-explicado/). Entenderla bien es imprescindible tanto si programas como si te dedicas a la seguridad.

> Todo lo que verás aquí debe practicarse solo en laboratorios como DVWA, OWASP Juice Shop o PortSwigger Web Security Academy. Probarlo en webs ajenas es ilegal.

## Qué es SQL

Casi todas las aplicaciones web guardan sus datos en una base de datos (usuarios, pedidos, productos...). Para consultarla usan un lenguaje llamado SQL. Por ejemplo:

```sql
SELECT * FROM usuarios WHERE nombre = 'ana';
```

"Dame todos los datos del usuario cuyo nombre es *ana*".

## Qué es una inyección SQL

El problema aparece cuando la aplicación construye la consulta pegando directamente lo que escribe el usuario. Imagina este código de un formulario de inicio de sesión (inseguro):

```python
# ❌ CÓDIGO VULNERABLE: no lo uses
consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "' AND clave = '" + clave + "'"
```

Si el usuario escribe un nombre normal, todo funciona. Pero ¿qué pasa si escribe algo que contiene una comilla? La comilla cierra el texto antes de tiempo y lo que viene después se interpreta como parte de la orden SQL, no como un dato.

El ejemplo didáctico clásico es introducir algo como `' OR '1'='1` en el campo. La consulta resultante queda así:

```sql
SELECT * FROM usuarios WHERE nombre = '' OR '1'='1' AND clave = '...';
```

Como `'1'='1'` siempre es verdadero, la condición puede cumplirse para cualquier registro y, según cómo esté escrito el código, el sistema podría dejar entrar sin una contraseña válida.

**La idea clave:** el fallo no es la comilla, sino que la aplicación mezcla datos y código. Los datos del usuario pasan a ser instrucciones.

## Qué puede conseguir un atacante

Dependiendo del caso, una inyección SQL puede permitir:

- **Saltarse la autenticación** (como en el ejemplo).
- **Leer datos** de otras tablas: usuarios, correos, *hashes* de contraseñas...
- **Modificar o borrar** información.
- En configuraciones muy inseguras, llegar a ejecutar comandos en el servidor.

Muchas de las grandes filtraciones de datos de la historia empezaron por una inyección SQL.

## Tipos de inyección SQL (resumen)

- **Clásica o en banda:** el resultado aparece directamente en la página.
- **Basada en errores:** los mensajes de error de la base de datos revelan información.
- **Ciega (*blind*):** la página no muestra datos, pero se puede deducir información por cómo cambia la respuesta (o cuánto tarda).
- **Fuera de banda:** los datos salen por otro canal, como una petición DNS.

## Cómo se previene

### 1. Consultas parametrizadas (la solución principal)
Se escribe la consulta con huecos y se pasan los datos por separado. La base de datos sabe que lo que va en el hueco es siempre un dato, nunca código, aunque contenga comillas.

```python
# ✅ CÓDIGO SEGURO (Python con sqlite3)
cursor.execute(
    "SELECT * FROM usuarios WHERE nombre = ? AND clave_hash = ?",
    (nombre, clave_hash)
)
```

```php
// ✅ CÓDIGO SEGURO (PHP con PDO)
$stmt = $pdo->prepare("SELECT * FROM usuarios WHERE email = :email");
$stmt->execute(['email' => $email]);
```

Todos los lenguajes y *frameworks* modernos tienen esta opción. Los ORM (como los de Django, Laravel o Hibernate) también la usan por defecto, siempre que no construyas consultas a mano concatenando texto.

### 2. Validación de entradas
Si un campo debe ser un número, comprueba que lo es. Si es un correo, que tiene formato de correo. No sustituye a las consultas parametrizadas, pero añade una capa.

### 3. Mínimo privilegio en la base de datos
La cuenta con la que la aplicación se conecta a la base de datos debe tener solo los permisos que necesita. Si solo lee productos, que no pueda borrar tablas.

### 4. No mostrar errores detallados
Los mensajes de error de la base de datos ayudan al atacante. Muestra un mensaje genérico al usuario y guarda el detalle en los registros internos.

### 5. Contraseñas con *hash*
Nunca guardes contraseñas en texto plano. Si alguien consigue leer la tabla, al menos no tendrá las contraseñas directamente.

### 6. Cortafuegos de aplicaciones web (WAF)
Un WAF puede bloquear muchos intentos conocidos, pero es una capa extra, no un sustituto de un código bien hecho.

## Cómo practicar de forma legal

- **PortSwigger Web Security Academy:** tiene una sección completa de laboratorios de inyección SQL, gratuita y muy bien explicada.
- **DVWA:** módulo de *SQL Injection* con niveles de dificultad, para ver cómo cambia la defensa en cada uno.
- **OWASP Juice Shop:** retos de inyección en una tienda moderna.

Si aún no tienes laboratorio, empieza por [instalar Kali Linux en VirtualBox](/instalar-kali-linux-virtualbox/).

## Preguntas frecuentes

**¿La inyección SQL sigue existiendo en 2026?**
Sí. Es menos frecuente que hace años gracias a los *frameworks* modernos, pero sigue apareciendo, sobre todo en código antiguo o en consultas construidas a mano.

**¿Escapar las comillas es suficiente?**
No es lo recomendado. Es fácil equivocarse y hay casos en los que no basta. La defensa correcta son las consultas parametrizadas.

**¿Las bases de datos NoSQL son inmunes?**
No. Existen inyecciones NoSQL con la misma idea de fondo: mezclar datos del usuario con la lógica de la consulta.
