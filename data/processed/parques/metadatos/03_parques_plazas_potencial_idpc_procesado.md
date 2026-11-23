# Registro de Metadatos — Dataset Procesado: Potencial Plazas y Parques

## Información del Archivo Procesado

- **Archivo raw de origen:** `parques_plazas_potencial_idpc_2026.geojson`
- **Ubicación del raw:** `lisboa360-backend/data/raw/parques/parques_plazas_potencial_idpc_2026.geojson`
- **Archivo procesado:** `parques_plazas_potencial_idpc_2026_procesado.geojson`
- **Ubicación del procesado:** `lisboa360-backend/data/processed/parques/parques_plazas_potencial_idpc_2026_procesado.geojson`
- **Fecha de procesamiento:** 22/11/2026 (Fase 7) y verificación Fase 7.1
- **Procesado por:** Fase 7 — Procesamiento y validación de datos GIS / Fase 7.1 — Verificación de CRS

## Información Geoespacial

- **Formato:** GeoJSON (RFC 7946)
- **CRS declarado en el archivo:** EPSG:4686 (`urn:ogc:def:crs:EPSG::4686`) — MAGNA-SIRGAS / Colombia Bogotá zone (CRS PROYECTADO, unidades en metros)
- **CRS verificado empíricamente:** Las coordenadas contenidas están en GRADOS GEOGRÁFICOS (longitud/latitud), no en metros proyectados
- **CRS de salida:** EPSG:4686 (sin cambios — no se realizó reproyección)
- **CRS objetivo para Leaflet:** EPSG:4326 (WGS 84)
- **Reproyección realizada:** NO — no se pudo verificar el CRS de origen con certeza
- **Tipo de geometría:** MultiPolygon
- **Número de features (raw):** 11
- **Número de features (procesado):** 11
- **Tamaño archivo (bytes):** 25,244

## Verificación de CRS (Fase 7.1)

### Evidencia recopilada

1. **CRS declarado:** El archivo declara `urn:ogc:def:crs:EPSG::4686`, que según el registro EPSG es un CRS PROYECTADO (MAGNA-SIRGAS / Colombia Bogotá zone, unidades en metros)

2. **Coordenadas reales contenidas:** Todas las 482 coordenadas verificadas están en grados geográficos:
   - Rango X (longitud): -74.08647124 a -74.06750055
   - Rango Y (latitud): 4.58859919 a 4.61275568
   - Estas son coordenadas típicas de longitud/latitud para Bogotá D.C.

3. **Intento de reproyección (EPSG:4686 → EPSG:4326) usando proj4:**
   - Coordenada de prueba: [-74.08579912, 4.60522212]
   - Resultado de la transformación: [-83.052618, -4.392386]
   - **Resultado incorrecto:** No corresponde a Bogotá D.C.
   - **Conclusión:** Las coordenadas NO están en EPSG:4686 proyectado (metros). Ya están en grados geográficos.

### Conclusión sobre el CRS

Hay una **inconsistencia entre el CRS declarado y los datos contenidos**:
- El archivo declara EPSG:4686 (proyectado, metros)
- Pero los valores de coordenada son claramente grados geográficos (longitud/latitud)
- El intento de reproyección desde EPSG:4686 (proyectado) produce resultados incorrectos

**No se puede realizar reproyección confiable** porque:
- No se puede verificar con certeza cuál es el CRS de origen real
- No se dispone de herramientas GIS especializadas (GDAL, QGIS) para resolver la incertidumbre
- Las instrucciones del proyecto establecen: "Si el CRS no puede verificarse, no reproyectes" y "No asignes un CRS por intuición"

## Validación Geométrica

- **Geometrías nulas:** 0
- **Geometrías vacías:** 0
- **Geometrías inválidas detectadas:** 0 (verificación estructural básica)
- **Features sin geometría:** 0
- **Features duplicados (por OBJECTID):** 0
- **Coordenadas fuera de rango Bogotá:** 0 de 482 coordenadas verificadas — todas dentro del rango geográfico de Bogotá D.C.
- **Validación topológica avanzada:** No realizada (no se dispuso de herramientas GEOS/Shapely/QGIS)

