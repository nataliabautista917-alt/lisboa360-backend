# Auditoría frontend — Integración GIS (Fase 13)

## 1. Componentes auditados

`js/main.js`, `js/layers.js`, `js/ui.js`, `js/api.js`, `js/map.js`, `js/config.js`, `index.html`, `css/styles.css`.

## 2. Carga dinámica de capas

- `Api.listCapas()` se invoca **una sola vez** en `boot()` (`main.js`).
- Por cada capa se llama `mountCapaLayer(capa, def.style, def.toDisplay)` → `Api.getCapaGeojson(id)` **una sola vez**.
- El toggle solo agrega/remueve el `L.featureGroup` ya cargado: **sin solicitudes adicionales**.
- Verificado por inspección de código: OK.

## 3. Visualización de capas

| Capa | Features | Geometría | Estilo | Estado |
|------|----------|-----------|--------|--------|
| Ficticia id=1 | 3 | Point, Polygon, LineString | ámbar (`--layer-capas`) | OK (preexistente) |
| Pistas IDRD id=2 | 429 | MultiPolygon | naranja `#e67e22` | OK (código) |
| Escenarios IDRD id=3 | 57 | MultiPolygon | verde `#27ae60` | OK (código) |
| Suba id=4 | 1 | MultiPolygon | rojo translúcido `#c0392b` | OK (código) |

La compatibilidad con geometrías GeoJSON está implementada en `geometriaToLeaflet()`: Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollection.

## 4. Toggles, leyenda y estados

- `buildLayerToggle()` crea checkbox + swatch + label + count + badge + estado por capa.
- `setLayerVisible()` agrega/remueve el grupo del mapa.
- `onLayerToggle()` re-renderiza la leyenda con `layerHandles` dinámicos.
- Indicador de carga: `setLayerState(def,'loading')` antes de la petición; se limpia al terminar; «Sin datos — error de conexión» si falla.
- Leyenda: `legendEntries(extraDefs)` incluye estáticas + dinámicas; `faded` cuando está oculta.

## 5. Panel informativo

- `showInfo()` construye atributos filtrando `undefined`/`null`/`''`/objetos.
- Todo se escapa con `esc()` (prevención de HTML inseguro).
- Muestra origen, dataset, licencia, atribución y nota CRS para capas reales.
- `centerMap()` centra usando `L.geoJson(geometry).getBounds()`.

## 6. Escapado y seguridad

- `esc()` aplica escape de `& < > " '`.
- No se usa `innerHTML` con valores sin escapar (verificado por inspección).
- No se exponen rutas internas del servidor (el frontend solo conoce `/api/v1/...`).

## 7. Responsive

- CSS usa `max-width: calc(100% - 16px)` en el panel y layout flexible.
- No se modificó el diseño base; se añadieron estilos puntuales.
- **No se ejecutó en navegador**: responsive no verificado visualmente.

## 8. Pruebas visuales

**NO EJECUTADO** — no se dispuso de navegador en el entorno de verificación. Se documenta expresamente.

## 9. Assets

Todos los recursos (HTML, CSS, JS, Leaflet) responden HTTP 200 desde un servidor estático local.

## Conclusión

**Frontend: APROBADO CON OBSERVACIONES** (pruebas visuales no ejecutadas).
