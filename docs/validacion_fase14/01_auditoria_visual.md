# Auditoría visual — Fase 14 (Lisboa360)

## 1. Entorno de pruebas

- SO: Windows.
- Navegador disponible: Microsoft Edge 157/158 (headless).
- Herramientas: Edge `--headless=new` con `--dump-dom` y `--screenshot`.
- Frontend servido en `http://127.0.0.1:8000`, backend en `http://127.0.0.1:5000`, conectados vía `?api_url=`.
- CORS configurado para `127.0.0.1:8000`.

## 2. Resoluciones evaluadas

| Resolución | Método | Resultado |
|------------|--------|-----------|
| 1366 × 768 | Headless Edge `--window-size=1366,768` + screenshot | Renderizado OK, sin errores |
| 1280 × 720 | No evaluado individualmente | NO EJECUTADO |
| 768 × 1024 | No evaluado individualmente | NO EJECUTADO |
| 390 × 844 | No evaluado individualmente | NO EJECUTADO |

Solo se capturó screenshot a 1366×768. Las demás resoluciones quedan pendientes de verificación manual.

## 3. Resultados visuales (verificados por DOM renderizado)

- Mapa base OpenStreetMap cargó correctamente (tiles visibles en el DOM).
- Las 4 capas se renderizaron: capa 1 (ámbar), capa 2 (naranja, 429), capa 3 (verde, 57), capa 4 (rojo, 1).
- Badges «Real»/«Ficticio» presentes en los toggles.
- Leyenda con entradas estáticas + dinámicas, con puntos de color.
- Panel informativo inicialmente oculto (`hidden`), sin superposiciones.
- `global-banner` sin mensaje de error (vacío).
- `backend-status`: «Backend conectado».
- Sin errores críticos en la consola capturada (solo un aviso de task_manager no relacionado).

## 4. Problemas encontrados

- **Defecto real detectado y corregido:** el GeoJSON de Suba declara `type: "MultiPolygon"` pero su estructura de coordenadas es la de un `Polygon` (un único anillo). Esto provocaba `Cannot read properties of undefined (reading '0')` en `layers.js` y impedía cargar la capa 4. Se corrigió en el frontend con normalización robusta (sin modificar el archivo GIS).
- El resto de la UI no presentó defectos visibles en el render headless.

## 5. Pruebas no ejecutadas

- Inspección visual humana de colores/contraste.
- Responsive en tablet/móvil (solo 1366×768 capturado).
- Interacción manual (clics, toggles, panel).

## Conclusión

**Auditoría visual: APROBADO CON OBSERVACIONES** (render headless sin errores; validación humana pendiente).
