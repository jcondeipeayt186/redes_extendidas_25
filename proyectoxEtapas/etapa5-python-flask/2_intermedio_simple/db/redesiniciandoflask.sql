-- Script SQL para crear la base de datos y tabla de protocolos
-- Base de datos para el proyecto de redes extendidas con Flask

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
('Internet Protocol', 'IP', 'Capa 3 - Red', 'Protocolo principal de la capa de red que permite el enrutamiento de paquetes'),
('Hypertext Transfer Protocol', 'HTTP', 'Capa 7 - Aplicación', 'Protocolo para la transferencia de hipertexto en la World Wide Web'),
('File Transfer Protocol', 'FTP', 'Capa 7 - Aplicación', 'Protocolo para la transferencia de archivos entre sistemas'),
('User Datagram Protocol', 'UDP', 'Capa 4 - Transporte', 'Protocolo no orientado a conexión para transmisión rápida de datos'),
('Simple Mail Transfer Protocol', 'SMTP', 'Capa 7 - Aplicación', 'Protocolo para el envío de correo electrónico'),
('Post Office Protocol', 'POP3', 'Capa 7 - Aplicación', 'Protocolo para recibir correo electrónico'),
('Internet Message Access Protocol', 'IMAP', 'Capa 7 - Aplicación', 'Protocolo avanzado para acceso a correo electrónico'),
('Domain Name System', 'DNS', 'Capa 7 - Aplicación', 'Sistema de nombres de dominio para resolver nombres a direcciones IP'),
('Dynamic Host Configuration Protocol', 'DHCP', 'Capa 7 - Aplicación', 'Protocolo para asignar automáticamente direcciones IP'); 