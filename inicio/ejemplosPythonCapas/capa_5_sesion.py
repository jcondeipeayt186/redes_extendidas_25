# Ejemplos de Python para la Capa de Sesión del modelo OSI

# 1. Conexión con reconexión automática
import socket, time

def conectar():
    while True:
        try:
            s = socket.create_connection(("localhost", 12345))
            print("Conectado al servidor")
            s.sendall(b"Hola, servidor")
            s.close()
            break
        except ConnectionRefusedError:
            print("Servidor no disponible. Reintentando en 2 segundos...")
            time.sleep(2)

conectar()

# 2. Múltiples sesiones con threads
import threading

def cliente(id):
    s = socket.socket()
    s.connect(("localhost", 12345))
    s.sendall(f"Soy el cliente {id}".encode())
    s.close()

for i in range(3):
    threading.Thread(target=cliente, args=(i,)).start()

# 3. Desconexión abrupta
s = socket.socket()
s.connect(("localhost", 12345))
s.sendall(b"Mensaje antes del corte")
s.close()


