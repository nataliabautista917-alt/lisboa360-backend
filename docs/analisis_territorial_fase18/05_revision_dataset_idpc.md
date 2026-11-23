# Revisión del dataset IDPC — Fase 18 (Lisboa360)

## 1. Inspección del archivo

Archivo: `data/raw/parques/parques_plazas_potencial_idpc_2026.geojson`.

| Atributo | Valor |
|----------|-------|
| Tipo | FeatureCollection |
| CRS declarado | `urn:ogc:def:crs:EPSG::4686` |
| Features | 11 |
| Geometrías | MultiPolygon (11), profundidad 4 |
| Geometrías nulas | 0 |
| Rango lon | -74.0858 … -74.0848 |
| Rango lat | 4.6047 … 4.6054 |
| Atributos | `OBJECTID`, `Lugar`, `Direccion`, `Periodo`, `Observa`, `Shape_Leng`, `Shape_Area`, `Tipo_EP` |

## 2. Análisis de CRS

- CRS declarado: EPSG:4686 (MAGNA-SIRGAS).
- Coordenadas: grados (lon/lat), rango de Bogotá.
- Reproyección de prueba EPSG:4686→4326 (Fase 7.1) produjo resultados incorrectos (coordenadas fuera de Bogotá).
- **Conclusión:** el CRS declarado es inconsistente con las coordenadas. El CRS real no está confirmado.

## 3. Posibilidad de identificación

- No se dispone de evidencia autoritativa (metadatos oficiales del IDPC, IGAC) que confirme el CRS real.
- La reproyección de prueba no es confiable.

## 4. Decisión

**El dataset IDPC permanece excluido** de la integración activa. No se reproyectó ni se integró.

## 5. Recomendación

1. Consultar al IDPC/IGAC el CRS real del dataset.
2. Si se confirma, reproyectar con herramientas GIS verificables (GDAL/QGIS).
3. Validar las coordenadas resultantes.
4. Integrar como capa adicional en una fase autorizada.

## Conclusión

**Revisión IDPC: EXCLUIDO** (CRS incierto, sin verificación autoritativa).
