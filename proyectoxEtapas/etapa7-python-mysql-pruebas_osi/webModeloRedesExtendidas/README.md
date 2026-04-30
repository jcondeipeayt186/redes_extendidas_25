# Proyecto WebModeloRedesExtendidas

## Descripción General

Esta aplicación web está desarrollada con **Python** y el microframework **Flask**. Permite a los usuarios aprender y experimentar con el modelo OSI de redes de computadoras, realizando pruebas interactivas sobre cada capa y guardando los resultados en una base de datos MySQL.

El proyecto está pensado para quienes están dando sus primeros pasos en Python y Flask, por lo que el código y las plantillas incluyen comentarios explicativos.

## ¿Qué puedes hacer con esta web?
- Registrarte o iniciar sesión como usuario.
- Realizar pruebas interactivas sobre distintas capas del modelo OSI (por ejemplo, ping, consulta DNS, chat TCP, codificación Base64, etc.).
- Visualizar el historial de todas tus pruebas realizadas.
- Aprender sobre los protocolos y funciones de cada capa del modelo OSI.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask. Aquí se definen las rutas, la lógica de negocio y la interacción con la base de datos.
- `db/`:
  - `conexion.py`: Función para conectarse a la base de datos MySQL.
  - `gestiondb.py`: Funciones para crear usuarios, autenticar, guardar y consultar pruebas.
  - `redesextendidas.sql`: Script para crear la base de datos y las tablas necesarias.
- `templates/`: Archivos HTML que definen la interfaz de usuario. Usan Bootstrap para el diseño y heredan de una plantilla base.
- `img/`: Carpeta para imágenes utilizadas en la web.
- `requirements.txt`: Lista de dependencias de Python necesarias para ejecutar la aplicación.

## ¿Cómo funciona la aplicación?

1. **Inicio y registro:**
   - Al ingresar a la web, puedes registrarte o iniciar sesión desde la página de registro.
   - Una vez autenticado, puedes acceder a las pruebas interactivas y ver tu historial.

2. **Pruebas interactivas:**
   - Cada capa del modelo OSI tiene su propia página y, en algunas, puedes realizar pruebas (por ejemplo, hacer ping, consultar DNS, probar un chat TCP, etc.).
   - Los resultados de cada prueba se guardan en la base de datos, asociados a tu usuario.

3. **Historial:**
   - En la página de registro, si estás autenticado, verás una tabla con todas las pruebas que realizaste, incluyendo fecha, capa, tipo de prueba, protocolo, datos de entrada y resultado.

## ¿Cómo ejecutar el proyecto?

1. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Crea la base de datos:**
   - Ejecuta el script SQL en tu servidor MySQL:
   ```bash
   mysql -u root -p < db/redesextendidas.sql
   ```
   - Modifica el usuario y contraseña en `db/conexion.py` según tu configuración.
3. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```
4. **Abre tu navegador:**
   - Ve a [http://localhost:5000](http://localhost:5000)

## Consejos para principiantes
- Lee los comentarios en el código Python y en los archivos HTML para entender cada parte.
- Puedes modificar las pruebas o agregar nuevas funcionalidades para experimentar.
- Si tienes dudas, consulta la documentación oficial de Flask: https://flask.palletsprojects.com/

¡Éxitos en tu aprendizaje de Python y Flask! 

## Cómo crear un entorno virtual en Python y probar la aplicación

1. **Crea un entorno virtual (recomendado):**
   - Abre una terminal en la carpeta del proyecto.
   - Ejecuta el siguiente comando para crear el entorno virtual:
     ```bash
     python3 -m venv env
     ```
   - Activa el entorno virtual:
     - En Linux/Mac:
       ```bash
       source env/bin/activate
       ```
     - En Windows:
       ```cmd
       .\env\Scripts\activate
       ```

2. **Instala las dependencias:**
   - Con el entorno virtual activado, ejecuta:
     ```bash
     pip install -r requirements.txt
     ```

3. **Crea la base de datos:**
   - Ejecuta el script SQL en tu servidor MySQL:
     ```bash
     mysql -u root -p < db/redesextendidas.sql
     ```
   - Modifica el usuario y contraseña en `db/conexion.py` según tu configuración.

4. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

5. **Abre tu navegador:**
   - Ve a [http://localhost:5000](http://localhost:5000)

6. **Desactiva el entorno virtual (opcional):**
   - Cuando termines, puedes salir del entorno virtual con:
     ```bash
     deactivate
     ```

¡Usar un entorno virtual te ayuda a mantener tus proyectos organizados y evitar conflictos de dependencias entre diferentes proyectos de Python! 