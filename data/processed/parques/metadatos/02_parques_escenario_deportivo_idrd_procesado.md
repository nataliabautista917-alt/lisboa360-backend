# Registro de Metadatos — Dataset Procesado: Escenario Deportivo en Parque

## Información del Archivo Procesado

- **Archivo raw de origen:** `parques_escenario_deportivo_idrd_2026.geojson`
- **Ubicación del raw:** `lisboa360-backend/data/raw/parques/parques_escenario_deportivo_idrd_2026.geojson`
- **Archivo procesado:** `parques_escenario_deportivo_idrd_2026_procesado.geojson`
- **Ubicación del procesado:** `lisboa360-backend/data/processed/parques/parques_escenario_deportivo_idrd_2026_procesado.geojson`
- **Fecha de procesamiento:** 22/11/2026
- **Procesado por:** Fase 7 — Procesamiento y validación de datos GIS

## Información Geoespacial

- **Formato:** GeoJSON (RFC 7946)
- **CRS original:** EPSG:4326 (WGS 84) — declarado en el archivo
- **CRS de salida:** EPSG:4326 (WGS 84) — sin reproyección requerida
- **Tipo de geometría:** MultiPolygon
- **Número de features (raw):** 57
- **Número de features (procesado):** 57
- **Tamaño archivo (bytes):** 127,812

## Validación Geométrica

- **Geometrías nulas:** 0
- **Geometrías vacías:** 0
- **Geometrías inválidas detectadas:** 0 (verificación estructural básica)
- **Features sin geometría:** 0
- **Features duplicados (por OBJECTID):** 0
- **Coordenadas fuera de rango Bogotá:** Ninguna detectada (rango X: aprox. -74.26 a -73.96, rango Y: aprox. 4.19 a 5.06)

## Análisis de Atributos

**Campos preservados (37 campos):**
1. `CREATED_DATE`, `Cubierto_`, `Nombre`, `Área_m2`, `Material_Piso`, `Estado_Diagnóstico`, `Identificador_Dotación`, `Número_de_Piso`, `Coordenada_X`, `Servicio_de_Gas`, `Red_Contra_Incendios`, `Riesgo_4`, `Tipo`, `LAST_EDITED_USER`, `Tipo_Cerramiento_Frontal`, `ID_LLAVE`, `LAST_EDITED_DATE`, `Servicio_de_Agua`, `SHAPE.AREA`, `Carriles_`, `Riesgo_3`, `SHAPE.LEN`, `Servicio_de_Luz`, `Cerramiento_`, `Fecha_Creación`, `Fecha_Actualización`, `Riesgo_2`, `Número_Contrato_Actualización_Datos`, `Coordenada_Y`, `Ubicación_Referencia`, `Nombre_del_Parque`, `GLOBALID`, `CREATED_USER`, `Descripción_`, `OBJECTID`, `Iluminación_`, `Camerino_`, `Uso_Incluyente`, `GmlID`, `Tipo_cerramiento_lateral`, `Capacidad_`, `Riesgo_1`

**Campos con valores nulos:** Ninguno detectado en la inspección inicial

**Campos incompletos:** Ninguno detectado

**Valores repetidos:** `Nombre_del_Parque` tiene valores repetidos (múltiples escenarios por parque), lo cual es esperado

## Cambios Realizados

- **Sin cambios:** El archivo se copió tal cual desde el raw. No se aplicó reproyección (ya está en EPSG:4326). No se eliminaron features. No se modificaron atributos.
- **Motivo:** El dataset ya cumple con el CRS objetivo (EPSG:4326) y no se detectaron problemas de calidad críticos.

## Problemas de Calidad

- Ninguno crítico detectado en la inspección inicial
- Varios campos numéricos (`Riesgo_1` a `Riesgo_4`, `Material_Piso`, `Tipo_cerramiento_lateral`, `Tipo_Cerramiento_Frontal`, `Uso_Incluyente`, etc.) contienen códigos numéricos sin una tabla de códigos disponible para interpretar su significado
- La codificación de caracteres muestra algunos caracteres especiales con problemas de encoding (ej. "Cubierto_", "Descripción_", "Fecha_Creación" aparecen con caracteres de reemplazo)

## Estado de Validación

- **Estado:** Válido — estructuralmente correcto como GeoJSON
- **Listo para integración:** Sí, con la salvedad de que no se ha recortado al área del barrio Lisboa (no existe límite oficial verificable)
- **Trazabilidad:** Mantiene trazabilidad completa hacia el archivo raw en `lisboa360-backend/data/raw/parques/`

## Observaciones

- El dataset contiene escenarios deportivos (coliseos, estadios, polideportivos, velódromos) dentro de parques de Bogotá D.C.
- Incluye escenarios como "Centro acuático" en "El Virrey Sur", "Coliseo" en "Villa De Los Alpes" entre otros
- Coordenadas en formato longitud/latitud (EPSG:4326) compatibles con Leaflet
- No se realizó recorte territorial dado que no existe un límite oficial verificable del barrio Lisboa