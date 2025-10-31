# Archivo de gestión de la base de datos
# Este archivo contiene las funciones para realizar operaciones CRUD en la tabla protocolos

from db.conexion import conectar_bd, cerrar_conexion
from mysql.connector import Error

def obtener_todos_protocolos():
    """
    Función para obtener todos los protocolos de la base de datos
    Retorna: lista de tuplas con los datos de los protocolos
    """
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        
        if conexion:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para obtener todos los protocolos
            # SELECT: selecciona todas las columnas de la tabla protocolos
            consulta = "SELECT * FROM protocolos ORDER BY nombreCapa, nombre"
            
            # Ejecutar la consulta
            cursor.execute(consulta)
            
            # Obtener todos los resultados
            protocolos = cursor.fetchall()
            
            # Cerrar el cursor y la conexión
            cursor.close()
            cerrar_conexion(conexion)
            
            return protocolos
        else:
            print("No se pudo conectar a la base de datos")
            return []
            
    except Error as e:
        print(f"Error al obtener protocolos: {e}")
        return []

def agregar_protocolo(nombre, acronimo, nombreCapa, descripcion):
    """
    Función para agregar un nuevo protocolo a la base de datos
    Parámetros:
    - nombre: nombre completo del protocolo
    - acronimo: acrónimo del protocolo
    - nombreCapa: capa del modelo OSI donde se encuentra
    - descripcion: descripción del protocolo
    Retorna: True si se agregó correctamente, False en caso contrario
    """
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        
        if conexion:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para insertar un nuevo protocolo
            # INSERT INTO: inserta datos en la tabla protocolos
            # VALUES: especifica los valores a insertar
            consulta = """
                INSERT INTO protocolos (nombre, acronimo, nombreCapa, descripcion) 
                VALUES (%s, %s, %s, %s)
            """
            
            # Valores a insertar (tupla con los parámetros)
            valores = (nombre, acronimo, nombreCapa, descripcion)
            
            # Ejecutar la consulta con los valores
            cursor.execute(consulta, valores)
            
            # Confirmar los cambios en la base de datos
            conexion.commit()
            
            # Cerrar el cursor y la conexión
            cursor.close()
            cerrar_conexion(conexion)
            
            print(f"Protocolo '{nombre}' agregado correctamente")
            return True
        else:
            print("No se pudo conectar a la base de datos")
            return False
            
    except Error as e:
        print(f"Error al agregar protocolo: {e}")
        return False

def obtener_protocolo_por_id(id_protocolo):
    """
    Función para obtener un protocolo específico por su ID
    Parámetros: id_protocolo - ID del protocolo a buscar
    Retorna: tupla con los datos del protocolo o None si no existe
    """
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        
        if conexion:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para obtener un protocolo por ID
            consulta = "SELECT * FROM protocolos WHERE id = %s"
            
            # Ejecutar la consulta con el ID
            cursor.execute(consulta, (id_protocolo,))
            
            # Obtener el resultado (fetchone porque solo esperamos un registro)
            protocolo = cursor.fetchone()
            
            # Cerrar el cursor y la conexión
            cursor.close()
            cerrar_conexion(conexion)
            
            return protocolo
        else:
            print("No se pudo conectar a la base de datos")
            return None
            
    except Error as e:
        print(f"Error al obtener protocolo: {e}")
        return None

def actualizar_protocolo(id_protocolo, nombre, acronimo, nombreCapa, descripcion):
    """
    Función para actualizar un protocolo existente
    Parámetros:
    - id_protocolo: ID del protocolo a actualizar
    - nombre: nuevo nombre del protocolo
    - acronimo: nuevo acrónimo del protocolo
    - nombreCapa: nueva capa del modelo OSI
    - descripcion: nueva descripción del protocolo
    Retorna: True si se actualizó correctamente, False en caso contrario
    """
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        
        if conexion:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para actualizar un protocolo
            # UPDATE: actualiza datos en la tabla protocolos
            # SET: especifica las columnas y valores a actualizar
            # WHERE: condición para identificar el registro a actualizar
            consulta = """
                UPDATE protocolos 
                SET nombre = %s, acronimo = %s, nombreCapa = %s, descripcion = %s 
                WHERE id = %s
            """
            
            # Valores para la actualización
            valores = (nombre, acronimo, nombreCapa, descripcion, id_protocolo)
            
            # Ejecutar la consulta
            cursor.execute(consulta, valores)
            
            # Confirmar los cambios
            conexion.commit()
            
            # Cerrar el cursor y la conexión
            cursor.close()
            cerrar_conexion(conexion)
            
            print(f"Protocolo con ID {id_protocolo} actualizado correctamente")
            return True
        else:
            print("No se pudo conectar a la base de datos")
            return False
            
    except Error as e:
        print(f"Error al actualizar protocolo: {e}")
        return False

def eliminar_protocolo(id_protocolo):
    """
    Función para eliminar un protocolo de la base de datos
    Parámetros: id_protocolo - ID del protocolo a eliminar
    Retorna: True si se eliminó correctamente, False en caso contrario
    """
    try:
        # Conectar a la base de datos
        conexion = conectar_bd()
        
        if conexion:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para eliminar un protocolo
            # DELETE FROM: elimina registros de la tabla protocolos
            # WHERE: condición para identificar el registro a eliminar
            consulta = "DELETE FROM protocolos WHERE id = %s"
            
            # Ejecutar la consulta
            cursor.execute(consulta, (id_protocolo,))
            
            # Confirmar los cambios
            conexion.commit()
            
            # Cerrar el cursor y la conexión
            cursor.close()
            cerrar_conexion(conexion)
            
            print(f"Protocolo con ID {id_protocolo} eliminado correctamente")
            return True
        else:
            print("No se pudo conectar a la base de datos")
            return False
            
    except Error as e:
        print(f"Error al eliminar protocolo: {e}")
        return False

# Función de prueba para verificar las operaciones CRUD
def probar_operaciones_crud():
    """
    Función para probar las operaciones CRUD de la base de datos
    """
    print("=== Probando operaciones CRUD ===")
    
    # Probar obtener todos los protocolos
    print("\n1. Obteniendo todos los protocolos:")
    protocolos = obtener_todos_protocolos()
    for protocolo in protocolos:
        print(f"  - {protocolo[1]} ({protocolo[2]}) - {protocolo[3]}")
    
    # Probar agregar un nuevo protocolo
    print("\n2. Agregando nuevo protocolo:")
    resultado = agregar_protocolo(
        "Secure Shell", 
        "SSH", 
        "Capa 7 - Aplicación", 
        "Protocolo para acceso seguro a sistemas remotos"
    )
    print(f"  Resultado: {'Exitoso' if resultado else 'Fallido'}")
    
    # Probar obtener protocolo por ID
    print("\n3. Obteniendo protocolo por ID (1):")
    protocolo = obtener_protocolo_por_id(1)
    if protocolo:
        print(f"  - {protocolo[1]} ({protocolo[2]})")
    else:
        print("  No se encontró el protocolo")

# Si ejecutamos este archivo directamente, probar las operaciones
if __name__ == "__main__":
    probar_operaciones_crud() 