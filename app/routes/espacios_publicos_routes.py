"""Rutas del recurso EspacioPublico — GET /api/v1/espacios-publicos (OpenAPI: operationId listEspaciosPublicos)."""
from flask import Blueprint, jsonify, request

from app.services.espacio_publico_service import listar_espacios_publicos

bp = Blueprint("espacios_publicos", __name__, url_prefix="/api/v1")


@bp.get("/espacios-publicos")
def listar_espacios_publicos_endpoint():
    """Devuelve la lista paginada de espacios públicos del barrio."""
    data = listar_espacios_publicos(
        categoria=request.args.get("categoria"),
        q=request.args.get("q"),
        limite=request.args.get("limite"),
        offset=request.args.get("offset"),
    )
    return jsonify(data), 200
