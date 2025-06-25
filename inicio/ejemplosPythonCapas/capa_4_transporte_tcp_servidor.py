# Ejemplos de Python para la Capa de Transporte del modelo OSI

# 1. Servidor TCP básico
import socket
servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_tcp.bind(("localhost", 5555))
servidor_tcp.listen(1)
print("Servidor TCP escuchando en puerto 5555")
conn, addr = servidor_tcp.accept()
print("Conectado por:", addr)
print("Mensaje recibido:", conn.recv(1024).decode())
conn.close()

