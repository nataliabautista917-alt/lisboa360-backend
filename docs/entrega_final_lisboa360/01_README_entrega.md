# Lisboa360 — README de entrega

## Descripción

Lisboa360 es una aplicación web universitaria de exploración territorial del barrio Lisboa, ubicado en la localidad de Suba, Bogotá, Colombia. Integra un mapa Leaflet con capas GIS reales y ficticias, un backend Flask con API REST y un explorador de infraestructura deportiva.

## Objetivos

- Visualizar el territorio del barrio Lisboa y su contexto (localidad de Suba).
- Consultar capas geográficas dinámicas (pistas, escenarios, Suba, Lisboa, ficticia).
- Explorar infraestructura deportiva con filtros y estadísticas.
- Documentar fuentes, licencias y limitaciones.

## Funcionalidades

- Mapa interactivo Leaflet/OpenStreetMap.
- 5 capas GIS: 1 ficticia + 4 reales (IDRD pistas/escenarios, Suba, Lisboa).
- Toggles, leyenda sincronizada, panel informativo.
- Explorador deportivo con filtros por Tipo y Parque.
- Botón "Centrar en Lisboa".
- Badges Real/Ficticio.

## Estructura

- `lisboa360-frontend/` — HTML, CSS, JS (ES modules), Leaflet vendor.
- `lisboa360-backend/` — Flask, SQLite, datos GIS.
- `lisboa360-api/` — OpenAPI y documentación.

## Licencias de datos

- IDRD: CC-BY-4.0 (pistas), CC-BY-SA-4.0 (escenarios).
- SDP/IDECA: CC-BY-4.0 (Suba, Lisboa).

## Estado

Listo para entrega con observaciones (responsive y CRS de Lisboa pendientes de verificación autoritativa).
