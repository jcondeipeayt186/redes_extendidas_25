Mi App Flask - Proyecto Inicial

Este es un proyecto mínimo con Python y Flask para comenzar rápidamente.

Estructura

mi_app/

- app.py
- requirements.txt
- README.md
- templates/
  - base.html
  - index.html
- static/
  - (opcional: imágenes, etc.)

Requisitos

- Python 3.10+ (recomendado)

Instalar Python en Windows

1. Descarga Python desde `https://www.python.org/downloads/windows/`.
2. Ejecuta el instalador y marca "Add Python to PATH".
3. Verifica en una terminal (PowerShell):
   python --version

Crear y usar un entorno virtual (Windows)

1. Crear el entorno virtual:
   python -m venv .venv
2. Activar el entorno virtual:
   .\.venv\Scripts\Activate.ps1
   Si aparece una advertencia de ejecución de scripts, ejecuta PowerShell como Administrador y corre:
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   Luego vuelve a activar el entorno.
3. Instalar dependencias desde requirements.txt:
   pip install -r requirements.txt

Ejecutar la aplicación
Con el entorno virtual activado:
   python app.py

La aplicación escuchará en `http://127.0.0.1:5000/`.

Uso diario

- Activa el entorno: .\.venv\Scripts\Activate.ps1
- Instala nuevas deps: pip install paquete
- Congela deps: pip freeze > requirements.txt
- Ejecuta la app: python app.py
