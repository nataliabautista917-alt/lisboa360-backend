"""Rutas del recurso CapasGeograficas — GET /api/v1/capas y GET /api/v1/capas/{capaId}/geojson."""
from flask import Blueprint, jsonify, request

from app.services.capas_service import get_capa_geojson, listar_capas

bp = Blueprint("capas", __name__, url_prefix="/api/v1")


@bp.get("/capas")
def listar_capas_endpoint():
    """Devuelve la lista paginada de capas geográficas registradas (OpenAPI: listCapasGeograficas)."""
    data = listar_capas(
        q=request.args.get("q"),
        limite=request.args.get("limite"),
        offset=request.args.get("offset"),
    )
    return jsonify(data), 200


@bp.get("/capas/<int:capa_id>/geojson")
def get_capa_geojson_endpoint(capa_id):
    """Devuelve los datos GeoJSON de una capa en formato FeatureCollection (OpenAPI: getCapaGeojson)."""
    data = get_capa_geojson(capa_id)
    return jsonify(data), 200
