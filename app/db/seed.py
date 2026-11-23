"""Datos de semilla para desarrollo.

Todos los registros son datos ficticios de desarrollo, claramente marcados con prefijo
'Ejemplo ficticio'. No representan información real del barrio Lisboa.
"""
import json

POLIGONO_LISBOA_FIC = [
    [-74.22, 4.65],
    [-74.21, 4.65],
    [-74.21, 4.66],
    [-74.22, 4.66],
    [-74.22, 4.65],
]

GEOMETRIA_LISBOA = json.dumps(
    {"type": "Polygon", "coordinates": [POLIGONO_LISBOA_FIC]}, ensure_ascii=False
)

BARRIO_NOMBRE = "Lisboa"
BARRIO_DESCRIPCION = "Ejemplo ficticio: barrio Lisboa — datasets territoriales para el conocimiento del barrio."
BARRIO_CREATED_AT = "2026-01-01T00:00:00"

LUGARES_FICTICIOS = [
    {
        "id": 1,
        "nombre": "Ejemplo ficticio: Plaza Central",
        "descripcion": "Ejemplo ficticio: plaza pública del barrio.",
        "categoria": "servicios",
        "observaciones": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.20, 4.65]}, ensure_ascii=False
        ),
        "created_at": "2026-01-01T00:00:01",
    },
    {
        "id": 2,
        "nombre": "Ejemplo ficticio: Complejo cultural",
        "descripcion": "Ejemplo ficticio: espacio dedicado a las artes y la cultura.",
        "categoria": "educación",
        "observaciones": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.21, 4.65]}, ensure_ascii=False
        ),
        "created_at": "2026-01-01T00:00:02",
    },
    {
        "id": 3,
        "nombre": "Ejemplo ficticio: Zona de accesibilidad universal",
        "descripcion": "Ejemplo ficticio: zona del barrio con características de accesibilidad.",
        "categoria": "accesibilidad",
        "observaciones": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.22, 4.66]}, ensure_ascii=False
        ),
        "created_at": "2026-01-01T00:00:03",
    },
]

EQUIPAMENTOS_FICTICIOS = [
    {
        "id": 1,
        "nombre": "Ejemplo ficticio: Centro comunitario",
        "tipo": "saneamiento",
        "descripcion": None,
        "capacidad": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.21, 4.65]}, ensure_ascii=False
        ),
        "estado": "activa",
        "categoria": "saneamiento",
        "created_at": "2026-01-01T00:00:04",
    },
    {
        "id": 2,
        "nombre": "Ejemplo ficticio: Punto de salud",
        "tipo": "salud",
        "descripcion": None,
        "capacidad": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.22, 4.66]}, ensure_ascii=False
        ),
        "estado": "activa",
        "categoria": "salud",
        "created_at": "2026-01-01T00:00:05",
    },
    {
        "id": 3,
        "nombre": "Ejemplo ficticio: Central de emergencias",
        "tipo": "seguridad",
        "descripcion": None,
        "capacidad": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.23, 4.65]}, ensure_ascii=False
        ),
        "estado": "activa",
        "categoria": "seguridad",
        "created_at": "2026-01-01T00:00:06",
    },
]

ESPACIOS_PUBLICOS_FICTICIOS = [
    {
        "id": 1,
        "nombre": "Ejemplo ficticio: Plaza principal",
        "tipo": "plaza",
        "categoria": "plaza",
        "descripcion": None,
        "area_estimada": None,
        "geometria": json.dumps(
            {
                "type": "Polygon",
                "coordinates": [
                    [[-74.20, 4.65], [-74.19, 4.65], [-74.19, 4.66], [-74.20, 4.66], [-74.20, 4.65]]
                ],
            },
            ensure_ascii=False,
        ),
        "estado": "activa",
        "created_at": "2026-01-01T00:00:07",
    },
    {
        "id": 2,
        "nombre": "Ejemplo ficticio: Parque de recreación",
        "tipo": "parque",
        "categoria": "parque",
        "descripcion": None,
        "area_estimada": None,
        "geometria": None,
        "estado": "activa",
        "created_at": "2026-01-01T00:00:08",
    },
]

MOVILIDAD_FICTICIA = [
    {
        "id": 1,
        "tipo": "parada_transporte_publico",
        "nombre": "Ejemplo ficticio: Parada de transporte público",
        "descripcion": None,
        "capacidad": None,
        "geometria": json.dumps(
            {"type": "Point", "coordinates": [-74.21, 4.67]}, ensure_ascii=False
        ),
        "estado": "activa",
        "created_at": "2026-01-01T00:00:09",
    },
    {
        "id": 2,
        "tipo": "ciclovia",
        "nombre": "Ejemplo ficticio: Ruta de ciclovía",
        "descripcion": None,
        "capacidad": None,
        "geometria": json.dumps(
            {
                "type": "LineString",
                "coordinates": [[-74.22, 4.65], [-74.22, 4.66], [-74.23, 4.66]],
            },
            ensure_ascii=False,
        ),
        "estado": "activa",
        "created_at": "2026-01-01T00:00:10",
    },
]

