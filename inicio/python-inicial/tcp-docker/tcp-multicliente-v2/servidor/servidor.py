import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(5)
print("Servidor TCP esperando conexiones...")

for _ in range(6):  # Espera 6 mensajes
    conn, addr = server.accept()
    mensaje = conn.recv(1024).decode()
    print(f"Mensaje recibido desde {addr}: {mensaje}")
    conn.close()