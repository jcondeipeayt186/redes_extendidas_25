CREATE DATABASE IF NOT EXISTS tipos_mysql;
USE tipos_mysql;

CREATE TABLE ejemplo_tipos (
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- Números
    edad TINYINT,
    anio SMALLINT,
    poblacion MEDIUMINT,
    dni INT,
    telefono BIGINT,
    precio DECIMAL(8,2),
    temperatura FLOAT,
    altura DOUBLE,

    -- Textos
    codigo CHAR(5),
    nombre VARCHAR(50),
    comentario TINYTEXT,
    descripcion TEXT,
    articulo MEDIUMTEXT,
    documento LONGTEXT,

    -- Fechas
    fecha_nac DATE,
    created_at DATETIME,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hora TIME,
    anio_solo YEAR,

    -- Booleanos y enums
    activo BOOLEAN,
    sexo ENUM('M','F','X'),
    dias_laborales SET('Lunes','Martes','Miercoles','Jueves','Viernes')
);

-- Inserts de ejemplo
INSERT INTO ejemplo_tipos 
(edad, anio, poblacion, dni, telefono, precio, temperatura, altura, codigo, nombre, comentario, descripcion, articulo, documento, fecha_nac, created_at, hora, anio_solo, activo, sexo, dias_laborales)
VALUES
(25, 1999, 7500000, 12345678, 5493515551234, 12345.67, 36.6, 1.75234, 'A12', 'María', 'OK', 'Texto descriptivo corto.', 'Artículo largo...', 'Documento completo...', '1990-07-25', '2025-09-08 12:30:00', '14:45:10', 2025, TRUE, 'F', 'Lunes,Martes');

INSERT INTO ejemplo_tipos 
(edad, anio, poblacion, dni, telefono, precio, temperatura, altura, codigo, nombre, comentario, descripcion, articulo, documento, fecha_nac, created_at, hora, anio_solo, activo, sexo, dias_laborales)
VALUES
(30, 2020, 1200000, 87654321, 541134444567, 250.50, 22.3, 1.85, 'B55', 'Juan', 'Todo bien', 'Otra descripción...', 'Más texto...', 'Documento extenso...', '1995-12-01', NOW(), '08:15:00', 2020, FALSE, 'M', 'Miercoles,Viernes');

