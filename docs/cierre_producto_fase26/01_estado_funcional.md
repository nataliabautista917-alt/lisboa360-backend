# Estado funcional — Fase 26 (Lisboa360)

## 1. Backend

- Flask operativo. 5 capas registradas (ids 1–5).
- Endpoints: `/api/v1/capas` y `/api/v1/capas/{id}/geojson` funcionales (HTTP 200; 404 para inexistente).
- pytest: 39/39 pasan.

## 2. Frontend

- Mapa Leaflet centrado en Lisboa (4.7426, -74.1225), zoom 15.
- 5 capas GIS cargadas dinámicamente (ficticia, pistas, escenarios, Suba, Lisboa).
- Toggles, leyenda sincronizada, panel informativo, badges Real/Ficticio.
- Explorador deportivo con filtros, estadísticas reales y gráfico CSS.
- Botón "Centrar en Lisboa".

## 3. Capas

| id | Capa | Features | Licencia |
|----|------|----------|----------|
| 1 | Ficticia: Capa general | 3 | n/a |
| 2 | Pistas IDRD | 429 | CC-BY-4.0 |
| 3 | Escenarios IDRD | 57 | CC-BY-SA-4.0 |
| 4 | Suba (contexto administrativo) | 1 | CC-BY-4.0 |
| 5 | Límite oficial del barrio Lisboa | 1 | CC-BY-4.0 |

## 4. Restricciones cumplidas

No se modificaron GeoJSON originales, SQLite, OpenAPI, backend, datos ficticios ni remotos Git. No se realizaron commits ni pushes.

## Conclusión

**Estado funcional: OPERATIVO.**
