# Diseño del buscador — Fase 30 (Lisboa360)

## 1. Componentes

- Input `#search-general` en la barra lateral (tarjeta "Buscar").
- Contenedor `#search-results` para resultados.
- Búsqueda en tiempo real con debounce de 200 ms.

## 2. Fuentes de datos

El buscador itera sobre `layerHandles` (7 capas) y sus items cargados. No realiza peticiones adicionales al backend.

## 3. Campos de búsqueda

Nombre, categoría, dirección (según disponibilidad en cada dataset).

## 4. Resultados

Máximo 50 resultados. Clic en un resultado abre el panel informativo y centra el mapa.
