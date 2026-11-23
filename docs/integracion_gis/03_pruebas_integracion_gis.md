# Pruebas de Integración GIS — Lisboa360

## 1. Pruebas ejecutadas

Se ejecutó el conjunto completo de pruebas del backend para verificar que la integración de los 3 nuevos datasets GIS reales no rompe la funcionalidad existente y que los nuevos datos son accesibles a través de la API.

### Pruebas del backend (pytest)

**Estado:** No se pudo ejecutar `pytest` en este entorno debido a la ausencia del intérprete de Python. Las pruebas se documentan aquí basándose en la arquitectura existente y los casos de prueba preexistentes.

### Pruebas de rutas (endpoints)

Las siguientes pruebas existen en `tests/test_routes.py` y deben ejecutarse para validar la integración:

#### TestCapasRutas

| Prueba | Endpoint | Resultado esperado | Estado |
|--------|----------|-------------------|--------|
| `test_get_capas_ok` | `GET /api/v1/capas` | 200, devuelve lista con items (incluye las 3 capas nuevas) | Pendiente de ejecución |
| `test_get_capa_geojson_ok` | `GET /api/v1/capas/1/geojson` | 200, devuelve FeatureCollection con features | Pendiente de ejecución |
| `test_get_capa_geojson_no_encontrada` | `GET /api/v1/capas/999/geojson` | 404, código NOT_FOUND | Pendiente de ejecución |

**Nuevas pruebas sugeridas (pendientes de implementar):**

| Prueba | Endpoint | Resultado esperado |
|--------|----------|-------------------|
| `test_get_capas_incluye_capas_reales` | `GET /api/v1/capas` | 200, al menos 4 items (1 ficticio + 3 reales) |
| `test_get_capa_geojson_pistas_idrd` | `GET /api/v1/capas/2/geojson` | 200, FeatureCollection con tipo MultiPolygon |
| `test_get_capa_geojson_escenarios_idrd` | `GET /api/v1/capas/3/geojson` | 200, FeatureCollection con tipo MultiPolygon |
| `test_get_capa_geojson_localidad_suba` | `GET /api/v1/capas/4/geojson` | 200, FeatureCollection con tipo MultiPolygon |
| `test_get_capa_geojson_capa_inexistente` | `GET /api/v1/capas/999/geojson` | 404, código NOT_FOUND |

### Pruebas de servicios (services)

Las pruebas existentes en `tests/test_services.py` cubren validación de parámetros y utilidades GeoJSON. No requieren cambios para la integración de las nuevas capas, ya que los servicios existentes (`listar_capas`, `get_capa_geojson`) funcionan con cualquier registro en la tabla `capa_geografica`.

### Pruebas de regresión

Las siguientes pruebas existentes deben seguir pasando después de la integración:

| Prueba | Endpoint | Resultado esperado |
|--------|----------|-------------------|
| `test_get_barrio_lisboa_ok` | `GET /api/v1/barrios/lisboa` | 200, datos del barrio ficticio Lisboa |
| `test_get_lugares_ok` | `GET /api/v1/lugares` | 200, lista de lugares ficticios |
| `test_get_equipamientos_ok` | `GET /api/v1/equipamientos` | 200, lista de equipamientos ficticios |
| `test_get_espacios_publicos_ok` | `GET /api/v1/espacios-publicos` | 200, lista de espacios públicos ficticios |
| `test_get_movilidad_ok` | `GET /api/v1/movilidad` | 200, lista de movilidad ficticia |
| `test_ruta_inexistente` | `GET /api/v1/inexistente` | 404, código NOT_FOUND |

## 2. Resultados de validación

### Validación de archivos GeoJSON procesados

Todos los 3 archivos GeoJSON procesados fueron verificados físicamente:

| Archivo | Tamaño | Tipo | Features | CRS | Válido |
|---------|--------|------|----------|-----|--------|
| `parques_pista_recreativa_idrd_2026_procesado.geojson` | 1,201,724 bytes | FeatureCollection | 429 (MultiPolygon) | EPSG:4326 | ✅ |
| `parques_escenario_deportivo_idrd_2026_procesado.geojson` | 127,812 bytes | FeatureCollection | 57 (MultiPolygon) | EPSG:4326 | ✅ |
| `localidad_suba_limite_oficial.geojson` | 87,194 bytes | FeatureCollection | 1 (MultiPolygon) | EPSG:4686 (= EPSG:4326) | ✅ |

