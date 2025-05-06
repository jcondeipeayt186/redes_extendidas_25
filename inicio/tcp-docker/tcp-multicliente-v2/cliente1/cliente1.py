import socket
import time

ip_servidor = "172.28.0.2"
puerto = 12345

time.sleep(3)  # Esperar al servidor
print("[Cliente 1] Enviando 3 mensajes")
for i in range(3):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_servidor, puerto))
    mensaje = f"Cliente 1: Mensaje #{i+1}"
    client.send(mensaje.encode())
    client.close()
    print(mensaje)
    time.sleep(2)