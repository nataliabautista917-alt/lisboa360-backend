# Metadatos de Capas GIS — Lisboa360

## 1. Capa: Pistas Recreativas y Deportivas en Parque (IDRD)

### Información básica

| Campo | Valor |
|-------|-------|
| **Identificador** | 2 |
| **Nombre** | Pistas Recreativas y Deportivas en Parque (IDRD) |
| **Tipo** | parque_deportivo |
| **Descripción** | Pistas recreativas y deportivas dentro de parques de Bogotá D.C. Fuente: IDRD. Cobertura distrital. |
| **Formato** | GeoJSON (RFC 7946) |
| **Archivo** | `parques_pista_recreativa_idrd_2026_procesado.geojson` |
| **Ruta completa** | `lisboa360-backend/data/geojson/parques_pista_recreativa_idrd_2026_procesado.geojson` |
| **Fecha de generación** | 2026-11-22 |
| **Estado** | activa |
| **Tipo de geometría** | MultiPolygon |
| **Número de features** | 429 |
| **Tamaño del archivo** | 1,201,724 bytes (~1.2 MB) |

### Sistema de referencia de coordenadas

| Campo | Valor |
|-------|-------|
| **CRS declarado** | EPSG:4326 (WGS 84) |
| **Unidades** | Grados decimales (longitud, latitud) |
| **Primera meridiana** | Greenwich |
| **Compatibilidad con Leaflet** | Sí (nativo) |

### Atributos conservados

| Campo | Descripción |
|-------|-------------|
| `GmlID` | Identificador GML |
| `OBJECTID` | Identificador de objeto |
| `Ubicación_Referencia` | Código de referencia de ubicación |
| `Identificador_Dotación` | Identificador de dotación |
| `Tipo` | Código numérico de tipo de pista |
| `Nombre` | Código numérico de nombre |
| `Número_de_Piso` | Número de piso |
| `GLOBALID` | Identificador global único |
| `LAST_EDITED_DATE` | Fecha de última edición |
| `Nombre_del_Parque` | Nombre del parque donde se ubica la pista |
| `SHAPE.LEN` | Longitud de la geometría |

### Parques identificados (ejemplos)

- El Recreo
- Naranjos
- Las Margaritas (Gilma Jimenez)

### Licencias y atribución

| Campo | Valor |
|-------|-------|
| **Licencia** | CC-BY-4.0 (Creative Commons Attribution 4.0) |
| **URL de licencia** | https://creativecommons.org/licenses/by/4.0/ |
| **Entidad distribuidora** | Instituto Distrital de Recreación y Deporte - IDRD |
| **Mantenedor** | Erika Ladino (erika.ladino@idrd.gov.co) |
| **Frecuencia de actualización** | Anual |
| **Atribución requerida** | Fuente: IDRD. Licencia: CC-BY-4.0. Datos: Lisboa360. |

### Formatos originales disponibles (en fuente original)

GeoJSON, GPKG, SHP, KMZ, DXF, WFS, WMS, Esri REST

### Utilidad para Lisboa360

Capa de equipamientos deportivos dentro de parques; útil para visualización de escenarios deportivos en el barrio Lisboa y localidad de Suba.

### Limitaciones

- Cobertura distrital (Bogotá D.C.), no recortada específicamente al barrio Lisboa.
- Campos numéricos (Tipo, Nombre, Identificador_Dotación, Número_de_Piso) sin tabla de códigos disponible para interpretar su significado.
- Algunos campos muestran caracteres de reemplazo por problemas de encoding en el archivo original.

---

## 2. Capa: Escenario Deportivo en Parque (IDRD)

### Información básica

| Campo | Valor |
|-------|-------|
| **Identificador** | 3 |
| **Nombre** | Escenario Deportivo en Parque (IDRD) |
| **Tipo** | escenario_deportivo |
| **Descripción** | Escenarios deportivos en parques de Bogotá D.C. (coliseos, estadios, polideportivos, velódromos). Fuente: IDRD. Cobertura distrital. |
| **Formato** | GeoJSON (RFC 7946) |
| **Archivo** | `parques_escenario_deportivo_idrd_2026_procesado.geojson` |
| **Ruta completa** | `lisboa360-backend/data/geojson/parques_escenario_deportivo_idrd_2026_procesado.geojson` |
| **Fecha de generación** | 2026-11-22 |
| **Estado** | activa |
| **Tipo de geometría** | MultiPolygon |
| **Número de features** | 57 |
| **Tamaño del archivo** | 127,812 bytes |

### Sistema de referencia de coordenadas

| Campo | Valor |
|-------|-------|
| **CRS declarado** | EPSG:4326 (WGS 84) |
| **Unidades** | Grados decimales (longitud, latitud) |
| **Primera meridiana** | Greenwich |
| **Compatibilidad con Leaflet** | Sí (nativo) |

