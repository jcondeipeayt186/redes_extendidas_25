# =============================
# IMPORTACIÓN DE LIBRERÍAS Y MÓDULOS
# =============================
# Flask: framework web
# render_template: para renderizar HTML
# redirect, url_for, request, session, flash: utilidades de Flask para formularios, sesiones y mensajes
# threading, time: para manejar el servidor TCP en segundo plano
# socket, base64: para pruebas de red y codificación
#
# Los módulos de la carpeta db/ permiten la conexión y gestión de la base de datos
from flask import Flask, render_template, redirect, url_for, request, session, flash
from db.conexion import get_db_connection
import os
from db.gestiondb import crear_usuario, obtener_usuario, actualizar_acceso_usuario, obtener_resultados_usuario, crear_resultado_testcapa
import socket
import base64
import threading
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from ftplib import FTP
from scapy.all import sniff
import uuid

# =============================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================
# Se crea la app Flask y se define la clave secreta para sesiones
app = Flask(__name__)
app.secret_key = os.urandom(24)

# =============================
# VARIABLES GLOBALES PARA EL CHAT TCP
# =============================
# Estas variables permiten manejar el estado del servidor TCP y el historial de mensajes
MAX_CLIENTES = 4
chat_clientes = {}
chat_messages = {}
tcp_server_thread = None
tcp_server_running = False


# =============================
# RUTAS PRINCIPALES DE LA APLICACIÓN
# =============================
# Cada @app.route define una URL de la web y su función asociada
# Página de inicio
@app.route('/')
def index():
    # Renderiza la página principal (index.html)
    return render_template('index.html')

# Introducción
@app.route('/introduccion')
def introduccion():
    return render_template('introduccion.html')

# Registro de usuario
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    historial = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = obtener_usuario(username)
        if user:
            if user['pass'] == password:
                session['user_id'] = user['id']
                session['username'] = user['username']
                actualizar_acceso_usuario(user['id'])
                flash('¡Bienvenido de nuevo, {}!'.format(username), 'success')
                historial = obtener_resultados_usuario(user['id'])
            else:
                flash('Contraseña incorrecta.', 'danger')
        else:
            crear_usuario(username, password)
            user = obtener_usuario(username)
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Usuario registrado exitosamente.', 'success')
            historial = obtener_resultados_usuario(user['id'])
    elif 'user_id' in session:
        historial = obtener_resultados_usuario(session['user_id'])
    return render_template('registro.html', historial=historial)

# Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('index'))

# Capa 1
@app.route('/capa1')
def capa1():
    return render_template('capa1.html')

# Capa 2
@app.route('/capa2')
def capa2():
    return render_template('capa2.html')

# Capa 3
@app.route('/capa3')
def capa3():
    return render_template('capa3.html')

# Capa 4 (Pruebas de red)
@app.route('/capa4', methods=['GET', 'POST'])
def capa4():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para realizar pruebas.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        host = request.form['host']
        puerto = int(request.form['puerto'])
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((host, puerto))
            s.close()
            resultado = f'Conexión TCP exitosa a {host}:{puerto}'
        except Exception as e:
            resultado = f'No se pudo conectar a {host}:{puerto} - {e}'
        crear_resultado_testcapa(
            capa='Transporte',
            testcapa='Conexión TCP',
            protocol='TCP',
            datain=f'{host}:{puerto}',
            resultado=resultado,
            user_id=session['user_id']
        )
    return render_template('capa4.html', resultado=resultado)

# Capa 5 (Simulación de sesión)
@app.route('/capa5', methods=['GET', 'POST'])
def capa5():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para realizar pruebas.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        accion = request.form['accion']
        if accion == 'iniciar':
            resultado = 'Sesión iniciada correctamente (simulación).'
        else:
            resultado = 'Sesión cerrada correctamente (simulación).'
        crear_resultado_testcapa(
            capa='Sesión',
            testcapa='Simulación de sesión',
            protocol='Simulación',
            datain=accion,
            resultado=resultado,
            user_id=session['user_id']
        )
    return render_template('capa5.html', resultado=resultado)

