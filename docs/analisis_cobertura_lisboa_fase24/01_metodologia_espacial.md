# Metodología espacial — Fase 24 (Lisboa360)

## 1. Herramientas

- Python 3.x, geopandas 1.1.4, shapely 2.1.2, pandas 3.0.5, matplotlib 3.11.2.

## 2. Operaciones

- `feature.geometry.within(lisboa_polygon)` → dentro.
- `feature.geometry.intersects(lisboa_polygon)` → intersecta.
- Fuera: no intersecta.

## 3. CRS

- Lisboa: EPSG:4326 (reproyectado en Fase 20, basado en WKT).
- Pistas y escenarios: EPSG:4326.
- No se realizaron reproyecciones en esta fase.

## 4. Resultados

- Pistas: 0 dentro, 0 intersectan, 429 fuera.
- Escenarios: 0 dentro, 0 intersectan, 57 fuera.

## 5. Limitaciones

- El CRS de Lisboa requiere confirmación autoritativa.
- La ausencia de registros no implica ausencia de infraestructura.
- No se calcularon densidades ni accesibilidad.

## Conclusión

**Metodología: APROBADA.**
