"""Servicio del recurso Barrio — lógica de negocio del acceso al barrio Lisboa."""
from app.db.connection import get_db
from app.models.barrio import Barrio
from app.repositories import barrio_repository as repo
from app.utils.errors import NotFoundError
from app.utils.geojson import geometria_a_diccionario


def get_barrio_lisboa() -> dict:
    """Devuelve la información general del barrio Lisboa (GET /api/v1/barrios/lisboa)."""
    conn = get_db()
    barrio: Barrio = repo.get_by_nombre(conn, "Lisboa")
    if barrio is None:
        raise NotFoundError("Barrio Lisboa no encontrado.")
    return {
        "id": barrio.id,
        "nombre": barrio.nombre,
        "descripcion": barrio.descripcion,
        "geometria": geometria_a_diccionario(barrio.geometria),
        "created_at": barrio.created_at,
    }
