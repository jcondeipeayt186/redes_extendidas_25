import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(5)
print("Servidor TCP esperando conexiones...")

while True:
    conn, addr = server.accept()
    print(f"Conexión desde {addr}")
    mensaje = conn.recv(1024).decode()
    print("Mensaje recibido:", mensaje)
    conn.close()
