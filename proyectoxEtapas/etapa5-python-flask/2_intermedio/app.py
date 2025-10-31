# Archivo principal de la aplicación web Flask
# Este archivo contiene la configuración y rutas de la aplicación web

# Importar Flask - el framework web que estamos usando
from flask import Flask, render_template, request, redirect, url_for, flash
# render_template: para renderizar archivos HTML
# request: para obtener datos de formularios y peticiones HTTP
# redirect: para redirigir a otras páginas
# url_for: para generar URLs de las rutas
# flash: para mostrar mensajes temporales al usuario

# Importar las funciones de gestión de la base de datos
from db.gestiondb import obtener_todos_protocolos, agregar_protocolo, obtener_protocolo_por_id, actualizar_protocolo, eliminar_protocolo

# Crear una instancia de la aplicación Flask
# __name__ es una variable especial de Python que contiene el nombre del módulo actual
app = Flask(__name__)

# Configurar una clave secreta para la aplicación
# Esta clave se usa para sesiones, mensajes flash, etc.
# En producción, esta clave debe ser más segura y no estar en el código
app.secret_key = 'mi_clave_secreta_para_flask'

# Definir las rutas de la aplicación web
# Las rutas son las URLs que los usuarios pueden visitar

@app.route('/')
def index():
    """
    Ruta principal de la aplicación (página de inicio)
    Esta función se ejecuta cuando alguien visita la URL raíz (/)
    """
    # Renderizar la plantilla HTML 'index.html'
    # Esta función busca el archivo en la carpeta 'templates'
    return render_template('index.html')

@app.route('/redes')
def redes():
    """
    Ruta para la página de redes de computadoras
    Esta función se ejecuta cuando alguien visita /redes
    """
    # Renderizar la plantilla HTML 'redes.html'
    return render_template('redes.html')

@app.route('/protocolos')
def protocolos():
    """
    Ruta para la página de protocolos
    Esta función se ejecuta cuando alguien visita /protocolos
    """
    # Obtener todos los protocolos de la base de datos
    # Esta función está definida en db/gestiondb.py
    lista_protocolos = obtener_todos_protocolos()
    
    # Renderizar la plantilla HTML 'protocolos.html' pasando los protocolos
    # Los protocolos estarán disponibles en la plantilla como variable 'protocolos'
    return render_template('protocolos.html', protocolos=lista_protocolos)

# Rutas para las capas del modelo OSI
@app.route('/capa1')
def capa1():
    """
    Ruta para la página de la Capa 1 - Física
    Esta función se ejecuta cuando alguien visita /capa1
    """
    return render_template('capa1.html')

@app.route('/capa2')
def capa2():
    """
    Ruta para la página de la Capa 2 - Enlace de Datos
    Esta función se ejecuta cuando alguien visita /capa2
    """
    return render_template('capa2.html')

@app.route('/capa3')
def capa3():
    """
    Ruta para la página de la Capa 3 - Red
    Esta función se ejecuta cuando alguien visita /capa3
    """
    return render_template('capa3.html')

@app.route('/capa4')
def capa4():
    """
    Ruta para la página de la Capa 4 - Transporte
    Esta función se ejecuta cuando alguien visita /capa4
    """
    return render_template('capa4.html')

@app.route('/capa5')
def capa5():
    """
    Ruta para la página de la Capa 5 - Sesión
    Esta función se ejecuta cuando alguien visita /capa5
    """
    return render_template('capa5.html')

@app.route('/capa6')
def capa6():
    """
    Ruta para la página de la Capa 6 - Presentación
    Esta función se ejecuta cuando alguien visita /capa6
    """
    return render_template('capa6.html')

@app.route('/capa7')
def capa7():
    """
    Ruta para la página de la Capa 7 - Aplicación
    Esta función se ejecuta cuando alguien visita /capa7
    """
    return render_template('capa7.html')

