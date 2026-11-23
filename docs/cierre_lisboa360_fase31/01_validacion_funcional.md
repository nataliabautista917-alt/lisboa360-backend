# Validación funcional — Fase 31 (Lisboa360)

## 1. Componentes verificados

- Backend Flask: 7 capas registradas (ids 1–7).
- Endpoints: `/api/v1/capas` y `/api/v1/capas/{id}/geojson` → HTTP 200 (404 para inexistente).
- Frontend: mapa Leaflet, 7 toggles, leyenda, panel informativo, buscador, explorador deportivo.
- Botón "Centrar en Lisboa": presente.

## 2. Pruebas ejecutadas

- pytest: 39/39 pasan.
- Sintaxis JS: OK (6 módulos).
- Headless Edge: 7 capas cargadas, sin banner de error, buscador y botón presentes.

## 3. Pruebas no ejecutadas

- Interacción manual (clics, filtros, búsqueda) en navegador.
- Responsive en tablet/móvil (visual).
- Capturas de pantalla válidas.

## Conclusión

**Validación funcional: APROBADO CON OBSERVACIONES.**
