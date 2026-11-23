# Integración de Capas GIS — Lisboa360 Backend

## 1. Arquitectura implementada

La integración de datos GIS reales en Lisboa360 se realizó siguiendo la arquitectura existente del backend, sin modificar el código de las capas existentes (rutas, servicios, repositorios, modelos). Los datos reales se incorporan exclusivamente a través de la tabla existente `capa_geografica`, que ya estaba definida en el esquema de SQLite.

### Arquitectura de capas

```
Frontend (lisboa360-frontend)
    │
    └─► lisboa360-api  (API REST, contrato OpenAPI)
            │
            └─► lisboa360-backend  (Backend Flask + SQLite + GeoJSON)
                    │
                    ├─► app/routes/capas_routes.py        (GET /api/v1/capas, GET /api/v1/capas/{capa_id}/geojson)
                    ├─► app/services/capas_service.py     (Lógica de negocio: listar capas, obtener GeoJSON)
                    ├─► app/repositories/capa_geografica_repository.py  (DAO: consultas SQL)
                    ├─► app/models/capa_geografica.py     (Dataclass CapaGeografica)
                    └─► app/db/capa_geografica table      (Metadatos de capas: nombre, tipo, ruta_archivo, CRS, etc.)
                            │
                            └─► data/geojson/*.geojson    (Archivos GeoJSON físicos servidos por la API)
```

### Arquitectura de datos

Los datos geoGIS reales se almacenan como archivos GeoJSON en `data/geojson/` y se registran como registros en la tabla `capa_geografica` de SQLite. Los datos ficticios existentes permanecen intactos en la base de datos y no se mezclan con los datos reales.

| Capa | ID | Fuente | Tipo | Formato | CRS | Ubicación del archivo |
|------|-----|--------|------|---------|-----|----------------------|
| Capa general ficticia | 1 | Lisboa360 (desarrollo) | general | GeoJSON | N/A (ficticio) | `data/geojson/ejemplo_ficticio_capa_general.geojson` |
| Pistas Recreativas IDRD | 2 | IDRD | parque_deportivo | GeoJSON | EPSG:4326 | `data/geojson/parques_pista_recreativa_idrd_2026_procesado.geojson` |
| Escenario Deportivo IDRD | 3 | IDRD | escenario_deportivo | GeoJSON | EPSG:4326 | `data/geojson/parques_escenario_deportivo_idrd_2026_procesado.geojson` |
| Localidad de Suba | 4 | SDP/IDECA | localidad | GeoJSON | EPSG:4686 (= EPSG:4326) | `data/geojson/localidad_suba_limite_oficial.geojson` |

## 2. Capas incorporadas

### Capa 2: Pistas Recreativas y Deportivas en Parque (IDRD)
- **Nombre:** Pistas Recreativas y Deportivas en Parque (IDRD)
- **Tipo:** parque_deportivo
- **Descripción:** Pistas recreativas y deportivas dentro de parques de Bogotá D.C. Fuente: IDRD. Cobertura distrital.
- **Archivo:** `parques_pista_recreativa_idrd_2026_procesado.geojson`
- **Formato:** GeoJSON
- **CRS:** EPSG:4326
- **Número de features:** 429
- **Tipo de geometría:** MultiPolygon
- **Estado:** activa
- **Utilidad:** Equipamientos deportivos dentro de parques; útil para visualización de escenarios deportivos en el barrio Lisboa y localidad de Suba.

### Capa 3: Escenario Deportivo en Parque (IDRD)
- **Nombre:** Escenario Deportivo en Parque (IDRD)
- **Tipo:** escenario_deportivo
- **Descripción:** Escenarios deportivos en parques de Bogotá D.C. (coliseos, estadios, polideportivos, velódromos). Fuente: IDRD. Cobertura distrital.
- **Archivo:** `parques_escenario_deportivo_idrd_2026_procesado.geojson`
- **Formato:** GeoJSON
- **CRS:** EPSG:4326
- **Número de features:** 57
- **Tipo de geometría:** MultiPolygon
- **Estado:** activa
- **Utilidad:** Escenarios deportivos en parques; útil para visualización de equipamientos deportivos en el barrio Lisboa y localidad de Suba.

### Capa 4: Delimitación Localidad de Suba (SDP/IDECA)
- **Nombre:** Delimitación Localidad de Suba (SDP/IDECA)
- **Tipo:** localidad
- **Descripción:** Delimitación territorial oficial de la localidad de Suba, Bogotá D.C. (código 11). Fuente: Secretaría Distrital de Planeación / IDECA. Contexto administrativo, NO es el límite del barrio Lisboa.
- **Archivo:** `localidad_suba_limite_oficial.geojson`
- **Formato:** GeoJSON
- **CRS:** EPSG:4686 (numéricamente equivalente a EPSG:4326 para Bogotá)
- **Número de features:** 1
- **Tipo de geometría:** Polígono
- **Estado:** activa
- **Utilidad:** Contexto administrativo de la localidad donde se ubica el barrio Lisboa. NO se utiliza como límite del barrio Lisboa.

## 3. Rutas de archivos

Todos los archivos GeoJSON procesados se almacenan en `lisboa360-backend/data/geojson/` (directorio configurado como `GEOJSON_DIR` en la configuración del backend):

