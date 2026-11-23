"""Conexión SQLite centralizada a la base de datos de Lisboa360.

Patrón de conexión por aplicación con `sqlite3`, `Row` factory, habilitación de claves
foráneas (`PRAGMA foreign_keys = ON`) y acceso desde la request context mediante
`current_app`. El archivo de base de datos se crea en `database/lisboa360.db` (o el
valor de `DATABASE_PATH`).
"""
import sqlite3
from pathlib import Path

from flask import current_app

from app.db import schema, seed


def get_db():
    """Devuelve la conexión SQLite de la aplicación actual (crea y registra si no existe)."""
    if "db_connection" not in current_app.extensions:
        db_path = Path(current_app.config["DATABASE_PATH"])
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(db_path), check_same_thread=False)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        current_app.extensions["db_connection"] = conn
    return current_app.extensions["db_connection"]


def init_db(app):
    """Crea el esquema (si no existe) y aplica el seed de datos ficticios de desarrollo."""
    with app.app_context():
        conn = get_db()
        schema.create_all(conn)
        seed.seed(conn, enabled=app.config.get("SEED_FICTICIO", True))


def close_db(app):
    """Cierra la conexión de la aplicación si está abierta."""
    with app.app_context():
        conn = current_app.extensions.pop("db_connection", None)
        if conn is not None:
            conn.close()
