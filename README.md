# Proyecto Urban Grocers 

## Descripción: 
Este proyecto tiene como objetivo la automatización de pruebas para la aplicación Urban Grocers. Se centra en pruebas de integración y pruebas API utilizando Python y Pytest.

## Instalación
1. Clona este repositorio a tu directorio local.
2. Asegúrate de tener Python instalado.
4. Se recomienda la instalación del entorno "PyCharm" para la ejecución de las pruebas
3. Instala la biblioteca "requests" utilizando pip en la terminal de comandos:
```
pip install requests
```
4. instala "pytest" utilizando pip en la terminal de comandos:
```
pip install pytest
```

## Contenido
1. En el archivo "configuration.py" se configuran las URLs y rutas de solicitud.
2. En el archivo "data.py" se definen los cuerpos de las solicitudes.
3. En el archivo "sender_stand_request.py" se implementan las funciones para enviar solicitudes.
4. En el archivo "create_kit_name_kit_test.py" se crean las pruebas de integración.

## Ejecución de Pruebas
Para ejecutar las pruebas, simplemente utiliza el comando pytest en la terminal de comandos:
```
pytest
```
Asegúrate de estar en el directorio raíz del proyecto para ejecutar el comando.
Otra alternativa es utilizar el entorno "PyCharm" para correr las pruebas con Pytest.

## Pruebas Disponibles
- Crear un nuevo usuario
- Crear un nuevo kit de producto
- Pruebas de validez del nombre del kit:
-   Nombre con un solo carácter
-   Nombre con la longitud de caracteres máxima permitida (511)
-   Nombre vacío
-   Nombre con que supere la longitud de caracteres máxima permitida (512)
-   Nombre con caracteres especiales
-   Nombre separado con espacios
-   Nombre con números
-   Nombre sin parámetros
-   Nombre con números como parámetros