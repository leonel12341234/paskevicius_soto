
# Proyecto Juego del Ahorcado

## Integrantes del equipo
Nombre:Leonel 
Apellido:Soto
DNI:48.537.499
Correo Electronico:lasoto@escuelasproa.edu.ar
paskevicius_soto
Nombre:Victorio 
Apellido:Paskevicius
DNI:48.074.409
Correo Electronico:vpaskevicius@escuelasproa.edu.ar

## Descripción
Este es un juego clásico del ahorcado, desarrollado como un proyecto de programación en Python para el curso de Programación III. El objetivo es adivinar una palabra seleccionada al azar, letra por letra, antes de que se acaben los intentos.

## Requisitos
- Python 3.8 o superior
- Biblioteca estándar de Python
- MySQL para la base de datos

## Instalación y uso
1. Clona el repositorio en tu computadora.
2. Ejecuta el archivo `estructura.sql` en MySQL para crear la base de datos.
3. Carga los datos iniciales con `datos.sql`.
4. Ejecuta `main.py` para iniciar el juego.

## Estructura de Archivos
- `aplicacion/`: contiene el código del juego.
  - `main.py`: archivo principal que ejecuta el juego y contiene el menú.
  - `funciones_juego.py`: funciones auxiliares del juego, como mostrar la palabra y validar intentos.
- `bd/`: contiene los scripts SQL y los diagramas de la base de datos.
  - `estructura.sql`: crea las tablas de la base de datos.
  - `datos.sql`: carga datos iniciales en las tablas.
  - `consultas.sql`: consultas SQL para el CRUD de la base de datos.
  - `base_de_datos_y_diagramas.pdf`: documento con los diagramas de la base de datos y una breve explicación de las consultas.

## Funcionalidades del Juego
1. Elige una palabra al azar de la lista.
2. Permite al usuario adivinar letra por letra.
3. Limita el número de intentos.
4. Finaliza cuando el usuario adivina la palabra o se queda sin intentos.
