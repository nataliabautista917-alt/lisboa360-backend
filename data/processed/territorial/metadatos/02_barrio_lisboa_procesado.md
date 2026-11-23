# Metadatos — Barrio Lisboa (límite oficial, EPSG:4326)

## 1. Archivo generado

- Ruta: `data/processed/territorial/barrio_lisboa_limite_oficial_4326.geojson`.
- Formato: GeoJSON (FeatureCollection, 1 feature).
- CRS: EPSG:4326 (WGS84).
- Licencia: CC-BY-4.0 (SDP).

## 2. Origen

- Fuente original: `data/raw/territorial/barrio_legalizado_bogota_sdp_20260630.json` (ArcGIS REST, SDP).
- Registro: LISBOA, CODIGO_ID LEG01324, localidad 11 (Suba), UPZ 71 (Tibabuyes).
- CRS original: PCS_CarMAGBOG (proyectado, metros, EPSG 6247/102771).
- Transformación: pyproj Transformer.from_crs (WKT → EPSG:4326), always_xy=True.
- No se modificó el archivo original.

## 3. Validación

- Geometría resultante: Polygon, válida (`is_valid=True`), simple, cerrada.
- Vértices: 160 + cierre.
- Área: 0.00001957 deg² (≈ 24 ha en origen).
- Bounds: lon [-74.1257, -74.1181], lat [4.7397, 4.7452].
- Centroide: (-74.1225, 4.7426) — coincide con el centro conocido de Lisboa.
- Coincide con Shape_Area (240314.16 m²) y Shape_Length (2601.58 m) del origen.

## 4. Atributos preservados

CODIGO_ID, NOMBRE, ESTADO, CODIGO_LOCALIDAD, CODIGO_UPZ, CODIGO_UPL, AREA_TOTAL_HA, LOTES_TOTAL, POBLACION_ESTIMADA, DENSIDAD, ACTO_ADMINISTRATIVO, NUMERO_ACTO_ADMINISTRATIVO, NUMERO_PLANO, LLAVE_PLANO, REGLAMENTACION, Shape_Area_m2, Shape_Length_m, FUENTE, LICENCIA, CRS_ORIGEN, CRS_DESTINO, FECHA_CONVERSION.

## 5. Limitaciones

- La reproyección se basó en el WKT del archivo (EPSG 6247/102771). No se verificó autoritativamente.
- El archivo no se integró al backend ni al frontend (fuera del alcance de esta fase).
- No se realizaron commits ni pushes.

## Conclusión

**Conversión y reproyección: COMPLETADA** (Polygon válido en EPSG:4326, centroide coincide con Lisboa).
