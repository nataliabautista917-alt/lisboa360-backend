"""Repositorio (DAO) de la entidad CapaGeografica — consultas SQL directas contra SQLite."""
from typing import List, Optional

from app.db.connection import get_db
from app.models.capa_geografica import CapaGeografica


def _row_to_capa_geografica(row) -> CapaGeografica:
    return CapaGeografica(
        id=row["id"],
        nombre=row["nombre"],
        tipo=row["tipo"],
        descripcion=row["descripcion"],
        formato=row["formato"],
        ruta_archivo=row["ruta_archivo"],
        fecha_generacion=row["fecha_generacion"],
        estado=row["estado"],
        tipo_geometria=row["tipo_geometria"],
        created_at=row["created_at"],
    )


def _build_where(q=None):
    conds, params = [], []
    if q:
        conds.append("(nombre LIKE ? OR tipo LIKE ? OR descripcion LIKE ?)")
        params.append(f"%{q}%")
        params.append(f"%{q}%")
        params.append(f"%{q}%")
    return conds, params


def list_filtered(conn, q=None, limite=50, offset=0) -> List[CapaGeografica]:
    """Lista capas geográficas paginadas y filtradas por búsqueda libre."""
    conds, params = _build_where(q)
    sql = "SELECT * FROM capa_geografica"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    sql += " ORDER BY id ASC LIMIT ? OFFSET ?"
    return [
        _row_to_capa_geografica(row)
        for row in conn.execute(sql, params + [limite, offset])
    ]


def count_filtered(conn, q=None) -> int:
    """Cuenta capas geográficas coincidentes con el filtro (sin paginación)."""
    conds, params = _build_where(q)
    sql = "SELECT COUNT(*) AS cnt FROM capa_geografica"
    if conds:
        sql += " WHERE " + " AND ".join(conds)
    return conn.execute(sql, params).fetchone()["cnt"]


def get_by_id(conn, capa_id: int) -> Optional[CapaGeografica]:
    row = conn.execute(
        "SELECT * FROM capa_geografica WHERE id = ?", (capa_id,)
    ).fetchone()
    return _row_to_capa_geografica(row) if row is not None else None
