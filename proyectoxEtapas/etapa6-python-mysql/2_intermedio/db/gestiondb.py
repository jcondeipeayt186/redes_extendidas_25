from .conexion import obtener_conexion  # Importamos la función de conexión

# Función para agregar un nuevo protocolo a la base de datos
def agregar_protocolo(nombre, acronimo, nombreCapa, fechaActualizacion, descripcion):
    conexion = obtener_conexion()  # Obtenemos la conexión a la base de datos
    cursor = conexion.cursor()
    # Ejecutamos la consulta SQL para insertar un nuevo protocolo
    cursor.execute(
        "INSERT INTO protocolos (nombre, acronimo, nombreCapa, fechaActualizacion, descripcion) VALUES (%s, %s, %s, %s, %s)",
        (nombre, acronimo, nombreCapa, fechaActualizacion, descripcion)
    )
    conexion.commit()  # Guardamos los cambios en la base de datos
    cursor.close()
    conexion.close()

# Función para obtener todos los protocolos de la base de datos
def obtener_protocolos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)  # Usamos dictionary=True para obtener los resultados como diccionarios
    cursor.execute("SELECT * FROM protocolos")
    protocolos = cursor.fetchall()  # Obtenemos todos los registros
    cursor.close()
    conexion.close()
    return protocolos

# Función para obtener un protocolo por su id
def obtener_protocolo_por_id(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM protocolos WHERE id = %s", (id,))
    protocolo = cursor.fetchone()
    cursor.close()
    conexion.close()
    return protocolo

# Función para actualizar un protocolo existente
def actualizar_protocolo(id, nombre, acronimo, nombreCapa, fechaActualizacion, descripcion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE protocolos SET nombre=%s, acronimo=%s, nombreCapa=%s, fechaActualizacion=%s, descripcion=%s WHERE id=%s",
        (nombre, acronimo, nombreCapa, fechaActualizacion, descripcion, id)
    )
    conexion.commit()
    cursor.close()
    conexion.close()

# Función para eliminar un protocolo por su id
def eliminar_protocolo(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM protocolos WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close() 