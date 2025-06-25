from scapy.all import *

""" 
Capturar paquetes ICMP (tipo ping) con scapy
Concepto: Capa de red, protocolo ICMP, inspección de paquetes
Qué hace: Usa scapy para enviar y recibir paquetes ICMP tipo “ping”.

🔧 Requiere instalar Scapy: pip install scapy
🛡️ Necesita permisos de administrador para enviar ICMP (ejecutar como root en Linux).
"""

ip_destino = "8.8.8.8"
paquete = IP(dst=ip_destino)/ICMP()
respuesta = sr1(paquete, timeout=1)

if respuesta:
    print(f"Respuesta de {ip_destino}: {respuesta.summary()}")
else:
    print("Sin respuesta.")
