# Regresión de API — Fase 15 (Lisboa360)

## 1. Tests ejecutados

Comando: `python -m pytest tests/ -v`
Resultado: **39 passed, 0 failed**.

## 2. Endpoints verificados

| Endpoint | HTTP | Resultado |
|----------|------|-----------|
| GET /api/v1/capas | 200 | 4 capas |
| GET /api/v1/capas/1/geojson | 200 | FeatureCollection, 3 features |
| GET /api/v1/capas/2/geojson | 200 | FeatureCollection, 429 features, EPSG:4326 |
| GET /api/v1/capas/3/geojson | 200 | FeatureCollection, 57 features, EPSG:4326 |
| GET /api/v1/capas/4/geojson | 200 | FeatureCollection, 1 feature, EPSG:4686 (declarado) |

## 3. Regresiones

Ninguna. 39/39 tests pasan.

## Conclusión

**Regresión de API: APROBADO.**
