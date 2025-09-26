import socket
import time

# Esperar unos segundos para asegurarse de que el servidor esté listo
time.sleep(3)

print(f"Hola, soy la pc cliente 1, y enviare un mensaje al servidor... Mi ip es {socket.gethostbyname(socket.gethostname())}")
print("Iniciando cuenta regresiva para enviar el mensaje al servidor...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.0.2", 12345))  # IP del contenedor del servidor
client.send("Hola desde el cliente en Docker".encode())
print("Enviado mensaje al servidor!!!!!!!!!!.")
client.close()