## Análisis de Atributos

**Campos preservados (8 campos):**
1. `Shape_Area` — Área del polígono
2. `OBJECTID` — Identificador de objeto
3. `Periodo` — Periodo histórico (ej. "Siglo XIX", "Siglo XVI", "Siglo XVII")
4. `Lugar` — Nombre del lugar (ej. "Plaza España", "Plaza de los Mártires", "Plaza de Bolívar")
5. `Dirección` — Dirección del lugar (ej. "Carrera 18 - Calle 11", "Calle 10 - Carrera 7")
6. `Shape_Leng` — Longitud de la geometría
7. `Observa` — Observación arqueológica
8. `Tipo_EP` — Tipo de espacio público (ej. "Plaza", "Parque")

**Campos con valores nulos:** Ninguno detectado

**Campos incompletos:** Ninguno detectado

**Valores repetidos:** `Lugar` tiene valores repetidos (ej. "Plaza España" aparece dos veces con diferentes geometrías), lo cual puede indicar múltiples polígonos para el mismo lugar — requiere revisión manual

## Cambios Realizados

- **Sin cambios:** El archivo se copió tal cual desde el raw. No se aplicó reproyección.
- **Motivo:** El CRS declarado (EPSG:4686 proyectado) es inconsistente con los datos (que están en grados geográficos). No se pudo verificar el CRS de origen con certeza, por lo que no se realizó reproyección, cumpliendo con las instrucciones del proyecto.

## Problemas de Calidad

1. **Inconsistencia de CRS:** El CRS declarado (EPSG:4686 proyectado) no coincide con los datos (grados geográficos). Requiere investigación adicional con la fuente original (IDPC).
2. **Codificación de caracteres:** Algunos campos muestran caracteres de reemplazo (ej. "Observa", "Dirección").
3. `Lugar` tiene valores repetidos que pueden o no ser duplicados reales — requiere revisión manual.

## Estado de Validación

- **Estado:** Válido estructuralmente como GeoJSON
- **CRS:** Sin cambios (mantiene EPSG:4686 declarado, aunque los datos están en grados geográficos)
- **Listo para integración:** No completamente — requiere resolución de la incertidumbre de CRS antes de la integración
- **Trazabilidad:** Mantiene trazabilidad completa hacia el archivo raw en `lisboa360-backend/data/raw/parques/`

## Observaciones

- El dataset contiene plazas y parques con potencial de hallazgos arqueológicos en el centro histórico de Bogotá
- Incluye lugares como "Plaza España", "Plaza de los Mártires", "Plaza de Bolívar", "Plaza Santander", "Parque de la Independencia", "Parque Centenario" entre otros
- Las coordenadas están concentradas en el centro histórico de Bogotá (aprox. -74.09 a -74.06, 4.58 a 4.61), no en la localidad de Suba
- Utilidad para Lisboa360: capa de lugares de interés territorial a nivel distrital, pero con cobertura principalmente en el centro de Bogotá
- No se realizó recorte territorial dado que no existe un límite oficial verificable del barrio Lisboa
- **No se generó archivo llamado "reproyectado"** ya que no se realizó reproyección (cumpliendo instrucción: "No afirmes que una reproyección se realizó si no se ejecutó")

## Recomendaciones

1. Consultar con IDPC o IGAC para obtener el CRS correcto de este dataset
2. Cuando se disponga de herramientas GIS (GDAL/ogr2ogr, QGIS), verificar si las coordenadas están en MAGNA-SIRGAS geográfico (que es esencialmente equivalente a WGS84/EPSG:4326 para Bogotá)
3. Si se confirma que los datos ya están en grados geográficos, actualizar la declaración CRS a EPSG:4326 con documentación de la evidencia