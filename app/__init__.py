"""Lisboa360 Backend — capa de procesamiento y acceso a datos (aplicación Flask)."""
from flask import Flask
from flask_cors import CORS

from app.db.connection import init_db
from app.routes import (
    barrio_routes,
    capas_routes,
    equipamientos_routes,
    espacios_publicos_routes,
    lugares_routes,
    movilidad_routes,
)
from app.utils.errors import register_error_handlers

__all__ = ["create_app", "init_db"]


def create_app(config_class="config.Config"):
    """Factory de la aplicación Flask con rutas versionadas, CORS restringido y manejo de errores centralizado."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # CORS restringido a los orígenes necesarios del frontend (lisboa360-frontend)
    CORS(app, origins=app.config["ALLOWED_ORIGINS"])

    # Manejo centralizado de errores (respuestas JSON estandarizadas)
    register_error_handlers(app)

    # Registro de blueprint con versionamiento /api/v1
    for blueprint in (
        barrio_routes.bp,
        capas_routes.bp,
        lugares_routes.bp,
        equipamientos_routes.bp,
        espacios_publicos_routes.bp,
        movilidad_routes.bp,
    ):
        app.register_blueprint(blueprint)

    return app
