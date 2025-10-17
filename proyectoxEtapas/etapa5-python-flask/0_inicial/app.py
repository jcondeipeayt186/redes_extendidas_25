from flask import Flask, render_template, request, redirect, url_for


# Creamos la aplicación Flask.
# __name__ le dice a Flask dónde está el archivo principal para ubicar recursos (templates, static, etc.).
app = Flask(__name__)


# =====================================================================
# "Base de datos" en memoria (solo para práctica)
# ---------------------------------------------------------------------
# En un proyecto real los datos se guardan en una base de datos.
# Aquí usamos una lista de diccionarios para simplificar y poder probar
# las operaciones básicas (listar, agregar, modificar, eliminar) sin
# necesitar instalar nada adicional.
# Cada protocolo tiene: id (int), nombre (str) y capa (str).
# =====================================================================
protocolos = [
    {"id": 1, "nombre": "HTTP", "capa": "Capa 7 - Aplicación"},
    {"id": 2, "nombre": "IP", "capa": "Capa 3 - Red"},
]

# Llevamos un contador simple para asignar el próximo ID disponible.
next_id = 3


# =====================================================================
# Ruta de inicio (home)
# ---------------------------------------------------------------------
# Cuando el usuario visita "/" devolvemos la plantilla index.html.
# render_template busca los archivos dentro de la carpeta "templates".
# =====================================================================
@app.route("/")
def index():
    return render_template("index.html")


# =====================================================================
# Ruta de Protocolos (listar, agregar y precargar edición)
# ---------------------------------------------------------------------
# - GET /protocolos: muestra la página con el listado y el formulario.
#   Si viene /protocolos?edit=<id>, precargamos ese protocolo en el formulario.
# - POST /protocolos: toma los datos del formulario y agrega uno nuevo.
# =====================================================================
@app.route("/protocolos", methods=["GET", "POST"])
def protocolos_view():
    global next_id

    # Si el método es POST, estamos intentando AGREGAR un nuevo protocolo.
    if request.method == "POST":
        # Obtenemos los valores enviados por el formulario.
        
        nombre = request.form.get("nombre", "").strip()
        """
        request.form: es un diccionario de Flask con los datos enviados por un formulario (método POST).
        .get("nombre", ""): intenta leer la clave "nombre". Si no existe (no fue enviada), devuelve la cadena vacía "" en lugar de lanzar error.
        .strip(): elimina espacios en blanco al inicio y al final de la cadena (incluye tabs y saltos de línea). 
        """
        capa = request.form.get("capa", "").strip()

        # Validación muy básica: ambos campos deben venir con valor.
        if nombre and capa:
            # Creamos el dict del nuevo protocolo y lo agregamos a la lista.
            protocolos.append({"id": next_id, "nombre": nombre, "capa": capa})
            next_id += 1  # avanzamos el contador para el próximo registro

        # Redirigimos a GET /protocolos para evitar reenvío de formularios.
        return redirect(url_for("protocolos_view"))

    # Si es GET, puede venir un parámetro ?edit=<id> para precargar datos.
    edit_id = request.args.get("edit", type=int)
    edit_item = None
    if edit_id is not None:
        # Buscamos el protocolo con ese id en nuestra "BD" en memoria.
        for p in protocolos:
            if p["id"] == edit_id:
                edit_item = p
                break

    # Enviamos a la plantilla la lista completa y, si corresponde,
    # el elemento (diccionario con los datos del protocolo) a editar (edit_item) para precargar el formulario.
    return render_template("protocolos.html", protocolos=protocolos, edit_item=edit_item)


# =====================================================================
# Eliminar un protocolo
# ---------------------------------------------------------------------
# - GET /protocolos/eliminar/<pid>: elimina el protocolo con ese id.
#   Luego redirige de vuelta a la lista.
# =====================================================================
@app.route("/protocolos/eliminar/<int:pid>")
def eliminar_protocolo(pid: int):
    global protocolos
    # Reemplazamos la lista por una nueva que no incluya el id recibido.
    protocolos = [p for p in protocolos if p["id"] != pid]
    return redirect(url_for("protocolos_view"))


# =====================================================================
# Modificar un protocolo existente
# ---------------------------------------------------------------------
# - POST /protocolos/modificar/<pid>: actualiza nombre y/o capa.
#   Usamos los valores del formulario. Si un campo viene vacío, no se
#   modifica (esto es opcional y esta asi para simplificar).
# =====================================================================
@app.route("/protocolos/modificar/<int:pid>", methods=["POST"])
def modificar_protocolo(pid: int):
    nombre = request.form.get("nombre", "").strip()
    capa = request.form.get("capa", "").strip()

    # Recorremos la lista y actualizamos el registro con id = pid.
    for p in protocolos:
        if p["id"] == pid:
            if nombre:
                p["nombre"] = nombre
            if capa:
                p["capa"] = capa
            break

    return redirect(url_for("protocolos_view"))

@app.route("/7b-redes")
def redes():
    return "Ahora pueden comenzar a programar web en Python con Flask. Aun no integramos MySQL."

@app.route("/prueba")
def prueba():
    return "Probando Flask"  

@app.route("/otroindex")
def otro():
    return render_template("index.html") 

# =====================================================================
# Punto de entrada de la aplicación
# ---------------------------------------------------------------------
# El bloque if __name__ == "__main__" permite ejecutar `python app.py`
# directamente para iniciar el servidor de desarrollo de Flask.
# debug=True reinicia el servidor automáticamente cuando detecta cambios
# en el código (útil para desarrollo, NO usar en producción).
# =====================================================================
if __name__ == "__main__":
    app.run(debug=True)


