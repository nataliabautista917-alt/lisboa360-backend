# Informe final — Fase 21 (Lisboa360)

## 1. Auditoría realizada

Se verificó la existencia e integridad de todos los archivos utilizados (Lisboa, Suba, pistas IDRD, escenarios IDRD). Se validó la geometría de Lisboa y su coherencia espacial con Suba.

## 2. Herramientas y versiones

- Python 3.x, geopandas 1.1.4, shapely 2.1.2, pandas 3.0.5, matplotlib 3.11.2.

## 3. Metodología

- Operación: `feature.geometry.intersects(lisboa_polygon)` y `feature.geometry.within(lisboa_polygon)`.
- CRS: EPSG:4326 para Lisboa, pistas y escenarios.
- Suba reconstruida como Polygon en memoria.

## 4. Resultados de pistas

- Total: 429.
- Intersectan con Lisboa: 0.
- Dentro: 0.
- Fuera: 429.

## 5. Resultados de escenarios

- Total: 57.
- Intersectan con Lisboa: 0.
- Dentro: 0.
- Fuera: 57.

## 6. Comparación Lisboa vs. Suba

| Métrica | Lisboa | Suba |
|---------|--------|------|
| Pistas | 0 | 38 |
| Escenarios | 0 | 4 |

## 7. Parques identificados

- 0 parques con infraestructura IDRD dentro de Lisboa.
- Parques más cercanos: Parque Juan Amarillo (~0.01°), La Gaitana (~0.012°), Tibabuyes (~0.013°).

## 8. Visualizaciones

5 visualizaciones en `data/analysis/fase21/` y copiadas a `docs/analisis_territorial_fase21/evidencias/`.

## 9. Validaciones

- Integridad de archivos: OK.
- CRS de cada dataset: verificado.
- Validez geométrica: OK.
- Conteos de features: OK.
- Consistencia de CSV, JSON y gráficos: OK.
- Reproducibilidad de scripts: OK.
- Correspondencia entre estadísticas y visualizaciones: OK.
- Conservación de archivos anteriores: OK.

## 10. Limitaciones y riesgos

- CRS de Lisboa requiere confirmación autoritativa.
- Tipo de geometría de Suba inconsistente.
- IDPC excluido.
- Ausencia de registros no implica ausencia de infraestructura.

## 11. Archivos creados

- `data/analysis/fase21/` — CSVs, JSON, PNGs.
- `docs/analisis_territorial_fase21/` — 10 documentos + evidencias.

## 12. Confirmación de conservación

No se modificó ningún archivo original, procesado, backend, SQLite, OpenAPI, frontend ni remotos Git. No se realizaron commits ni pushes.

## 13. Recomendaciones para la Fase 22

1. Verificar el CRS de Lisboa con fuente autoritativa.
2. Corregir el tipo de geometría del GeoJSON de Suba.
3. Integrar el límite de Lisboa como capa en la aplicación (fase autorizada).
4. Realizar análisis de cobertura con datos verificados.

Me detengo aquí y espero revisión y autorización. No inicio la Fase 22 automáticamente.