@app.route('/agregar_protocolo', methods=['GET', 'POST'])
def agregar_protocolo_web():
    """
    Ruta para agregar un nuevo protocolo
    Esta función maneja tanto GET (mostrar formulario) como POST (procesar formulario)
    """
    if request.method == 'POST':
        # Si es una petición POST, procesar el formulario enviado
        
        # Obtener los datos del formulario
        # request.form es un diccionario con los datos enviados por el formulario
        nombre = request.form['nombre']
        acronimo = request.form['acronimo']
        nombreCapa = request.form['nombreCapa']
        descripcion = request.form['descripcion']
        
        # Validar que todos los campos estén completos
        if nombre and acronimo and nombreCapa and descripcion:
            # Intentar agregar el protocolo a la base de datos
            resultado = agregar_protocolo(nombre, acronimo, nombreCapa, descripcion)
            
            if resultado:
                # Si se agregó correctamente, mostrar mensaje de éxito
                flash('Protocolo agregado correctamente', 'success')
            else:
                # Si hubo un error, mostrar mensaje de error
                flash('Error al agregar el protocolo', 'error')
        else:
            # Si faltan campos, mostrar mensaje de error
            flash('Todos los campos son obligatorios', 'error')
        
        # Redirigir de vuelta a la página de protocolos
        return redirect(url_for('protocolos'))
    
    else:
        # Si es una petición GET, mostrar el formulario
        return render_template('agregar_protocolo.html')

@app.route('/editar_protocolo/<int:id>', methods=['GET', 'POST'])
def editar_protocolo_web(id):
    """
    Ruta para editar un protocolo existente
    El parámetro <int:id> captura el ID del protocolo desde la URL
    """
    if request.method == 'POST':
        # Si es una petición POST, procesar el formulario de edición
        
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        acronimo = request.form['acronimo']
        nombreCapa = request.form['nombreCapa']
        descripcion = request.form['descripcion']
        
        # Validar que todos los campos estén completos
        if nombre and acronimo and nombreCapa and descripcion:
            # Intentar actualizar el protocolo en la base de datos
            resultado = actualizar_protocolo(id, nombre, acronimo, nombreCapa, descripcion)
            
            if resultado:
                flash('Protocolo actualizado correctamente', 'success')
            else:
                flash('Error al actualizar el protocolo', 'error')
        else:
            flash('Todos los campos son obligatorios', 'error')
        
        # Redirigir de vuelta a la página de protocolos
        return redirect(url_for('protocolos'))
    
    else:
        # Si es una petición GET, obtener el protocolo y mostrar el formulario
        protocolo = obtener_protocolo_por_id(id)
        
        if protocolo:
            # Si el protocolo existe, mostrar el formulario de edición
            return render_template('editar_protocolo.html', protocolo=protocolo)
        else:
            # Si no existe, mostrar mensaje de error y redirigir
            flash('Protocolo no encontrado', 'error')
            return redirect(url_for('protocolos'))

@app.route('/eliminar_protocolo/<int:id>')
def eliminar_protocolo_web(id):
    """
    Ruta para eliminar un protocolo
    Esta función se ejecuta cuando alguien visita /eliminar_protocolo/<id>
    """
    # Intentar eliminar el protocolo de la base de datos
    resultado = eliminar_protocolo(id)
    
    if resultado:
        flash('Protocolo eliminado correctamente', 'success')
    else:
        flash('Error al eliminar el protocolo', 'error')
    
    # Redirigir de vuelta a la página de protocolos
    return redirect(url_for('protocolos'))

# Manejo de errores - página 404 (página no encontrada)
@app.errorhandler(404)
def pagina_no_encontrada(error):
    """
    Función que se ejecuta cuando se accede a una página que no existe
    """
    return render_template('404.html'), 404

# Configuración para ejecutar la aplicación
if __name__ == '__main__':
    # Esta condición se cumple solo si ejecutamos este archivo directamente
    # (no si lo importamos desde otro archivo)
    
    # Habilitar el modo debug para desarrollo
    # En modo debug, Flask recarga automáticamente cuando hay cambios en el código
    # y muestra mensajes de error detallados
    app.debug = True
    
    # Ejecutar la aplicación
    # host='0.0.0.0' permite acceder desde cualquier IP (no solo localhost)
    # port=5000 es el puerto por defecto de Flask
    # threaded=True permite manejar múltiples peticiones simultáneamente
    print("Iniciando aplicación Flask...")
    print("Abre tu navegador y ve a: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, threaded=True) 