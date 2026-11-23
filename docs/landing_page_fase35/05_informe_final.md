# Informe final — Fase 35 (Lisboa360)

## Resumen
Se implementó una **landing page institucional** en `index.html` y se movió el mapa interactivo existente a `mapa.html`, preservando su funcionalidad.

## Entregables
- Landing: hero, qué es, qué puedes encontrar, datos reales, CTA al mapa, fuentes y footer.
- Navegación: `/` inicio, `/mapa.html` mapa; nav Inicio/Mapa en el header del mapa.
- Diseño: Inter, paleta verde/azul, tarjetas, responsive CSS.

## Conservación del mapa
- 7 datasets reales registrados (capa ficticia id=1 oculta en UI, como en Fase 32).
- Explorador territorial, búsqueda, toggles, leyenda, iconos, panel informativo, centrar Lisboa: conservados.
- `setupBuscador()` restaurado.

## Pruebas
- `node --check`: OK.
- `pytest`: 39 passed.
- Headless Edge: landing y mapa cargan correctamente; mapa sin banner y con 6 capas.

## Limitaciones
- Sin verificación visual manual/responsive/capturas PNG.
- Imágenes fotográficas externas no embebidas; se usó hero visual con gradiente/SVG (diseño limpio, sin dependencia rota crítica).

## Estado final
**APROBADO CON OBSERVACIONES.** Landing implementada y mapa preservado.

Me detengo aquí y espero revisión y autorización. No inicio una nueva fase automáticamente.