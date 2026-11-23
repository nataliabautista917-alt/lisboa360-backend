"""Repositorio (DAO) del recurso Movilidad — consultas SQL directas contra SQLite."""
from typing import List, Optional

from app.db.connection import get_db
from app.models.movilidad import Movilidad


def _row_to_movilidad(row) -> Movilidad:
    return Movilidad(
        id=row["id"],
        tipo=row["tipo"],
        nombre=row["nombre"],
        descripcion=row["descripcion"],
        capacidad=row["capacidad"],
        geometria=row["geometria"],
        estado=row["estado"],
        barrio_id=row["barrio_id"],
        created_at=row["created_at"],
    )


def _build_where(tipo=None, q=None):
    conds, params = [], []
    if tipo:
        conds.append("tipo = ?")
        params.append(tipo)
    if q:
        conds.append("(nombre LIKE ? OR descripcion LIKE ?)")
        params.append(f"%{q}%")
        params.append(f"%{q}%")
    return conds, params


def list_filtered(conn, tipo=None, q=None, limite=50, offset=0) -> List[Movilidad]:
    """Lista elementos de movilidad paginados y filtrados por tipo y búsqueda libre."""
    conds, params = _build_where(tipo, q)
    sql = "SELECT * FROM movilidad"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    sql += " ORDER BY id ASC LIMIT ? OFFSET ?"
    return [
        _row_to_movilidad(row)
        for row in conn.execute(sql, params + [limite, offset])
    ]


def count_filtered(conn, tipo=None, q=None) -> int:
    """Cuenta elementos de movilidad coincidentes con los filtros (sin paginación)."""
    conds, params = _build_where(tipo, q)
    sql = "SELECT COUNT(*) AS cnt FROM movilidad"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    return conn.execute(sql, params).fetchone()["cnt"]


def get_by_id(conn, movilidad_id: int) -> Optional[Movilidad]:
    row = conn.execute(
        "SELECT * FROM movilidad WHERE id = ?", (movilidad_id,)
    ).fetchone()
    return _row_to_movilidad(row) if row is not None else None
