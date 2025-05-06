import socket
import time

# Esperar unos segundos para asegurarse de que el servidor esté listo
time.sleep(3)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.0.2", 12345))  # IP del contenedor del servidor
client.send("Hola desde el cliente en Docker".encode())
client.close()
