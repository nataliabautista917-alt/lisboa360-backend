# Metodología de análisis — Fase 17 (Lisboa360)

## 1. Operaciones espaciales

- Predicado: `feature.geometry.intersects(suba_polygon)`.
- CRS de trabajo: EPSG:4326 (numérico), sin reproyección.
- Suba reconstruida en memoria como Polygon (no se modificó el archivo).

## 2. Análisis estadístico

- Conteos por dataset y por parque.
- Distribución por atributos existentes (`Tipo`, `Estado_Diagnóstico`, `Material_Piso`, `Cubierto_`).
- Valores nulos por campo.
- Relación espacial entre pistas y escenarios (intersección de geometrías).
- Porcentajes de representación dentro de Suba.

## 3. Limitaciones

- No se calcularon densidades por población (sin datos demográficos compatibles).
- No se realizó análisis de accesibilidad (sin red vial verificable).
- La ausencia de registros no implica ausencia de infraestructura.
- Los resultados describen Suba, no Lisboa.

## Conclusión

**Metodología: APROBADA.**
