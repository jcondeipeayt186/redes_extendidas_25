from flask import Flask, render_template  # Importamos Flask y render_template para usar plantillas HTML

app = Flask(__name__)  # Creamos la aplicación Flask

# Ruta para la página principal (index)
@app.route('/')
def index():
    # Renderiza el archivo index.html que estará en la carpeta templates
    return render_template('index.html')

# Ruta para la página de redes
@app.route('/redes')
def redes():
    # Renderiza el archivo redes.html que estará en la carpeta templates
    return render_template('redes.html')

# Ruta para la página de protocolos
@app.route('/protocolos')
def protocolos():
    # Renderiza el archivo protocolos.html que estará en la carpeta templates
    # Aquí en el futuro se mostrarán los protocolos desde la base de datos
    return render_template('protocolos.html')

# Este bloque permite ejecutar la aplicación solo si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la app en modo debug para ver errores en desarrollo 