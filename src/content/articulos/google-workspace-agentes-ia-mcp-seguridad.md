---
title: "Google Workspace obligará a los agentes de IA a usar MCP o CLI desde 2027"
description: "Google exigirá desde el 1 de febrero de 2027 que los agentes de IA accedan a Gmail, Drive y Docs solo por MCP o CLI, con permisos mínimos y confirmación humana."
date: 2026-11-26T20:58:00+01:00
category: noticias
tags: [Google Workspace, agentes de IA, MCP, Gmail, Google Drive, seguridad IA, inyección de prompts]
author: Redacción
photo: "File:Googleplex HQ (cropped).jpg"
imageAlt: "Sede de Google en Mountain View, empresa que endurece las reglas de Google Workspace para agentes de IA"
---

**Google Workspace** cambiará las reglas para los agentes de inteligencia artificial que leen y escriben en Gmail, Drive, Docs o Calendar. A partir del **1 de febrero de 2027**, cualquier agente de IA que quiera acceder a los datos de una cuenta de Workspace tendrá que hacerlo a través de los servidores **MCP** (Model Context Protocol) oficiales de Google o de su herramienta de línea de comandos, y no por las API REST de siempre. La compañía lo anunció el 25 de noviembre junto a un paquete de controles de seguridad pensados para frenar el uso indebido de estos asistentes.

## Qué cambia para los agentes de IA en Google Workspace

Google ha declarado disponibles para todos los clientes los servidores MCP de Workspace, que cubren Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat y Tasks, y la Workspace CLI. Un nuevo anexo a las condiciones de uso, el *Workspace AI Tools Addendum*, obliga a los agentes a usar esas vías. Las aplicaciones tradicionales que no son agentes podrán seguir usando las API REST.

Las principales exigencias son:

- **Identificadores OAuth propios para cada agente**, con permisos mínimos. Google anuncia también aprobaciones con caducidad "próximamente".
- **Confirmación humana obligatoria** para acciones delicadas: enviar un correo, cambiar los permisos de compartición de un archivo de Drive o hacer ediciones masivas.
- **Límites de datos**: los agentes no podrán guardar de forma permanente datos en bruto de Workspace, usarlos para entrenar modelos ni extraerlos de forma masiva, y deberán borrarlos cuando el usuario desconecte la herramienta.
- A partir del 1 de abril de 2027 se empezará a facturar el uso por cuotas.

## ¿Por qué Google pone estas restricciones?

El motivo es la seguridad. Un agente de IA con acceso al correo y a los documentos de una empresa es un objetivo muy atractivo: si alguien consigue engañarlo con una **inyección de prompts** escondida en un correo o en un documento, puede convencerlo de reenviar información confidencial o de compartir carpetas con un extraño. Google lo resume así: "Las comprobaciones de políticas, los límites de datos y la confirmación humana tienen que estar en el camino de la petición".

Al canalizar todo por sus propios servidores MCP, Google puede aplicar esas reglas en un único punto, registrar lo que hace cada agente y cortarle el acceso al instante. Los administradores verán en la consola qué agentes están conectados, podrán auditarlos y revocarlos.

La medida llega en un momento en el que los ataques con agentes de IA ya son reales. Esta misma semana, Microsoft explicó que el grupo chino [Salt Typhoon usa la plataforma de IA ARTEX para automatizar ataques](/microsoft-artex-ia-salt-typhoon/), y el NCSC británico y Suiza alertaron de los [primeros ciberataques con agentes de IA contra organizaciones](/ncsc-ciberataques-agentes-ia/).

## Novedades para Google Cloud: Agent Gateway

En la parte de Google Cloud, la empresa ha lanzado **Cloud Agent Gateway**, una pasarela que verifica la identidad de cada agente frente a un registro, aplica los permisos de IAM, bloquea por defecto las conexiones salientes no autorizadas y analiza las peticiones con Model Armor, su filtro contra la inyección de prompts. Las organizaciones podrán exigir MFA o aprobación humana antes de que un agente lea un almacenamiento sensible, cambie permisos o toque sistemas de producción.

Google anuncia también, sin fecha, controles para impedir que los agentes accedan a los mensajes de Gmail o a carpetas concretas de Drive, integrados con la prevención de pérdida de datos (DLP) y el cifrado del lado del cliente.

## Qué deberían hacer las empresas que usan Workspace

- **Revisar ya qué aplicaciones y agentes** tienen acceso OAuth a las cuentas de la organización y retirar los que no se usen.
- Configurar las reglas de DLP y vigilar los registros de OAuth para detectar accesos raros.
- Si desarrolláis agentes propios, planificar la migración a MCP o CLI antes de febrero de 2027 y añadir confirmaciones humanas y filtros contra la inyección de prompts.
- Formar a los empleados: un agente con permisos amplios multiplica el daño de un simple [correo de phishing](/como-detectar-phishing/).

## Fuentes

- [Google Cloud Blog: Deploying agents safely in your enterprise](https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise)
- [Help Net Security: Google mandates MCP or CLI access for Workspace AI agents starting February 2027](https://www.helpnetsecurity.com/2026/11/26/google-ai-agent-security-requirements/)
