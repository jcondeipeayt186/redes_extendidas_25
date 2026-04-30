-- Crear base de datos
CREATE DATABASE IF NOT EXISTS redesextendidas;
USE redesextendidas;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    pass VARCHAR(255) NOT NULL,
    creation DATETIME NOT NULL,
    lastaccess DATETIME NOT NULL,
    access INT DEFAULT 0
);

-- Tabla de resultados de test por capa
CREATE TABLE IF NOT EXISTS resultadoTestCapa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    capa VARCHAR(50) NOT NULL,
    testcapa VARCHAR(100) NOT NULL,
    protocol VARCHAR(100) NOT NULL,
    datain TEXT,
    resultado TEXT,
    fecha DATETIME NOT NULL,
    user INT NOT NULL,
    FOREIGN KEY (user) REFERENCES usuarios(id)
); 