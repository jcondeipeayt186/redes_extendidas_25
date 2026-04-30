CREATE TABLE comentario (
  id INT AUTO_INCREMENT PRIMARY KEY,

  capa ENUM('App', 'Pre', 'Ses'),

  otracapa VARCHAR(20),
  CHECK (otracapa IN ('App', 'Pre', 'Ses'))


);