### Atributos conservados (37 campos)

| Campo | Descripción |
|-------|-------------|
| `GmlID` | Identificador GML |
| `OBJECTID` | Identificador de objeto |
| `Ubicación_Referencia` | Código de referencia de ubicación |
| `Identificador_Dotación` | Identificador de dotación |
| `Tipo` | Código numérico de tipo |
| `Nombre` | Código numérico de nombre |
| `Coordenada_X` | Coordenada X |
| `Coordenada_Y` | Coordenada Y |
| `Descripción_` | Descripción del escenario |
| `Material_Piso` | Código numérico de material de piso |
| `Área_m2` | Área en metros cuadrados |
| `Capacidad_` | Capacidad |
| `Iluminación_` | Código de iluminación |
| `Cubierto_` | Código de cubierto |
| `Cerramiento_` | Código de cerramiento |
| `Tipo_cerramiento_lateral` | Código de cerramiento lateral |
| `Tipo_Cerramiento_Frontal` | Código de cerramiento frontal |
| `Carriles_` | Número de carriles |
| `Camerino_` | Código de camerino |
| `Servicio_de_Luz` | Código de servicio de luz |
| `Servicio_de_Agua` | Código de servicio de agua |
| `Servicio_de_Gas` | Código de servicio de gas |
| `Red_Contra_Incendios` | Código de red contra incendios |
| `Uso_Incluyente` | Código de uso incluyente |
| `Fecha_Creación` | Fecha de creación |
| `Fecha_Actualización` | Fecha de actualización |
| `Riesgo_1` a `Riesgo_4` | Códigos de riesgo |
| `Estado_Diagnóstico` | Código de estado de diagnóstico |
| `Número_Contrato_Actualización_Datos` | Número de contrato de actualización |
| `Número_de_Piso` | Número de piso |
| `GLOBALID` | Identificador global único |
| `CREATED_USER` | Usuario creador |
| `CREATED_DATE` | Fecha de creación |
| `LAST_EDITED_USER` | Usuario que editó por última vez |
| `LAST_EDITED_DATE` | Fecha de última edición |
| `Nombre_del_Parque` | Nombre del parque |
| `ID_LLAVE` | Identificador de llave |
| `SHAPE.AREA` | Área de la geometría |
| `SHAPE.LEN` | Longitud de la geometría |

### Parques identificados (ejemplos)

- El Virrey Sur (Centro acuático)
- Villa De Los Alpes (Coliseo)

### Licencias y atribución

| Campo | Valor |
|-------|-------|
| **Licencia** | CC-BY-SA-4.0 (Creative Commons Attribution Share-Alike 4.0) |
| **URL de licencia** | https://creativecommons.org/licenses/by-sa/4.0/ |
| **Entidad distribuidora** | Instituto Distrital de Recreación y Deporte - IDRD |
| **Mantenedor** | Manuel Alonso Diaz Pinto (manuel.diaz@idrd.gov.co) |
| **Frecuencia de actualización** | Según necesidad |
| **Atribución requerida** | Fuente: IDRD. Licencia: CC-BY-SA-4.0. Datos: Lisboa360. |

### Formatos originales disponibles (en fuente original)

GeoJSON, GPKG, SHP, KMZ, DXF, WFS, WMS, Esri REST

### Utilidad para Lisboa360

Escenarios deportivos en parques; útil para visualización de equipamientos deportivos en el barrio Lisboa y localidad de Suba.

### Limitaciones

- Cobertura distrital (Bogotá D.C.), no recortada específicamente al barrio Lisboa.
- Varios campos numéricos (Riesgo_1 a Riesgo_4, Material_Piso, Tipo_cerramiento_lateral, Tipo_Cerramiento_Frontal, Uso_Incluyente, etc.) contienen códigos numéricos sin tabla de códigos disponible.
- Algunos campos muestran caracteres de reemplazo por problemas de encoding en el archivo original.

---

## 3. Capa: Delimitación Localidad de Suba (SDP/IDECA)

### Información básica

| Campo | Valor |
|-------|-------|
| **Identificador** | 4 |
| **Nombre** | Delimitación Localidad de Suba (SDP/IDECA) |
| **Tipo** | localidad |
| **Descripción** | Delimitación territorial oficial de la localidad de Suba, Bogotá D.C. (código 11). Fuente: Secretaría Distrital de Planeación / IDECA. Contexto administrativo, NO es el límite del barrio Lisboa. |
| **Formato** | GeoJSON (RFC 7946) |
| **Archivo** | `localidad_suba_limite_oficial.geojson` |
| **Ruta completa** | `lisboa360-backend/data/geojson/localidad_suba_limite_oficial.geojson` |
| **Fecha de generación** | 2026-11-22 |
| **Estado** | activa |
| **Tipo de geometría** | Polígono |
| **Número de features** | 1 |
| **Tamaño del archivo** | 87,194 bytes |

