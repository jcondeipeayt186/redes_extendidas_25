# Ejemplos de Python para la Capa de Presentación del modelo OSI

# 1. Codificación Base64
import base64
mensaje = "Hola, mundo!"
mensaje_codificado = base64.b64encode(mensaje.encode('utf-8'))
print("Base64 codificado:", mensaje_codificado.decode())

# 2. Cifrado SSL/TLS (simulación de handshake)
import ssl, socket
contexto = ssl.create_default_context()
with contexto.wrap_socket(socket.socket(), server_hostname="www.google.com") as s:
    s.connect(("www.google.com", 443))
    print("Conexión segura establecida con www.google.com")

# 3. Serialización/deserialización JSON
import json
datos = {"usuario": "Ana", "activo": True}
json_str = json.dumps(datos)
print("JSON serializado:", json_str)
objeto = json.loads(json_str)
print("Objeto recuperado:", objeto)

# 4. Conversión UTF-8 y manejo de errores en ASCII
texto = "Ñandú con acento"
utf8 = texto.encode("utf-8")
try:
    ascii = texto.encode("ascii")
except UnicodeEncodeError as error:
    print("Error al convertir a ASCII:", error)
print("UTF-8 codificado:", utf8)