# Capa 6 (Codificación/decodificación Base64)
@app.route('/capa6', methods=['GET', 'POST'])
def capa6():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para realizar pruebas.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        texto = request.form['texto']
        accion = request.form['accion']
        try:
            if accion == 'codificar':
                resultado = base64.b64encode(texto.encode()).decode()
            else:
                resultado = base64.b64decode(texto.encode()).decode()
        except Exception as e:
            resultado = f'Error en la operación: {e}'
        crear_resultado_testcapa(
            capa='Presentación',
            testcapa='Base64',
            protocol='Base64',
            datain=f'{accion}: {texto}',
            resultado=resultado,
            user_id=session['user_id']
        )
    return render_template('capa6.html', resultado=resultado)

# Capa 7 (Consulta DNS)
@app.route('/capa7', methods=['GET', 'POST'])
def capa7():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para realizar pruebas.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        dominio = request.form['dominio']
        try:
            ip = socket.gethostbyname(dominio)
            resultado = f'La IP de {dominio} es {ip}'
        except Exception as e:
            resultado = f'Error al resolver dominio: {e}'
        crear_resultado_testcapa(
            capa='Aplicación',
            testcapa='Consulta DNS',
            protocol='DNS',
            datain=dominio,
            resultado=resultado,
            user_id=session['user_id']
        )
    return render_template('capa7.html', resultado=resultado)

# Capa 2 (Pruebas de enlace de datos)
@app.route('/capa2/pruebas', methods=['GET', 'POST'])
def capa2_pruebas():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para realizar pruebas.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        prueba = request.form['prueba']
        if prueba == 'mac':
            mac = uuid.getnode()
            mac_str = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
            resultado = f"Dirección MAC local: {mac_str}"
            crear_resultado_testcapa(
                capa='Enlace de Datos',
                testcapa='Obtener MAC local',
                protocol='Ethernet',
                datain='-',
                resultado=resultado,
                user_id=session['user_id']
            )
        elif prueba == 'interfaces':
            try:
                import subprocess
                interfaces = subprocess.check_output(['ip', 'a']).decode(errors='ignore')
                resultado = interfaces
            except Exception as e:
                resultado = f'Error al obtener interfaces: {e}'
            crear_resultado_testcapa(
                capa='Enlace de Datos',
                testcapa='Mostrar interfaces de red',
                protocol='Ethernet',
                datain='-',
                resultado=resultado[:5000],  # Limita el tamaño guardado
                user_id=session['user_id']
            )
        elif prueba == 'scapy':
            try:
                paquetes = sniff(count=3, timeout=5)
                resumen = paquetes.summary()
                resultado = f"Captura de 3 paquetes:\n{resumen}"
            except Exception as e:
                resultado = f'Error al capturar paquetes: {e}'
            crear_resultado_testcapa(
                capa='Enlace de Datos',
                testcapa='Captura de paquetes con Scapy',
                protocol='Ethernet',
                datain='-',
                resultado=resultado[:5000],
                user_id=session['user_id']
            )
    return render_template('capa2_pruebas.html', resultado=resultado)

