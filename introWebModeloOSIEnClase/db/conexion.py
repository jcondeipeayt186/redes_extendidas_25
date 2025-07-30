import mysql.connector  # Importamos el conector de MySQL para Python

# Definimos una función para obtener la conexión a la base de datos
# Esta función será utilizada por otros módulos para conectarse a MySQL

def obtener_conexion():
    # Creamos la conexión usando los parámetros de la base de datos
    # Cambia el usuario y la contraseña según tu configuración de MySQL
    conexion = mysql.connector.connect(
        host='localhost',         # Dirección del servidor MySQL
        user='usuario',              # Usuario de MySQL (ajusta según tu configuración)
        password='clave',              # Contraseña de MySQL (ajusta según tu configuración)
        database='redesiniciandoflask'  # Nombre de la base de datos
    )
    return conexion  # Retornamos el objeto de conexión 