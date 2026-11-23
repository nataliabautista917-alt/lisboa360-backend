"""Servicio del recurso Equipamiento — lógica de negocio y transformación de respuestas."""
from app.db.connection import get_db
from app.models.equipamiento import Equipamiento
from app.repositories import equipamento_repository as repo
from app.utils.geojson import geometria_a_diccionario
from app.utils.validation import validar_categoria, validar_limite_offset, validar_q


def _equipamiento_a_diccionario(equipamiento: Equipamiento) -> dict:
    return {
        "id": equipamiento.id,
        "nombre": equipamiento.nombre,
        "tipo": equipamiento.tipo,
        "descripcion": equipamiento.descripcion,
        "capacidad": equipamiento.capacidad,
        "geometria": geometria_a_diccionario(equipamiento.geometria),
        "estado": equipamiento.estado,
        "categoria": equipamiento.categoria,
        "barrio_id": equipamiento.barrio_id,
        "created_at": equipamiento.created_at,
    }


def listar_equipamientos(categoria=None, q=None, limite=None, offset=None):
    """Lista equipamientos paginados con validación de parámetros y transformación a diccionarios."""
    limite, offset = validar_limite_offset(limite, offset)
    categoria = validar_categoria(categoria)
    q = validar_q(q)
    conn = get_db()
    items = [
        _equipamiento_a_diccionario(equipamiento)
        for equipamiento in repo.list_filtered(conn, categoria=categoria, q=q, limite=limite, offset=offset)
    ]
    total = repo.count_filtered(conn, categoria=categoria, q=q)
    return {"items": items, "total": total, "limit": limite, "offset": offset}
