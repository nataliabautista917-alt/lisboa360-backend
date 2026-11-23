"""Utilidades de validación de parámetros y de estructuras GeoJSON."""
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

MAX_LIMITE_DEFAULT = 50
LIMITE_MAXIMO = 500
MAX_LARGO_CADENA = 100


def validar_limite_offset(limite, offset):
    """Valida y normaliza `limite` (entre 1 y 500, default 50) y `offset` (>= 0, default 0)."""
    if limite is None:
        limite = MAX_LIMITE_DEFAULT
    if offset is None:
        offset = 0
    try:
        limite = int(limite)
        offset = int(offset)
    except (TypeError, ValueError) as exc:
        raise ValidationError(
            "Parámetros inválidos: 'limite' y 'offset' deben ser enteros.",
            details={"campos": ["limite", "offset"]},
        ) from exc
    if not 1 <= limite <= LIMITE_MAXIMO:
        raise ValidationError(
            f"El parámetro 'limite' debe estar entre 1 y {LIMITE_MAXIMO}.",
            details={"campos": ["limite"], "valor": limite},
        )
    if offset < 0:
        raise ValidationError(
            "El parámetro 'offset' debe ser mayor o igual a 0.",
            details={"campos": ["offset"], "valor": offset},
        )
    return limite, offset


def _validar_categoria_generico(valor, campo):
    if valor is None:
        return None
    if not isinstance(valor, str) or len(valor.strip()) == 0 or len(valor) > MAX_LARGO_CADENA:
        raise ValidationError(
            f"El parámetro '{campo}' debe ser una cadena no vacía de 1 a {MAX_LARGO_CADENA} caracteres.",
            details={"campos": [campo]},
        )
    return valor.strip()


def validar_categoria(categoria):
    """Valida el filtro de categoría (cualquier cadena no vacía)."""
    return _validar_categoria_generico(categoria, "categoria")


def validar_tipo_filtro(tipo):
    """Valida el filtro de tipo (cualquier cadena no vacía)."""
    return _validar_categoria_generico(tipo, "tipo")


def validar_q(q):
    """Valida la búsqueda libre 'q' (cadena no vacía)."""
    return _validar_categoria_generico(q, "q")
