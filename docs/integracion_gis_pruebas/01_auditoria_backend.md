# Auditoría backend — Integración GIS (Fase 13)

## 1. Endpoints auditados

| Endpoint | Método | Resultado |
|----------|--------|-----------|
| `/api/v1/capas` | GET | **APROBADO** — HTTP 200, `{items, total, limit, offset}` |
| `/api/v1/capas/1/geojson` | GET | **APROBADO** — FeatureCollection, 3 features |
| `/api/v1/capas/2/geojson` | GET | **APROBADO** — FeatureCollection, 429 features, CRS EPSG:4326 |
| `/api/v1/capas/3/geojson` | GET | **APROBADO** — FeatureCollection, 57 features, CRS EPSG:4326 |
| `/api/v1/capas/4/geojson` | GET | **APROBADO** — FeatureCollection, 1 feature, CRS declarado EPSG:4686 |
| `/api/v1/capas/999/geojson` | GET | **APROBADO** — HTTP 404 con error JSON estandarizado |
| `/api/v1/barrios/lisboa` | GET | **APROBADO** — HTTP 200 |

## 2. Capas registradas (GET /api/v1/capas)

| id | nombre | tipo | tipo_geometria | estado |
|----|--------|------|----------------|--------|
| 1 | Ejemplo ficticio: Capa general | general | Point, LineString, Polygon | activa |
| 2 | Pistas Recreativas y Deportivas en Parque (IDRD) | parque_deportivo | MultiPolygon | activa |
| 3 | Escenario Deportivo en Parque (IDRD) | escenario_deportivo | MultiPolygon | activa |
| 4 | Delimitación Localidad de Suba (SDP/IDECA) | localidad | Polígono | activa |

- **4 capas** disponibles, ids 1–4, sin duplicados.
- Capa ficticia id=1 preservada.
- Capas reales id=2,3,4 disponibles.

## 3. Servicios, repositorios y modelos

- `capas_service.listar_capas()` valida `limite`/`offset`/`q`, pagina y transforma con `_capa_a_diccionario()`.
- `capas_service.get_capa_geojson()` lee el archivo físico bajo `GEOJSON_DIR`, valida estructura mínima (dict con `type == "FeatureCollection"`), lanza `NotFoundError` si no existe o es inválido.
- `capa_geografica_repository` provee `list_filtered` y `get_by_id`.
- Modelo `CapaGeografica` mapea la tabla `capa_geografica` (sin cambios de schema).

## 4. Archivos físicos y rutas

`GEOJSON_DIR = <repo>/data/geojson`. Archivos verificados existentes:
- `ejemplo_ficticio_capa_general.geojson` (3 features)
- `parques_pista_recreativa_idrd_2026_procesado.geojson` (429 features)
- `parques_escenario_deportivo_idrd_2026_procesado.geojson` (57 features)
- `localidad_suba_limite_oficial.geojson` (1 feature)

Los metadatos de `capa_geografica.ruta_archivo` coinciden con los archivos servidos (comprobado por `/geojson` exitoso).

## 5. Inicialización SQLite y seed

- `init_db()` crea el schema y ejecuta `seed()` con `SEED_FICTICIO=1`.
- Seed inserta capas ficticias (id=1) y reales (id=2,3,4) con `INSERT OR IGNORE` (idempotente).
- Prueba en memoria (`:memory:`) con `init_db(app)` ejecutada por la suite: **39/39 tests pasan**.

## 6. Manejo de errores

- Errores estandarizados JSON (`{error:{code,message,details}}`).
- `NotFoundError` → 404; validación → 422; inesperado → 500.
- Ruta inexistente → 404 JSON (verificado por test y por endpoint real).
- No se exponen rutas internas del servidor en las respuestas.

## 7. Pruebas automatizadas

- Comando: `python -m pytest tests/ -v` (con Python 3.14.7 + pytest 9.2.0, dependencias instaladas en venv auxiliar).
- **Resultado: 39 passed, 0 failed** (incluye `TestCapasRutas`: `test_get_capas_ok`, `test_get_capa_geojson_ok`, `test_get_capa_geojson_no_encontrada`).

## 8. Servidor Flask real

- Servidor iniciado en `127.0.0.1:5000` con `SEED_FICTICIO=1`.
- Los 4 endpoints de capas y `/barrios/lisboa` respondieron HTTP 200; capa inexistente respondió HTTP 404.

## Conclusión

**Backend: APROBADO.**
