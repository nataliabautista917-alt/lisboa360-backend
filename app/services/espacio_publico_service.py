"""Servicio del recurso EspacioPublico — lógica de negocio y transformación de respuestas."""
from app.db.connection import get_db
from app.models.espacio_publico import EspacioPublico
from app.repositories import espacio_publico_repository as repo
from app.utils.geojson import geometria_a_diccionario
from app.utils.validation import validar_categoria, validar_limite_offset, validar_q


def _espacio_publico_a_diccionario(espacio_publico: EspacioPublico) -> dict:
    return {
        "id": espacio_publico.id,
        "nombre": espacio_publico.nombre,
        "tipo": espacio_publico.tipo,
        "descripcion": espacio_publico.descripcion,
        "area_estimada": espacio_publico.area_estimada,
        "geometria": geometria_a_diccionario(espacio_publico.geometria),
        "estado": espacio_publico.estado,
        "categoria": espacio_publico.categoria,
        "barrio_id": espacio_publico.barrio_id,
        "created_at": espacio_publico.created_at,
    }


def listar_espacios_publicos(categoria=None, q=None, limite=None, offset=None):
    """Lista espacios públicos paginados con validación de parámetros y transformación a diccionarios."""
    limite, offset = validar_limite_offset(limite, offset)
    categoria = validar_categoria(categoria)
    q = validar_q(q)
    conn = get_db()
    items = [
        _espacio_publico_a_diccionario(espacio_publico)
        for espacio_publico in repo.list_filtered(conn, categoria=categoria, q=q, limite=limite, offset=offset)
    ]
    total = repo.count_filtered(conn, categoria=categoria, q=q)
    return {"items": items, "total": total, "limit": limite, "offset": offset}