# Capa 1 (Física) - Conversión de texto a binario/hexadecimal y de binario a texto/decimal
@app.route('/capa1/conversion', methods=['GET', 'POST'])
def capa1_conversion():
    resultado = None
    tipo = request.form.get('tipo', 'texto_a_binario')
    entrada = request.form.get('entrada', '')
    if request.method == 'POST':
        if tipo == 'texto_a_binario':
            texto = entrada
            binario = ' '.join(format(ord(c), '08b') for c in texto)
            hexadecimal = ' '.join(format(ord(c), '02x') for c in texto)
            resultado = {
                'texto': texto,
                'binario': binario,
                'hexadecimal': hexadecimal
            }
            # Guardar en la base de datos si el usuario está autenticado
            if 'user_id' in session:
                crear_resultado_testcapa(
                    capa='Física',
                    testcapa='Texto a Binario/Hexadecimal',
                    protocol='Conversión',
                    datain=texto,
                    resultado=f"Binario: {binario}, Hexadecimal: {hexadecimal}",
                    user_id=session['user_id']
                )
        elif tipo == 'binario_a_texto':
            binario = entrada.replace(' ', '')
            try:
                chars = [binario[i:i+8] for i in range(0, len(binario), 8)]
                texto = ''.join([chr(int(b, 2)) for b in chars])
                decimal = ' '.join(str(int(b, 2)) for b in chars)
                resultado = {
                    'binario': entrada,
                    'texto': texto,
                    'decimal': decimal
                }
                # Guardar en la base de datos si el usuario está autenticado
                if 'user_id' in session:
                    crear_resultado_testcapa(
                        capa='Física',
                        testcapa='Binario a Texto/Decimal',
                        protocol='Conversión',
                        datain=entrada,
                        resultado=f"Texto: {texto}, Decimal: {decimal}",
                        user_id=session['user_id']
                    )
            except Exception as e:
                resultado = {'error': f'Error en la conversión: {e}'}
    return render_template('capa1_conversion.html', resultado=resultado, tipo=tipo, entrada=entrada)

