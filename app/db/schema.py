"""Módulo que ejecuta app/db/schema.sql — esquema de SQLite de forma idempotente."""
import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def create_all(conn: sqlite3.Connection):
    """Ejecuta el script DDL de `schema.sql` en la conexión SQLite activa."""
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    conn.commit()
