import socket, time

while True:
    try:
        s = socket.create_connection(("localhost", 12345))
        print("Conectado al servidor")
        s.sendall(b"Hola desde el cliente con reconexion")
        s.close()
        break
    except ConnectionRefusedError:
        print("Servidor no disponible. Reintentando en 2 segundos...")
        time.sleep(2)

        
