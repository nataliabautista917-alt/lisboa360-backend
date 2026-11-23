# Verificación de CRS — Fase 18 (Lisboa360)

## 1. Pistas y escenarios IDRD

- CRS declarado: EPSG:4326.
- Coordenadas: grados (lon/lat), rango Bogotá.
- Datum: WGS84 (implícito en EPSG:4326).
- Compatibilidad con Leaflet: sí (Leaflet interpreta GeoJSON como WGS84).
- **Verificado.**

## 2. Localidad de Suba

- CRS declarado en archivo: `urn:ogc:def:crs:EPSG::4686`.
- Coordenadas: grados (lon -74.13…-74.03, lat 4.68…4.84).
- EPSG:4686 = MAGNA-SIRGAS (datum colombiano).
- Los valores numéricos están en el rango de Bogotá y son compatibles con la interpretación de Leaflet (grados WGS84).
- **No se confirmó autoritativamente** que las coordenadas sean MAGNA-SIRGAS; la reproyección de prueba EPSG:4686→4326 produjo resultados incorrectos en Fase 7.1.
- **Conclusión:** incertidumbre documentada. No se reproyectó.

## 3. IDPC

- CRS declarado: EPSG:4686.
- Coordenadas: grados (lon -74.08, lat 4.60).
- Reproyección de prueba dio resultados incorrectos.
- **Conclusión:** CRS incierto, dataset excluido.

## 4. Compatibilidad general

- Pistas y escenarios: compatibles con Leaflet sin transformación.
- Suba: visualmente compatible (coordenadas en grados), pero CRS declarado no verificado.
- No se realizaron transformaciones ni reproyecciones.

## Conclusión

**CRS: APROBADO CON OBSERVACIONES** (Suba e IDPC con incertidumbre documentada).
