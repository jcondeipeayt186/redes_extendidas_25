Vamos a hacer paso a paso la prueba del ejemplo de comunicación TCP entre cliente y servidor en Python. Esta práctica es ideal para introducir los conceptos de conexión cliente-servidor, puertos y capa de transporte del modelo TCP/IP.

🧠 ¿Qué vamos a hacer?
Vas a ejecutar dos scripts:

Uno hace de servidor TCP que espera una conexión.

Otro actúa como cliente TCP, que se conecta y envía un mensaje.

Esto simula cómo funcionan muchas aplicaciones: el navegador (cliente) se conecta a un servidor web por el puerto 80 o 443, por ejemplo.

✅ Requisitos previos
Tener Python instalado en tu computadora.

Usar un sistema operativo como Windows, Linux o macOS.

Acceso a la terminal o consola.

🗂 Paso 1: Crear los dos scripts
A. Crear el archivo del servidor:
Abrí tu editor (Notepad, VS Code, etc.)

Pegá este código y guardalo como servidor.py:

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))  # Acepta conexiones en cualquier IP en el puerto 12345
server.listen(1)
print("Esperando conexión...")

conn, addr = server.accept()
print(f"Conexión desde: {addr}")

data = conn.recv(1024).decode()
print("Mensaje recibido:", data)
conn.close()
B. Crear el archivo del cliente:
Abrí otro archivo nuevo.

Pegá este código y guardalo como cliente.py:

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))  # Conecta al servidor en el mismo equipo
client.send("Hola desde el cliente".encode())
client.close()
🧪 Paso 2: Ejecutar el servidor
Abrí una terminal (o consola).

Navegá hasta la carpeta donde guardaste el archivo.

Ejecutá:

python servidor.py
Deberías ver:

Esperando conexión...
⚠️ Esto indica que el servidor está “escuchando” en el puerto 12345 y esperando que alguien se conecte.

📡 Paso 3: Ejecutar el cliente
En otra ventana de terminal, corré:

python cliente.py
✅ El cliente se conecta al servidor, envía el mensaje y se cierra.

🔁 Volvé a la primera ventana donde está el servidor: debería haber aparecido algo como:

Conexión desde: ('127.0.0.1', 54832)
Mensaje recibido: Hola desde el cliente
🧠 Explicación de cada parte del código
🖥 Servidor:

socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Crea un socket usando TCP (SOCK_STREAM) y direcciones IPv4 (AF_INET).

server.bind(("0.0.0.0", 12345))
Indica que acepta conexiones en cualquier interfaz de red, en el puerto 12345.

server.listen(1)
Le dice al socket que empiece a escuchar conexiones entrantes (hasta 1 conexión simultánea).

conn, addr = server.accept()
Espera hasta que un cliente se conecte. Cuando lo hace, devuelve dos cosas:
conn: canal para intercambiar datos.
addr: dirección IP del cliente.

data = conn.recv(1024).decode()
Recibe hasta 1024 bytes de datos, los decodifica de bytes a texto.

💻 Cliente:
client.connect(("localhost", 12345))
Se conecta al servidor que está en la misma máquina (localhost) por el puerto 12345.

client.send("Hola desde el cliente".encode())
Envía el mensaje convertido a bytes.

🔄 Variaciones y extensiones
Podés usar Wireshark y filtrar por tcp.port == 12345 para ver los paquetes.

Usar IP de otra computadora si están en red (ej: client.connect(("192.168.1.100", 12345)))

Hacer que el servidor responda al mensaje recibido (conn.send(...)).
