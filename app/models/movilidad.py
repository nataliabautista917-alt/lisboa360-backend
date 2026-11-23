"""Modelo de la entidad Movilidad — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Movilidad:
    id: int
    tipo: str
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    capacidad: Optional[int] = None
    geometria: Optional[str] = None
    estado: Optional[str] = None
    barrio_id: Optional[int] = None
    created_at: Optional[str] = None
