"""Servicio del recurso Lugar — lógica de negocio y transformación de respuestas."""
from app.db.connection import get_db
from app.models.lugar import Lugar
from app.repositories import lugar_repository as repo
from app.utils.geojson import geometria_a_diccionario
from app.utils.validation import validar_categoria, validar_limite_offset, validar_q


def _lugar_a_diccionario(lugar: Lugar) -> dict:
    return {
        "id": lugar.id,
        "nombre": lugar.nombre,
        "descripcion": lugar.descripcion,
        "categoria": lugar.categoria,
        "observaciones": lugar.observaciones,
        "geometria": geometria_a_diccionario(lugar.geometria),
        "barrio_id": lugar.barrio_id,
        "created_at": lugar.created_at,
    }


def listar_lugares(categoria=None, q=None, limite=None, offset=None):
    """Lista lugares paginados con validación de parámetros y transformación a diccionarios."""
    limite, offset = validar_limite_offset(limite, offset)
    categoria = validar_categoria(categoria)
    q = validar_q(q)
    conn = get_db()
    items = [
        _lugar_a_diccionario(lugar)
        for lugar in repo.list_filtered(conn, categoria=categoria, q=q, limite=limite, offset=offset)
    ]
    total = repo.count_filtered(conn, categoria=categoria, q=q)
    return {"items": items, "total": total, "limit": limite, "offset": offset}
