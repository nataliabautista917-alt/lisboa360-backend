"""Pruebas de servicios y utilidades de Lisboa360 Backend."""
import json

import pytest

from app.utils.errors import ValidationError
from app.utils.geojson import (
    feature,
    feature_collection,
    geometria_a_diccionario,
    validar_geometria,
)
from app.utils.validation import validar_limite_offset


class TestValidarLimiteOffset:
    def test_defaults(self):
        assert validar_limite_offset(None, None) == (50, 0)

    def test_valores_validos(self):
        assert validar_limite_offset("10", "5") == (10, 5)

    def test_error_limite_cero(self):
        with pytest.raises(ValidationError):
            validar_limite_offset(0, 0)

    def test_error_limite_maximo(self):
        with pytest.raises(ValidationError):
            validar_limite_offset(501, 0)

    def test_error_offset_negativo(self):
        with pytest.raises(ValidationError):
            validar_limite_offset(50, -1)


class TestValidarGeometria:
    def test_punto_valido(self):
        validar_geometria({"type": "Point", "coordinates": [1.0, 2.0]})

    def test_linea_valida(self):
        validar_geometria({"type": "LineString", "coordinates": [[1.0, 2.0], [3.0, 4.0]]})

    def test_poligono_valido(self):
        validar_geometria({"type": "Polygon", "coordinates": [[[0, 0], [0, 1], [1, 1], [0, 0]]]})

    def test_tipo_invalido(self):
        with pytest.raises(ValidationError):
            validar_geometria({"type": "Circulo", "coordinates": []})

    def test_punto_sin_coordenadas(self):
        with pytest.raises(ValidationError):
            validar_geometria({"type": "Point"})

    def test_coordenadas_no_numericas(self):
        with pytest.raises(ValidationError):
            validar_geometria({"type": "Point", "coordinates": ["a", "b"]})

    def test_none_es_aceptado(self):
        validar_geometria(None)


class TestGeoJsonUtil:
    def test_geometria_a_diccionario(self):
        text = json.dumps({"type": "Point", "coordinates": [1.0, 2.0]})
        assert geometria_a_diccionario(text) == {"type": "Point", "coordinates": [1.0, 2.0]}

    def test_geometria_a_diccionario_none(self):
        assert geometria_a_diccionario(None) is None

    def test_geometria_a_diccionario_invalida(self):
        assert geometria_a_diccionario("nope") is None

    def test_feature(self):
        geom = {"type": "Point", "coordinates": [1.0, 2.0]}
        feat = feature(geom, {"id": 1})
        assert feat["type"] == "Feature"
        assert feat["geometry"] == geom
        assert feat["properties"] == {"id": 1}

    def test_feature_collection(self):
        fc = feature_collection([])
        assert fc == {"type": "FeatureCollection", "features": []}