| Archivo | Ruta completa | Tamaño | Origen |
|---------|--------------|--------|--------|
| `parques_pista_recreativa_idrd_2026_procesado.geojson` | `lisboa360-backend/data/geojson/parques_pista_recreativa_idrd_2026_procesado.geojson` | 1,201,724 bytes | Copia de `lisboa360-backend/data/processed/parques/` |
| `parques_escenario_deportivo_idrd_2026_procesado.geojson` | `lisboa360-backend/data/geojson/parques_escenario_deportivo_idrd_2026_procesado.geojson` | 127,812 bytes | Copia de `lisboa360-backend/data/processed/parques/` |
| `localidad_suba_limite_oficial.geojson` | `lisboa360-backend/data/geojson/localidad_suba_limite_oficial.geojson` | 87,194 bytes | Copia de `lisboa360-backend/data/processed/territorial/` |

Los archivos originales en `data/raw/` y `data/processed/` se mantienen intactos sin modificaciones.

## 4. Endpoints utilizados

Se reutilizan los endpoints existentes de la API REST del backend Lisboa360, sin crear nuevas rutas ni modificar contratos OpenAPI existentes:

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `GET /api/v1/capas` | GET | Lista paginada de todas las capas geográficas registradas (incluye las 3 nuevas capas reales) |
| `GET /api/v1/capas/{capa_id}/geojson` | GET | Devuelve los datos GeoJSON de una capa específica en formato FeatureCollection |

Los capas reales están disponibles inmediatamente después de ejecutar el seed de base de datos, sin necesidad de modificar el código de las rutas ni los servicios existentes.

### Ejemplo de respuesta `GET /api/v1/capas`

```json
{
  "items": [
    {
      "id": 1,
      "nombre": "Ejemplo ficticio: Capa general",
      "tipo": "general",
      "descripcion": "Ejemplo ficticio: capa con geometrías puntuales, líneas y áreas.",
      "formato": "GeoJSON",
      "ruta_archivo": "ejemplo_ficticio_capa_general.geojson",
      "fecha_generacion": "2026-01-01",
      "estado": "activa",
      "tipo_geometria": "Point, LineString, Polygon",
      "created_at": "2026-01-01T00:00:00"
    },
    {
      "id": 2,
      "nombre": "Pistas Recreativas y Deportivas en Parque (IDRD)",
      "tipo": "parque_deportivo",
      "descripcion": "Pistas recreativas y deportivas dentro de parques de Bogotá D.C. Fuente: IDRD. Cobertura distrital.",
      "formato": "GeoJSON",
      "ruta_archivo": "parques_pista_recreativa_idrd_2026_procesado.geojson",
      "fecha_generacion": "2026-11-22",
      "estado": "activa",
      "tipo_geometria": "MultiPolygon",
      "created_at": "2026-11-22T00:00:00"
    },
    ...
  ],
  "total": 4,
  "limit": 50,
  "offset": 0
}
```

### Ejemplo de respuesta `GET /api/v1/capas/2/geojson`

Devuelve el archivo GeoJSON completo de las pistas recreativas IDRD como `FeatureCollection`.

## 5. Cambios realizados en el backend

### Archivos modificados:
- **`app/db/seed.py`**: Se añadió la lista `CAPAS_GEOGRAFICAS_REALES` con 3 registros y el correspondiente bucle de inserción en la función `seed()`. Los datos ficticios existentes (id=1) se mantienen sin cambios.

### Archivos no modificados (intactos):
- `app/__init__.py`
- `app/routes/capas_routes.py`
- `app/services/capas_service.py`
- `app/repositories/capa_geografica_repository.py`
- `app/models/capa_geografica.py`
- `app/db/schema.sql`
- `app/db/connection.py`
- `app/utils/errors.py`
- `app/utils/validation.py`
- `config/__init__.py`

### Archivos de datos copiados (no modificados):
- Los 3 archivos GeoJSON originales en `data/raw/` y `data/processed/` se mantienen sin cambios.
- Se crearon copias en `data/geojson/` para ser servidas por el backend a través de `GEOJSON_DIR`.

## 6. Separación entre datos reales y ficticios

| Aspecto | Datos ficticios | Datos reales (IDRD/SDP) |
|---------|----------------|------------------------|
| Origen | Desarrollo interno | Fuentes oficiales distritales |
| Tabla | `capa_geografica` (id=1) | `capa_geografica` (ids 2,3,4) |
| Archivo | `data/geojson/ejemplo_ficticio_capa_general.geojson` | `data/geojson/parques_*_idrd_*.geojson`, `localidad_suba_limite_oficial.geojson` |
| Cobertura | Barrio Lisboa ficticio | Localidad de Suba / Bogotá D.C. |
| Licencia | N/A (desarrollo) | CC-BY-4.0 / CC-BY-SA-4.0 |
| Uso | Pruebas y desarrollo | Datos territoriales reales para exploración |

Los datos ficticios se mantienen completamente separados y no se eliminan ni se mezclan con los datos reales. Cada capa tiene su identificador único y su origen documentado.

## 7. Limitaciones

- El dataset IDPC (Potencial Plazas y Parques) NO se integra como capa GIS activa debido a la inconsistencia de CRS documentada (EPSG:4686 declarado vs. coordenadas en grados geográficos en el archivo).
- El archivo de la localidad de Suba representa el límite de la localidad, NO el límite del barrio Lisboa. No existe delimitación oficial verificable del barrio Lisboa en fuentes abiertas.
- Los datos tienen cobertura distrital (Bogotá D.C.), no recortados específicamente al barrio Lisboa.
- No se implementó ninguna transformación de reproyección; los archivos se mantienen en su CRS original.

## 8. Próximos pasos

- Implementar reproyección de EPSG:4686 a EPSG:4326 para el dataset de plazas IDPC si se resuelve la inconsistencia de CRS.
- Obtener delimitación oficial verificable del barrio Lisboa para recortar los datasets distritales al área del barrio.
- Implementar endpoints adicionales si se requiere filtrado por tipo de capa o por localidad.
- Agregar pruebas automatizadas específicas para las nuevas capas reales.