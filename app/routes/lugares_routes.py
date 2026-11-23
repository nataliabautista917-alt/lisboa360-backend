"""Rutas del recurso Lugar — GET /api/v1/lugares (OpenAPI: operationId listLugares)."""
from flask import Blueprint, jsonify, request

from app.services.lugar_service import listar_lugares

bp = Blueprint("lugares", __name__, url_prefix="/api/v1")


@bp.get("/lugares")
def listar_lugares_endpoint():
    """Devuelve la lista paginada de lugares de interés geográfico."""
    data = listar_lugares(
        categoria=request.args.get("categoria"),
        q=request.args.get("q"),
        limite=request.args.get("limite"),
        offset=request.args.get("offset"),
    )
    return jsonify(data), 200
