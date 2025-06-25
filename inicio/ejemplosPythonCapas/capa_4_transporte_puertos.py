# Ejemplos de Python para la Capa de Transporte del modelo OSI
import socket

# 4. Escaneo básico de puertos TCP
host = "localhost"
puertos = [21, 22, 80, 443, 5555]
print(f"Escaneando puertos en {host}...")
for puerto in puertos:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, puerto))
    if resultado == 0:
        print(f"Puerto {puerto} ABIERTO")
    sock.close()
