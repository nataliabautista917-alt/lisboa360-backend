# Implementación — Fase 35 (Lisboa360)

## Archivos creados/modificados
- `lisboa360-frontend/index.html` — **nueva landing page** (reemplaza la entrada directa al mapa).
- `lisboa360-frontend/mapa.html` — **mapa interactivo anterior** (copiado del antiguo `index.html`, funcionalidad preservada).
- `lisboa360-frontend/css/landing.css` — estilos de landing, responsive.
- `lisboa360-frontend/js/landing.js` — menú móvil y efecto scroll del header.
- `lisboa360-frontend/js/ui.js` — header del mapa con nav Inicio/Mapa.
- `lisboa360-frontend/css/styles.css` — estilos `.top-nav` para el header del mapa.
- `lisboa360-frontend/js/main.js` — restaurado `setupBuscador()` para conservar búsqueda general.

## Decisiones
- Se separó landing (`index.html`) del mapa (`mapa.html`) para no duplicar lógica GIS.
- No se modificaron GeoJSON, SQLite, OpenAPI, endpoints ni backend.
- El mapa conserva capas, explorador, buscador, filtros, toggles, leyenda, panel informativo y centrado en Lisboa.