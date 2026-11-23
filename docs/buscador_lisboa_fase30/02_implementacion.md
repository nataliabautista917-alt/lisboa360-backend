# Implementación — Fase 30 (Lisboa360)

## 1. Archivos modificados

- `js/ui.js`: tarjeta "Buscar" con input y contenedor de resultados en `mountSidebar()`.
- `js/main.js`: función `setupBuscador()`, `getItemName()`, `getItemCategory()`, `escHtml()`.

## 2. Funcionamiento

- Al escribir, se filtran los items de todas las capas cargadas.
- Los resultados se muestran en una lista clicables.
- Al seleccionar, se llama a `showInfoForItem()` que abre el panel y centra el mapa.

## 3. Restricciones cumplidas

- Sin peticiones adicionales al backend.
- Sin modificación de GeoJSON ni backend.
- Escape de HTML en resultados.

## Conclusión

**Buscador: IMPLEMENTADO.**
