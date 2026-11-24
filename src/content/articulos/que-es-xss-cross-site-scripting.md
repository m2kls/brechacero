---
title: "Qué es el XSS (Cross-Site Scripting): tipos, ejemplos en laboratorio y cómo evitarlo"
description: "Cómo funciona el Cross-Site Scripting, sus tres tipos (reflejado, almacenado y DOM), qué riesgos tiene y cómo se previene en una aplicación web."
date: 2026-12-14
category: guias
tags: [XSS, seguridad web, OWASP, JavaScript, desarrollo seguro]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
---

El Cross-Site Scripting, o XSS, es una de las vulnerabilidades más frecuentes en aplicaciones web. Igual que la [inyección SQL](/que-es-inyeccion-sql/), pertenece a la categoría de inyección del [OWASP Top 10](/owasp-top-10-explicado/). La diferencia es que aquí el código inyectado no se ejecuta en el servidor, sino en el navegador de otros usuarios.

> Practica solo en laboratorios como PortSwigger Web Security Academy, DVWA u OWASP Juice Shop. Probar XSS en webs ajenas sin permiso es ilegal.

## La idea en una frase

Hay XSS cuando una web muestra en la página algo que ha escrito un usuario sin tratarlo, y el navegador lo interpreta como código (HTML o JavaScript) en lugar de como texto.

## Un ejemplo sencillo

Imagina un buscador que muestra: *"Resultados para: [lo que has buscado]"*. Si la web inserta directamente el texto de la búsqueda en el HTML, sin procesarlo, y alguien busca:

```html
<script>alert('XSS')</script>
```

el navegador no mostrará ese texto: lo ejecutará y saldrá una ventana emergente. El `alert` es la prueba de concepto típica en laboratorios: inofensiva, pero demuestra que se puede ejecutar código.

## Por qué es peligroso

Si se puede ejecutar JavaScript en la web de otra persona, en el contexto de esa web, se puede:

- **Robar la sesión** del usuario si las cookies no están protegidas, y entrar en su cuenta.
- **Hacer acciones en su nombre**: cambiar su correo, publicar mensajes, hacer compras.
- **Modificar lo que ve**, por ejemplo mostrar un formulario de inicio de sesión falso.
- **Redirigirle** a una web maliciosa.

## Los tres tipos de XSS

### 1. XSS reflejado
El código malicioso va en la propia petición (por ejemplo, en un parámetro de la URL) y la web lo "refleja" en la respuesta. Para que afecte a alguien, el atacante tiene que conseguir que la víctima abra un enlace preparado, normalmente mediante [phishing](/phishing-con-ia/).

### 2. XSS almacenado (persistente)
El código se guarda en la web: un comentario, un nombre de perfil, una reseña... y se ejecuta a todo el que visita esa página. Es el más peligroso porque no hace falta engañar a nadie con un enlace.

### 3. XSS basado en DOM
El fallo está en el JavaScript del propio navegador: el código de la página toma un dato (por ejemplo, de la URL) y lo inserta en la página de forma insegura, sin que el servidor intervenga.

## Cómo se previene

### 1. Codificar la salida (lo más importante)
Antes de mostrar un dato del usuario en la página, se convierten los caracteres especiales para que el navegador los muestre como texto:

| Carácter | Se convierte en |
|---|---|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `"` | `&quot;` |
| `'` | `&#x27;` |
| `&` | `&amp;` |

Así, `<script>` se ve en pantalla como texto y no se ejecuta. La codificación correcta depende del contexto (dentro de HTML, de un atributo, de JavaScript o de una URL).

### 2. Usar frameworks modernos correctamente
React, Angular, Vue o los motores de plantillas modernos codifican automáticamente por defecto. El peligro aparece cuando se salta esa protección con funciones como `innerHTML`, `dangerouslySetInnerHTML` o `v-html`. Úsalas solo si es imprescindible y con contenido ya saneado.

```javascript
// ❌ Inseguro: interpreta el texto como HTML
elemento.innerHTML = textoDelUsuario;

// ✅ Seguro: lo trata siempre como texto
elemento.textContent = textoDelUsuario;
```

### 3. Sanear el HTML cuando haya que permitirlo
Si tu web debe aceptar algo de formato (por ejemplo, negritas en comentarios), usa una librería de saneado reconocida, como DOMPurify, que elimina todo lo peligroso.

### 4. Content Security Policy (CSP)
Una cabecera HTTP que indica al navegador de dónde puede cargar y ejecutar scripts. Bien configurada, puede bloquear la mayoría de ataques XSS aunque exista el fallo. Es una segunda capa de defensa.

### 5. Proteger las cookies
Marcar las cookies de sesión como `HttpOnly` impide que JavaScript las lea, lo que evita el robo directo de la sesión. Añade también `Secure` y `SameSite`.

### 6. Validar las entradas
Si un campo debe ser un número o una fecha, comprueba que lo es. Ayuda, pero no sustituye a la codificación de la salida.

## Cómo practicar de forma legal

- **PortSwigger Web Security Academy:** decenas de laboratorios de XSS de todos los niveles, gratis.
- **DVWA:** módulos de XSS reflejado, almacenado y DOM, con niveles de seguridad para ver cómo cambia la defensa.
- **OWASP Juice Shop:** retos de XSS en una aplicación moderna.

## Preguntas frecuentes

**¿El XSS afecta al servidor?**
Normalmente no directamente: afecta a los usuarios de la web. Pero si la víctima es un administrador, el atacante puede acabar controlando la web entera.

**¿Los navegadores modernos no lo bloquean?**
Algunos tenían filtros anti-XSS, pero se retiraron por ser poco fiables. La protección debe estar en la propia aplicación (y en la CSP).

**¿Una ventana `alert` es un ataque?**
No. Es solo la forma estándar de demostrar en un laboratorio o en un informe de seguridad que existe la vulnerabilidad.
