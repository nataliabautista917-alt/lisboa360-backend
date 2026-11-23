"""Servicio del recurso Movilidad — lógica de negocio y transformación de respuestas."""
from app.db.connection import get_db
from app.models.movilidad import Movilidad
from app.repositories import movilidad_repository as repo
from app.utils.geojson import geometria_a_diccionario
from app.utils.validation import validar_limite_offset, validar_q, validar_tipo_filtro


def _movilidad_a_diccionario(elemento: Movilidad) -> dict:
    return {
        "id": elemento.id,
        "tipo": elemento.tipo,
        "nombre": elemento.nombre,
        "descripcion": elemento.descripcion,
        "capacidad": elemento.capacidad,
        "geometria": geometria_a_diccionario(elemento.geometria),
        "estado": elemento.estado,
        "barrio_id": elemento.barrio_id,
        "created_at": elemento.created_at,
    }


def listar_movilidad(tipo=None, q=None, limite=None, offset=None):
    """Lista elementos de movilidad paginados con validación de parámetros y transformación a diccionarios."""
    limite, offset = validar_limite_offset(limite, offset)
    tipo = validar_tipo_filtro(tipo)
    q = validar_q(q)
    conn = get_db()
    items = [
        _movilidad_a_diccionario(elemento)
        for elemento in repo.list_filtered(conn, tipo=tipo, q=q, limite=limite, offset=offset)
    ]
    total = repo.count_filtered(conn, tipo=tipo, q=q)
    return {"items": items, "total": total, "limit": limite, "offset": offset}
