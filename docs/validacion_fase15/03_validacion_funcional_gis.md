# Validación funcional GIS — Fase 15 (Lisboa360)

## 1. Capas verificadas (render headless)

| Capa | ID | Features | Estado en DOM | Toggle | Badge |
|------|----|----------|---------------|--------|-------|
| Ficticia | 1 | 3 | OK | OK | Ficticio |
| Pistas IDRD | 2 | 429 | OK | OK | Real |
| Escenarios IDRD | 3 | 57 | OK | OK | Real |
| Suba | 4 | 1 | OK (tras corrección) | OK | Real |

## 2. Corrección de geometría de Suba

- Archivo: `lisboa360-frontend/js/layers.js`, función `geometriaToLeaflet()`, caso `MultiPolygon`.
- Problema: el GeoJSON de Suba declara `type: "MultiPolygon"` pero su estructura de coordenadas es la de un `Polygon` (un único anillo). Esto causaba `Cannot read properties of undefined (reading '0')`.
- Corrección: normalización robusta que detecta cuando `polys[0][0]` es un array de números y envuelve en un polígono. **No se modificó el archivo GIS.**
- Verificación: dump-dom confirmó que la capa 4 ahora carga sin error y el banner queda vacío.

## 3. Funcionalidades verificadas

- Activación/desactivación: OK (sin nuevas peticiones).
- Múltiples capas simultáneas: OK (4 capas activas en el render).
- Leyenda sincronizada: OK.
- Panel informativo: OK (atributos escapados).
- Manejo de geometrías Polygon y MultiPolygon: OK.
- Comportamiento ante errores: OK (estado «Sin datos — error de conexión»).

## 4. Inconsistencia de datos documentada

El archivo `localidad_suba_limite_oficial.geojson` tiene `geometry.type = "MultiPolygon"` pero estructura de `Polygon`. Requiere mantenimiento de datos autorizado para corregir el tipo. No se realizó en esta fase por restricción.

## Conclusión

**Validación funcional GIS: APROBADO.**
