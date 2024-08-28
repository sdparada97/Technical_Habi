# TECHNICAL-HABI

Microservicio que busca las propiedades por diferentes filtros (STATUS, AÑO, CIUDAD) y sus reales caracteristicas.

## Technologies

<div align="center">
 <img width="50" src="https://user-images.githubusercontent.com/25181517/192107854-765620d7-f909-4953-a6da-36e1ef69eea6.png" alt="HTTP" title="HTTP"/>
 <img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/>
 <img width="50" src="https://user-images.githubusercontent.com/25181517/184117132-9e89a93b-65fb-47c3-91e7-7d0f99e7c066.png" alt="pytest" title="pytest"/>
 <img width="50" src="https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png" alt="MySQL" title="MySQL"/>
</div>

### Preguntas Generales

* Como puedo saber si mi codigo sigue los estadares de la PEP8 y demas buenas practicas en estilos de codificación?
  * Se configuro la libreria pre-commit para realizar la validaciones de las librerias `flake8 and isort` las cuales previamente se instalaron y se configuraron para asegurar que cada commit se haya realizado haciendo buenas practicas.

* Como simular las peticiones del front?
  * Se dockerizo el proyecto eso hace que se pueda realizar dos opciones:
    1. Mediante una colleccion de postman y ejecutando una serie de comandos Makefile
    se hace muy interactivo para realizar distintas peticiones.
    2. Mediante pytest las pruebas unitarias que se ejecutan mediante el docker y herramienats de pytest como parametrized, hacen que se pueda evaluar distintas peticiones.

* Porque no hay un Docker-compose en el proyecto?
  * Debido a que la base de datos esta alojada en la red no hay necesidad de realizar un servicio de bases de datos y unirlo con el servicio de la aplicación.

### Arquitectura

El diseño que se implementara tendra conceptos relacionados con arquitecturas limpias:

* Patron Repositorio
* Capa de servicio
* Controladores

Estos conceptos estan implmentados en este microservicio donde se enctran en los siguientes directorios:

* VIEWS:
  * En estos ficheros encontraremos las acciones especificas y el manejo de peticiones entrantes, donde se puedan controlar caracteristicas como (Excepciones HTTP, Esquemas Request/Response)

* SERVICES:
  * En estos ficheros tienen la responsabilidad de implmentar la logica del negocio y actua como una zona de abstracción entre la zona de datos y los controladores.

* REPOSITORY:
  * En estos ficheros se encargan de separar la logica del negocio del acceso hacia los datos

Esto hace que haya una mayor independencia de todas las capas y esto nso brinda muchos beneficios como lo es la flexibilidad, mantenibilidad y para realizar pruebas es mucho mas sencillo.

### Preguntas

* Como puedo hacer un microservicio sin framework?
  * Gracias a la libreria `Werkzeug` que brinda mas herramientas que la que viene por defecto `http` de python, ya que utiliza como base la liberia `WSGI` y ayuda mucho en configuraciones como los es la autenticación, enrutamiento, uso de los metodos del protocolo HTTP.

* Como puedo manejar la conexion a la base de datos?
  * Gracias a la libreria para mysql en python se realizo un decorador para que se pudiera realizar distintas consultas haciendo buenas practicas de usar y cerrar la conexion cuando ya se haya dejado de usar `@with_connection`.

* Como puedo darle seguridad a mi microservicio?
  * Se realizo una autenticación basada en un API-KEY pensando que este microservicio no fuera pensado para el uso para usuarios finales, si no mas bien para una apliación de reporteria.
  Si fuera para usuarios finales lo mejor seria implementar JWT o un API-TOKEN

* Como puedo manejar la capa de los filtros relacionada con la lógica del negocio?
  * En la capa del servicio se hizo una separación de la cosnulta relacionada a esos filtros haciendolos dinamicos, para la respuesta.

* Como puedo controlar el formato de lo que entra y lo que responde mis microservicios?
  * Gracias a la liberia `Marshmellow` realizo esquemas tanto para la request como para el response, brindadome serialización y deserialización de algunos campos asi mismo como validación de estos mismos, cumpliendo con la logica del negocio.

## Description

### ***SERVICIO DE " ME GUSTA " Y PROPUESTA DE MODELO :***

#### MODELO ANTIGUO

![entidad_relacion](https://github.com/sdparada97/API-Properties/assets/49702755/7f40e262-3ec2-457a-9f77-9a094d508b5a)

#### MODELO PROPUESTA

![new_entidad_relacion](https://github.com/sdparada97/API-Properties/assets/49702755/92afe9c6-e92a-4392-a490-143e6fd02d8e)

### ***JUSTIFICACION DE LA PROPUESTA :***

En base al anterior diagrama propuesto se deberia de eliminar la tabla status y crear un dominio de campo para ahorrar JOINS en las consultas.

Con esta sentencia SQL se podria añadir:

```sql
     CREATE DOMAIN status VARCHAR(10)
     CHECK (VALUE IN ('pre_venta', 'en_venta', 'vendido'));
```

## Instalación

Este `Makefile` te ayudará a automatizar la construcción, ejecución y limpieza de contenedores Docker para tu proyecto **Technical_Habi**. Sigue los pasos a continuación para utilizar cada comando disponible.

### Comandos Disponibles

| Comando           | Descripción                                      |
|-------------------|--------------------------------------------------|
| `make build`      | Construye la imagen Docker del proyecto.         |
| `make run`        | Ejecuta el contenedor Docker.                    |
| `make stop`       | Detiene la ejecución del contenedor Docker.      |
| `make clean`      | Elimina el contenedor Docker.                    |
| `make test`       | Ejecuta los tests dentro del contenedor Docker.  |
| `make help`       | Muestra la ayuda con los comandos disponibles.   |

## Pasos para Usar el Makefile

### 1. Construir la Imagen Docker

Para construir la imagen Docker de tu proyecto, ejecuta el siguiente comando:

```bash
make build
```

Este comando construirá la imagen utilizando el Dockerfile en tu directorio actual, etiquetándola como habi-test.

### 2. Ejecutar el Contenedor Docker

Para iniciar el contenedor, usa:

```bash
make run
```

Este comando ejecutará el contenedor y lo expondrá en el puerto 5000.

### 3. Detener el Contenedor

Para detener la ejecución del contenedor, utiliza:

```bash
make stop
```

Este comando detendrá el contenedor habi-test que se está ejecutando.

### 4. Eliminar el Contenedor

Si necesitas eliminar el contenedor, ejecuta:

```bash
make clean
```

Esto removerá el contenedor habi-test de tu sistema.

### 5. Ejecutar Pruebas

Para ejecutar las pruebas del proyecto con Pytest, utiliza:

```bash
make test
```

Esto ejecutará los tests definidos en la carpeta tests dentro del contenedor, asegurando que todo funcione correctamente.

### 6. Mostrar la Ayuda

Si necesitas ver los comandos disponibles y su descripción, usa:

```bash
make help
```

Esto mostrará una lista de los comandos y su propósito.

<span style="background:#53b418"> DENTRO DEL PROYECTO ESTARA LA COLECCION DE POSTMAN QUE PODRA IMPORTARLA DIRECTAMENTE Y REALIZAR LAS PETICIONES CUANDO TENGA EL PROYECTO ARRIAB CON EL DOCKER </span>
