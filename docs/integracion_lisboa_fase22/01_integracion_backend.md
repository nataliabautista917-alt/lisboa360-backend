# Integración backend — Fase 22 (Lisboa360)

## 1. Capa registrada

- ID: 5.
- Nombre: "Límite oficial del barrio Lisboa".
- Tipo: territorial.
- Geometría: Polygon.
- Fuente: SDP — dataset "Barrio legalizado. Bogotá D.C.".
- Licencia: CC-BY-4.0.
- CRS: EPSG:4326.
- Ruta: `barrio_lisboa_limite_oficial_4326.geojson` (en `data/geojson/`).
- Estado: activa.

## 2. Archivos

- Copiado (sin modificar el original): `data/processed/territorial/barrio_lisboa_limite_oficial_4326.geojson` → `data/geojson/barrio_lisboa_limite_oficial_4326.geojson`.
- Modificado: `app/db/seed.py` — nueva lista `CAPAS_GEOGRAFICAS_LISBOA` y loop de seeding (INSERT OR IGNORE, idempotente).

## 3. Endpoints

- `GET /api/v1/capas` ahora devuelve 5 capas (ids 1–5).
- `GET /api/v1/capas/5/geojson` devuelve FeatureCollection con 1 feature Polygon, CRS EPSG:4326.

## 4. Tests

- pytest: 39/39 pasan.
- Endpoint real verificado (HTTP 200, FeatureCollection, 1 feature).

## Conclusión

**Integración backend: COMPLETADA.**
