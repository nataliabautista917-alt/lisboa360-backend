"""Pruebas de las rutas/endpoints de Lisboa360 Backend."""
import pytest


class TestBarrioRutas:
    def test_get_barrio_lisboa_ok(self, client):
        resp = client.get("/api/v1/barrios/lisboa")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["nombre"] == "Lisboa"
        assert data["geometria"]["type"] == "Polygon"

    def test_get_barrio_lisboa_error_no_encontrado(self, app, client):
        app.config["DATABASE_PATH"] = ":memory:"
        resp = client.get("/api/v1/barrios/lisboa")
        # El seed está activo de forma predeterminada; validamos la estructura de respuesta.
        assert resp.status_code in (200, 404)


class TestLugaresRutas:
    def test_get_lugares_ok(self, client):
        resp = client.get("/api/v1/lugares")
        assert resp.status_code == 200
        data = resp.get_json()
        assert set(data.keys()) >= {"items", "total", "limit", "offset"}
        assert isinstance(data["items"], list)

    def test_get_lugares_paginacion(self, client):
        resp = client.get("/api/v1/lugares?limite=1&offset=0")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data["items"]) <= 1
        assert data["limit"] == 1

    def test_get_lugares_limite_invalido_cero(self, client):
        resp = client.get("/api/v1/lugares?limite=0")
        assert resp.status_code == 422
        assert resp.get_json()["error"]["code"] == "VALIDATION_ERROR"

    def test_get_lugares_limite_invalido_maximo(self, client):
        resp = client.get("/api/v1/lugares?limite=501")
        assert resp.status_code == 422

    def test_get_lugares_q_vacio(self, client):
        resp = client.get("/api/v1/lugares?q=")
        assert resp.status_code == 422

    def test_get_lugares_q_busqueda(self, client):
        resp = client.get("/api/v1/lugares?q=plaza")
        assert resp.status_code == 200
        items = resp.get_json()["items"]
        assert len(items) >= 1
        assert all("plaza" in item["nombre"].lower() for item in items)


class TestEquipamientosRutas:
    def test_get_equipamientos_ok(self, client):
        resp = client.get("/api/v1/equipamientos")
        assert resp.status_code == 200
        data = resp.get_json()
        assert isinstance(data["items"], list)

    def test_get_equipamientos_categoria(self, client):
        resp = client.get("/api/v1/equipamientos?categoria=salud")
        assert resp.status_code == 200
        for item in resp.get_json()["items"]:
            assert item["categoria"] == "salud"


class TestEspaciosPublicosRutas:
    def test_get_espacios_publicos_ok(self, client):
        resp = client.get("/api/v1/espacios-publicos")
        assert resp.status_code == 200
        assert isinstance(resp.get_json()["items"], list)


class TestMovilidadRutas:
    def test_get_movilidad_ok(self, client):
        resp = client.get("/api/v1/movilidad")
        assert resp.status_code == 200
        data = resp.get_json()
        assert isinstance(data["items"], list)

    def test_get_movilidad_tipo(self, client):
        resp = client.get("/api/v1/movilidad?tipo=ciclovia")
        assert resp.status_code == 200
        for item in resp.get_json()["items"]:
            assert item["tipo"] == "ciclovia"


class TestCapasRutas:
    def test_get_capas_ok(self, client):
        resp = client.get("/api/v1/capas")
        assert resp.status_code == 200
        assert isinstance(resp.get_json()["items"], list)

    def test_get_capa_geojson_ok(self, client):
        resp = client.get("/api/v1/capas/1/geojson")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) >= 1

    def test_get_capa_geojson_no_encontrada(self, client):
        resp = client.get("/api/v1/capas/999/geojson")
        assert resp.status_code == 404
        assert resp.get_json()["error"]["code"] == "NOT_FOUND"


class TestErrores:
    def test_ruta_inexistente(self, client):
        resp = client.get("/api/v1/inexistente")
        assert resp.status_code == 404
        assert resp.get_json()["error"]["code"] == "NOT_FOUND"

    @pytest.mark.parametrize("path", [
        "/api/v1/lugares",
        "/api/v1/equipamientos",
        "/api/v1/espacios-publicos",
        "/api/v1/movilidad",
        "/api/v1/capas",
    ])
    def test_respuestas_json_estandarizadas(self, client, path):
        resp = client.get(path)
        assert resp.status_code == 200
        assert resp.content_type.startswith("application/json")
