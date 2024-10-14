# Manual para la implementación de la aplicación web Flask: AppModelGame

## Introducción
Este manual proporcionará instrucciones paso a paso para descargar y configurar la aplicación web AppGames, que utiliza el microframework Flask de Python. AppGames es una aplicación de aprendizaje automático que predice las ventas globales de videojuegos según el género, la plataforma y la compañía de desarrollo del juego.

## Requisitos previos
- Python 3.7 o superior
- Git instalado en tu sistema

## Paso 1: Clonar el repositorio

- Para descargar el código de la aplicación, primero debes clonar el repositorio desde GitHub. Para hacerlo, abre tu terminal y escribe el siguiente comando:

``` bash
git clone https://github.com/jc-gi/AppGames

```

- Reemplaza "username" con el nombre de usuario de GitHub donde se aloja el repositorio.

## Paso 2: Crear un entorno virtual (opcional)

- Crear un entorno virtual es una buena práctica para mantener las dependencias de tu proyecto aisladas del resto de tu sistema. Aquí te mostramos cómo puedes hacerlo con el módulo venv que viene incorporado con Python:

``` bash
python3 -m venv env
```
- Para activar el entorno virtual:

* En Windows:

``` bash

env\Scripts\activate
```
* En Unix o MacOS:

``` bash
source env/bin/activate
```

## Paso 3: Instalar las dependencias

- Dentro de la carpeta del proyecto, instala las dependencias necesarias con el siguiente comando:

``` bash 
pip install -r requirements.txt

```

## Paso 4: Ejecutar la aplicación

- Finalmente, puedes ejecutar la aplicación con el siguiente comando:

``` bash
python app.py
```
- Ahora deberías poder acceder a la aplicación en tu navegador web en Source: http://127.0.0.1:5000.

## Descripción de la aplicación

- La aplicación AppGames toma tres entradas del usuario: el género del juego, la plataforma y la compañía de desarrollo. Luego, utiliza un modelo de regresión lineal previamente entrenado para predecir las ventas globales del juego.

- El modelo fue entrenado con un conjunto de datos que contiene información sobre diferentes videojuegos, como el género, la plataforma, la compañía de desarrollo y las ventas globales. Se utilizó la biblioteca scikit-learn para entrenar el modelo.

- El modelo y los datos se cargan en la aplicación al inicio. Cuando el usuario envía el formulario en la página web, los datos se procesan y se pasan al modelo para hacer la predicción. El resultado se muestra luego en una nueva página.