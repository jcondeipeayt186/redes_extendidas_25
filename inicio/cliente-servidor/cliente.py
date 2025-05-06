import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))  # Se conecta al servidor que está en la misma máquina (localhost) por el puerto 12345.

client.send("Hola desde el cliente".encode()) #Envía el mensaje convertido a bytes.
client.close()

""" 
🔄 Variaciones y extensiones
Podés usar Wireshark y filtrar por tcp.port == 12345 para ver los paquetes.

Usar IP de otra computadora si están en red (ej: client.connect(("192.168.1.100", 12345)))

Hacer que el servidor responda al mensaje recibido (conn.send(...)).


"""