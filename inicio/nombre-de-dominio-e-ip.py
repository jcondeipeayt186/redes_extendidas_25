import socket

""" 
Resolver el nombre de dominio e identificar IP (DNS)
Concepto: Capa de aplicación (DNS), resolución de nombres, dirección IP
Qué hace: Convierte un dominio a su dirección IP utilizando resolución DNS.

👉 Se puede capturar esta consulta DNS en Wireshark con el filtro dns.

"""

dominio = "wikipedia.org"
#dominio = "evelia.unrc.edu.ar"
ip = socket.gethostbyname(dominio)
print(f"La IP de {dominio} es {ip}")
