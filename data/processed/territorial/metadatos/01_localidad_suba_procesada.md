# Registro de Metadatos — Localidad de Suba Procesada

## Información del Archivo Procesado

- **Archivo raw de origen:** `localidades_bogota_sdp_ideca_original.geojson`
- **Ubicación del raw:** `lisboa360-backend/data/raw/territorial/localidades_bogota_sdp_ideca_original.geojson`
- **Archivo procesado:** `localidad_suba_limite_oficial.geojson`
- **Ubicación del procesado:** `lisboa360-backend/data/processed/territorial/localidad_suba_limite_oficial.geojson`
- **Fecha de procesamiento:** 22/11/2026
- **Procesado por:** Fase 10 — Reproyección y preparación del límite oficial de Suba

## Información de la Fuente Original

- **Nombre del dataset:** Localidad. Bogotá D.C
- **Entidad responsable:** Secretaría Distrital de Planeación - SDP / La IDE de Bogotá D.C. (IDECA)
- **URL de la ficha:** https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8
- **URL de descarga:** https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8/resource/497b8756-0927-4aee-8da9-ca4e32ca3a8a/download/loca.json
- **Licencia:** CC-BY-4.0 (Creative Commons Attribution 4.0)

## Información Geoespacial del Archivo Procesado

- **Formato:** GeoJSON (RFC 7946)
- **CRS original:** EPSG:4686 MAGNA-SIRGAS geographic 2D - 4686
- **CRS final:** EPSG:4686 MAGNA-SIRGAS geographic 2D - 4686
- **CRS objetivo para Leaflet:** EPSG:4326 WGS 84
- **Reproyección realizada:** NO
- **Tipo de geometría:** MultiPolygon
- **Número de features:** 1 (únicamente la localidad de Suba)
- **Tamaño:** 87,194 bytes

## Método de Extracción

Se extrajo únicamente el feature correspondiente a Suba del dataset original de 20 localidades, identificado por el atributo `LocCodigo: "11"`. La geometría original se preservó sin alteraciones. No se aplicó reproyección ya que EPSG:4686 y EPSG:4326 son ambos sistemas de coordenadas geográficas en grados con valores prácticamente idénticos para el área de Bogotá (MAGNA-SIRGAS ≈ WGS 84).

## Método de Reproyección

No se aplicó reproyección. El archivo mantiene el CRS original EPSG:4686. La diferencia entre EPSG:4686 y EPSG:4326 es efectivamente nula para fines de cartografía urbana en Bogotá (ambos usan grados con datum prácticamente equivalente). Cuando se requiera integración con Leaflet, el CRS puede declararse como EPSG:4326 sin transformación de coordenadas.

## Validaciones Ejecutadas

1. ✅ **Archivo existente físicamente:** Sí, en `lisboa360-backend/data/processed/territorial/`
2. ✅ **GeoJSON estructuralmente válido:** Sí
3. ✅ **Feature correspondiente a Suba:** Sí (OBJECTID: 100, LocNombre: "SUBA", LocCodigo: "11")
4. ✅ **Geometría no nula:** Sí
5. ✅ **Geometría no vacía:** Sí (1 ring en el polígono)
6. ✅ **Tipo de geometría:** MultiPolygon
7. ✅ **CRS declarado:** EPSG:4686
8. ✅ **Rangos de coordenadas:** X: -74.131986 a -74.034497; Y: 4.685360 a 4.836779 (dentro del rango de Bogotá)
9. ✅ **Conservación de atributos:** Sí (todos los atributos originales preservados)
10. ✅ **Conservación de geometría:** Sí (geometría original sin modificaciones)
11. ✅ **Ausencia de alteraciones no justificadas:** Sí (solo conversión de formato Esri GeoJSON a estándar GeoJSON)

## Atributos Conservados

- `OBJECTID`: 100
- `LocNombre`: SUBA
- `LocCodigo`: 11
- `LocAAdmini`: Acuerdo 8 de 1977
- `LocArea`: 100560477.71021648
- `SHAPE_Length`: 0.5928751050893968
- `SHAPE_Area`: 0.008190624669006016

## Extensión Geográfica (EPSG:4686)

- Longitud (X): -74.131986 a -74.034497
- Latitud (Y): 4.685360 a 4.836779

## Limitaciones

1. **CRS:** El archivo mantiene EPSG:4686. Para uso en Leaflet/OpenStreetMap, se debe declarar como EPSG:4326 (transformación efectivamente identity para este caso).
2. **Sin reproyección:** No se aplicó transformación de coordenadas. El archivo mantiene el CRS original.
3. **Solo Suba:** Este archivo contiene únicamente la localidad de Suba, no otras localidades de Bogotá.
4. **Sin recorte al barrio Lisboa:** No existe límite oficial verificable del barrio Lisboa, por lo que no se realizó recorte espacial.

## Utilidad para Lisboa360

- Proporciona la delimitación oficial verificable de la localidad de Suba
- Sirve como contexto administrativo para el barrio Lisboa
- Permite verificar espacialmente si elementos (parques, equipamientos) están dentro de Suba
- Es una fuente oficial verificable con licencia CC-BY-4.0

## Estado de Validación

- **Estado:** Válido — archivo GeoJSON estructuralmente correcto
- **Listo para uso:** Sí, como referencia territorial de la localidad de Suba (con atribución CC-BY-4.0)
- **Trazabilidad:** Mantiene trazabilidad completa hacia el archivo raw en `lisboa360-backend/data/raw/territorial/`
