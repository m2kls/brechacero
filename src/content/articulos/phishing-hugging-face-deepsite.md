---
title: "Phishing en Hugging Face: crean con IA webs falsas de Microsoft y Google"
description: "Phishing en Hugging Face: 42 páginas falsas de 28 marcas, 29 hechas con su IA DeepSite, robaban contraseñas y códigos 2FA. Cómo detectarlas y qué hacer."
date: 2026-11-25T16:57:00+01:00
category: noticias
tags: [phishing, Hugging Face, DeepSite, inteligencia artificial, Microsoft, Google, robo de contraseñas]
author: Redacción
photo: "File:Phishing Login.jpg"
imageAlt: "Pantalla de inicio de sesión falsa de una campaña de phishing"
---

Una campaña de phishing en Hugging Face, la plataforma de referencia para compartir modelos de inteligencia artificial, usaba su propio generador de webs con IA para crear páginas falsas de inicio de sesión de Microsoft, Google, PayPal o Coinbase. La firma de seguridad Aikido localizó 42 de estas páginas alojadas en Hugging Face Spaces, que suplantaban a 28 marcas. Al menos 29 se habían construido con DeepSite, la herramienta que permite crear una web describiéndola en lenguaje natural. Hugging Face ya las ha retirado, pero el caso muestra cómo la IA y los dominios de servicios conocidos rebajan el listón para montar estafas convincentes.

## Cómo funcionaba el phishing en Hugging Face

Hugging Face Spaces permite publicar pequeñas aplicaciones y webs estáticas con una dirección del tipo `nombre.hf.space`. Es un servicio legítimo y muy usado por desarrolladores, lo que da a los enlaces una apariencia de confianza y ayuda a esquivar algunos filtros de correo.

Según el informe de Aikido, publicado el 24 de noviembre, los delincuentes describían a DeepSite la página que querían ("un portal de acceso de Microsoft", por ejemplo) y la herramienta la generaba. Los mensajes de cambios de muchas páginas eran literalmente las instrucciones que el atacante había dado a la IA, escritas en francés, inglés, hindi, portugués, indonesio o ruso. En algunos casos pedían a la herramienta que ocultara la página a los rastreadores de Google y Bing para evitar que la detectaran.

Un ejemplo: una copia del acceso de Microsoft pedía correo, contraseña, teléfono y fecha de nacimiento, enviaba los datos a un bot de Telegram y luego redirigía a la víctima al Outlook real para que no sospechara. Se construyó en 15 cambios, 14 de ellos en apenas 90 minutos. Otras páginas solicitaban también los códigos de un solo uso de la verificación en dos pasos, datos de tarjeta o claves de banca online. Los datos robados acababan en bots de Telegram (25 páginas), webhooks de Discord (11) o servicios de formularios (6).

## ¿A quién afecta?

Las páginas imitaban sobre todo servicios de correo e identidad (13), bancos y pagos (12), redes sociales (9) y plataformas de videojuegos (6). Algunas llevaban publicadas más de un año: la más antigua, una copia de Instagram, data de abril de 2025.

Aikido no tiene datos de visitas, así que **no se sabe cuántas personas introdujeron sus credenciales**. La empresa avisó a Hugging Face el 16 de octubre, cuando 34 de las 42 páginas seguían activas, y el 29 de octubre todas estaban desactivadas o ya no eran accesibles. El problema no afecta a los modelos ni a los conjuntos de datos de la plataforma, solo a estas webs alojadas en Spaces.

No es un caso aislado. El abuso de servicios gratuitos y de confianza (Google Forms, Notion, GitHub Pages, Cloudflare Workers…) para alojar phishing es una técnica clásica, y la IA generativa la hace más rápida: lo contamos en [phishing con IA: por qué los correos fraudulentos ya no tienen faltas de ortografía](/phishing-con-ia/).

## Cómo protegerte del phishing alojado en webs legítimas

- **Mira el dominio, no el diseño.** Microsoft, Google o tu banco nunca te pedirán iniciar sesión en una dirección acabada en `hf.space` ni en ningún otro dominio que no sea el suyo. Como resume Aikido, hay que tratar los enlaces a hf.space en un correo "como cualquier otro dominio de alojamiento gratuito".
- **Entra siempre desde un marcador o tecleando la dirección**, nunca desde el enlace de un correo o mensaje.
- **Usa passkeys o llaves de seguridad** cuando el servicio lo permita: no se pueden "teclear" en una web falsa. Más consejos en [cómo detectar un correo de phishing](/como-detectar-phishing/).
- **Si metiste tus datos**, cambia la contraseña de inmediato, cierra todas las sesiones abiertas, revisa la actividad reciente y comprueba que no te hayan añadido métodos de verificación o reglas de reenvío en el correo. Si diste datos bancarios, llama a tu banco.

Para las empresas, Aikido recomienda buscar en los registros de DNS, proxy y pasarela de correo los nombres de host que publica en su informe y marcar para revisión los correos entrantes con enlaces a hf.space. Los nuevos casos se pueden notificar a security@huggingface.co.

## Fuentes

- [Aikido Security – Attackers use Hugging Face's AI to make phishing pages](https://www.aikido.dev/blog/hugging-face-phishing-pages)
- [Cyber Security News – Hackers Use Hugging Face AI to Build Fake Microsoft and Google Login Pages](https://cybersecuritynews.com/hugging-face-ai-phishing-pages/)
- [Mallory – Attackers Abuse Hugging Face Spaces and DeepSite AI to Host Credential-Stealing Pages](https://mallory.ai/stories/01a2130b-320f-7e97-9c2f-bd81c38dc846)
