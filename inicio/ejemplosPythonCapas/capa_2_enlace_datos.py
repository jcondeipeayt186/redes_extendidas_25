# Ejemplos de Python para la Capa de Enlace de Datos del modelo OSI

# 1. Obtener dirección MAC local
import uuid
mac = uuid.getnode()
print(f"uuid.getnode() queda en variable {mac=}")
mac_str = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
print("Dirección MAC:", mac_str)

# 2. Mostrar interfaces de red (Linux/macOS)
import os
print("Interfaces de red:")
os.system("ip a")  # En Windows: usar 'ipconfig'

# 3. Captura de paquetes con Scapy (requiere root)
# pip install scapy
from scapy.all import sniff
print("Capturando 3 paquetes de red:")
paquetes = sniff(count=3)
paquetes.summary()

# 4. Solicitud ARP con Scapy (requiere root)
from scapy.all import ARP, Ether, srp
ip_destino = "192.168.1.1"  # Reemplazar por IP válida en tu red
paquete = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_destino)
respuesta = srp(paquete, timeout=2, verbose=False)[0]
for envio, resp in respuesta:
    print(f"IP: {resp.psrc}, MAC: {resp.hwsrc}")
