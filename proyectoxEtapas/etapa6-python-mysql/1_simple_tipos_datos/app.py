from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'usuario',        # cámbialo por tu usuario
    'password': 'clave',    # cámbialo por tu contraseña
    'database': 'tipos_mysql'
}

@app.route("/")
def index():
    # Mostrar registros existentes
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ejemplo_tipos")
    registros = cursor.fetchall()
    conn.close()
    return render_template("index.html", registros=registros)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/agregar", methods=["POST"])
def agregar():
    # Captura de datos desde el formulario
    edad = request.form.get("edad")
    anio = request.form.get("anio")
    poblacion = request.form.get("poblacion")
    dni = request.form.get("dni")
    telefono = request.form.get("telefono")
    precio = request.form.get("precio")
    temperatura = request.form.get("temperatura")
    altura = request.form.get("altura")
    codigo = request.form.get("codigo")
    nombre = request.form.get("nombre")
    comentario = request.form.get("comentario")
    descripcion = request.form.get("descripcion")
    articulo = request.form.get("articulo")
    documento = request.form.get("documento")
    fecha_nac = request.form.get("fecha_nac")
    hora = request.form.get("hora")
    anio_solo = request.form.get("anio_solo")
    activo = request.form.get("activo")
    sexo = request.form.get("sexo")
    
    # Días laborales (checkbox múltiples → lista)
    dias_laborales = request.form.getlist("dias_laborales")
    dias_laborales_str = ",".join(dias_laborales) if dias_laborales else None

    # Conexión e inserción
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
    INSERT INTO ejemplo_tipos
    (edad, anio, poblacion, dni, telefono, precio, temperatura, altura, codigo, nombre, comentario, descripcion, articulo, documento, fecha_nac, hora, anio_solo, activo, sexo, dias_laborales)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values = (edad, anio, poblacion, dni, telefono, precio, temperatura, altura, codigo, nombre, comentario, descripcion, articulo, documento, fecha_nac, hora, anio_solo, activo, sexo, dias_laborales_str)
    
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/editar/<int:registro_id>")
def editar(registro_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre, edad, dni, telefono, sexo, activo, dias_laborales FROM ejemplo_tipos WHERE id = %s", (registro_id,))
    registro = cursor.fetchone()
    conn.close()
    if not registro:
        return redirect("/")
    # Transformar dias_laborales a lista para checks (soporta SET, lista o cadena)
    raw_dias = registro.get("dias_laborales")
    if isinstance(raw_dias, (set, list, tuple)):
        dias_list = [str(d).strip() for d in raw_dias]
    elif isinstance(raw_dias, str):
        dias_list = [d.strip() for d in raw_dias.split(",") if d.strip()]
    else:
        dias_list = []
    return render_template("edit.html", r=registro, dias_list=dias_list)

@app.route("/actualizar/<int:registro_id>", methods=["POST"])
def actualizar(registro_id):
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    dni = request.form.get("dni")
    telefono = request.form.get("telefono")
    sexo = request.form.get("sexo")
    activo = request.form.get("activo")
    dias_laborales = request.form.getlist("dias_laborales")
    dias_laborales_str = ",".join(dias_laborales) if dias_laborales else None

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
    UPDATE ejemplo_tipos
    SET nombre=%s, edad=%s, dni=%s, telefono=%s, sexo=%s, activo=%s, dias_laborales=%s
    WHERE id=%s
    """
    values = (nombre, edad, dni, telefono, sexo, activo, dias_laborales_str, registro_id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/eliminar/<int:registro_id>", methods=["POST"])
def eliminar(registro_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ejemplo_tipos WHERE id = %s", (registro_id,))
    conn.commit()
    conn.close()
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)

