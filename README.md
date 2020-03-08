# Web Scrapper Elemental 📥
Un web scrapper elemental desarrollado con Python utilizando las librerías Requests y Beautifulsoup+ durante las clases del [Curso de Python de Platzi](http://platzi.com/python "Curso de Python de Platzi").

El scrapper descarga imágenes (comics) del website https://xkcd.com/ 


## Para correr el scrapper sigue estos pasos:

1. Asegurate de tener Python3 instalado.
2. Clona el repositorio.
3. Accede desde terminal a la carpeta venv3 en los archivos del proyecto.*
4. Ejecuta el comando `$source bin/activate` para activar el entorno virtual.
5. Corre el script con `$python3 web_scraping.py`

*Las librerías Request y Beautifulsoup ya se encuentran en los archivos del proyecto. Fueron subidas para poder correr el proyecto más rápidamente y porque no representan mucho peso. 

##¿Cómo descargar más cantidad de imágenes?

Las imágenes en url están numeradas, para decargar más imágenes o imágenes de tal número a tal número modificar el range del ciclo for al inicio de la función run().