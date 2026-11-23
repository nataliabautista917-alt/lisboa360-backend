# Metadatos — Barrio legalizado. Bogotá D.C. (SDP)

## 1. Dataset

- Nombre: Barrio legalizado. Bogotá D.C.
- Entidad responsable: Secretaría Distrital de Planeación (SDP).
- Fuente: Datos Abiertos Bogotá (datosabiertos.bogota.gov.co).
- URL de descarga (GeoJSON): https://datosabiertos.bogota.gov.co/dataset/36a80ef3-02c1-4a48-b3c7-c285e1de4323/resource/ba69f395-13ed-4071-802d-3808e2ba9062/download/barriolegalizado.json
- Fecha de publicación del dato: 2026-06-30.
- Fecha de descarga: 2026-11-22.
- Formato original: GeoJSON (ArcGIS REST export, extensión .json).
- Tamaño: 8,179,729 bytes.
- Archivo guardado como: `data/raw/territorial/barrio_legalizado_bogota_sdp_20260630.json`.
- Licencia: Creative Commons Attribution 4.0 (CC-BY-4.0).
- CRS declarado: EPSG 4686 MAGNA-SIRGAS geographic 2D (EPSG:4686).
- Sistema de referencia real del archivo: PCS_CarMAGBOG (proyección Transverse Mercator, coordenadas en metros, central meridian -74.1466, origin 4.6805). Corresponde a MAGNA-SIRGAS Bogotá (EPSG 102771 / 6247).
- Geometría: esriGeometryPolygon (polígonos).
- Número de registros: 1,775 barrios legalizados.

## 2. Identificación de Lisboa

- Campo `NOMBRE`: "LISBOA".
- `CODIGO_ID`: LEG01324.
- `CODIGO_LOCALIDAD`: "11" (Suba).
- `CODIGO_UPZ`: 71 (Tibabuyes).
- `CODIGO_UPL`: UPL10.
- `ESTADO`: 1.
- `AREA_TOTAL`: 24.04 ha.
- `LOTES_TOTAL`: 2490.
- `POBLACION_ESTIMADA`: 13446.
- `DENSIDAD`: 103.58.
- `ACTO_ADMINISTRATIVO`: RES.
- `NUMERO_ACTO_ADMINISTRATIVO`: 370.
- `FECHA_ACTO_ADMINISTRATIVO`: 903571200000 (ms) ≈ 1998-08-20.
- `NUMERO_PLANO`: S628/4-03.
- `LLAVE_PLANO`: 111786B001.
- `REGLAMENTACION`: 3.
- `Shape_Area`: 240314.16 m².
- `Shape_Length`: 2601.58 m.

## 3. Validación de geometría de Lisboa

- Tipo de geometría: Polygon (1 anillo, 160 vértices + cierre).
- `is_valid`: True.
- `is_simple`: True.
- Anillo cerrado: sí.
- Área calculada: 240,314.16 m² (coincide con `Shape_Area`).
- Perímetro calculado: 2,601.58 m (coincide con `Shape_Length`).
- Bounds nativos (metros): X [94655.43, 95498.23], Y [115873.78, 116480.44].
- Coordenadas en metros (proyección PCS_CarMAGBOG), no en grados.

## 4. Validaciones realizadas

- Integridad del archivo JSON: OK (parseo exitoso).
- Identificación de Lisboa: OK (1 registro, pertenece a localidad 11 = Suba, UPZ 71 = Tibabuyes).
- Geometría válida: OK (Polygon simple y cerrado).
- Coincidencia de área/perímetro con atributos: OK.

## 5. Limitaciones

- El archivo está en formato ArcGIS REST (no GeoJSON estándar). Requiere conversión para uso en Leaflet/backend.
- El CRS es proyectado (metros), no grados. Requiere reproyección a EPSG:4326 para visualización web, lo cual no se realizó en esta fase.
- La geometría no fue alterada ni reproyectada.
- No se integró al backend ni al frontend.

## 6. Observaciones

- El registro de Lisboa corresponde a un barrio legalizado por la SDP, con acto administrativo de 1998.
- El área (~24 ha) es consistente con la descripción textual del barrio (Calle 131–139, Carrera 136–151).
- Este es el primer polígono GIS oficial verificable del barrio Lisboa encontrado.

## Conclusión

**Límite oficial de Lisboa: ENCONTRADO** (dataset "Barrio legalizado. Bogotá D.C.", SDP, CC-BY-4.0).
El archivo original se conserva intacto en `data/raw/territorial/`.
