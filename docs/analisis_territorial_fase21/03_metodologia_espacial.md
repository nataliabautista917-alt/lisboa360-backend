# Metodología espacial — Fase 21 (Lisboa360)

## 1. Herramientas

- Python 3.x, geopandas 1.1.4, shapely 2.1.2, pandas 3.0.5, matplotlib 3.11.2.

## 2. Operaciones

- Predicado de inclusión: `geometry.intersects(lisboa_polygon)` (intersección geométrica).
- Predicado de contención: `geometry.within(lisboa_polygon)` (completamente dentro).
- Parcial: intersecta pero no está completamente dentro.
- Fuera: no intersecta.

## 3. CRS

- Lisboa, pistas y escenarios: EPSG:4326.
- Suba: reconstruida como Polygon en memoria (no se modificó el archivo).

## 4. Limitaciones

- El análisis es exploratorio.
- No se calcularon densidades ni accesibilidad.
- La reproyección de Lisboa se basó en el WKT del origen.
- No se afirmó que el CRS esté oficialmente confirmado.

## Conclusión

**Metodología: APROBADA.**
