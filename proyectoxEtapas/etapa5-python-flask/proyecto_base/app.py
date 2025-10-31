from flask import Flask, render_template, request, redirect, url_for


# Creamos la aplicación Flask.
# __name__ le dice a Flask dónde está el archivo principal para ubicar recursos (templates, static, etc.).
app = Flask(__name__)



# =====================================================================
# Ruta de inicio (home)
# ---------------------------------------------------------------------
# Cuando el usuario visita "/" devolvemos la plantilla index.html.
# render_template busca los archivos dentro de la carpeta "templates".
# =====================================================================
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/otrapagina")
def otrapagina():
    return render_template("otrapagina.html")

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


