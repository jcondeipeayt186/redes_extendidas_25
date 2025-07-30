# Aplicación Web: Modelo OSI y Redes de Computadoras

Este proyecto es una aplicación web educativa desarrollada con Python, Flask y MySQL. Permite explorar conceptos de redes de computadoras y gestionar protocolos del modelo OSI.

## Estructura del proyecto

```
introWebModeloOSIEnClase/
│
├── app.py                # Archivo principal de la aplicación Flask
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo
│
├── db/                   # Archivos relacionados con la base de datos
│   ├── redesiniciandoflask.sql   # Script SQL para crear la base de datos y tabla
│   ├── conexion.py               # Conexión a MySQL
│   └── gestiondb.py              # Gestión de la tabla protocolos
│
├── templates/            # Archivos HTML de las páginas
│   ├── index.html
│   ├── redes.html
│   └── protocolos.html
│
└── img/                  # Imágenes para la aplicación (agrega aquí tus imágenes)
```

## Tecnologías utilizadas
- Python
- Flask
- MySQL
- mysql-connector-python
- HTML5

## Pasos para ejecutar la aplicación

1. **Clona el repositorio o copia la carpeta del proyecto.**

2. **Crea un entorno virtual (opcional pero recomendado):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crea la base de datos en MySQL:**

   - Ingresa a tu consola de MySQL y ejecuta el script `db/redesiniciandoflask.sql`:
     ```sql
     SOURCE ruta/a/introWebModeloOSIEnClase/db/redesiniciandoflask.sql;
     ```
   - Asegúrate de ajustar el usuario y contraseña en `db/conexion.py` según tu configuración de MySQL.

5. **Agrega una imagen representativa en la carpeta `img/` y nómbrala `redes.jpg` (o ajusta el nombre en `index.html`).**

6. **Ejecuta la aplicación Flask:**

   ```bash
   python app.py
   ```

7. **Abre tu navegador y visita:**
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Notas
- Por ahora, la funcionalidad CRUD de protocolos no está implementada, solo la estructura.
- Los archivos HTML son simples, sin estilos CSS.
- Si tienes dudas, revisa los comentarios en el código fuente. 