### Sistema de referencia de coordenadas

| Campo | Valor |
|-------|-------|
| **CRS declarado en origen** | EPSG:4686 MAGNA-SIRGAS geographic 2D - 4686 |
| **CRS declarado en salida** | EPSG:4686 (sin reproyección) |
| **CRS objetivo para Leaflet** | EPSG:4326 (WGS 84) |
| **Unidades** | Grados decimales (longitud, latitud) |
| **Primera meridiana** | Greenwich |
| **Compatibilidad con Leaflet** | Sí (EPSG:4686 es numéricamente equivalente a EPSG:4326 para Bogotá; las coordenadas están en grados geográficos) |

### Sistema de referencia - Nota importante

El archivo declara CRS EPSG:4686 (MAGNA-SIRGAS geographic 2D). Sin embargo, las coordenadas contenidas en el archivo están en grados geográficos (longitud: aprox. -74.09 a -74.06, latitud: aprox. 4.58 a 4.61), que son compatibles con EPSG:4326 (WGS 84). No se realizó reproyección; el CRS se mantiene como declarado en el origen.

### Atributos conservados

| Campo | Descripción |
|-------|-------------|
| `OBJECTID` | Identificador de objeto |
| `LocNombre` | Nombre de la localidad (SUBA) |
| `LocAAdmini` | Acto administrativo (Acuerdo 8 de 1977) |
| `LocCodigo` | Código de la localidad (11) |
| `LocArea` | Área de la localidad |
| `SHAPE_Length` | Longitud de la geometría |
| `SHAPE_Area` | Área de la geometría |

### Extensión geográfica (EPSG:4686)

| Campo | Valor |
|-------|-------|
| **Longitud mínima** | -74.131986 |
| **Longitud máxima** | -74.034497 |
| **Latitud mínima** | 4.685360 |
| **Latitud máxima** | 4.836779 |

### Licencias y atribución

| Campo | Valor |
|-------|-------|
| **Licencia** | CC-BY-4.0 (Creative Commons Attribution 4.0) |
| **URL de licencia** | https://creativecommons.org/licenses/by/4.0/ |
| **Entidad distribuidora** | Secretaría Distrital de Planeación - SDP / IDECA |
| **URL de la ficha** | https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8 |
| **Fecha del dato** | 2022-08-05 |
| **Última actualización del metadato** | 2023-02-28 |
| **Atribución requerida** | Fuente: SDP/IDECA. Licencia: CC-BY-4.0. Datos: Lisboa360. |

### Formatos originales disponibles (en fuente original)

GeoJSON, GPKG, SHP, KMZ, DXF, WFS, WMS, Esri REST

### Utilidad para Lisboa360

Contexto administrativo de la localidad donde se ubica el barrio Lisboa. NO se utiliza como límite del barrio Lisboa.

### Limitaciones

- Cobertura distrital (Bogotá D.C.), no recortada específicamente al barrio Lisboa.
- No existe delimitación oficial verificable del barrio Lisboa en fuentes abiertas.
- CRS declarado EPSG:4686, pero las coordenadas están en grados geográficos (equivalentes a EPSG:4326).

---

## 4. Resumen de metadatos de todas las capas

| ID | Nombre | Tipo | Formato | CRS | Features | Licencia | Utilidad |
|----|--------|------|---------|-----|----------|----------|----------|
| 1 | Ejemplo ficticio: Capa general | general | GeoJSON | N/A (ficticio) | Múltiples | N/A (desarrollo) | Pruebas y desarrollo |
| 2 | Pistas Recreativas y Deportivas en Parque (IDRD) | parque_deportivo | GeoJSON | EPSG:4326 | 429 | CC-BY-4.0 | Equipamientos deportivos en parques |
| 3 | Escenario Deportivo en Parque (IDRD) | escenario_deportivo | GeoJSON | EPSG:4326 | 57 | CC-BY-SA-4.0 | Escenarios deportivos en parques |
| 4 | Delimitación Localidad de Suba (SDP/IDECA) | localidad | GeoJSON | EPSG:4686 | 1 | CC-BY-4.0 | Contexto administrativo de Suba |

## 5. Atribución requerida en la aplicación

Cada capa que se visualice en el frontend debe incluir la siguiente atribución:

```
Fuente: IDRD/SDP. Licencia: CC-BY-4.0 / CC-BY-SA-4.0. Datos: Lisboa360.
```

Esto cumple con los requisitos de atribución de las licencias Creative Commons.
