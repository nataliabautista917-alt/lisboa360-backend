# Riesgos y limitaciones — Fase 18 (Lisboa360)

## 1. Riesgos técnicos

1. **CRS de Suba sin verificación autoritativa:** el CRS declarado (EPSG:4686) no coincide con la interpretación de las coordenadas. Cualquier análisis espacial definitivo requiere resolución.
2. **Inconsistencia de tipo de geometría en Suba:** declarado MultiPolygon, estructura Polygon. Requiere corrección de datos.
3. **Ausencia de límite oficial de Lisboa:** no existe un polígono GIS verificable. No se puede realizar análisis específico de Lisboa.
4. **Dataset IDPC excluido:** CRS incierto, sin verificación autoritativa.
5. **Códigos numéricos sin diccionario:** los campos `Tipo`, `Estado_Diagnóstico`, `Material_Piso` son códigos sin significado verificado.

## 2. Limitaciones de la fase

- No se descargaron nuevos datasets (restricción).
- No se reproyectaron datos.
- No se modificaron archivos fuente.
- La investigación de Lisboa se basó en fuentes públicas (Wikipedia, código postal, planes institucionales), no en polígonos GIS oficiales.

## 3. Riesgos de interpretación

- Los resultados de las fases 16–17 describen Suba, no Lisboa.
- La ausencia de registros en un sector no implica ausencia de infraestructura.

## Conclusión

**Riesgos y limitaciones: DOCUMENTADOS.**
