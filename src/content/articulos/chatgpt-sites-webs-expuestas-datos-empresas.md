---
title: "ChatGPT Sites: miles de webs creadas con IA exponen datos de empresas"
description: "ChatGPT Sites deja públicas webs internas: un estudio halla 12.830 accesibles a cualquiera, con datos de clientes y ventas. Cómo saber si tu empresa está expuesta."
date: 2026-11-28T02:58:00+01:00
category: privacidad
tags: [ChatGPT Sites, OpenAI, ChatGPT, fuga de datos, IA, privacidad, empresas]
author: Redacción
photo: "File:Smartphone with ChatGPT app and laptop (52917381683).jpg"
imageAlt: "Móvil con la aplicación de ChatGPT junto a un portátil, en relación con las webs de ChatGPT Sites expuestas"
---

ChatGPT Sites, la función de OpenAI que permite crear y publicar una aplicación web simplemente pidiéndosela al chatbot, se ha convertido en una nueva fuente de fugas de datos corporativos. La empresa de seguridad Pluto Security ha localizado 16.666 webs hechas con esta herramienta y 12.830 de ellas, el 77 %, se podían abrir sin iniciar sesión. Entre ellas hay paneles de ventas, listados de clientes y datos personales de vecinos de una urbanización. El estudio, publicado el 23 de noviembre, lo recogió este viernes SecurityWeek.

## Qué es ChatGPT Sites y por qué expone datos

ChatGPT Sites está integrado en ChatGPT (web, escritorio y Codex). El usuario describe lo que quiere, por ejemplo "un panel con las ventas del trimestre a partir de este Excel", y el asistente escribe el código, lo despliega y le asigna una dirección del tipo `nombre.propietario.chatgpt.site`. Cada web puede tener su propia base de datos y almacenamiento de archivos.

Por defecto, solo la ven el propietario y los administradores del espacio de trabajo. El problema aparece cuando se comparte: el usuario puede abrirla a personas concretas, a toda su organización o a cualquiera en internet si la publicación pública está permitida. Según Pluto, muchos autores no piensan en ese último paso como una publicación real, aunque la documentación de OpenAI trata cada dirección desplegada como un entorno de producción.

Hay un segundo fallo, más técnico y muy frecuente: las pantallas de inicio de sesión "caseras". Algunas webs piden una contraseña, pero los datos ya van incluidos en el código que descarga el navegador antes de mostrar el formulario. Es decir, el candado es solo visual.

## Qué datos han quedado al descubierto

Los investigadores revisaron a mano solo una pequeña parte y confirmaron exposición de información sensible en 27 organizaciones. Algunos ejemplos que describen:

- Una empresa de transporte de mercancías con 1.185 presupuestos a clientes desde 2023, tasas de conversión mensuales y un registro de pagos.
- Una cadena europea de tiendas con un listado de cierres de locales aún no anunciados.
- Una urbanización residencial con teléfono, correo y fecha de cumpleaños de 425 vecinos.
- Una empresa de la lista Fortune 500 con 207 reuniones comerciales, nombres y cargos de clientes potenciales y fichas de rendimiento de cada comercial.

Pluto subraya que reunió el conjunto de datos en unos diez minutos, buscando en archivos web, repositorios de código público, buscadores y rastreos de internet, así que la exposición real es probablemente mucho mayor. En el caso de la empresa de Fortune 500, el propietario restringió el acceso tras el aviso. El informe no menciona una respuesta de OpenAI.

## ¿Está expuesta mi empresa? Cómo comprobarlo

El caso recuerda a las fugas de cubos de almacenamiento en la nube mal configurados: la herramienta no tiene un fallo de seguridad como tal, sino que hace muy fácil publicar algo que nunca debió salir de la empresa. Las recomendaciones para reducir el riesgo:

- **Administradores**: hacer inventario de qué webs de ChatGPT Sites existen en la organización y quién puede abrirlas. En los planes Enterprise, activar Sites solo para los perfiles que lo necesiten y mantener desactivada la publicación pública.
- **Usuarios**: compartir con personas concretas o con el espacio de trabajo, nunca con "cualquiera con el enlace" si hay datos internos. Usar el inicio de sesión de ChatGPT en lugar de una contraseña programada a mano y borrar las webs que ya no se usen.
- **Política interna**: tratar cualquier archivo que se sube a un generador de aplicaciones con IA como un dato que sale de la empresa, igual que si se enviara a un proveedor externo.

Es el mismo patrón que vimos con las [fugas de prompts en proveedores de IA](/openrouter-fugas-prompts-proveedores-ia/) y con las [webs falsas creadas con IA en Hugging Face](/phishing-hugging-face-deepsite/): las herramientas de IA aceleran el trabajo, pero también la publicación de errores. Si tus datos personales han podido quedar expuestos, consulta [qué hacer si apareces en una filtración](/datos-en-filtracion-que-hacer/).

## Fuentes

- [Pluto Security: Your CRM Data Is One Search Away, 16,666 Exposed ChatGPT Sites](https://pluto.security/blog/exposed-chatgpt-sites/)
- [SecurityWeek: In Other News, Tanker Cyberattacks, EU Quantum Act, New VirusTotal Capabilities](https://www.securityweek.com/in-other-news-tanker-cyberattacks-eu-quantum-act-new-virustotal-capabilities/)
