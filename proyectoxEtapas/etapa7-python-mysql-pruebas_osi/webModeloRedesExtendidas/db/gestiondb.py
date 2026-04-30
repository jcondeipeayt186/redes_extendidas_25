# gestiondb.py
# Este archivo contiene funciones para manipular la base de datos:
# crear usuarios, obtener usuarios, actualizar accesos y guardar/consultar pruebas.
# Todas las funciones usan la conexión definida en conexion.py

from .conexion import get_db_connection

# Función para crear un nuevo usuario en la base de datos
# Guarda el nombre de usuario, contraseña y fechas de creación/acceso

def crear_usuario(username, password):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO usuarios (username, pass, creation, lastaccess, access) VALUES (%s, %s, NOW(), NOW(), 1)"
            cursor.execute(sql, (username, password))
        conn.commit()
    finally:
        conn.close()

# Función para obtener un usuario por su nombre de usuario
# Devuelve un diccionario con los datos del usuario si existe

def obtener_usuario(username):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE username = %s"
            cursor.execute(sql, (username,))
            return cursor.fetchone()
    finally:
        conn.close()

# Función para actualizar la fecha y cantidad de accesos de un usuario
# Se llama cada vez que el usuario inicia sesión correctamente

def actualizar_acceso_usuario(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE usuarios SET lastaccess = NOW(), access = access + 1 WHERE id = %s"
            cursor.execute(sql, (user_id,))
        conn.commit()
    finally:
        conn.close()

# Función para guardar el resultado de una prueba realizada por el usuario
# Guarda la capa, tipo de test, protocolo, datos de entrada, resultado, fecha y usuario

def crear_resultado_testcapa(capa, testcapa, protocol, datain, resultado, user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO resultadoTestCapa (capa, testcapa, protocol, datain, resultado, fecha, user)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """
            cursor.execute(sql, (capa, testcapa, protocol, datain, resultado, user_id))
        conn.commit()
    finally:
        conn.close()

# Función para obtener el historial de pruebas de un usuario
# Devuelve una lista de diccionarios con los resultados de las pruebas

def obtener_resultados_usuario(user_id):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM resultadoTestCapa WHERE user = %s"
            cursor.execute(sql, (user_id,))
            return cursor.fetchall()
    finally:
        conn.close() 