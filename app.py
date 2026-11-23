"""Punto de entrada de la aplicación Lisboa360 Backend.

Inicializa la aplicación Flask con la configuración, ejecuta las rutes y el seed de datos.
Ejecutar desde la raíz del repositorio:

    python app.py
"""
from app import create_app
from app.db.connection import init_db

app = create_app()
init_db(app)

if __name__ == "__main__":
    app.run(host=app.config["SERVER_HOST"], port=app.config["SERVER_PORT"], debug=app.config["DEBUG"])
