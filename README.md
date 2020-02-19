# pocket-json-ops

Pocket JSON Ops es un diccionario de ritmos extraido del libro [Pocket Operations](https://b.shittyrecording.studio/file/shittyrec/print/Pocket+Operations+(2019-07-01).pdf), que compila distintos ritmos de percusión.

## Qué es este repo

Con el fin de usar los distintos ritmos compilados con distintos lenguajes de livecoding, convertimos el PDF en un hermoso JSON para la computadora de le musique moderne. Este fue generado a partir de una version HTML, generada a lo bruto desde el PDF, y luego parseada usando la libreria de Python Beautiful Soup 4.

## Qué falta hacer

Faltaría extraer también la acentuación de los distintos ritmos, identificada por la fila "AC" en las tablas del libro. Actualment se encuentran exceptuadas y no son extraídas por el script soup.py.

Scrapeado con [amor](https://colectivo-de-livecoders.gitlab.io/).
