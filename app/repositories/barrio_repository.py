"""Repositorio (DAO) del recurso Barrio — consultas SQL directas contra SQLite."""
from typing import Optional

from app.db.connection import get_db
from app.models.barrio import Barrio


def _row_to_barrio(row) -> Barrio:
    return Barrio(
        id=row["id"],
        nombre=row["nombre"],
        descripcion=row["descripcion"],
        geometria=row["geometria"],
        created_at=row["created_at"],
    )


def get_by_nombre(conn, nombre: str) -> Optional[Barrio]:
    """Devuelve el barrio con el nombre dado, o None."""
    row = conn.execute("SELECT * FROM barrio WHERE nombre = ?", (nombre,)).fetchone()
    return _row_to_barrio(row) if row is not None else None


def get_by_id(conn, barrio_id: int) -> Optional[Barrio]:
    """Devuelve el barrio con el id dado, o None."""
    row = conn.execute("SELECT * FROM barrio WHERE id = ?", (barrio_id,)).fetchone()
    return _row_to_barrio(row) if row is not None else None


def count_all(conn) -> int:
    """Cuenta registros totales de la tabla barrio."""
    return conn.execute("SELECT COUNT(*) AS cnt FROM barrio").fetchone()["cnt"]