CAPAS_GEOGRAFICAS_FICTICIAS = [
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
    },
]

CAPAS_GEOGRAFICAS_REALES = [
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
    },
    {
        "id": 3,
        "nombre": "Escenario Deportivo en Parque (IDRD)",
        "tipo": "escenario_deportivo",
        "descripcion": "Escenarios deportivos en parques de Bogotá D.C. (coliseos, estadios, polideportivos). Fuente: IDRD. Cobertura distrital.",
        "formato": "GeoJSON",
        "ruta_archivo": "parques_escenario_deportivo_idrd_2026_procesado.geojson",
        "fecha_generacion": "2026-11-22",
        "estado": "activa",
        "tipo_geometria": "MultiPolygon",
    },
    {
        "id": 4,
        "nombre": "Delimitación Localidad de Suba (SDP/IDECA)",
        "tipo": "localidad",
        "descripcion": "Delimitación territorial oficial de la localidad de Suba, Bogotá D.C. (código 11). Fuente: Secretaría Distrital de Planeación / IDECA. Contexto administrativo, no límite del barrio Lisboa.",
        "formato": "GeoJSON",
        "ruta_archivo": "localidad_suba_limite_oficial.geojson",
        "fecha_generacion": "2026-11-22",
        "estado": "activa",
        "tipo_geometria": "Polígono",
    },
]


CAPAS_GEOGRAFICAS_LISBOA = [
    {
        "id": 5,
        "nombre": "Limite oficial del barrio Lisboa",
        "tipo": "territorial",
        "descripcion": "Limite territorial oficial del barrio Lisboa (barrio legalizado, codigo LEG01324), localidad de Suba, Bogota D.C. Fuente: Secretaria Distrital de Planeacion (dataset Barrio legalizado. Bogota D.C.). Licencia CC-BY-4.0. Reproyectado a EPSG:4326 en Fase 20.",
        "formato": "GeoJSON",
        "ruta_archivo": "barrio_lisboa_limite_oficial_4326.geojson",
        "fecha_generacion": "2026-11-22",
        "estado": "activa",
        "tipo_geometria": "Polygon",
    },
]


CAPAS_GEOGRAFICAS_TRANSPORTE = [
    {
        "id": 6,
        "nombre": "Paraderos SITP (TransMilenio/SDM)",
        "tipo": "transporte",
        "descripcion": "Paraderos zonales del SITP en el entorno del barrio Lisboa (radio ~1.5 km). Fuente: TransMilenio S.A. / Secretaria Distrital de Movilidad. Licencia CC BY 4.0.",
        "formato": "GeoJSON",
        "ruta_archivo": "paraderos_sitp_lisboa_area.geojson",
        "fecha_generacion": "2026-11-22",
        "estado": "activa",
        "tipo_geometria": "Point",
    },
]


CAPAS_GEOGRAFICAS_LUGARES = [
    {
        "id": 7,
        "nombre": "Lugares de interes (OSM)",
        "tipo": "lugares_interes",
        "descripcion": "Lugares de interes del entorno de Lisboa (colegios, parques, iglesias, comercio, biblioteca) segun OpenStreetMap (ODbL 1.0).",
        "formato": "GeoJSON",
        "ruta_archivo": "lugares_interes_lisboa_osm.geojson",
        "fecha_generacion": "2026-11-22",
        "estado": "activa",
        "tipo_geometria": "Point",
    },
]



