import socket

print("Tu IP local es:", socket.gethostbyname(socket.gethostname()))

import subprocess

# Obtener la puerta de enlace
resultado = subprocess.run(['ip', 'route', 'show', 'default'], capture_output=True, text=True)
print(resultado.stdout)