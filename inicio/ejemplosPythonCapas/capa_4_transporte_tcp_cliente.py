import socket

# 2. Cliente TCP
cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_tcp.connect(("localhost", 5555))
cliente_tcp.sendall(b"Hola desde el cliente TCP")
cliente_tcp.close()

