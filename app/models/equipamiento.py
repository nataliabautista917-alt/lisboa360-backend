"""Modelo de la entidad Equipamiento — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Equipamiento:
    id: int
    nombre: str
    tipo: str
    descripcion: Optional[str] = None
    capacidad: Optional[int] = None
    geometria: Optional[str] = None
    estado: Optional[str] = None
    categoria: Optional[str] = None
    barrio_id: Optional[int] = None
    created_at: Optional[str] = None
