# Archivo de gestión de la base de datos
# Este archivo contiene las funciones para realizar operaciones CRUD en la base de datos

from conexion import conectar_bd, cerrar_conexion
from mysql.connector import Error

def obtener_todos_protocolos():
    """
    Función para obtener todos los protocolos de la base de datos
    Retorna: lista de tuplas con los datos de los protocolos
    """
    conexion = conectar_bd()
    protocolos = []
    
    if conexion:
        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para obtener todos los protocolos
            # ORDER BY id DESC para mostrar los más recientes primero
            consulta = "SELECT id, nombre, acronimo, nombreCapa, fechaActualizacion, descripcion FROM protocolos ORDER BY id DESC"
            
            # Ejecutar la consulta
            cursor.execute(consulta)
            
            # Obtener todos los resultados
            protocolos = cursor.fetchall()
            
            # Cerrar el cursor
            cursor.close()
            
        except Error as e:
            print(f"Error al obtener protocolos: {e}")
        finally:
            # Cerrar la conexión
            cerrar_conexion(conexion)
    
    return protocolos

def agregar_protocolo(nombre, acronimo, nombreCapa, descripcion):
    """
    Función para agregar un nuevo protocolo a la base de datos
    Parámetros:
    - nombre: nombre completo del protocolo
    - acronimo: acrónimo del protocolo
    - nombreCapa: capa del modelo OSI a la que pertenece
    - descripcion: descripción del protocolo
    Retorna: True si se agregó exitosamente, False en caso contrario
    """
    conexion = conectar_bd()
    
    if conexion:
        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para insertar un nuevo protocolo
            # Los valores se pasan como parámetros para evitar inyección SQL
            consulta = "INSERT INTO protocolos (nombre, acronimo, nombreCapa, descripcion) VALUES (%s, %s, %s, %s)"
            valores = (nombre, acronimo, nombreCapa, descripcion)
            
            # Ejecutar la consulta
            cursor.execute(consulta, valores)
            
            # Confirmar los cambios en la base de datos
            conexion.commit()
            
            # Cerrar el cursor
            cursor.close()
            
            print(f"Protocolo '{nombre}' agregado exitosamente")
            return True
            
        except Error as e:
            print(f"Error al agregar protocolo: {e}")
            return False
        finally:
            # Cerrar la conexión
            cerrar_conexion(conexion)
    
    return False

def eliminar_protocolo(id_protocolo):
    """
    Función para eliminar un protocolo de la base de datos
    Parámetros:
    - id_protocolo: ID del protocolo a eliminar
    Retorna: True si se eliminó exitosamente, False en caso contrario
    """
    conexion = conectar_bd()
    
    if conexion:
        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para eliminar un protocolo
            consulta = "DELETE FROM protocolos WHERE id = %s"
            
            # Ejecutar la consulta
            cursor.execute(consulta, (id_protocolo,))
            
            # Confirmar los cambios en la base de datos
            conexion.commit()
            
            # Cerrar el cursor
            cursor.close()
            
            print(f"Protocolo con ID {id_protocolo} eliminado exitosamente")
            return True
            
        except Error as e:
            print(f"Error al eliminar protocolo: {e}")
            return False
        finally:
            # Cerrar la conexión
            cerrar_conexion(conexion)
    
    return False

def obtener_protocolo_por_id(id_protocolo):
    """
    Función para obtener un protocolo específico por su ID
    Parámetros:
    - id_protocolo: ID del protocolo a buscar
    Retorna: tupla con los datos del protocolo o None si no existe
    """
    conexion = conectar_bd()
    protocolo = None
    
    if conexion:
        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para obtener un protocolo específico
            consulta = "SELECT id, nombre, acronimo, nombreCapa, fechaActualizacion, descripcion FROM protocolos WHERE id = %s"
            
            # Ejecutar la consulta
            cursor.execute(consulta, (id_protocolo,))
            
            # Obtener el resultado
            protocolo = cursor.fetchone()
            
            # Cerrar el cursor
            cursor.close()
            
        except Error as e:
            print(f"Error al obtener protocolo: {e}")
        finally:
            # Cerrar la conexión
            cerrar_conexion(conexion)
    
    return protocolo

def actualizar_protocolo(id_protocolo, nombre, acronimo, nombreCapa, descripcion):
    """
    Función para actualizar un protocolo existente
    Parámetros:
    - id_protocolo: ID del protocolo a actualizar
    - nombre: nuevo nombre del protocolo
    - acronimo: nuevo acrónimo del protocolo
    - nombreCapa: nueva capa del modelo OSI
    - descripcion: nueva descripción del protocolo
    Retorna: True si se actualizó exitosamente, False en caso contrario
    """
    conexion = conectar_bd()
    
    if conexion:
        try:
            # Crear un cursor para ejecutar consultas SQL
            cursor = conexion.cursor()
            
            # Consulta SQL para actualizar un protocolo
            consulta = "UPDATE protocolos SET nombre = %s, acronimo = %s, nombreCapa = %s, descripcion = %s WHERE id = %s"
            valores = (nombre, acronimo, nombreCapa, descripcion, id_protocolo)
            
            # Ejecutar la consulta
            cursor.execute(consulta, valores)
            
            # Confirmar los cambios en la base de datos
            conexion.commit()
            
            # Cerrar el cursor
            cursor.close()
            
            print(f"Protocolo con ID {id_protocolo} actualizado exitosamente")
            return True
            
        except Error as e:
            print(f"Error al actualizar protocolo: {e}")
            return False
        finally:
            # Cerrar la conexión
            cerrar_conexion(conexion)
    
    return False 