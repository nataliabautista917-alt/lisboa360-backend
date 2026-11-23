# Auditoría de datasets — Fase 16 (Lisboa360)

## 1. Archivos utilizados

| Archivo | Ubicación | Existe | Tamaño |
|---------|-----------|--------|--------|
| `parques_pista_recreativa_idrd_2026.geojson` (raw) | `data/raw/parques/` | Sí | 1,201,724 B |
| `parques_pista_recreativa_idrd_2026_procesado.geojson` (procesado) | `data/processed/parques/` | Sí | 1,201,724 B |
| `parques_pista_recreativa_idrd_2026_procesado.geojson` (servido) | `data/geojson/` | Sí | 1,201,724 B |
| `parques_escenario_deportivo_idrd_2026.geojson` (raw) | `data/raw/parques/` | Sí | 127,812 B |
| `parques_escenario_deportivo_idrd_2026_procesado.geojson` (procesado) | `data/processed/parques/` | Sí | 127,812 B |
| `parques_escenario_deportivo_idrd_2026_procesado.geojson` (servido) | `data/geojson/` | Sí | 127,812 B |
| `localidades_bogota_sdp_ideca_original.geojson` (raw) | `data/raw/territorial/` | Sí | 2,363,493 B |
| `localidad_suba_limite_oficial.geojson` (procesado) | `data/processed/territorial/` | Sí | 87,194 B |
| `localidad_suba_limite_oficial.geojson` (servido) | `data/geojson/` | Sí | 87,194 B |
| `parques_plazas_potencial_idpc_2026.geojson` (raw, excluido) | `data/raw/parques/` | Sí | 25,244 B |

## 2. Fuentes y licencias

| Dataset | Fuente | Licencia |
|---------|--------|----------|
| Pistas IDRD | IDRD — Open Data Bogotá | CC-BY-4.0 |
| Escenarios IDRD | IDRD — Open Data Bogotá | CC-BY-SA-4.0 |
| Localidad de Suba | SDP/IDECA | CC-BY-4.0 |
| IDPC plazas/parques | IDPC (excluido por CRS inconsistente) | CC-BY-SA-4.0 |

## 3. CRS y geometrías

| Dataset | CRS declarado | Coordenadas | Tipo declarado | Estructura real |
|---------|---------------|-------------|----------------|-----------------|
| Pistas IDRD | EPSG:4326 | Grados (lon/lat) | MultiPolygon | MultiPolygon (profundidad 4) |
| Escenarios IDRD | EPSG:4326 | Grados (lon/lat) | MultiPolygon | MultiPolygon (profundidad 4) |
| Suba | EPSG:4686 (declarado) | Grados (lon/lat, rango Bogotá) | MultiPolygon | **Polygon** (profundidad 3) — inconsistencia |
| IDPC | EPSG:4686 (declarado, inconsistente) | Grados | MultiPolygon | No utilizado |

## 4. Features y geometrías nulas

| Dataset | Features | Geometrías nulas | Tipos |
|---------|----------|------------------|-------|
| Pistas | 429 | 0 | MultiPolygon (429) |
| Escenarios | 57 | 0 | MultiPolygon (57) |
| Suba | 1 | 0 | MultiPolygon declarado / Polygon real |

## 5. Atributos disponibles

- **Pistas:** `GmlID`, `OBJECTID`, `Ubicación_Referencia`, `Identificador_Dotación`, `Tipo`, `Nombre`, `Número_de_Piso`, `GLOBALID`, `LAST_EDITED_DATE`, `Nombre_del_Parque`, `SHAPE.LEN`.
- **Escenarios:** además de los anteriores: `Coordenada_X`, `Coordenada_Y`, `Descripción_`, `Material_Piso`, `Área__m2_`, `Capacidad_`, `Iluminación_`, `Cubierto_`, `Cerramiento_`, `Tipo_cerramiento_lateral`, `Tipo_Cerramiento_Frontal`, `Carriles_`, `Camerino_`, `Servicio_de_Luz`, `Servicio_de_Agua`, `Servicio_de_Gas`, `Red_Contra_Incendios`, `Uso_Incluyente`, `Fecha_Creación`, `Fecha_Actualización`, `Riesgo_1–4`, `Estado_Diagnóstico`, `Número_Contrato_Actualización_Datos`, `Nombre_del_Parque`, `ID_LLAVE`, `SHAPE.AREA`, `SHAPE.LEN`.
- **Suba:** `OBJECTID`, `LocNombre`, `LocCodigo`, `LocAAdmini`, `LocArea`, `SHAPE_Length`, `SHAPE_Area`.

## 6. Limitaciones

- El dataset de Suba tiene una inconsistencia de tipo de geometría (declarado MultiPolygon, estructura Polygon).
- El CRS declarado de Suba (EPSG:4686) no coincide con el uso (grados geográficos).
- El dataset IDPC está excluido por inconsistencia de CRS.
- No existe límite oficial verificable del barrio Lisboa.

## Conclusión

**Auditoría de datasets: APROBADO CON OBSERVACIONES** (inconsistencia de geometría en Suba documentada).
