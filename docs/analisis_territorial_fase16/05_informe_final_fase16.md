# Informe final — Fase 16 (Lisboa360)

## 1. Datasets analizados

- Pistas Recreativas y Deportivas en Parque (IDRD) — 429 features, EPSG:4326, CC-BY-4.0.
- Escenarios Deportivos en Parque (IDRD) — 57 features, EPSG:4326, CC-BY-SA-4.0.
- Localidad de Suba (SDP/IDECA) — 1 feature, CRS declarado EPSG:4686, CC-BY-4.0.
- IDPC plazas/parques — excluido por inconsistencia de CRS.

## 2. Validación espacial

- CRS de pistas y escenarios: EPSG:4326 (verificado).
- CRS de Suba: declarado EPSG:4686, coordenadas en grados (compatible numéricamente con EPSG:4326 para Bogotá). No se reproyectó.
- Geometría de Suba: inconsistencia de tipo (declarado MultiPolygon, estructura Polygon). Reconstruida en memoria como Polygon. No se modificó el archivo.

## 3. Metodología

- Herramientas: geopandas, shapely, pandas, matplotlib.
- Operación: `feature.geometry.intersects(suba_polygon)`.
- Sin transformaciones, recortes ni reproyecciones.
- Sin alteración de archivos fuente.

## 4. Resultados estadísticos

| Métrica | Pistas | Escenarios |
|---------|--------|------------|
| Total | 429 | 57 |
| En Suba | 38 | 4 |
| Fuera de Suba | 391 | 53 |

## 5. Resultados espaciales

- 38 pistas recreativas dentro de Suba (8.9% del total).
- 4 escenarios deportivos dentro de Suba (7.0% del total).
- Los resultados describen la localidad de Suba, **no** el barrio Lisboa.

## 6. Visualizaciones generadas

4 visualizaciones (mapas + gráfico de barras) en `data/analysis/fase16/` y copiadas a `docs/analisis_territorial_fase16/evidencias/`.

## 7. Limitaciones

- CRS de Suba sin verificación autoritativa.
- Inconsistencia de tipo de geometría en Suba (requiere mantenimiento de datos).
- Sin límite oficial del barrio Lisboa.
- No se realizaron análisis de densidad, distancia ni accesibilidad.
- El dataset IDPC está excluido.

## 8. Archivos creados

- `data/analysis/fase16/` — CSVs, JSON, PNGs.
- `docs/analisis_territorial_fase16/` — 5 documentos + evidencias.

## 9. Confirmación de conservación de datos originales

No se modificó ningún archivo original, procesado, backend, SQLite, OpenAPI ni frontend. No se realizaron commits ni pushes.

## 10. Recomendaciones para la siguiente fase

1. Verificar el CRS de Suba con fuente autoritativa.
2. Corregir el tipo de geometría del GeoJSON de Suba en un paso autorizado.
3. Obtener el límite oficial del barrio Lisboa.
4. Realizar análisis de cobertura/accesibilidad solo después de resolver los puntos anteriores.

Me detengo aquí y espero revisión y autorización.
