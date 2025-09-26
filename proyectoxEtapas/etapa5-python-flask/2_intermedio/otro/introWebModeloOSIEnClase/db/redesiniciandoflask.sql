-- Script SQL para crear la base de datos y tabla de protocolos
-- Base de datos para el proyecto web de redes de computadoras

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS redesiniciandoflask;

-- Usar la base de datos
USE redesiniciandoflask;

-- Crear la tabla protocolos
CREATE TABLE IF NOT EXISTS protocolos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    acronimo VARCHAR(20) NOT NULL,
    nombreCapa VARCHAR(50) NOT NULL,
    fechaActualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    descripcion TEXT
);

-- Insertar algunos protocolos de ejemplo
INSERT INTO protocolos (nombre, acronimo, nombreCapa, descripcion) VALUES
('Transmission Control Protocol', 'TCP', 'Capa 4 - Transporte', 'Protocolo orientado a conexión que garantiza la entrega confiable de datos'),
('Internet Protocol', 'IP', 'Capa 3 - Red', 'Protocolo de red que permite la comunicación entre dispositivos'),
('Hypertext Transfer Protocol', 'HTTP', 'Capa 7 - Aplicación', 'Protocolo para la transferencia de hipertexto en la World Wide Web'),
('File Transfer Protocol', 'FTP', 'Capa 7 - Aplicación', 'Protocolo para la transferencia de archivos entre sistemas'),
('Simple Mail Transfer Protocol', 'SMTP', 'Capa 7 - Aplicación', 'Protocolo para el envío de correos electrónicos'),
('Domain Name System', 'DNS', 'Capa 7 - Aplicación', 'Sistema de nombres de dominio que traduce nombres a direcciones IP'),
('User Datagram Protocol', 'UDP', 'Capa 4 - Transporte', 'Protocolo no orientado a conexión para transmisión rápida de datos'),
('Address Resolution Protocol', 'ARP', 'Capa 2 - Enlace de Datos', 'Protocolo para mapear direcciones IP a direcciones MAC'); 