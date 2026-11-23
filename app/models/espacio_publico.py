"""Modelo de la entidad EspacioPublico — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class EspacioPublico:
    id: int
    nombre: str
    tipo: str
    descripcion: Optional[str] = None
    area_estimada: Optional[float] = None
    geometria: Optional[str] = None
    estado: Optional[str] = None
    categoria: Optional[str] = None
    barrio_id: Optional[int] = None
    created_at: Optional[str] = None
