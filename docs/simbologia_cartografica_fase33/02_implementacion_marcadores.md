# Implementación de marcadores — Fase 33 (Lisboa360)

## 1. Cambios en `js/layers.js`

- `pointMarker(coords, style, iconSvg)`: usa `L.divIcon` con SVG cuando `iconSvg` está presente; fallback a `circleMarker`.
- `geometriaToLeaflet(feature, style, iconSvg)`: propaga `iconSvg`.
- `addItemsToMap()`: calcula `iconSvg` por item usando `def.icon(item)`.

## 2. Cambios en `js/main.js`

- Constante `GIS_ICONS` con SVGs temáticos.
- Función `svgForCapa(capaId, item)` que selecciona el icono según la capa y la categoría.
- `buildDynamicCapaDef()` asigna `def.icon`.

## 3. CSS

- `.gis-marker-wrap`, `.gis-marker`, `.gis-marker svg` en `styles.css`.

## Conclusión

**Marcadores temáticos: IMPLEMENTADOS.**
