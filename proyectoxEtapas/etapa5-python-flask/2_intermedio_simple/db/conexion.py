# Archivo de conexión a la base de datos MySQL
# Este archivo maneja la conexión con la base de datos MySQL

import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """
    Función para establecer conexión con la base de datos MySQL
    Retorna: objeto de conexión si es exitoso, None si hay error
    """
    try:
        # Crear la conexión con la base de datos
        # host: dirección del servidor MySQL (localhost para desarrollo local)
        # user: nombre de usuario de MySQL
        # password: contraseña del usuario
        # database: nombre de la base de datos que queremos usar
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',  # Cambiar por tu usuario de MySQL
            password='',  # Cambiar por tu contraseña de MySQL
            database='redesiniciandoflask'
        )
        
        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return conexion
            
    except Error as e:
        # Si hay un error, mostrar el mensaje de error
        print(f"Error al conectar a MySQL: {e}")
        return None

def cerrar_conexion(conexion):
    """
    Función para cerrar la conexión con la base de datos
    Parámetros: conexion - objeto de conexión a cerrar
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada")

def probar_conexion():
    """
    Función para probar la conexión a la base de datos
    Útil para verificar que todo esté configurado correctamente
    """
    conexion = conectar_bd()
    if conexion:
        cerrar_conexion(conexion)
        return True
    return False

# Si ejecutamos este archivo directamente, probar la conexión
if __name__ == "__main__":
    print("Probando conexión a la base de datos...")
    if probar_conexion():
        print("✅ Conexión exitosa")
    else:
        print("❌ Error en la conexión") 