# Ejemplos de Python para la Capa de Sesión del modelo OSI

# 4. Servidor multicliente que registra sesiones
import socketserver

class MiHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Nueva sesión desde: {self.client_address}")
        datos = self.request.recv(1024)
        print(f"Datos: {datos.decode()}")

# Ejecutar este código en una terminal independiente
# server = socketserver.ThreadingTCPServer(("", 12345), MiHandler)
# print("Servidor listo")
# server.serve_forever()
