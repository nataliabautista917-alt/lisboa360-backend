# Auditoría de datasets — Fase 17 (Lisboa360)

## 1. Datasets utilizados

| Dataset | Fuente | Licencia | Features | CRS |
|---------|--------|----------|----------|-----|
| Pistas recreativas IDRD | IDRD / Open Data Bogotá | CC-BY-4.0 | 429 | EPSG:4326 |
| Escenarios deportivos IDRD | IDRD / Open Data Bogotá | CC-BY-SA-4.0 | 57 | EPSG:4326 |
| Localidad de Suba | SDP/IDECA | CC-BY-4.0 | 1 | EPSG:4686 (declarado) |

## 2. Verificación de integridad

- Todos los archivos existen en `data/geojson/`, `data/processed/` y `data/raw/`.
- Estructura GeoJSON válida (FeatureCollection).
- 0 geometrías nulas en los tres datasets.
- Rangos de coordenadas dentro de Bogotá D.C.

## 3. Herramientas

- Python 3.x, geopandas 1.1.4, shapely 2.1.2, pandas 3.0.5, matplotlib 3.11.2.

## 4. Inconsistencias documentadas

- Suba: CRS declarado EPSG:4686 pero coordenadas en grados (compatible numéricamente con EPSG:4326 para Bogotá). No se reproyectó.
- Suba: tipo de geometría declarado MultiPolygon con estructura de Polygon. Reconstruido en memoria como Polygon.

## 5. Conservación

No se modificaron archivos originales, procesados ni del backend. Resultados en `data/analysis/fase17/`.

## Conclusión

**Auditoría: APROBADO CON OBSERVACIONES** (inconsistencias de Suba documentadas).
