# Integración frontend — Fase 22 (Lisboa360)

## 1. Cambios

- `css/styles.css`: nueva variable `--layer-lisboa: #2874a6`.
- `js/main.js`: rama de estilo y `toDisplay` para Lisboa (id=5); `title`, `origin`, `license`, `attribution`, `crs_note`.
- La carga dinámica existente (`boot()`) recoge automáticamente la nueva capa (id=5) desde `GET /api/v1/capas`.
- `js/layers.js`: ya soportaba Polygon; no se modificó (la geometría de Lisboa es Polygon válido).

## 2. Comportamiento

- Toggle independiente con badge «Real».
- Estilo: borde azul discontinuo (`8,4`), relleno translúcido (0.12).
- Leyenda sincronizada.
- Panel informativo con fuente, dataset, licencia, atribución y nota de CRS.
- Compatible con las capas de pistas, escenarios y Suba.

## 3. Verificación

- Headless Edge: los 5 toggles se renderizaron, estado vacío (sin error), banner sin mensaje de error.
- Sintaxis JS: OK.

## Conclusión

**Integración frontend: COMPLETADA.**
