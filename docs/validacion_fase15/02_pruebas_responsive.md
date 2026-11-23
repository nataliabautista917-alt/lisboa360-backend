# Pruebas responsive — Fase 15 (Lisboa360)

## Resoluciones evaluadas

| Resolución | Estado | Evidencia |
|------------|--------|-----------|
| 1366 × 768 | Render headless OK | dump-dom + screenshot |
| 768 × 1024 | NO EJECUTADO | Captura falló |
| 390 × 844 | Captura válida (PNG) | Screenshot generado, render temprano |

## CSS responsive existente

`css/styles.css` incluye `@media (max-width: 768px)` con:
- Grid de 1 columna.
- Ocultación de `.brand-text`.
- Menú toggle visible.
- Sidebar colapsable (`#sidebar.open`).
- Panel informativo anclado abajo a ancho completo.
- Mapa con altura ajustada.

## Limitaciones

- No se verificó scroll, superposiciones ni usabilidad en dispositivo real.
- El media query solo cubre `max-width: 768px`; no hay breakpoints específicos para tablet (768–1024) ni móvil pequeño (< 390).

## Conclusión

**Pruebas responsive: NO EJECUTADO** (solo 1366×768 verificado por dump-dom).
