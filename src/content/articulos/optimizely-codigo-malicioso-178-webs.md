---
title: "Código malicioso en una herramienta de marketing llega a las webs de al menos 178 empresas"
description: "El 16 de noviembre alguien inyectó JavaScript en proyectos de Optimizely Web Experimentation. Podía robar tarjetas, cookies y cambiar direcciones de criptomonedas."
date: 2026-11-24
category: noticias
tags: [cadena de suministro, Optimizely, JavaScript, skimming, robo de tarjetas]
author: Redacción
imageCredit: "Ilustración: Brecha Cero"
photo: "File:Code_on_computer_monitor_(Unsplash).jpg"
imageAlt: "Código fuente en un monitor"
---

Muchas webs grandes cargan scripts de terceros para hacer pruebas A/B, medir audiencias o personalizar contenido. Si alguien compromete a uno de esos proveedores, su código acaba ejecutándose en el navegador de los visitantes de todas las webs que lo usan. Eso es lo que ocurrió el 16 de noviembre con Optimizely Web Experimentation.

## Qué pasó

Según recogen Senthorus y The Layman Security, citando a KrebsOnSecurity, se insertó JavaScript malicioso en proyectos de clientes de Optimizely. Ese código se sirvió a quienes visitaban las webs de al menos 178 organizaciones, entre ellas medios de comunicación, bancos, tiendas y empresas tecnológicas.

El código podía:

- Copiar los datos de tarjetas que se escribían en formularios de pago (lo que se conoce como skimming).
- Robar cookies y hacer capturas de pantalla.
- Cambiar direcciones de monederos de criptomonedas por las del atacante.
- Intentar comprometer iPhone y iPad antiguos.

## Cómo respondió Optimizely

La empresa bloqueó la vía de acceso, eliminó el código inyectado, revocó tokens y cerró sesiones activas.

## Por qué importa

Este tipo de ataque a la cadena de suministro es especialmente difícil de ver desde fuera: la web legítima no ha sido hackeada, pero sirve código malicioso igualmente. La empresa afectada a menudo no se entera hasta que su proveedor lo comunica.

## Qué puedes hacer

Como usuario:

- Mantén actualizado el sistema de tu móvil. Las cadenas de exploits iban contra dispositivos antiguos sin parches.
- Revisa los movimientos de tu tarjeta si compraste online entre el 16 y el 17 de noviembre, y activa las notificaciones de cargos en la app del banco.
- Si envías criptomonedas, comprueba la dirección de destino completa antes de confirmar.

Si administras una web:

- Haz inventario de todos los scripts de terceros que cargas y quita los que no uses.
- Usa una política de seguridad de contenido (CSP) para limitar desde dónde se puede cargar código.
- En las páginas de pago, carga el menor número posible de scripts externos.

## Fuentes

- [Senthorus, revisión semanal del 16 al 22 de noviembre](https://blog.senthorus.ch/posts/weekly_reviews/23_11_2026)
- [The Layman Security, 22 de noviembre de 2026](https://thelaymansecurity.com/cybersecurity-news-this-week-2026-11-22/)