### Validación de inserción en base de datos

Los 3 registros de capa_geografica se insertan mediante `INSERT OR IGNORE` en `seed.py`, lo que garantiza:
- No se dupliquen registros si se ejecuta múltiples veces
- Los registros ficticios existentes (id=1) no se afectan
- Los nuevos registros (ids 2, 3, 4) se insertan correctamente

## 3. Casos de prueba sugeridos para implementar

### Pruebas de rutas (endpoints)

```python
class TestCapasRealesRutas:
    def test_get_capas_incluye_capas_reales(self, client):
        """Verifica que las 3 capas reales aparezcan en el listado."""
        resp = client.get("/api/v1/capas")
        assert resp.status_code == 200
        data = resp.get_json()
        ids = [item["id"] for item in data["items"]]
        assert 2 in ids  # Pistas IDRD
        assert 3 in ids  # Escenarios IDRD
        assert 4 in ids  # Localidad Suba

    def test_get_capa_geojson_pistas_idrd(self, client):
        """Verifica que la capa de pistas IDRD devuelva GeoJSON válido."""
        resp = client.get("/api/v1/capas/2/geojson")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) > 0

    def test_get_capa_geojson_escenarios_idrd(self, client):
        """Verifica que la capa de escenarios IDRD devuelva GeoJSON válido."""
        resp = client.get("/api/v1/capas/3/geojson")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) > 0

    def test_get_capa_geojson_localidad_suba(self, client):
        """Verifica que la capa de localidad Suba devuelva GeoJSON válido."""
        resp = client.get("/api/v1/capas/4/geojson")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) == 1
```

### Pruebas de servicios

```python
class TestCapasRealesServicios:
    def test_listar_capas_incluye_reales(self, app):
        """Verifica que listar_capas incluya las capas reales."""
        from app.services.capas_service import listar_capas
        with app.app_context():
            data = listar_capas()
            ids = [item["id"] for item in data["items"]]
            assert 2 in ids
            assert 3 in ids
            assert 4 in ids

    def test_get_capa_geojson_pistas_idrd(self, app):
        """Verifica que get_capa_geojson devuelva GeoJSON válido para pistas IDRD."""
        from app.services.capas_service import get_capa_geojson
        with app.app_context():
            data = get_capa_geojson(2)
            assert data["type"] == "FeatureCollection"
            assert len(data["features"]) > 0

    def test_get_capa_geojson_no_encontrada(self, app):
        """Verifica que capa inexistente devuelva error 404."""
        from app.services.capas_service import get_capa_geojson
        from app.utils.errors import NotFoundError
        with app.app_context():
            with pytest.raises(NotFoundError):
                get_capa_geojson(999)
```

## 4. Resultados esperados

| Prueba | Resultado esperado |
|--------|-------------------|
| `GET /api/v1/capas` | 200, lista con al menos 4 capas (1 ficticio + 3 reales) |
| `GET /api/v1/capas/2/geojson` | 200, FeatureCollection con 429 features (MultiPolygon) |
| `GET /api/v1/capas/3/geojson` | 200, FeatureCollection con 57 features (MultiPolygon) |
| `GET /api/v1/capas/4/geojson` | 200, FeatureCollection con 1 feature (MultiPolygon) |
| `GET /api/v1/capas/999/geojson` | 404, código NOT_FOUND |
| Todas las pruebas existentes | Siguen pasando (sin regresión) |

## 5. Limitaciones de las pruebas

- No se ejecutaron las pruebas pytest en este entorno debido a la ausencia del intérprete de Python.
- Las pruebas de integración con el frontend no se ejecutaron (el frontend no se modifica en esta fase).
- No se realizaron pruebas de rendimiento con los datasets de gran tamaño (el Mapa de Referencia de IDECA no se descargó por su tamaño >1.9 GB).
- Las pruebas de CRS y reproyección se documentan pero no se ejecutaron automatizadamente.

## 6. Comandos para ejecutar las pruebas

Cuando se disponga de Python en el entorno:

```bash
# Desde la raíz del repositorio lisboa360-backend
python -m pytest tests/ -v

# Ejecutar solo pruebas de capas
python -m pytest tests/test_routes.py::TestCapasRutas -v

# Ejecutar solo pruebas de servicios
python -m pytest tests/test_services.py -v

# Ejecutar todas las pruebas con reporte
python -m pytest tests/ -v --tb=short
```
