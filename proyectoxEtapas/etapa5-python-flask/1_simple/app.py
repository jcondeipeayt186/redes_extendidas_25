# Archivo principal de la aplicación Flask
# Este es el punto de entrada de nuestra aplicación web

# Importar Flask y sus componentes necesarios
from flask import Flask, render_template, request, redirect, url_for, flash
# Flask: el framework web principal
# render_template: para renderizar archivos HTML
# request: para manejar datos enviados desde formularios
# redirect: para redirigir a otras páginas
# url_for: para generar URLs de forma segura
# flash: para mostrar mensajes temporales al usuario


# Crear una instancia de la aplicación Flask
# __name__ es una variable especial de Python que contiene el nombre del módulo actual
app = Flask(__name__)

# Configurar una clave secreta para la aplicación
# Esta clave se usa para firmar cookies y otros datos de sesión
# En producción, deberías usar una clave secreta más segura
app.secret_key = 'mi_clave_secreta_super_segura_123'

# Almacenamiento en memoria (simple) para evitar uso de base de datos
# Nota: Esto se reinicia cada vez que se reinicia la aplicación
protocolos_memoria = []
proximo_id = 1


# Definir las rutas (URLs) de nuestra aplicación
# Cada función que empiece con @app.route() define una página web



@app.route('/')
def index():
    """
    Función que maneja la página principal (ruta '/')
    Esta es la página que se muestra cuando alguien visita nuestro sitio web
    """
    # Renderizar el template 'index.html' y pasarle datos
    # Los datos se pasan como un diccionario y estarán disponibles en el HTML
    return render_template('index.html', 
                         titulo="Redes de Computadoras - Modelo OSI",
                         subtitulo="Introducción a las redes de computadoras")

@app.route('/protocolos', methods=['GET', 'POST'])
def protocolos():
    """
    Función que maneja la página de protocolos
    Puede recibir tanto GET (mostrar página) como POST (procesar formulario)
    """
    # Si la petición es POST (envío de formulario)
    if request.method == 'POST':
        # Obtener los datos del formulario
        # request.form es un diccionario con todos los campos del formulario
        nombre = request.form.get('nombre')
        acronimo = request.form.get('acronimo')
        nombreCapa = request.form.get('nombreCapa')
        descripcion = request.form.get('descripcion')
        
        # Validar que todos los campos estén completos
        if nombre and acronimo and nombreCapa and descripcion:
            # Agregar a almacenamiento en memoria
            agregado = agregar_protocolo_en_memoria(nombre, acronimo, nombreCapa, descripcion)
            if agregado:
                flash('Protocolo agregado exitosamente!', 'success')
            else:
                flash('Error al agregar el protocolo', 'error')
        else:
            # Si faltan campos, mostrar mensaje de error
            flash('Todos los campos son obligatorios', 'error')
        
        # Redirigir a la misma página para evitar reenvío del formulario
        return redirect(url_for('protocolos'))
    
    # Si la petición es GET (mostrar página)
    # Obtener todos los protocolos desde memoria
    protocolos_lista = list(protocolos_memoria)
    
    # Renderizar el template con los protocolos
    return render_template('protocolos.html', 
                         titulo="Protocolos del Modelo OSI",
                         protocolos=protocolos_lista)

@app.route('/eliminar_protocolo/<int:id>')
def eliminar_protocolo_ruta(id):
    """
    Función para eliminar un protocolo específico
    Parámetros:
    - id: ID del protocolo a eliminar (se obtiene de la URL)
    """
    # Intentar eliminar el protocolo
    if eliminar_protocolo(id):
        flash('Protocolo eliminado exitosamente!', 'success')
    else:
        flash('Error al eliminar el protocolo', 'error')
    
    # Redirigir de vuelta a la página de protocolos
    return redirect(url_for('protocolos'))

# Rutas para las diferentes capas del modelo OSI (placeholder)
# Estas rutas están preparadas para futuras implementaciones

@app.route('/capa1')
def capa1():
    """Página para la Capa 1 - Física"""
    return render_template('capa1.html', titulo="Capa 1 - Física")

@app.route('/capa2')
def capa2():
    """Página para la Capa 2 - Enlace de Datos"""
    return render_template('capa2.html', titulo="Capa 2 - Enlace de Datos")

@app.route('/capa3')
def capa3():
    """Página para la Capa 3 - Red"""
    return render_template('capa3.html', titulo="Capa 3 - Red")

@app.route('/capa4')
def capa4():
    """Página para la Capa 4 - Transporte"""
    return render_template('capa4.html', titulo="Capa 4 - Transporte")

@app.route('/capa5')
def capa5():
    """Página para la Capa 5 - Sesión"""
    return render_template('capa5.html', titulo="Capa 5 - Sesión")

@app.route('/capa6')
def capa6():
    """Página para la Capa 6 - Presentación"""
    return render_template('capa6.html', titulo="Capa 6 - Presentación")

@app.route('/capa7')
def capa7():
    """Página para la Capa 7 - Aplicación"""
    return render_template('capa7.html', titulo="Capa 7 - Aplicación")

# Manejo de errores
@app.errorhandler(404)
def pagina_no_encontrada(error):
    """
    Función que maneja el error 404 (página no encontrada)
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_interno(error):
    """
    Función que maneja el error 500 (error interno del servidor)
    """
    return render_template('500.html'), 500



#Funciones auxiliares
def agregar_protocolo_en_memoria(nombre, acronimo, nombre_capa, descripcion):
    global proximo_id
    protocolo = {
        'id': proximo_id,
        'nombre': nombre,
        'acronimo': acronimo,
        'nombreCapa': nombre_capa,
        'descripcion': descripcion
    }
    protocolos_memoria.append(protocolo)
    proximo_id += 1
    return True

def eliminar_protocolo(id_protocolo):
    indice_a_eliminar = None
    for indice, protocolo in enumerate(protocolos_memoria):
        if protocolo.get('id') == id_protocolo:
            indice_a_eliminar = indice
            break
    if indice_a_eliminar is not None:
        protocolos_memoria.pop(indice_a_eliminar)
        return True
    return False


# Configuración para ejecutar la aplicación
if __name__ == '__main__':
    """
    Este bloque solo se ejecuta si ejecutamos este archivo directamente
    (no si lo importamos desde otro archivo)
    """
    # Configurar la aplicación para modo desarrollo
    # debug=True: activa el modo debug (muestra errores detallados)
    # host='0.0.0.0': permite conexiones desde cualquier IP
    # port=5000: puerto en el que se ejecutará la aplicación
    app.run(debug=True, host='0.0.0.0', port=5000) 