"""Configuración de pytest para Lisboa360 Backend."""
import pytest

from app import create_app
from app.db.connection import init_db


@pytest.fixture
def app():
    """Aplicación con base de datos en memoria (SQLite `:memory:`) y seed de desarrollo."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["DATABASE_PATH"] = ":memory:"
    init_db(app)
    return app


@pytest.fixture
def client(app):
    """Cliente de pruebas de Flask."""
    return app.test_client()
