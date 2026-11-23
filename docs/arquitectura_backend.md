# Arquitectura del Backend (lisboa360-backend)

## 1. Estructura de la aplicación Flask

```
lisboa360-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # create_app, configuración (host, puerto, db path)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── barrio_routes.py     # GET /api/v1/barrios/lisboa
│   │   ├── capas_routes.py      # GET /api/v1/capas, GET /api/v1/capas/{capaId}/geojson
│   │   ├── lugares_routes.py    # GET /api/v1/lugares
│   │   ├── equipamientos_routes.py   # GET /api/v1/equipamientos
│   │   ├── espacios_publicos_routes.py  # GET /api/v1/espacios-publicos
│   │   ├── movilidad_routes.py  # GET /api/v1/movilidad
│   │   └── errors.py            # Manejo de errores estandarizado
│   ├── services/
│   │   ├── __init__.py
│   │   ├── barrio_service.py
│   │   ├── capas_service.py
│   │   ├── lugares_service.py
│   │   ├── equipamientos_service.py
│   │   ├── espacios_publicos_service.py
│   │   ├── movilidad_service.py
│   │   └── geo_utils.py         # Utilidades de validación de GeoJSON
│   ├── models/
│   │   ├── __init__.py
│   │   ├── barrio.py
│   │   ├── lugar.py
│   │   ├── equipamiento.py
│   │   ├── espacio_publico.py
│   │   ├── movilidad.py
│   │   └── capa_geografica.py
│   └── db/
│       ├── __init__.py
│       ├── connection.py        # Conexión SQLite y caché de conexiones
│       └── schema.sql           # Esquema de SQLite de los seis tablas
├── data/
│   └── geojson/                 # Archivos GeoJSON de capas (futuro: ingesta de capas)
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_services.py
├── requirements.txt
└── README.md
```

## 2. Lógica de negocio: Servicios

Un módulo de servicio por recurso. Cada servicio contiene:

1. **Validación de entradas:** tipos, rangos y parámetros obligatorios (de acuerdo al contrato OpenAPI).
2. **Filtrado y paginación:** aplicación de `limite` y `offset` y de filtros (`q`, `categoria`, `tipo`).
3. **Orquestación del acceso a datos:** llamada al modelo/DAO correspondiente.
4. **Transformación de respuestas:** conversión de registros a esquemas JSON según el contrato OpenAPI.
5. **Manejo de excepciones:** envío de errores al flujo de manejo estandarizado.

## 3. Acceso a datos: Modelos/DAO

- `app/models/*.py`: funciones de DAO por entidad (`select_barrio_lisboa`, `list_lugares(limite, offset, q, categoria)`, `count_lugares`, etc.).
- Cada función ejecuta SQL con parámetros parametrizados (no interpolación) contra SQLite.
- `app/db/connection.py`: conexión global: `sqlite3.connect(DATABASE_PATH, check_same_thread=False)`, `Row` factory, `PRAGMA foreign_keys = ON`.
- Consultas con `JOIN` para resolver relaciones (ej.: espacios públicos con `barrio_id`).

## 4. Manejo de errores estandarizado

| Código HTTP | Código de error | Descripción |
|---|---|---|
| 200 | `OK` | Éxito en consultas. |
| 400 | `VALIDATION_ERROR` | Parámetros inválidos en query o path. |
| 404 | `NOT_FOUND` | Recurso no encontrado. |
| 422 | `UNPROCESSABLE_ENTITY` | Parámetros procesables pero no válidos. |
| 500 | `INTERNAL_ERROR` | Error interno no controlado. |

Todas las respuestas de error usan el esquema `ErrorResponse` definido en `lisboa360-api/openapi.yaml`.

## 5. Pruebas

- **Pruebas unitarias (pytest):** `tests/test_services.py` — validación de servicios con base de datos en memoria.
- **Pruebas de rutas:** `tests/test_routes.py` — cliente de prueba de Flask validando contratos de respuesta y códigos HTTP.
- **Datos de prueba:** seeds ficticios, claramente marcados como datos de desarrollo, usados solo en pruebas. No se ingresa información real del barrio Lisboa.
