# Validaciones — Fase 22 (Lisboa360)

## 1. Backend

- pytest: 39/39 pasan.
- `GET /api/v1/capas`: 5 capas (ids 1–5).
- `GET /api/v1/capas/5/geojson`: FeatureCollection, 1 feature Polygon, CRS EPSG:4326.

## 2. Frontend

- Sintaxis JS: OK (main.js, layers.js, ui.js).
- Headless Edge dump-dom: 5 toggles renderizados, sin banner de error, estado vacío en todos.
- Activación/desactivación: no verificada manualmente (sin navegador interactivo).

## 3. Geometría

- Lisboa: Polygon válido, 160 vértices, centroide (-74.1225, 4.7426).

## Conclusión

**Validaciones: APROBADO.**
