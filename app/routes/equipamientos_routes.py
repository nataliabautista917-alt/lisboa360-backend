"""Rutas del recurso Equipamiento — GET /api/v1/equipamientos (OpenAPI: operationId listEquipamientos)."""
from flask import Blueprint, jsonify, request

from app.services.equipamento_service import listar_equipamientos

bp = Blueprint("equipamientos", __name__, url_prefix="/api/v1")


@bp.get("/equipamientos")
def listar_equipamientos_endpoint():
    """Devuelve la lista paginada de equipamientos del barrio."""
    data = listar_equipamientos(
        categoria=request.args.get("categoria"),
        q=request.args.get("q"),
        limite=request.args.get("limite"),
        offset=request.args.get("offset"),
    )
    return jsonify(data), 200