# Chat TCP
@app.route('/capa4/chat', methods=['GET', 'POST'])
def capa4_chat():
    global tcp_server_thread, tcp_server_running, chat_messages
    resultado = None
    num_clientes = request.form.get('num_clientes', 1, type=int)
    if 'user_id' not in session:
        flash('Debes iniciar sesión para usar el chat TCP.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        if 'iniciar' in request.form:
            if not tcp_server_running:
                chat_messages.clear()
                tcp_server_thread = threading.Thread(target=tcp_server, daemon=True)
                tcp_server_thread.start()
                time.sleep(0.5)
                flash('Servidor TCP iniciado.', 'success')
            else:
                flash('El servidor TCP ya está en ejecución.', 'info')
        elif 'detener' in request.form:
            tcp_server_running = False
            time.sleep(1)
            flash('Servidor TCP detenido.', 'info')
        elif 'enviar' in request.form:
            cliente_id = request.form['cliente_id']
            mensaje = request.form['mensaje']
            try:
                cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                cliente_tcp.connect(("localhost", 5555))
                # Enviar el id del cliente y el mensaje
                cliente_tcp.sendall(f"{cliente_id}:{mensaje}".encode())
                respuesta = cliente_tcp.recv(1024).decode()
                cliente_tcp.close()
                if cliente_id not in chat_messages:
                    chat_messages[cliente_id] = []
                chat_messages[cliente_id].append(f"Tú: {mensaje}")
                chat_messages[cliente_id].append(f"Servidor: {respuesta}")
                resultado = respuesta
                crear_resultado_testcapa(
                    capa='Transporte',
                    testcapa=f'Chat TCP Cliente {cliente_id}',
                    protocol='TCP',
                    datain=mensaje,
                    resultado=respuesta,
                    user_id=session['user_id']
                )
            except Exception as e:
                if cliente_id not in chat_messages:
                    chat_messages[cliente_id] = []
                chat_messages[cliente_id].append(f"Error al enviar mensaje: {e}")
                resultado = f"Error: {e}"
    return render_template('capa4_chat.html', chat_messages=chat_messages, tcp_server_running=tcp_server_running, num_clientes=num_clientes, max_clientes=MAX_CLIENTES)

@app.route('/capa7/mail', methods=['GET', 'POST'])
def capa7_mail():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para enviar correos.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        remitente = request.form['remitente']
        destinatario = request.form['destinatario']
        token = request.form['token']
        asunto = request.form['asunto']
        cuerpo = request.form['cuerpo']
        exito, mensaje = enviar_mail_smtp(remitente, destinatario, token, asunto, cuerpo)
        resultado = mensaje
        crear_resultado_testcapa(
            capa='Aplicación',
            testcapa='Envío de Mail SMTP',
            protocol='SMTP',
            datain=f'Remitente: {remitente}, Destinatario: {destinatario}, Asunto: {asunto}',
            resultado=mensaje,
            user_id=session['user_id']
        )
    return render_template('capa7_mail.html', resultado=resultado)

@app.route('/capa7/ftp', methods=['GET', 'POST'])
def capa7_ftp():
    resultado = None
    if 'user_id' not in session:
        flash('Debes iniciar sesión para usar FTP.', 'warning')
        return redirect(url_for('registro'))
    if request.method == 'POST':
        host = request.form['host']
        usuario = request.form['usuario']
        password = request.form['password']
        archivo = request.files['archivo']
        archivo_local = f'inicio/ejemplosPythonCapas/webModeloRedesExtendidas/files/{archivo.filename}'
        archivo.save(archivo_local)
        archivo_remoto = request.form.get('archivo_remoto', archivo.filename)
        exito, mensaje = subir_archivo_ftp(host, usuario, password, archivo_local, archivo_remoto)
        resultado = mensaje
        crear_resultado_testcapa(
            capa='Aplicación',
            testcapa='Subida de archivo FTP',
            protocol='FTP',
            datain=f'Host: {host}, Usuario: {usuario}, Archivo: {archivo.filename}',
            resultado=mensaje,
            user_id=session['user_id']
        )
    return render_template('capa7_ftp.html', resultado=resultado)



# =============================
# FUNCIÓN DEL SERVIDOR TCP (HILO)
# =============================
# Esta función corre en segundo plano y simula un servidor TCP local para la prueba de chat
def tcp_server():
    global tcp_server_running, chat_messages
    tcp_server_running = True
    servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor_tcp.bind(("localhost", 5555))
    servidor_tcp.listen(MAX_CLIENTES)
    while tcp_server_running:
        try:
            servidor_tcp.settimeout(1)
            conn, addr = servidor_tcp.accept()
            data = conn.recv(1024)
            if data:
                msg = data.decode()
                # El primer carácter del mensaje es el número de cliente
                cliente_id = msg[0]
                texto = msg[2:]
                if cliente_id not in chat_messages:
                    chat_messages[cliente_id] = []
                chat_messages[cliente_id].append(f"Cliente {cliente_id}: {texto}")
                conn.sendall(f"Servidor recibió de Cliente {cliente_id}: {texto}".encode())
            conn.close()
        except socket.timeout:
            continue
        except Exception as e:
            for cid in chat_messages:
                chat_messages[cid].append(f"Error en el servidor: {e}")
    servidor_tcp.close()

# Función para enviar correo usando SMTP y Gmail
# Requiere remitente, destinatario, token de app y mensaje

def enviar_mail_smtp(remitente, destinatario, token, asunto, cuerpo):
    msg = MIMEText(cuerpo)
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(remitente, token)
            servidor.send_message(msg)
        return True, 'Correo enviado exitosamente.'
    except Exception as e:
        return False, f'Error al enviar correo: {e}'

# Función para subir un archivo a un servidor FTP
# Requiere host, usuario, contraseña, ruta remota y archivo local

def subir_archivo_ftp(host, usuario, password, archivo_local, archivo_remoto):
    try:
        ftp = FTP(host)
        ftp.login(usuario, password)
        with open(archivo_local, 'rb') as f:
            ftp.storbinary(f'STOR {archivo_remoto}', f)
        ftp.quit()
        return True, 'Archivo subido exitosamente.'
    except Exception as e:
        return False, f'Error al subir archivo por FTP: {e}'


# =============================
# INICIO DE LA APLICACIÓN
# =============================
# Este bloque permite ejecutar la app en modo debug si corres 'python app.py'
if __name__ == '__main__':
    app.run(debug=True) 