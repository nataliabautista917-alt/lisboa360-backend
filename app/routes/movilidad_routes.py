"""Rutas del recurso Movilidad — GET /api/v1/movilidad (OpenAPI: operationId listMovilidad)."""
from flask import Blueprint, jsonify, request

from app.services.movilidad_service import listar_movilidad

bp = Blueprint("movilidad", __name__, url_prefix="/api/v1")


@bp.get("/movilidad")
def listar_movilidad_endpoint():
    """Devuelve la lista paginada de elementos de movilidad del barrio."""
    data = listar_movilidad(
        tipo=request.args.get("tipo"),
        q=request.args.get("q"),
        limite=request.args.get("limite"),
        offset=request.args.get("offset"),
    )
    return jsonify(data), 200
