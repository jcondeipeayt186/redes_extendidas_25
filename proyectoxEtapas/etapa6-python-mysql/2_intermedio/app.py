from flask import Flask, render_template, request, redirect, url_for  # Importamos Flask, render_template, request, redirect y url_for
from db.gestiondb import agregar_protocolo, obtener_protocolos, obtener_protocolo_por_id, actualizar_protocolo, eliminar_protocolo  # Importamos las funciones CRUD

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

# Ruta para mostrar y agregar protocolos
@app.route('/protocolos', methods=['GET', 'POST'])
def protocolos():
    if request.method == 'POST':
        # Si el método es POST, obtenemos los datos del formulario y agregamos el protocolo
        nombre = request.form['nombre']
        acronimo = request.form['acronimo']
        nombreCapa = request.form['nombreCapa']
        fechaActualizacion = request.form['fechaActualizacion']
        descripcion = request.form['descripcion']
        agregar_protocolo(nombre, acronimo, nombreCapa, fechaActualizacion, descripcion)
        return redirect(url_for('protocolos'))  # Redirigimos para evitar reenvío del formulario
    # Si el método es GET, mostramos la lista de protocolos
    lista_protocolos = obtener_protocolos()
    return render_template('protocolos.html', protocolos=lista_protocolos)

# Ruta para mostrar el formulario de edición de un protocolo
@app.route('/protocolos/editar/<int:id>', methods=['GET', 'POST'])
def editar_protocolo(id):
    if request.method == 'POST':
        # Si el método es POST, actualizamos el protocolo
        nombre = request.form['nombre']
        acronimo = request.form['acronimo']
        nombreCapa = request.form['nombreCapa']
        fechaActualizacion = request.form['fechaActualizacion']
        descripcion = request.form['descripcion']
        actualizar_protocolo(id, nombre, acronimo, nombreCapa, fechaActualizacion, descripcion)
        return redirect(url_for('protocolos'))
    # Si el método es GET, mostramos el formulario con los datos actuales
    protocolo = obtener_protocolo_por_id(id)
    return render_template('editar_protocolo.html', protocolo=protocolo)

# Ruta para eliminar un protocolo
@app.route('/protocolos/eliminar/<int:id>', methods=['POST'])
def eliminar_protocolo_route(id):
    eliminar_protocolo(id)
    return redirect(url_for('protocolos'))

# Este bloque permite ejecutar la aplicación solo si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la app en modo debug para ver errores en desarrollo 