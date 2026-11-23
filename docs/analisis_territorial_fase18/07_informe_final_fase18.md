# Informe final — Fase 18 (Lisboa360)

## 1. Pendientes resueltos

- Auditoría geográfica completa de los datasets (CRS, geometría, atributos).
- Verificación del CRS de pistas, escenarios y Suba.
- Auditoría de la geometría de Suba (inconsistencia de tipo documentada).
- Investigación del límite del barrio Lisboa (no encontrado en GIS verificable).
- Revisión del dataset IDPC (excluido por CRS incierto).

## 2. Pendientes abiertos

- CRS de Suba sin verificación autoritativa.
- Tipo de geometría de Suba incorrecto (requiere mantenimiento de datos).
- Límite oficial del barrio Lisboa no encontrado.
- Dataset IDPC excluido (CRS incierto).

## 3. Fuentes consultadas y evidencia

- Datos Abiertos Bogotá, IDECA, SDP, Alcaldía Local de Suba, Wikipedia, código postal, Mapcarta, OSM.
- Archivos físicos inspeccionados con Python (shapely, geopandas).
- Metadatos de los GeoJSON.

## 4. Herramientas y versiones

- Python 3.x, shapely 2.1.2, geopandas 1.1.4, pandas 3.0.5.

## 5. Archivos creados

- `data/analysis/fase18/` — subdirectorios audit/, geometry/, territory/, reports/, evidence/.
- `docs/analisis_territorial_fase18/` — 7 documentos.

## 6. Resultados de validación

- Integridad de archivos: OK.
- Inspección de coordenadas: OK.
- CRS: APROBADO CON OBSERVACIONES.
- Estructura GeoJSON: OK.
- Geometría: APROBADO CON OBSERVACIONES.
- Evidencias de fuentes: documentadas.
- Consistencia documental: OK.

## 7. Riesgos

- CRS de Suba sin verificación autoritativa.
- Inconsistencia de tipo de geometría en Suba.
- Ausencia de límite oficial de Lisboa.
- IDPC excluido.

## 8. Recomendaciones para la Fase 19

1. Obtener el dataset "Barrio legalizado. Bogotá D.C." de Datos Abiertos Bogotá y verificar si incluye Lisboa.
2. Consultar al IDPC/IGAC el CRS real del dataset de plazas.
3. Corregir el tipo de geometría del GeoJSON de Suba en un paso autorizado.
4. Obtener el límite oficial de Lisboa de la Alcaldía Local de Suba o el Consejo Comunal Lisboa.

Me detengo aquí y espero revisión y autorización. No inicio la Fase 19 automáticamente.
