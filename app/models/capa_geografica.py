"""Modelo de la entidad CapaGeografica — dataclasses para mapeo de datos a SQLite."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class CapaGeografica:
    id: int
    nombre: str
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    formato: Optional[str] = None
    ruta_archivo: Optional[str] = None
    fecha_generacion: Optional[str] = None
    estado: Optional[str] = None
    tipo_geometria: Optional[str] = None
    created_at: Optional[str] = None
