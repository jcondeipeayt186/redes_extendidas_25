import socket

s = socket.socket()
s.connect(("localhost", 12345))
s.sendall(b"Mensaje antes del corte abrupto")
s.close()  # No hay cierre ordenado de sesión

