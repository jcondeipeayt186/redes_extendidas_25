# Ejemplos de Python para la Capa de Transporte del modelo OSI

import socket
# 3. Comunicación UDP
# Servidor UDP
udp_srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_srv.bind(("localhost", 6666))
print("Servidor UDP esperando...")
msg, addr = udp_srv.recvfrom(1024)
print(f"Mensaje UDP desde {addr}: {msg.decode()}")

