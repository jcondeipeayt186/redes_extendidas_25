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
│   └── gestiondb.py              # Gestión de la tabla protocolos (CRUD)
│
├── templates/            # Archivos HTML de las páginas
│   ├── index.html
│   ├── redes.html
│   ├── protocolos.html           # Página con formulario y tabla CRUD
│   └── editar_protocolo.html     # Página para editar protocolos
│
├── static/               # Archivos estáticos (CSS, JS, imágenes)
│   ├── css/
│   │   ├── bootstrap.min.css     # Bootstrap CSS local
│   │   └── bootstrap.bundle.min.js # Bootstrap JS local
│   └── img/              # Imágenes para la aplicación
│
└── img/                  # Imágenes para la aplicación (carpeta alternativa)
```

## Tecnologías utilizadas
- Python
- Flask
- MySQL
- mysql-connector-python
- HTML5
- Bootstrap 5.3.2 (local)
- CSS3

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

5. **Agrega una imagen representativa en la carpeta `static/img/` y nómbrala como corresponda (por ejemplo, `red1.png`).**

6. **Ejecuta la aplicación Flask:**

   ```bash
   python app.py
   ```

7. **Abre tu navegador y visita:**
   - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Funcionalidad CRUD de Protocolos
- En la página "Protocolos" puedes:
  - Agregar un nuevo protocolo completando el formulario y presionando "Agregar Protocolo".
  - Ver todos los protocolos registrados en una tabla responsiva.
  - Editar un protocolo haciendo clic en "Editar" y modificando los datos.
  - Eliminar un protocolo presionando el botón "Eliminar" correspondiente.

## Características del diseño
- **Bootstrap 5.3.2**: Framework CSS para un diseño moderno y responsivo.
- **Navegación**: Barra de navegación con menú hamburguesa para dispositivos móviles.
- **Formularios**: Diseño mejorado con validación y campos organizados.
- **Tablas**: Tablas responsivas con estilos modernos.
- **Tarjetas**: Contenido organizado en tarjetas con sombras.
- **Botones**: Botones estilizados con colores semánticos.

## Notas
- Bootstrap se descarga localmente para evitar dependencias externas.
- La aplicación es completamente responsiva y funciona en dispositivos móviles.
- Si tienes dudas, revisa los comentarios en el código fuente. 