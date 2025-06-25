import socketserver

class MiHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Sesión iniciada desde: {self.client_address}")
        datos = self.request.recv(1024)
        print(f"Datos recibidos: {datos.decode()}")

if __name__ == "__main__":
    with socketserver.ThreadingTCPServer(("localhost", 12345), MiHandler) as server:
        print("Servidor listo en puerto 12345")
        server.serve_forever()
