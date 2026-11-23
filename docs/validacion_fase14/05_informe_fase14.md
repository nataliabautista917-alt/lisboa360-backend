# Informe consolidado — Fase 14 (Lisboa360)

## 1. Auditoría inicial

Se inspeccionó la estructura del frontend y backend, el flujo de carga de capas, toggles, leyenda, panel, badges, rutas y endpoints. Se verificó que existían pruebas automatizadas (39) y documentación previa. Se identificaron Microsoft Edge (headless) como navegador disponible y Node.js/Python para validaciones.

## 2. Herramientas disponibles

- Microsoft Edge 157/158 (headless) — screenshots y dump-dom.
- Node.js v26.13.1 — validación de sintaxis y estructura GeoJSON.
- Python 3.14.7 + Flask 3.1.3 + pytest 9.2.0 (venv auxiliar) — backend y tests.

## 3. Pruebas visuales realizadas

- Render headless a 1366×768: OK, sin errores críticos, todas las capas renderizadas.
- Pruebas visuales humanas: NO EJECUTADO.
- Responsive 1280/768/390: NO EJECUTADO (solo 1366×768).

## 4. Resultados funcionales de las cuatro capas

- Capa 1 (ficticia): APROBADO.
- Capa 2 (pistas IDRD): APROBADO.
- Capa 3 (escenarios IDRD): APROBADO.
- Capa 4 (Suba): APROBADO CON OBSERVACIONES (CRS pendiente).

## 5. Validación responsive

**NO EJECUTADO** (solo 1366×768 renderizado).

## 6. Resultados de API y pytest

- pytest: 39/39 pasan.
- 6 endpoints verificados (HTTP 200/404 correctos).
- GeoJSON válido en las 4 capas.

## 7. Auditoría de atribución y licencias

- IDRD atribuido correctamente (CC-BY-4.0 / CC-BY-SA-4.0).
- Suba atribuido a SDP/IDECA (CC-BY-4.0).
- IDPC no se presenta como capa activa.
- Procedencia visible en el panel informativo.
- **APROBADO.**

## 8. Problemas encontrados

1. GeoJSON de Suba declara `MultiPolygon` pero tiene estructura de `Polygon` → provocaba error de renderizado. **Corregido en frontend** (normalización robusta, sin modificar el archivo GIS).
2. Sin pruebas visuales humanas ni responsive en móvil/tablet.

## 9. Correcciones aplicadas

- `js/layers.js`: normalización de MultiPolygon con estructura de Polygon (Suba).
- Documentación de la inconsistencia en docs.

No se modificaron datos, backend, SQLite, OpenAPI ni arquitectura.

## 10. Archivos creados o modificados

Creados en `lisboa360-backend/docs/validacion_fase14/`:
- `01_auditoria_visual.md`
- `02_validacion_funcional_capas.md`
- `03_validacion_responsive.md`
- `04_regresion_api.md`
- `05_informe_fase14.md`

Modificado:
- `lisboa360-frontend/js/layers.js` (corrección de robustez).

## 11. Limitaciones pendientes

- Pruebas visuales humanas no realizadas.
- Responsive en tablet/móvil no verificado.
- CRS de Suba sin verificación autoritativa.
- Sin límite oficial del barrio Lisboa.

## 12. Estado general

**APROBADO CON OBSERVACIONES.**

## 13. Recomendaciones para la siguiente fase

1. Realizar validación visual humana en navegador.
2. Verificar responsive en tablet/móvil (768×1024, 390×844).
3. Resolver CRS de Suba con fuente autoritativa.
4. Obtener límite oficial del barrio Lisboa.
5. Corregir el tipo de geometría del GeoJSON de Suba (`MultiPolygon` → `Polygon`) en un paso autorizado de mantenimiento de datos.

Me detengo aquí y espero revisión y autorización.
