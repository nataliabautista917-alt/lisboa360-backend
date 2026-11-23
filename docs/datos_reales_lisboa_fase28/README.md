# Datos reales del barrio Lisboa — Fase 28 (Lisboa360)

## Fuentes

- Paraderos SITP: TransMilenio S.A. / Secretaría Distrital de Movilidad (ArcGIS REST MapServer, CC BY 4.0). 74 paraderos en el entorno de Lisboa (radio ~1.5 km).
- Lugares de interés: no se integraron datos adicionales verificables en esta fase.

## Archivos creados

- `data/raw/transporte/paraderos_sitp_lisboa_area.geojson` (74 features, Point, EPSG:4326).
- `data/raw/transporte/paraderos_sitp_lisboa_area.csv`.
- `data/geojson/paraderos_sitp_lisboa_area.geojson` (servido por el backend).
- `app/db/seed.py` — nueva capa id=6 "Paraderos SITP (TransMilenio/SDM)".

## Frontend

- `js/main.js`: estilo (azul oscuro), toDisplay, origin/licencia/atribución para id=6.
- `css/styles.css`: variable `--layer-paraderos`.

## Pruebas

- pytest: 39/39 pasan.
- Sintaxis JS: OK.
- Headless Edge: 6 capas cargadas sin error, paraderos toggle presente.

## Limitaciones

- Los paraderos son zonales (no troncales). No se incluyeron rutas verificables.
- No se integraron lugares de interés reales (colegios, salud, iglesias) por falta de datasets verificados en esta fase.
- La capa ficticia (id=1) se mantiene.

## Conclusión

**Paraderos SITP integrados como capa real (id=6).** La aplicación ahora muestra datos reales de transporte público en el entorno de Lisboa.
