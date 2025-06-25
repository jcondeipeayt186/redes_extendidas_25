import socket

""" 
Simular un escaneo de puertos básicos en una IP
Concepto: Capas de red y transporte (TCP/IP), puertos, servicios
Qué hace: Escanea algunos puertos conocidos de un sitio para ver si están abiertos.
"""

ip = "google.com"
puertos = [21, 22, 80, 443, 3306]

for puerto in puertos:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((ip, puerto))
    if resultado == 0:
        print(f"Puerto {puerto} abierto")
    else:
        print(f"Puerto {puerto} cerrado")
    s.close()
