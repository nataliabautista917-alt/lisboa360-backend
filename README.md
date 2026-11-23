# Lisboa360 Backend

Backend de la aplicación web Lisboa360: lógica de negocio, procesamiento y acceso a datos.

## Responsabilidad exclusiva

Este repositorio corresponde a la capa de procesamiento y acceso a datos de la aplicación de tres capas:

- Lógica de negocio que valida y procesa las consultas recibidas desde la API (`lisboa360-api`).
- Acceso a la fuente de datos SQLite y GeoJSON para recuperar la información territorial del barrio Lisboa.
- Centralización de las reglas de consulta, validación de solicitudes y transformación de datos antes de devolverlas a la API.
- Respuesta a las solicitudes de la capa API en formato JSON procesado.

## Estructura del proyecto

```
lisboa360-backend/
├── app.py                         # Punto de entrada (create_app + init_db + app.run)
├── config/                        # Configuración por variables de entorno
├── app/
│   ├── __init__.py                # create_app() (factory)
│   ├── routes/                    # Blueprints de Flask (una por recurso, /api/v1)
│   ├── services/                  # Lógica de negocio por recurso
│   ├── repositories/              # Capa DAO: consultas SQL directas contra SQLite
│   ├── models/                    # Modelos (dataclasses) por entidad
│   ├── db/                        # Conexión SQLite, schema.sql y seed de desarrollo
│   └── utils/                     # Errores estandarizados, validación, utilitarios GeoJSON
├── database/                      # Archivo SQLite (lisboa360.db, creado en tiempo de ejecución)
├── data/geojson/                  # Archivos GeoJSON de capas (ej. ejemplo_ficticio_capa_general.geojson)
├── tests/                         # Pruebas: rutas (endpoints) y servicios/utilidades
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md                      # (este archivo)
```

## Objetivo

Implementar los endpoints de consulta de la información territorial del barrio Lisboa
(`/api/v1/barrios/lisboa`, `/api/v1/capas`, `/api/v1/lugares`, `/api/v1/equipamientos`,
`/api/v1/espacios-publicos`, `/api/v1/movilidad`) con validación de parámetros, paginación
y respuestas en JSON, respaldando los contratos OpenAPI de `lisboa360-api`.

## Tecnologías previstas

- Python
- Flask

## Integración con los otros repositorios

- **`lisboa360-api`:** Implementa los endpoints de la API REST que expone el contrato de este repositorio; recibe las peticiones de la capa API y devuelve las respuestas procesadas.
- **`lisboa360-frontend`:** El frontend no accede directamente a la base de datos ni a los archivos GeoJSON; obtiene toda la información mediante la API REST implementada por este backend.

## Requisitos previos

- Python 3.10+
- Dependencias: `pip install -r requirements.txt`

## Configuración (variables de entorno)

- `DATABASE_PATH`: ruta del archivo SQLite (por defecto `./database/lisboa360.db`).
- `GEOJSON_DIR`: directorio de capas GeoJSON (por defecto `./data/geojson`).
- `SERVER_HOST` / `SERVER_PORT`: dirección y puerto del backend (por defecto `127.0.0.1:5000`).
- `ALLOWED_ORIGINS`: orígenes permitidos para CORS (por defecto `http://localhost:3000,http://localhost:8080,http://127.0.0.1:8000,http://localhost:8000`).
- `SEED_FICTICIO`: activa (`1`, predeterminado) o desactiva (`0`) el seed de datos ficticios de desarrollo.
- `FLASK_ENV` / `FLASK_DEBUG`: configuración de ejecución (por defecto `development`/`1`).

## Ejecución

Desde la raíz del repositorio:

```bash
python app.py
```

El servidor escucha en `127.0.0.1:5000` y expone los endpoints versionados bajo `/api/v1`.

## Datos ficticios de desarrollo

- `app/db/seed.py` inserta registros ficticios claramente identificados con prefijo 'Ejemplo ficticio'
  (barrio Lisboa, lugares, equipamientos, espacios públicos, movilidad y capas geográficas).
- `data/geojson/ejemplo_ficticio_capa_general.geojson` contiene features ficticias con geometrías
  Point, LineString y Polygon.
- No se presentan datos de ejemplo como información real del barrio Lisboa.

## Estructura del código (enfoque en arquitectura)

1. `app/db/connection.py`: conexión SQLite por aplicación (`check_same_thread=False`, `Row` factory,
   `PRAGMA foreign_keys = ON`); `init_db()` crea el esquema y aplica el seed.
2. `app/db/schema.sql`: esquema de las tablas `barrio`, `lugar`, `equipamiento`, `espacio_publico`,
   `movilidad` y `capa_geografica` con FKs y índices.
3. `app/models/*.py`: dataclasses por entidad (mapeo de filas SQLite).
4. `app/repositories/*.py`: consultas SQL directas contra SQLite (DAO).
5. `app/services/*.py`: lógica de negocio por recurso (validación, paginación, transformación).
6. `app/routes/*.py`: blueprints (`/api/v1/...`) con respuestas JSON y manejo de errores.
7. `app/utils/errors.py`: manejo centralizado de errores en JSON estandarizado.
8. `app/utils/validation.py` / `app/utils/geojson.py`: validadores de parámetros y estructuras GeoJSON.

## Pruebas

Desde la raíz del repositorio:

```bash
python -m pytest tests/ -v
```

## Próximos pasos (planificación)

- Implementar pruebas de contratos OpenAPI en cada endpoint.
- Documentar advertencias de retención de datos si se aplica.
- Evaluar advertencias de observabilidad y seguridad para la Fase 3.


## Fase 4 — Integración y pruebas funcionales (22 Nov 2026)

Bugs detectados y corregidos (Parte A — integración backend):

1. **Bug: `GET /api/v1/espacios-publicos?categoria=...` devolvía 500**
   (`sqlite3.OperationalError: no such column: categoria`; `row["categoria"]` → `IndexError`).
   Raíz: `CREATE TABLE IF NOT EXISTS` no migra; la columna faltaba en `espacio_publico`.
   Correcciones aplicadas:
   - `app/db/schema.sql`: columna `categoria` (TEXT) añadida a `espacio_publico`.
   - `app/db/seed.py`: INSERT de espacios públicos ficticios con `categoria` (Plaza: plaza; Parque: parque).
   - `openapi.yaml` (repo `lisoba360-api`): esquema `EspacioPublico` añade `categoria`.
   - Coherencia backend: `models/espacio_publico.py` (`categoria` en el dataclass), `repositories/espacio_publico_repository.py` (`categoria=row["categoria"]`), `services/espacio_publico_service.py` (`"categoria": espacio_publico.categoria` en la respuesta).

2. **CORS ampliado**: `ALLOWED_ORIGINS` por defecto ahora:
   `http://localhost:3000,http://localhost:8080,http://127.0.0.1:8000,http://localhost:8000`
   (orígenes del frontend `lisoba360-frontend` en desarrollo local).

Verificación (Parte A): `lisoba360_back_check.py` (script de verificación en Documents — temporal) — **5/5 secciones OK**: url_map vs openapi, estructuras de respuesta, filtros/paginación/errores, GeoJSON.

Tests (Parte A): `py -m pytest tests/ -q` → **39 passed**.
