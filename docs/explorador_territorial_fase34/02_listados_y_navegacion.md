# Listados y navegación — Fase 34 (Lisboa360)

## Listados
- Cada categoría renderiza nombres reales desde atributos del GeoJSON/capa cargada.
- `displayName()`: usa `nombre`, `NOMBRE`, `CENEFA`, `Nombre_del_Parque`, `LocNombre`; fallback descriptivo con OBJECTID/id.
- Sin nombres inventados.

## Interacción al seleccionar
1. Si la capa está desactivada, se activa automáticamente (toggle + leyenda actualizados).
2. `showInfoForItem()`: abre panel informativo (`ui.showInfo`), centra mapa (`ui.centerMap`), resalta temporalmente (`ui.highlightGeometry`).
3. Puntos: `setView` zoom 17. Polígonos: `fitBounds` con `maxZoom: 17`.

## Búsqueda
- Filtra por nombre, categoría, tipo, amenity/leisure/shop, parque, tipo de pista/escenario, NOMBRE/CENEFA/VIA/DIRECCION_, OBJECTID/id.
- Actualiza dinámicamente en `input`.

## Conclusión
**Listados y navegación: IMPLEMENTADOS.**