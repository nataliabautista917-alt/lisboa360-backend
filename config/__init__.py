"""Configuración centralizada de la aplicación Lisboa360 Backend."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"
GEOJSON_DIR = BASE_DIR / "data" / "geojson"


def _env_path(name, default):
    value = os.environ.get(name)
    return Path(value) if value else default


class Config:
    """Configuración del backend según variables de entorno."""

    APP_NAME = "Lisboa360 API"
    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = os.environ.get("FLASK_DEBUG", "0") not in ("0", "false", "False", "")

    # Conexión a la base de datos
    DATABASE_PATH = _env_path("DATABASE_PATH", DATABASE_DIR / "lisboa360.db")

    # Dato GeoJSON
    GEOJSON_DIR = _env_path("GEOJSON_DIR", GEOJSON_DIR)

    # Red y versionado de rutas
    SERVER_HOST = os.environ.get("SERVER_HOST", "127.0.0.1")
    SERVER_PORT = int(os.environ.get("SERVER_PORT", "5000"))

    # CORS restringido a los orígenes necesarios para el frontend
    ALLOWED_ORIGINS = [
        origin.strip()
        for origin in os.environ.get(
            "ALLOWED_ORIGINS",
            "http://localhost:3000,http://localhost:8080,http://127.0.0.1:8000,http://localhost:8000",
        ).split(",")
        if origin.strip()
    ]

    # Seed de datos ficticios (desarrollo)
    SEED_FICTICIO = os.environ.get("SEED_FICTICIO", "1") == "1"
