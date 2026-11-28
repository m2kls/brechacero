---
title: "Claves de AWS en Docker Hub: los bots las roban en 8 segundos"
description: "Un estudio con 300 imágenes trampa en Docker Hub y otros registros muestra que las claves de AWS filtradas se usan en una mediana de 51 segundos. Cómo evitarlo."
date: 2026-11-28T04:57:00+01:00
category: noticias
tags: [Docker Hub, AWS, claves API, secretos, contenedores, OpenAI, nube]
author: Redacción
photo: "File:Rear of rack at NERSC data center - closeup.jpg"
imageAlt: "Cableado de un rack de servidores en un centro de datos, donde se ejecutan contenedores Docker en la nube"
---

Subir a Docker Hub una imagen de contenedor con una clave de AWS dentro equivale, en la práctica, a regalarla. Es la conclusión de un estudio de la Universidad de Stony Brook (Nueva York) que publicó 300 imágenes trampa con credenciales falsas en ocho registros públicos: en Docker Hub, la mitad de las claves de AWS se usaron en menos de un minuto y la más rápida, a los 7,86 segundos de publicarse. "La publicación y el compromiso son, a efectos prácticos, el mismo evento", resumen los autores.

## Qué han descubierto con las claves de AWS en Docker Hub

Los investigadores Billy Tsouvalas y Nick Nikiforakis crearon copias de la imagen oficial de nginx e insertaron en ellas claves de API señuelo de AWS, OpenAI y Anthropic. Las subieron durante cuatro meses a registros como Docker Hub, Amazon ECR y Red Hat Quay, y vigilaron qué pasaba.

Los números son contundentes:

- Las claves de AWS recibieron más de **140.000 llamadas desde más de 5.000 direcciones IP**.
- En la primera ronda, con 100 imágenes en Docker Hub, más de la mitad de las claves se usaron en el primer minuto, el 93% en cinco y todas en quince. La **mediana fue de 51 segundos**.
- Las claves de OpenAI y Claude acabaron agotadas por terceros. En un caso, una clave recibió 143 peticiones y más de 18 millones de tokens en menos de 24 horas, alrededor de un mes después de la última subida, lo que hace sospechar que se revenden.

Los autores llaman *ContainerBots* a estos escáneres automáticos. No ejecutan las imágenes: las trampas ocultas que se activarían al arrancar el contenedor solo saltaron tres veces en 300 imágenes. Lo que hacen es consultar el catálogo de imágenes recientes, descargar solo las capas donde suele haber credenciales y buscar cadenas con forma de clave. Casi todos empezaban con una consulta de AWS del tipo "¿quién soy?" para comprobar qué permisos tenía la clave.

Dos detalles más: las claves con permisos restringidos no recibieron ninguna llamada que consumiera recursos, y las imágenes con nombres que sonaban sensibles atrajeron más del doble de descargas. El experimento costó unos 60 dólares en créditos, todos gastados por los atacantes. Docker ha reconocido el aviso y revisa los resultados.

## ¿A quién afecta?

A cualquier desarrollador o empresa que publique imágenes de contenedor, aunque sea por un descuido: un archivo `.env` copiado en el `Dockerfile`, credenciales usadas durante la compilación que quedan en una capa intermedia o una imagen de pruebas subida como pública. Borrar el archivo en una capa posterior no sirve, porque las capas anteriores siguen descargables.

El problema no es nuevo, pero el estudio le pone cronómetro. Encaja con otros datos de esta semana: VulnCheck calcula que el 18% de las vulnerabilidades explotadas que analizó se usaron para robar secretos, y GitGuardian estima que el 64% de los secretos válidos filtrados en 2022 siguen funcionando en 2026. Los ataques recientes a repositorios y cuentas de desarrolladores, como el [hackeo de SAP a través de GitHub](/hackeo-sap-github-codigo-fuente/) o el de [Radware y las claves de nube de sus clientes](/hackeo-radware-claves-nube-clientes/), demuestran el valor que tienen esas credenciales.

## Cómo evitar filtrar claves en imágenes de contenedor

- **No metas secretos en la imagen.** Usa variables de entorno en tiempo de ejecución o un gestor de secretos (AWS Secrets Manager, Vault, secretos de Kubernetes).
- **Usa los secretos de compilación de Docker** (`--secret` en BuildKit) en lugar de copiar archivos con credenciales, y un `.dockerignore` que excluya `.env`, claves y configuraciones locales.
- **Escanea antes de publicar** con herramientas de detección de secretos en la canalización de CI.
- **Permisos mínimos y claves temporales.** El estudio confirma que una clave con permisos restringidos es mucho menos atractiva. Mejor aún, roles y credenciales de corta duración.
- **Si se ha filtrado, revócala ya.** No basta con borrar la imagen: a los pocos segundos alguien puede tener una copia. Rota la clave y revisa los registros de CloudTrail o del proveedor.

Los autores también piden a los registros que analicen las imágenes al subirlas y avisen al usuario, y que limiten el listado público de imágenes recientes que hoy aprovechan los bots.

## Fuentes

- [Help Net Security: bots exploited leaked AWS key from Docker image in under 8 seconds](https://www.helpnetsecurity.com/2026/11/25/docker-aws-key-exposure-bots/)
- [BleepingComputer: cloud keys leaked in Docker Hub images are stolen within seconds](https://bleepingcomputer.com/news/security/cloud-keys-leaked-in-docker-hub-images-are-stolen-within-seconds)
- [SC Media: attackers exploit leaked credentials in Docker Hub images within seconds](https://www.scworld.com/brief/researchers-find-attackers-exploit-leaked-credentials-in-docker-hub-images-within-seconds)
- [Artículo académico (ACM)](https://dl.acm.org/doi/epdf/10.1145/3830454.3846791)
- [VulnCheck: robo de credenciales mediante vulnerabilidades explotadas](https://www.vulncheck.com/blog/credential-harvesting)
