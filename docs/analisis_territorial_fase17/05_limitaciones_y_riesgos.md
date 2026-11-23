# Limitaciones y riesgos — Fase 17 (Lisboa360)

## 1. Limitaciones técnicas

- CRS de Suba sin verificación autoritativa (EPSG:4686 declarado vs grados geográficos).
- Inconsistencia de tipo de geometría en Suba (MultiPolygon vs Polygon).
- Sin datos demográficos compatibles: no se calcularon densidades per cápita.
- Sin red vial verificable: no se realizó análisis de accesibilidad.
- Sin límite oficial del barrio Lisboa: no se realizaron análisis específicos de Lisboa.

## 2. Riesgos de interpretación

- La ausencia de registros en un sector no implica ausencia de infraestructura.
- Los porcentajes de cobertura dentro de Suba son exploratorios.
- Los códigos de `Tipo`, `Estado_Diagnóstico` y `Material_Piso` son códigos numéricos del dataset sin diccionario verificado.

## 3. Riesgos de datos

- El dataset IDPC está excluido por inconsistencia de CRS.
- Los datasets IDRD tienen cobertura distrital, no específica de Suba.

## Conclusión

**Limitaciones documentadas.** Los resultados deben interpretarse como exploratorios.
