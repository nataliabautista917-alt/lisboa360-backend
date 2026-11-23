"""Repositorio (DAO) del recurso Equipamiento — consultas SQL directas contra SQLite."""
from typing import List, Optional

from app.db.connection import get_db
from app.models.equipamiento import Equipamiento


def _row_to_equipamiento(row) -> Equipamiento:
    return Equipamiento(
        id=row["id"],
        nombre=row["nombre"],
        tipo=row["tipo"],
        descripcion=row["descripcion"],
        capacidad=row["capacidad"],
        geometria=row["geometria"],
        estado=row["estado"],
        categoria=row["categoria"],
        barrio_id=row["barrio_id"],
        created_at=row["created_at"],
    )


def _build_where(categoria=None, q=None):
    conds, params = [], []
    if categoria:
        conds.append("categoria = ?")
        params.append(categoria)
    if q:
        conds.append("(nombre LIKE ? OR descripcion LIKE ?)")
        params.append(f"%{q}%")
        params.append(f"%{q}%")
    return conds, params


def list_filtered(conn, categoria=None, q=None, limite=50, offset=0) -> List[Equipamiento]:
    """Lista equipamientos paginados y filtrados por categoría y búsqueda libre."""
    conds, params = _build_where(categoria, q)
    sql = "SELECT * FROM equipamiento"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    sql += " ORDER BY id ASC LIMIT ? OFFSET ?"
    return [
        _row_to_equipamiento(row)
        for row in conn.execute(sql, params + [limite, offset])
    ]


def count_filtered(conn, categoria=None, q=None) -> int:
    """Cuenta equipamientos coincidentes con los filtros (sin paginación)."""
    conds, params = _build_where(categoria, q)
    sql = "SELECT COUNT(*) AS cnt FROM equipamiento"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    return conn.execute(sql, params).fetchone()["cnt"]


def get_by_id(conn, equipamiento_id: int) -> Optional[Equipamiento]:
    row = conn.execute(
        "SELECT * FROM equipamiento WHERE id = ?", (equipamiento_id,)
    ).fetchone()
    return _row_to_equipamiento(row) if row is not None else None
