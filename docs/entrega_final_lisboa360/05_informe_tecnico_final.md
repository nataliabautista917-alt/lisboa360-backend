# Informe técnico final — Lisboa360

## Arquitectura

- Frontend: HTML/CSS/JS (ES modules), Leaflet 1.9.4, OpenStreetMap.
- Backend: Flask, SQLite, API REST (OpenAPI).
- Datos: GeoJSON dinámicos servidos por `/api/v1/capas` y `/api/v1/capas/{id}/geojson`.

## Frontend

- `js/map.js`: inicialización Leaflet.
- `js/layers.js`: conversión GeoJSON → Leaflet, toggles, leyenda.
- `js/ui.js`: interfaz, panel informativo, badges.
- `js/main.js`: orquestador (boot), carga dinámica de capas, explorador deportivo.
- `js/api.js`: cliente REST centralizado.
- `js/config.js`: URL backend, tiles, coordenadas iniciales.

## Backend

- `app/db/seed.py`: 5 capas (1 ficticia + 4 reales).
- `app/services/capas_service.py`: listado y GeoJSON por id.
- `app/routes/capas_routes.py`: endpoints `/api/v1/capas` y `/api/v1/capas/{id}/geojson`.

## GIS

- 5 capas: ficticia (3 features), pistas (429), escenarios (57), Suba (1), Lisboa (1).
- CRS: EPSG:4326 (pistas, escenarios, Lisboa); EPSG:4686 declarado (Suba, IDPC).
- Análisis espacial: Shapely/GeoPandas (Fases 16–24).

## Pruebas

- pytest: 39/39 pasan.
- Sintaxis JS: OK.
- Headless Edge: 5 capas cargadas, sin errores.

## Conclusión

Lisboa360 es una aplicación funcional con integración GIS real y ficticia, validada y documentada.
