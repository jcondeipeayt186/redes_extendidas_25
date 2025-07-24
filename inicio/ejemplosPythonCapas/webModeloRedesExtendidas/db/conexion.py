# conexion.py
# Este archivo contiene la función para conectarse a la base de datos MySQL.
# Se utiliza en toda la aplicación para obtener una conexión y realizar consultas.

import pymysql

# Función para obtener una conexión a la base de datos
# Modifica los parámetros según tu configuración de MySQL
# - host: dirección del servidor MySQL (usualmente 'localhost')
# - user: tu usuario de MySQL
# - password: tu contraseña de MySQL
# - database: nombre de la base de datos a usar
# - cursorclass: permite obtener los resultados como diccionarios

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='jconde',
        password='julian2023!',
        database='redesextendidas',
        cursorclass=pymysql.cursors.DictCursor
    ) 