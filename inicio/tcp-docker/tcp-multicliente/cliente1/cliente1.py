import socket
import time

ip_servidor = "172.28.0.2"
puerto = 12345

mensajes = [
    "Primer mensaje - Enviado inmediatamente",
    "Segundo mensaje - Enviado después de 3s",
    "Tercer mensaje - Enviado después de 6s"
]

tiempos = [0, 3, 6]

time.sleep(5)  # Esperar a que el servidor inicie

for msg, delay in zip(mensajes, tiempos):
    time.sleep(delay)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip_servidor, puerto))
    print("Enviando mensaje de cliente1...")
    client.send(f"Cliente {'1' if 'cliente1' in __file__ else '2'}: {msg}".encode())
    print("Mensaje enviado de c1")
    client.close()
