# Auditoría geográfica — Fase 18 (Lisboa360)

## 1. Fuentes revisadas (fases 7–17)

- `data/raw/parques/parques_pista_recreativa_idrd_2026.geojson` (IDRD, CC-BY-4.0).
- `data/raw/parques/parques_escenario_deportivo_idrd_2026.geojson` (IDRD, CC-BY-SA-4.0).
- `data/raw/parques/parques_plazas_potencial_idpc_2026.geojson` (IDPC, CC-BY-SA-4.0, excluido).
- `data/raw/territorial/localidades_bogota_sdp_ideca_original.geojson` (SDP/IDECA, CC-BY-4.0).
- `data/processed/territorial/localidad_suba_limite_oficial.geojson` (extraído, CC-BY-4.0).
- `data/geojson/*` (servidos por el backend).
- Documentación de fases 7–17 en `docs/`.

## 2. CRS verificados

| Dataset | CRS declarado | Coordenadas | Compatibilidad con EPSG:4326 |
|---------|---------------|-------------|------------------------------|
| Pistas IDRD | EPSG:4326 | Grados (lon/lat) | Sí (idéntico) |
| Escenarios IDRD | EPSG:4326 | Grados (lon/lat) | Sí (idéntico) |
| Suba | EPSG:4686 (declarado) | Grados (lon/lat, rango Bogotá) | Numéricamente compatible, no verificado autoritativamente |
| IDPC | EPSG:4686 (declarado, inconsistente) | Grados (rango Bogotá) | No verificable (reproyección de prueba dio resultados incorrectos) |

## 3. Geometría de Suba

- Tipo declarado: MultiPolygon.
- Estructura real: Polygon (un único anillo de 913 vértices).
- `shape()` con tipo declarado falla (`TypeError: 'float' object is not iterable`).
- Reconstruida en memoria como Polygon: válida, área 0.00819 deg², bounds lon [-74.132, -74.034], lat [4.685, 4.837].
- Sin agujeros (1 anillo exterior).

## 4. Límite del barrio Lisboa

- No se encontró un polígono GIS oficial verificable del barrio Lisboa en las fuentes consultadas (Datos Abiertos Bogotá, IDECA, SDP, geoportal, Alcaldía Local de Suba).
- Wikipedia y páginas de código postal describen límites textuales (barrios vecinos) y un punto central (-74.122, 4.743), pero no un polígono GIS.
- El dataset "Barrio legalizado. Bogotá D.C." (SDP, Datos Abiertos Bogotá, 3,856 descargas) es una fuente institucional prometedora, pero **no fue descargado ni verificado** (restricción de la Fase 18: no descargar datasets adicionales).
- Clasificación: **No encontrado (GIS verificable)**.

## 5. Dataset IDPC

- CRS declarado: EPSG:4686.
- Coordenadas: grados (lon -74.08, lat 4.60), rango Bogotá.
- Estructura: MultiPolygon válida (profundidad 4), 11 features.
- Reproyección de prueba EPSG:4686→4326 dio resultados incorrectos (documentado en Fase 7.1).
- Estado: **excluido** (CRS incierto, sin verificación autoritativa).

## 6. Resultados espaciales previos (Fases 16–17)

- Pistas: 429 total, 38 en Suba.
- Escenarios: 57 total, 4 en Suba.
- Resultados exploratorios, no específicos de Lisboa.

## Conclusión

**Auditoría geográfica: APROBADO CON OBSERVACIONES** (pendientes documentados).
