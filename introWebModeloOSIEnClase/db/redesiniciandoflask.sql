-- Script de creación de la base de datos y tabla protocolos para el proyecto Flask
CREATE DATABASE IF NOT EXISTS redesiniciandoflask;
USE redesiniciandoflask;

CREATE TABLE IF NOT EXISTS protocolos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    acronimo VARCHAR(20) NOT NULL,
    nombreCapa VARCHAR(50) NOT NULL,
    fechaActualizacion DATE NOT NULL,
    descripcion TEXT
); 

-- MySQL proporciona cuatro subtipos de TEXT:
-- TINYTEXT: Almacena hasta 255 bytes. 
-- TEXT: Almacena hasta 65,535 bytes (aproximadamente 64KB). 
-- MEDIUMTEXT: Almacena hasta 16,777,215 bytes (aproximadamente 16MB). 
-- LONGTEXT: Almacena hasta 4,294,967,295 bytes (aproximadamente 4GB). 
