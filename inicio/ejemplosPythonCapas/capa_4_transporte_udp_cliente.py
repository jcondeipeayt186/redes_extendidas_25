# Ejemplos de Python para la Capa de Transporte del modelo OSI
import socket


# 3. Comunicación UDP


# Cliente UDP
udp_cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_cli.sendto(b"Mensaje via UDP", ("localhost", 6666))

