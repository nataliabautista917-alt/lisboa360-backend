# Registro de Metadatos — Dataset Procesado: Pistas Recreativas y Deportivas en Parque

## Información del Archivo Procesado

- **Archivo raw de origen:** `parques_pista_recreativa_idrd_2026.geojson`
- **Ubicación del raw:** `lisboa360-backend/data/raw/parques/parques_pista_recreativa_idrd_2026.geojson`
- **Archivo procesado:** `parques_pista_recreativa_idrd_2026_procesado.geojson`
- **Ubicación del procesado:** `lisboa360-backend/data/processed/parques/parques_pista_recreativa_idrd_2026_procesado.geojson`
- **Fecha de procesamiento:** 22/11/2026
- **Procesado por:** Fase 7 — Procesamiento y validación de datos GIS

## Información Geoespacial

- **Formato:** GeoJSON (RFC 7946)
- **CRS original:** EPSG:4326 (WGS 84) — declarado en el archivo
- **CRS de salida:** EPSG:4326 (WGS 84) — sin reproyección requerida
- **Tipo de geometría:** MultiPolygon
- **Número de features (raw):** 429
- **Número de features (procesado):** 429
- **Tamaño archivo (bytes):** 1,201,724

## Validación Geométrica

- **Geometrías nulas:** 0
- **Geometrías vacías:** 0
- **Geometrías inválidas detectadas:** 0 (verificación estructural básica)
- **Features sin geometría:** 0
- **Features duplicados (por OBJECTID):** 0
- **Coordenadas fuera de rango Bogotá:** Ninguna detectada (rango X: aprox. -74.26 a -73.96, rango Y: aprox. 4.19 a 5.06)

## Análisis de Atributos

**Campos preservados (11 campos):**
1. `Tipo` — Código numérico de tipo de pista
2. `GLOBALID` — Identificador global único
3. `OBJECTID` — Identificador de objeto
4. `Ubicación_Referencia` — Código de referencia de ubicación
5. `GmlID` — Identificador GML
6. `SHAPE.LEN` — Longitud de la geometría
7. `Nombre_del_Parque` — Nombre del parque donde se ubica la pista
8. `Número_de_Piso` — Número de piso (campo numérico)
9. `Nombre` — Código numérico de nombre
10. `LAST_EDITED_DATE` — Fecha de última edición
11. `Identificador_Dotación` — Identificador de dotación

**Campos con valores nulos:** Ninguno detectado en la inspección inicial

**Campos incompletos:** Ninguno detectado

**Valores repetidos:** `Nombre_del_Parque` tiene valores repetidos (múltiples pistas por parque), lo cual es esperado

## Cambios Realizados

- **Sin cambios:** El archivo se copió tal cual desde el raw. No se aplicó reproyección (ya está en EPSG:4326). No se eliminaron features. No se modificaron atributos.
- **Motivo:** El dataset ya cumple con el CRS objetivo (EPSG:4326) y no se detectaron problemas de calidad críticos.

## Problemas de Calidad

- Ninguno crítico detectado en la inspección inicial
- Los campos `Tipo`, `Nombre`, `Identificador_Dotación` y `Número_de_Piso` contienen valores numéricos sin una tabla de códigos disponible para interpretar su significado
- La codificación de caracteres muestra algunos caracteres especiales con problemas de encoding (ej. "Ubicación_Referencia" aparece con caracteres de reemplazo)

## Estado de Validación

- **Estado:** Válido — estructuralmente correcto como GeoJSON
- **Listo para integración:** Sí, con la salvedad de que no se ha recortado al área del barrio Lisboa (no existe límite oficial verificable)
- **Trazabilidad:** Mantiene trazabilidad completa hacia el archivo raw en `lisboa360-backend/data/raw/parques/`

## Observaciones

- El dataset contiene pistas recreativas y deportivas dentro de parques de Bogotá D.C.
- Incluye parques como "El Recreo", "Naranjos", "Las Margaritas (Gilma Jimenez)" entre otros
- Coordenadas en formato longitud/latitud (EPSG:4326) compatibles con Leaflet
- No se realizó recorte territorial dado que no existe un límite oficial verificable del barrio Lisboa