# Visualizaciones — Fase 16 (Lisboa360)

## 1. Visualizaciones generadas

Ubicación: `data/analysis/fase16/` (copiadas a `docs/analisis_territorial_fase16/evidencias/`).

| Archivo | Descripción | Método |
|---------|-------------|--------|
| `mapa_suba_pistas_escenarios.png` | Mapa combinado: límite de Suba (rojo), pistas (naranja) y escenarios (verde). Distingue features dentro/fuera de Suba. | geopandas + matplotlib |
| `mapa_pistas_suba.png` | Distribución de las 429 pistas recreativas (naranja) sobre Suba (rojo). | geopandas + matplotlib |
| `mapa_escenarios_suba.png` | Distribución de los 57 escenarios deportivos (verde) sobre Suba (rojo). | geopandas + matplotlib |
| `grafico_conteos_suba.png` | Gráfico de barras con conteos totales y en Suba. | matplotlib |

## 2. Simbología

- Límite de Suba: contorno rojo (`#c0392b`).
- Pistas: naranja (`#e67e22`).
- Escenarios: verde (`#27ae60`).
- Features dentro de Suba: tonos más oscuros.

## 3. Limitaciones

- Las visualizaciones son exploratorias y no representan cobertura del barrio Lisboa.
- La geometría de Suba se reconstruyó en memoria como Polygon (no se modificó el archivo).
- No se realizaron análisis de distancia, densidad ni accesibilidad.

## Conclusión

**Visualizaciones: APROBADAS** (4 mapas/gráficos generados).
