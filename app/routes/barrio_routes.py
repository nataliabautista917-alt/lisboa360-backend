"""Rutas del recurso Barrio — GET /api/v1/barrios/lisboa (OpenAPI: operationId getBarrioLisboa)."""
from flask import Blueprint, jsonify

from app.services.barrio_service import get_barrio_lisboa

bp = Blueprint("barrio", __name__, url_prefix="/api/v1")


@bp.get("/barrios/lisboa")
def get_barrio_lisboa_endpoint():
    """Devuelve la información general del barrio Lisboa."""
    data = get_barrio_lisboa()
    return jsonify(data), 200
