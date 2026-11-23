"""Modelo de la entidad Barrio — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Barrio:
    id: int
    nombre: str
    descripcion: Optional[str] = None
    geometria: Optional[str] = None
    created_at: Optional[str] = None
