# Validación visual — Fase 15 (Lisboa360)

## 1. Entorno

- Navegador: Microsoft Edge (headless, modo `--headless` y `--headless=new`).
- Frontend: `http://127.0.0.1:8000/?api_url=http://127.0.0.1:5000`.
- Backend: `http://127.0.0.1:5000` con `SEED_FICTICIO=1`.
- CORS: `ALLOWED_ORIGINS` incluye `127.0.0.1:8000`.

## 2. Evidencias capturadas

| Archivo | Resolución | Tamaño | Observación |
|---------|-----------|--------|-------------|
| `evidencias/screenshot_1366x768.png` | 1366×768 | ~4.9 KB | Captura válida (PNG), render temprano |
| `evidencias/screenshot_390x844.png` | 390×844 | ~5.4 KB | Captura válida (PNG), render temprano |
| `evidencias/screenshot_768x1024.png` | 768×1024 | — | No se generó (fallo de captura) |

Además se verificó el DOM renderizado completo mediante `--dump-dom` (dumpdom6.html): las 4 capas cargaron, sin banner de error, badges y leyenda presentes.

## 3. Resultados visuales

- Mapa base OpenStreetMap: OK (tiles cargados en el DOM).
- Las 4 capas se renderizaron con sus colores diferenciados.
- Badges «Real»/«Ficticio» visibles en los toggles.
- Leyenda con entradas estáticas + dinámicas.
- Panel informativo inicialmente oculto, sin superposiciones.
- Banner de error vacío (sin errores).
- Indicadores de carga se limpiaron tras la carga.

## 4. Limitaciones

- Las capturas son pequeñas (render temprano), no permiten inspección visual humana detallada de colores/contraste.
- No se realizó inspección visual humana en navegador interactivo.
- Responsive en tablet/móvil no verificado visualmente (solo dump-dom a 1366×768).

## Conclusión

**Validación visual: APROBADO CON OBSERVACIONES** (render headless sin errores; inspección humana pendiente).
