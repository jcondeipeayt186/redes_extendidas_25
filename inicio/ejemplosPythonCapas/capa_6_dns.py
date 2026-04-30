#Resolución DNS (obtener IP desde nombre)
import socket
#host = "evelia.unrc.edu.ar"
host = "prueba.evelia.unrc.edu.ar"
ip = socket.gethostbyname(host)
print("La IP de", host, "es:", ip)