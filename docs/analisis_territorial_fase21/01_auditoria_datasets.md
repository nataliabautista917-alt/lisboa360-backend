# Auditoría de datasets — Fase 21 (Lisboa360)

## 1. Archivos verificados

| Archivo | Existe | Tamaño |
|---------|--------|--------|
| `barrio_lisboa_limite_oficial_4326.geojson` (procesado, Fase 20) | Sí | 17,130 B |
| `localidad_suba_limite_oficial.geojson` (procesado) | Sí | 87,194 B |
| `parques_pista_recreativa_idrd_2026_procesado.geojson` | Sí | 1,201,724 B |
| `parques_escenario_deportivo_idrd_2026_procesado.geojson` | Sí | 127,812 B |

## 2. Validación

- Lisboa: Polygon válido, 160 vértices, bounds lon [-74.1257, -74.1181], lat [4.7397, 4.7452], centroide (-74.1225, 4.7426). CRS EPSG:4326.
- Suba: Polygon (reconstruido), bounds lon [-74.1320, -74.0345], lat [4.6854, 4.8368]. CRS declarado EPSG:4686 (coordenadas en grados).
- Pistas: 429 MultiPolygon, EPSG:4326, 0 geometrías nulas.
- Escenarios: 57 MultiPolygon, EPSG:4326, 0 geometrías nulas.

## 3. Licencias

- Pistas IDRD: CC-BY-4.0.
- Escenarios IDRD: CC-BY-SA-4.0.
- Lisboa (SDP): CC-BY-4.0.
- Suba (SDP/IDECA): CC-BY-4.0.

## Conclusión

**Auditoría: APROBADO** (con observación de CRS de Suba).
