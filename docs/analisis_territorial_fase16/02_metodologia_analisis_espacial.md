# Metodología de análisis espacial — Fase 16 (Lisboa360)

## 1. Herramientas

- Python 3.x con geopandas 1.1.4, shapely 2.1.2, pandas 3.0.5, matplotlib 3.11.2.
- CRS de trabajo: EPSG:4326 (numérico) para los tres datasets, sin reproyección.

## 2. Carga de datos

- Pistas y escenarios cargados con `geopandas.read_file()` sobre los GeoJSON servidos.
- Suba reconstruido en memoria como `Polygon` a partir de sus coordenadas (el archivo declara MultiPolygon pero tiene estructura de Polygon). **No se modificó el archivo fuente.**

## 3. Operación espacial

- Relación espacial: `feature.geometry.intersects(suba_polygon)`.
- Se considera "dentro de Suba" cualquier feature cuya geometría intersecte el polígono de Suba (incluye solapamientos parciales y contenidos).
- No se realizaron recortes, transformaciones ni reproyecciones.

## 4. Criterios de inclusión/exclusión

- Incluidos: todos los features con geometría no nula.
- Excluidos: ninguno (todos los features tienen geometría válida).
- El dataset IDPC no se incluyó (excluido por inconsistencia de CRS).

## 5. Validaciones

- Verificación de existencia de archivos.
- Verificación de estructura GeoJSON (FeatureCollection).
- Verificación de geometrías no nulas.
- Verificación de rangos de coordenadas (Bogotá D.C.).
- Verificación de CRS declarado vs coordenadas.

## 6. Limitaciones

- La geometría de Suba se reconstruyó en memoria como Polygon por inconsistencia del archivo; no se alteró el fuente.
- El CRS declarado de Suba (EPSG:4686) no se resolvió autoritativamente; se usó la interpretación numérica en grados.
- El análisis es exploratorio y no describe el barrio Lisboa (no existe límite oficial verificable).

## Conclusión

**Metodología: APROBADA CON OBSERVACIONES** (limitaciones documentadas).
