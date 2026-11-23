"""Modelo de la entidad Lugar — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Lugar:
    id: int
    nombre: str
    descripcion: Optional[str] = None
    categoria: Optional[str] = None
    observaciones: Optional[str] = None
    geometria: Optional[str] = None
    barrio_id: Optional[int] = None
    created_at: Optional[str] = None
