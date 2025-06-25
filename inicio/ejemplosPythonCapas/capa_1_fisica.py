# Ejemplos de Python para la Capa Física del modelo OSI

# 1. Medir latencia con ping (Linux/macOS)
import subprocess
print("Midiendo latencia con ping a 8.8.8.8...")
subprocess.run(["ping", "-c", "3", "8.8.8.8"])

# 2. Estado de interfaces de red
import os
print("Estado de interfaces:")
os.system("ip link show")  # En Windows: usar 'ipconfig /all'

# 3. Test de velocidad (requiere speedtest-cli)
# pip install speedtest-cli
import speedtest
st = speedtest.Speedtest()
st.get_best_server()
print("Velocidad de descarga:", st.download() / 1_000_000, "Mbps")
print("Velocidad de subida:", st.upload() / 1_000_000, "Mbps")

# 4. Señal Wi-Fi (Linux con iwconfig)
print("Potencia de señal Wi-Fi (si aplica):")
os.system("iwconfig")
