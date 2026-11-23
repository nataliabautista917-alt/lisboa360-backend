"""Servicio del recurso CapasGeograficas — consultas y lectura de datos GeoJSON."""
import json
from pathlib import Path

from flask import current_app

from app.db.connection import get_db
from app.models.capa_geografica import CapaGeografica
from app.repositories import capa_geografica_repository as repo
from app.utils.errors import NotFoundError
from app.utils.validation import validar_limite_offset, validar_q


def _capa_a_diccionario(capa: CapaGeografica) -> dict:
    return {
        "id": capa.id,
        "nombre": capa.nombre,
        "tipo": capa.tipo,
        "descripcion": capa.descripcion,
        "formato": capa.formato,
        "ruta_archivo": capa.ruta_archivo,
        "fecha_generacion": capa.fecha_generacion,
        "estado": capa.estado,
        "tipo_geometria": capa.tipo_geometria,
        "created_at": capa.created_at,
    }


def listar_capas(q=None, limite=None, offset=None):
    """Lista capas geográficas paginadas con validación de parámetros y transformación a diccionarios."""
    limite, offset = validar_limite_offset(limite, offset)
    q = validar_q(q)
    conn = get_db()
    items = [
        _capa_a_diccionario(capa)
        for capa in repo.list_filtered(conn, q=q, limite=limite, offset=offset)
    ]
    total = repo.count_filtered(conn, q=q)
    return {"items": items, "total": total, "limit": limite, "offset": offset}


def get_capa_geojson(capa_id: int) -> dict:
    """
    Devuelve la información geográfica de una capa en formato GeoJSON FeatureCollection.

    Se lee el archivo GeoJSON registrado en `capa_geografica.ruta_archivo` bajo
    `GEOJSON_DIR`. Los datos se entregan directamente; se asume que provienen de una fuente
    de datos controlada (backend), pero se valida estructura mínima de GeoJSON.
    """
    conn = get_db()
    capa = repo.get_by_id(conn, capa_id)
    if capa is None:
        raise NotFoundError(f"Capa geográfica con id {capa_id} no encontrada.")
    if not capa.ruta_archivo:
        raise NotFoundError("Capa geográfica sin archivo asociado.")
    geojson_path = Path(current_app.config["GEOJSON_DIR"]) / capa.ruta_archivo
    if not geojson_path.is_file():
        raise NotFoundError("Datos geográficos de la capa no disponibles.")
    try:
        data = json.loads(geojson_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise NotFoundError("Datos geográficos de la capa no válidos.") from exc
    if not isinstance(data, dict) or data.get("type") != "FeatureCollection":
        raise NotFoundError("Datos geográficos de la capa no válidos.")
    return data
