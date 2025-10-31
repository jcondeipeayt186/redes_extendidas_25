# Aplicación Web de Redes de Computadoras

## Descripción del Proyecto

Esta es una aplicación web educativa desarrollada con Python, Flask y MySQL que explica los conceptos fundamentales de las redes de computadoras. La aplicación incluye información sobre dispositivos de red, topologías, tipos de redes, modelos de referencia (TCP/IP y OSI), y protocolos de comunicación.

## Características Principales

- **Página de Inicio**: Información general sobre la aplicación y stack de tecnologías utilizadas
- **Página de Redes**: Conceptos completos sobre redes de computadoras, incluyendo:
  - Introducción a las redes con ejemplo práctico (Las Higueras a Génova)
  - Dispositivos de red y medios de transmisión
  - Topologías de red (físicas y lógicas)
  - Tipos de redes (LAN, WAN, MAN, etc.)
  - Modelos de referencia (TCP/IP y OSI)
  - Historia y evolución de las redes
- **Página de Protocolos**: Información sobre protocolos del modelo OSI con:
  - Descripción detallada de cada capa
  - Gestión de protocolos en base de datos
  - Funcionalidades CRUD para protocolos
  - Ejemplos de uso práctico

## Stack de Tecnologías

### Backend
- **Python 3.x**: Lenguaje de programación principal
- **Flask 3.0.0**: Framework web ligero y flexible
- **MySQL**: Sistema de gestión de bases de datos
- **mysql-connector-python 8.2.0**: Conector oficial de MySQL para Python

### Frontend
- **HTML5**: Estructura del contenido web
- **CSS**: Estilos (para futuras mejoras)
- **JavaScript**: Interactividad (para futuras funcionalidades)

### Base de Datos
- **MySQL**: Sistema de gestión de bases de datos relacional
- **Tabla protocolos**: Almacena información sobre protocolos de red

## Estructura del Proyecto

```
introWebModeloOSIEnClase/
├── app.py                          # Archivo principal de la aplicación Flask
├── requirements.txt                 # Dependencias de Python
├── README.md                       # Este archivo de documentación
├── templates/                      # Plantillas HTML
│   ├── index.html                  # Página principal
│   ├── redes.html                  # Página de redes de computadoras
│   ├── protocolos.html             # Página de protocolos
│   ├── agregar_protocolo.html     # Formulario para agregar protocolos
│   ├── editar_protocolo.html      # Formulario para editar protocolos
│   └── 404.html                   # Página de error 404
├── img/                           # Imágenes del proyecto
│   └── redes.png                  # Imagen representativa de redes
└── db/                           # Archivos de base de datos
    ├── conexion.py                # Configuración de conexión a MySQL
    ├── gestiondb.py               # Funciones CRUD para la base de datos
    └── redesiniciandoflask.sql    # Script SQL para crear la base de datos
```

## Instalación y Configuración

### Prerrequisitos

1. **Python 3.7 o superior**
2. **MySQL Server** instalado y funcionando
3. **Git** (opcional, para clonar el repositorio)

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes Git
git clone <url-del-repositorio>
cd introWebModeloOSIEnClase

# O simplemente descarga y extrae los archivos
```

### Paso 2: Crear un Entorno Virtual

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
# Instalar todas las dependencias del requirements.txt
pip install -r requirements.txt
```

### Paso 4: Configurar la Base de Datos

1. **Acceder a MySQL**:
   ```bash
   mysql -u root -p
   ```

2. **Ejecutar el script SQL**:
   ```sql
   source db/redesiniciandoflask.sql;
   ```

3. **Verificar la creación**:
   ```sql
   USE redesiniciandoflask;
   SHOW TABLES;
   SELECT * FROM protocolos;
   ```

### Paso 5: Configurar la Conexión a la Base de Datos

Editar el archivo `db/conexion.py` con tus credenciales de MySQL:

```python
conexion = mysql.connector.connect(
    host='localhost',          # Tu servidor MySQL
    user='tu_usuario',         # Tu usuario de MySQL
    password='tu_password',     # Tu contraseña de MySQL
    database='redesiniciandoflask'
)
```

### Paso 6: Ejecutar la Aplicación

```bash
# Asegúrate de estar en el directorio del proyecto
cd introWebModeloOSIEnClase

# Ejecutar la aplicación
python app.py
```

### Paso 7: Acceder a la Aplicación

Abre tu navegador web y ve a:
```
http://localhost:5000
```

## Funcionalidades CRUD

La aplicación incluye operaciones CRUD completas para la gestión de protocolos:

- **Create (Crear)**: Agregar nuevos protocolos a la base de datos
- **Read (Leer)**: Visualizar todos los protocolos almacenados
- **Update (Actualizar)**: Modificar información de protocolos existentes
- **Delete (Eliminar)**: Remover protocolos de la base de datos

## Rutas de la Aplicación

- `/` - Página principal (index)
- `/redes` - Página de redes de computadoras
- `/protocolos` - Página de protocolos con tabla de datos
- `/agregar_protocolo` - Formulario para agregar protocolos
- `/editar_protocolo/<id>` - Formulario para editar protocolos
- `/eliminar_protocolo/<id>` - Eliminar protocolos

## Base de Datos

### Estructura de la Tabla `protocolos`

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT | Identificador único (auto-increment) |
| nombre | VARCHAR(100) | Nombre completo del protocolo |
| acronimo | VARCHAR(20) | Acrónimo del protocolo |
| nombreCapa | VARCHAR(50) | Capa del modelo OSI |
| fechaActualizacion | TIMESTAMP | Fecha de última actualización |
| descripcion | TEXT | Descripción del protocolo |

### Protocolos Incluidos por Defecto

La base de datos incluye protocolos de ejemplo como:
- TCP (Transmission Control Protocol)
- IP (Internet Protocol)
- HTTP (Hypertext Transfer Protocol)
- FTP (File Transfer Protocol)
- SMTP (Simple Mail Transfer Protocol)
- DNS (Domain Name System)
- UDP (User Datagram Protocol)
- ARP (Address Resolution Protocol)

## Desarrollo

### Modo Debug

La aplicación está configurada en modo debug para desarrollo:
- Recarga automática cuando hay cambios en el código
- Mensajes de error detallados
- Acceso desde cualquier IP (host='0.0.0.0')

### Estructura de Archivos

- **app.py**: Contiene todas las rutas y lógica principal
- **db/conexion.py**: Maneja la conexión a MySQL
- **db/gestiondb.py**: Contiene funciones CRUD para la base de datos
- **templates/**: Plantillas HTML con Jinja2

## Solución de Problemas

### Error de Conexión a MySQL
1. Verificar que MySQL esté ejecutándose
2. Comprobar credenciales en `db/conexion.py`
3. Asegurar que la base de datos existe

### Error de Módulos No Encontrados
1. Verificar que el entorno virtual esté activado
2. Ejecutar `pip install -r requirements.txt`
3. Verificar versión de Python (3.7+)

### Error de Puerto en Uso
1. Cambiar el puerto en `app.py` línea 150
2. Verificar que no haya otra aplicación usando el puerto 5000

## Contribuciones

Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Crear un Pull Request

## Licencia

Este proyecto es educativo y está disponible para uso académico.

## Contacto

Para preguntas o sugerencias sobre este proyecto educativo de redes de computadoras.

---

**Nota**: Esta aplicación está diseñada con fines educativos para aprender sobre redes de computadoras, Flask, y bases de datos MySQL. 