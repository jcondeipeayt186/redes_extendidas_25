import socket, threading

def cliente(id):
    s = socket.socket()
    s.connect(("localhost", 12345))
    s.sendall(f"Soy el cliente {id}".encode())
    s.close()

for i in range(3):
    threading.Thread(target=cliente, args=(i,)).start()

