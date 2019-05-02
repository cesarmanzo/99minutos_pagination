# 99minutos pagination

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Ejemplo de paginación para 99minutos. Por rapidez, construido con CookieCutter. Funciona con Django y Docker para poder probarlo rápidamente. Utiliza base de datos PostgreSQL. Es un API muy básica que permite crear órdenes y obtenerlas.

# Prerequisitos

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Instrucciones

Levantar el servidor
```bash
docker-compose build
docker-compose up
```

No es necesario Iniciar Sesión para ver la parte de Órdenes (para ver y crear usuarios, sí).

DRF cuenta con una interfaz para ver y crear requests. Una vez levantado el proyecto, entrar a http://localhost:8000/api/v1/orders/

Podremos observar la lista de órdenes con paginación de 10 items por página y dar clic en alguna orden. En la parte de abajo, se puede hacer un POST para agregar una orden, o puede hacerse desde alguna herramienta externa como Postman. En el documento del examen adjunto una captura de pantalla de cómo se ve con los datos que yo ingresé



Para correr comandos dentro de un contenedor:

```bash
docker-compose run --rm web [comando]
```
