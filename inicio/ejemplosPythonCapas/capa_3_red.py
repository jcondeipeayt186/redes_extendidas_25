# Ejemplos de Python para la Capa de Red del modelo OSI

# 1. Obtener dirección IP local
import socket
nombre_host = socket.gethostname()
ip_local = socket.gethostbyname(nombre_host)
print("Nombre del host:", nombre_host)
print("IP local:", ip_local)

# 2. Hacer ping a una dirección (Linux/macOS)
import subprocess
print("Haciendo ping a 8.8.8.8...")
salida = subprocess.run(["ping", "-c", "3", "8.8.8.8"], capture_output=True, text=True)
print(salida.stdout)

# 3. Ejecutar traceroute (Linux/macOS)
import os
print("Trazando ruta a www.google.com...")
os.system("traceroute www.google.com")

# 4. Resolución inversa de IP
ip = "8.8.8.8"
try:
    nombre_remoto = socket.gethostbyaddr(ip)
    print(f"Nombre para {ip}: {nombre_remoto[0]}")
except socket.herror:
    print("No se pudo resolver la IP")
