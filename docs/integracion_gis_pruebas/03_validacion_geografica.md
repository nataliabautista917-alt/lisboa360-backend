# Validación geográfica — Integración GIS (Fase 13)

## 1. Coordenadas y orden

GeoJSON usa el orden `[longitud, latitud]`. `toLatLng()` en `layers.js` convierte correctamente a `L.latLng(lat, lon)` (lat=point[1], lon=point[0]).

## 2. Resultados por dataset

| Dataset | CRS declarado | CRS de las coordenadas | Rango lon | Rango lat | Geometría | Ubicación |
|---------|---------------|------------------------|-----------|-----------|-----------|-----------|
| Pistas IDRD id=2 | EPSG:4326 | Grados geográficos (WGS84) | −74.2048…−74.0245 | 4.4907…4.7656 | 429 MultiPolygon | Bogotá D.C. |
| Escenarios IDRD id=3 | EPSG:4326 | Grados geográficos (WGS84) | −74.2025…−74.0375 | 4.5010…4.7555 | 57 MultiPolygon | Bogotá D.C. |
| Suba id=4 | EPSG:4686 (declarado) | Grados geográficos (numéricamente compatibles con EPSG:4326 para Bogotá) | −74.1320…−74.0345 | 4.6854…4.8368 | 1 MultiPolygon | Localidad de Suba |
| Ficticia id=1 | n/a | Grados (ficticios) | −74.22…−74.20 | 4.65…4.67 | Point/Polygon/LineString | Ficticio |

## 3. CRS — diferencia documentada (Suba)

- **CRS declarado en el archivo:** `urn:ogc:def:crs:EPSG::4686`.
- **CRS real de las coordenadas:** grados geográficos (longitud/latitud), numéricamente en el rango de Bogotá.
- **CRS usado por Leaflet:** interpreta las coordenadas GeoJSON como grados WGS84 (EPSG:4326).

Conclusión: el polígono de Suba se renderiza en la ubicación correcta **sin reproyección**, porque las coordenadas están en grados geográficos. No se afirma que EPSG:4686 y EPSG:4326 sean idénticos; se documenta que, para el rango de Bogotá, los valores numéricos son compatibles con la interpretación de Leaflet. Cualquier operación espacial definitiva requiere resolución autoritativa del CRS.

## 4. Geometrías no nulas

Los 487 features de las 3 capas reales tienen geometría no nula (verificado por parseo). La capa ficticia tiene 3 geometrías válidas (Point, Polygon, LineString).

## 5. Extensión geográfica

Todas las capas reales se ubican dentro de Bogotá D.C. (lon ≈ −74.2…−74.0, lat ≈ 4.49…4.84). Ninguna geometría está fuera del rango geográfico colombiano.

## 6. Limitaciones

- No se realizaron transformaciones ni reproyecciones (prohibido en esta fase).
- Suba es una localidad administrativa, **no** el límite del barrio Lisboa. No se generó ningún polígono del barrio.
- El CRS declarado de Suba (EPSG:4686) sigue sin verificación autoritativa.

## Conclusión

**Validación geográfica: APROBADO CON OBSERVACIONES** (CRS de Suba pendiente de verificación autoritativa).
