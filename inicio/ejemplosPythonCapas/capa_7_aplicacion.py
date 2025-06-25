# Ejemplos de Python para la Capa de Aplicación del modelo OSI

# 1. HTTP GET con requests
import requests
response = requests.get('https://httpbin.org/get')
print("Respuesta HTTP GET:", response.text)

# 2. Envío de correo electrónico con SMTP
import smtplib
from email.mime.text import MIMEText

remitente = "julianconde.ispc@gmail.com"
destinatario = "julianconde.ipeayt186@gmail.com"
msg = MIMEText("Este es un correo enviado desde Python usando SMTP.")
msg['Subject'] = "Prueba SMTP"
msg['From'] = remitente
msg['To'] = destinatario

token = "irglvrmkjkfgxpfp"

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
    servidor.login(remitente, token)#'tu_contraseña_o_token'
    servidor.send_message(msg)
    print("Correo enviado exitosamente")



# 3. Descargar un archivo desde FTP
from ftplib import FTP
ftp = FTP('speedtest.tele2.net')
ftp.login()
ftp.cwd('/')
with open('archivo_test.txt', 'wb') as f:
    ftp.retrbinary('RETR 1KB.zip', f.write)
ftp.quit()
print("Archivo descargado")

# 4. Resolución DNS (obtener IP desde nombre)
import socket
ip = socket.gethostbyname("www.google.com")
print("La IP de www.google.com es:", ip)
