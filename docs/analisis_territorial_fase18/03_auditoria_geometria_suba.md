# Auditoría de geometría de Suba — Fase 18 (Lisboa360)

## 1. Inspección del archivo

Archivo: `data/processed/territorial/localidad_suba_limite_oficial.geojson` (y copia en `data/geojson/`).

## 2. Tipo declarado vs estructura real

- Tipo declarado en el GeoJSON: `MultiPolygon`.
- Estructura real de coordenadas: `Polygon` (un único anillo de 913 vértices).
- `shapely.geometry.shape()` con el tipo declarado falla: `TypeError: 'float' object is not iterable`.
- Reconstruida en memoria como `Polygon`: válida (`is_valid = True`), sin agujeros, 1 anillo exterior.

## 3. Métricas

| Métrica | Valor |
|---------|-------|
| Vértices | 913 |
| Anillos | 1 (exterior) |
| Componentes | 1 |
| Área (deg²) | 0.008190624669006033 |
| Bounds lon | [-74.131986, -74.034497] |
| Bounds lat | [4.685360, 4.836779] |

## 4. Compatibilidad

- GeoJSON: estructura de Polygon es válida; el tipo declarado (MultiPolygon) es incorrecto.
- Leaflet: requiere normalización (implementada en `js/layers.js` en Fase 15) para renderizar correctamente.
- Backend: valida solo `type == "FeatureCollection"`, no el tipo de geometría interna.

## 5. Propuesta de corrección (no aplicada)

Crear un archivo corregido `localidad_suba_limite_oficial_polygon.geojson` con `type: "Polygon"` en un paso autorizado de mantenimiento de datos. Conservar el original.

## 6. Archivos creados en esta fase

- Ningún archivo de datos modificado. Solo documentación en `docs/analisis_territorial_fase18/`.

## Conclusión

**Auditoría de geometría: APROBADO CON OBSERVACIONES** (inconsistencia de tipo documentada).