def seed(conn, enabled=True):
    """Inserta los datos ficticios de desarrollo (idempotente)."""
    if not enabled:
        return

    conn.execute(
        "INSERT OR IGNORE INTO barrio (id, nombre, descripcion, geometria, created_at) "
        "VALUES (1, ?, ?, ?, ?)",
        (BARRIO_NOMBRE, BARRIO_DESCRIPCION, GEOMETRIA_LISBOA, BARRIO_CREATED_AT),
    )

    for lugar in LUGARES_FICTICIOS:
        conn.execute(
            "INSERT OR IGNORE INTO lugar "
            "(id, nombre, descripcion, categoria, observaciones, geometria, barrio_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, 1, ?)",
            (
                lugar["id"],
                lugar["nombre"],
                lugar["descripcion"],
                lugar["categoria"],
                lugar["observaciones"],
                lugar["geometria"],
                lugar["created_at"],
            ),
        )

    for equipamiento in EQUIPAMENTOS_FICTICIOS:
        conn.execute(
            "INSERT OR IGNORE INTO equipamiento "
            "(id, nombre, tipo, descripcion, capacidad, geometria, estado, categoria, barrio_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, ?)",
            (
                equipamiento["id"],
                equipamiento["nombre"],
                equipamiento["tipo"],
                equipamiento["descripcion"],
                equipamiento["capacidad"],
                equipamiento["geometria"],
                equipamiento["estado"],
                equipamiento["categoria"],
                equipamiento["created_at"],
            ),
        )

    for espacio_publico in ESPACIOS_PUBLICOS_FICTICIOS:
        conn.execute(
            "INSERT OR IGNORE INTO espacio_publico "
            "(id, nombre, tipo, descripcion, area_estimada, geometria, estado, categoria, barrio_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, ?)",
            (
                espacio_publico["id"],
                espacio_publico["nombre"],
                espacio_publico["tipo"],
                espacio_publico["descripcion"],
                espacio_publico["area_estimada"],
                espacio_publico["geometria"],
                espacio_publico["estado"],
                espacio_publico["categoria"],
                espacio_publico["created_at"],
            ),
        )

    for elemento in MOVILIDAD_FICTICIA:
        conn.execute(
            "INSERT OR IGNORE INTO movilidad "
            "(id, tipo, nombre, descripcion, capacidad, geometria, estado, barrio_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?)",
            (
                elemento["id"],
                elemento["tipo"],
                elemento["nombre"],
                elemento["descripcion"],
                elemento["capacidad"],
                elemento["geometria"],
                elemento["estado"],
                elemento["created_at"],
            ),
        )

    for capa in CAPAS_GEOGRAFICAS_FICTICIAS:
        conn.execute(
            "INSERT OR IGNORE INTO capa_geografica "
            "(id, nombre, tipo, descripcion, formato, ruta_archivo, fecha_generacion, estado, tipo_geometria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                capa["id"],
                capa["nombre"],
                capa["tipo"],
                capa["descripcion"],
                capa["formato"],
                capa["ruta_archivo"],
                capa["fecha_generacion"],
                capa["estado"],
                capa["tipo_geometria"],
            ),
        )

    for capa in CAPAS_GEOGRAFICAS_REALES:
        conn.execute(
            "INSERT OR IGNORE INTO capa_geografica "
            "(id, nombre, tipo, descripcion, formato, ruta_archivo, fecha_generacion, estado, tipo_geometria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                capa["id"],
                capa["nombre"],
                capa["tipo"],
                capa["descripcion"],
                capa["formato"],
                capa["ruta_archivo"],
                capa["fecha_generacion"],
                capa["estado"],
                capa["tipo_geometria"],
            ),
        )

    # Capa real adicional: límite oficial del barrio Lisboa (Fase 20/22).
    for capa in CAPAS_GEOGRAFICAS_LISBOA:
        conn.execute(
            "INSERT OR IGNORE INTO capa_geografica "
            "(id, nombre, tipo, descripcion, formato, ruta_archivo, fecha_generacion, estado, tipo_geometria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                capa["id"],
                capa["nombre"],
                capa["tipo"],
                capa["descripcion"],
                capa["formato"],
                capa["ruta_archivo"],
                capa["fecha_generacion"],
                capa["estado"],
                capa["tipo_geometria"],
            ),
        )


    # Capa real adicional: paraderos SITP (Fase 28).
    for capa in CAPAS_GEOGRAFICAS_TRANSPORTE:
        conn.execute(
            "INSERT OR IGNORE INTO capa_geografica "
            "(id, nombre, tipo, descripcion, formato, ruta_archivo, fecha_generacion, estado, tipo_geometria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                capa["id"],
                capa["nombre"],
                capa["tipo"],
                capa["descripcion"],
                capa["formato"],
                capa["ruta_archivo"],
                capa["fecha_generacion"],
                capa["estado"],
                capa["tipo_geometria"],
            ),
        )


    # Capa real adicional: lugares de interes (Fase 29).
    for capa in CAPAS_GEOGRAFICAS_LUGARES:
        conn.execute(
            "INSERT OR IGNORE INTO capa_geografica "
            "(id, nombre, tipo, descripcion, formato, ruta_archivo, fecha_generacion, estado, tipo_geometria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                capa["id"],
                capa["nombre"],
                capa["tipo"],
                capa["descripcion"],
                capa["formato"],
                capa["ruta_archivo"],
                capa["fecha_generacion"],
                capa["estado"],
                capa["tipo_geometria"],
            ),
        )

    conn.commit()
