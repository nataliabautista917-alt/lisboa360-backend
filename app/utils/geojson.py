"""Utilidades de validación y construcción de estructuras GeoJSON compatibles.

Soporta los tipos geométricos propuestos en el contrato OpenAPI:
Point, LineString, Polygon (y otras geometrías de uso general: MultiPoint,
MultiLineString, MultiPolygon, GeometryCollection).
"""
import json

from app.utils.errors import ValidationError

TIPOS_GEOJSON_SOPORTADOS = (
    "Point",
    "LineString",
    "Polygon",
    "MultiPoint",
    "MultiLineString",
    "MultiPolygon",
    "GeometryCollection",
)


def _validar_position(pos):
    if not isinstance(pos, list) or len(pos) < 2 or len(pos) > 3:
        raise ValidationError(
            "Una posición GeoJSON debe ser una lista [longitud, latitud] con opcional altitud."
        )
    for valor in pos:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValidationError("Los valores de la posición deben ser numéricos.")


def _validar_positions(positions, minimo):
    if not isinstance(positions, list) or len(positions) < minimo:
        raise ValidationError(f"Los posiciones GeoJSON deben tener al menos {minimo} elementos.")
    for pos in positions:
        _validar_position(pos)


def _validar_ring(ring):
    _validar_positions(ring, 4)


def _validar_coordenadas(tipo, coords):
    if tipo == "Point":
        _validar_position(coords)
    elif tipo == "LineString":
        _validar_positions(coords, 2)
    elif tipo == "Polygon":
        if not isinstance(coords, list) or not coords:
            raise ValidationError("Un Polygon debe tener al menos un anillo.")
        for ring in coords:
            _validar_ring(ring)
    elif tipo == "MultiPoint":
        _validar_positions(coords, 1)
    elif tipo == "MultiLineString":
        if not isinstance(coords, list) or not coords:
            raise ValidationError("Un MultiLineString debe tener al menos una línea.")
        for linea in coords:
            _validar_positions(linea, 2)
    elif tipo == "MultiPolygon":
        if not isinstance(coords, list) or not coords:
            raise ValidationError("Un MultiPolygon debe tener al menos un polígono.")
        for poly in coords:
            if not isinstance(poly, list) or not poly:
                raise ValidationError("Un polígono de un MultiPolygon debe tener al menos un anillo.")
            for ring in poly:
                _validar_ring(ring)


def validar_geometria(geometria, contexto="geometría"):
    """Valida que `geometria` sea un objeto GeoJSON válido con tipo soportado y estructura coherente."""
    if geometria is None:
        return
    if not isinstance(geometria, dict):
        raise ValidationError(f"El campo '{contexto}' debe ser un objeto GeoJSON.")
    tipo = geometria.get("type")
    if tipo not in TIPOS_GEOJSON_SOPORTADOS:
        raise ValidationError(
            f"El tipo de {contexto} '{tipo}' no está permitido.",
            details={"campos": [contexto], "tipos_soportados": list(TIPOS_GEOJSON_SOPORTADOS)},
        )
    if tipo == "GeometryCollection":
        geoms = geometria.get("geometries")
        if not isinstance(geoms, list) or not geoms:
            raise ValidationError("Un GeometryCollection debe tener una lista 'geometries' no vacía.")
        for g in geoms:
            validar_geometria(g, contexto=f"{contexto} (GeometryCollection)")
    elif "coordinates" not in geometria:
        raise ValidationError(f"El {contexto} debe contener el campo 'coordinates'.")
    else:
        _validar_coordenadas(tipo, geometria["coordinates"])


def geometria_a_diccionario(text):
    """Convierte una cadena GeoJSON almacenada en SQLite a diccionario, o None."""
    if text is None:
        return None
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None
    return data if isinstance(data, dict) else None


def feature(geometria, properties):
    """Construye un objeto GeoJSON Feature con geometría y propiedades."""
    return {
        "type": "Feature",
        "geometry": geometria,
        "properties": properties if properties is not None else {},
    }


def feature_collection(features):
    """Construye un objeto GeoJSON FeatureCollection con una lista de features."""
    return {"type": "FeatureCollection", "features": features}
