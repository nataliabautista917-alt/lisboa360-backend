"""Repositorio (DAO) del recurso Lugar — consultas SQL directas contra SQLite."""
from typing import List, Optional

from app.db.connection import get_db
from app.models.lugar import Lugar


def _row_to_lugar(row) -> Lugar:
    return Lugar(
        id=row["id"],
        nombre=row["nombre"],
        descripcion=row["descripcion"],
        categoria=row["categoria"],
        observaciones=row["observaciones"],
        geometria=row["geometria"],
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


def list_filtered(conn, categoria=None, q=None, limite=50, offset=0) -> List[Lugar]:
    """Lista lugares paginados y filtrados por categoría y búsqueda libre."""
    conds, params = _build_where(categoria, q)
    sql = "SELECT * FROM lugar"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    sql += " ORDER BY id ASC LIMIT ? OFFSET ?"
    return [
        _row_to_lugar(row)
        for row in conn.execute(sql, params + [limite, offset])
    ]


def count_filtered(conn, categoria=None, q=None) -> int:
    """Cuenta lugares coincidentes con los filtros (sin paginación)."""
    conds, params = _build_where(categoria, q)
    sql = "SELECT COUNT(*) AS cnt FROM lugar"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    return conn.execute(sql, params).fetchone()["cnt"]


def get_by_id(conn, lugar_id: int) -> Optional[Lugar]:
    row = conn.execute("SELECT * FROM lugar WHERE id = ?", (lugar_id,)).fetchone()
    return _row_to_lugar(row) if row is not None else None
