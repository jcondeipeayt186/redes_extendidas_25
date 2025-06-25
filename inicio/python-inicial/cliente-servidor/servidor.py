import socket

# Crea un socket usando TCP (SOCK_STREAM) y direcciones IPv4 (AF_INET).
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(("0.0.0.0", 12345))  # Acepta conexiones en cualquier IP en el puerto 12345
server.listen(1) # Le dice al socket que empiece a escuchar conexiones entrantes (hasta 1 conexión simultánea).
print("Esperando conexión...")

#Espera hasta que un cliente se conecte. Cuando lo hace, devuelve dos cosas:
#conn: canal para intercambiar datos.
#addr: dirección IP del cliente.
conn, addr = server.accept()
print(f"Conexión desde: {addr}")

#Recibe hasta 1024 bytes de datos, los decodifica de bytes a texto.
data = conn.recv(1024).decode()
print("Mensaje recibido:", data)
conn.close()
