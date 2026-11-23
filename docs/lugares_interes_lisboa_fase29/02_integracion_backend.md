# Integración backend — Fase 29 (Lisboa360)

## Capa registrada

- ID: 7.
- Nombre: "Lugares de interés (OSM)".
- Tipo: lugares_interes.
- Geometría: Point.
- Fuente: OpenStreetMap (ODbL 1.0).
- Ruta: `lugares_interes_lisboa_osm.geojson`.

## Endpoints

- `GET /api/v1/capas` → 7 capas.
- `GET /api/v1/capas/7/geojson` → FeatureCollection, 48 features, Point, EPSG:4326.

## Tests

- pytest: 39/39 pasan.

## Conclusión

**Integración backend: COMPLETADA.**
