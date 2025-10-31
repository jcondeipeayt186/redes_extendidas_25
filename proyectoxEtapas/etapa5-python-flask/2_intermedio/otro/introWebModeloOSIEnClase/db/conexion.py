# Archivo de conexión a la base de datos MySQL
# Este archivo contiene la configuración para conectarse a MySQL

import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """
    Función para establecer conexión con la base de datos MySQL
    Retorna: objeto de conexión si es exitoso, None si hay error
    """
    try:
        # Crear la conexión a MySQL
        # host: dirección del servidor MySQL (localhost para desarrollo local)
        # user: nombre de usuario de MySQL
        # password: contraseña del usuario
        # database: nombre de la base de datos a usar
        conexion = mysql.connector.connect(
            host='localhost',          # Servidor MySQL local
            user='jconde',               # Usuario por defecto (cambiar según tu configuración)
            password='julian2023!',               # Contraseña (dejar vacía si no tienes contraseña)
            database='redesiniciandoflask'  # Nombre de nuestra base de datos
        )
        
        # Verificar si la conexión fue exitosa
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            return conexion
            
    except Error as e:
        # Si hay un error, mostrar el mensaje
        print(f"Error al conectar a MySQL: {e}")
        return None

def cerrar_conexion(conexion):
    """
    Función para cerrar la conexión a la base de datos
    Parámetros: conexion - objeto de conexión a cerrar
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión a MySQL cerrada")

# Función de prueba para verificar la conexión
def probar_conexion():
    """
    Función para probar la conexión a la base de datos
    """
    conexion = conectar_bd()
    if conexion:
        print("¡Conexión exitosa!")
        cerrar_conexion(conexion)
    else:
        print("No se pudo conectar a la base de datos")

# Si ejecutamos este archivo directamente, probar la conexión
if __name__ == "__main__":
    probar_conexion() 