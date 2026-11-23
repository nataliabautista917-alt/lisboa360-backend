# Catálogo de iconos — Fase 33 (Lisboa360)

## Iconos SVG temáticos (blancos sobre círculo de color)

| Categoría | Clave | Color | Descripción |
|-----------|-------|-------|-------------|
| Paraderos SITP | bus | #1f618d | Autobús |
| Educación | escuela | #117864 | Edificio escolar |
| Religioso | iglesia | #117864 | Cruz |
| Espacio público | parque | #117864 | Árbol |
| Comercio y servicios | comercio | #117864 | Tienda |
| Comunitario | comunitario | #117864 | Edificio comunitario |
| Salud | salud | #117864 | Cruz médica |
| Default | default | #7f8c8d | Círculo |

## Implementación

- `GIS_ICONS` en `js/main.js` (SVG inline).
- `svgForCapa(capaId, item)` selecciona el icono según la capa y la categoría del feature.
- `pointMarker()` en `js/layers.js` usa `L.divIcon` con el SVG cuando está disponible.

## Conclusión

**Catálogo: IMPLEMENTADO.**
