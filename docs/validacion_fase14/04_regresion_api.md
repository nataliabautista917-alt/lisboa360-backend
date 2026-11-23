# Regresión de API — Fase 14 (Lisboa360)

## 1. Tests ejecutados

Comando: `python -m pytest tests/ -v`
Resultado: **39 passed, 0 failed** (ejecutado en esta fase).

## 2. Endpoints verificados

| Endpoint | HTTP | Resultado |
|----------|------|-----------|
| GET /api/v1/capas | 200 | 4 capas (ids 1–4) |
| GET /api/v1/capas/1/geojson | 200 | FeatureCollection, 3 features |
| GET /api/v1/capas/2/geojson | 200 | FeatureCollection, 429 features, EPSG:4326 |
| GET /api/v1/capas/3/geojson | 200 | FeatureCollection, 57 features, EPSG:4326 |
| GET /api/v1/capas/4/geojson | 200 | FeatureCollection, 1 feature, EPSG:4686 (declarado) |
| GET /api/v1/capas/999/geojson | 404 | Error JSON estandarizado |
| GET /api/v1/barrios/lisboa | 200 | OK |

## 3. Validación GeoJSON

- Los 4 archivos son `FeatureCollection` válidos.
- Features: 3 + 429 + 57 + 1 = 490.
- Geometrías no nulas.
- CRS declarados consistentes con los archivos.

## 4. Errores detectados

Ninguno nuevo. La corrección de robustez fue en el frontend (normalización de estructura MultiPolygon/Polygon de Suba).

## 5. Regresiones

Ninguna. 39/39 tests pasan.

## Conclusión

**Regresión de API: APROBADO.**
