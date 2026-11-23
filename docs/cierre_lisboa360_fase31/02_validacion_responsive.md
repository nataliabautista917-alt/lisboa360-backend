# Validación responsive — Fase 31 (Lisboa360)

## Resoluciones evaluadas

| Resolución | Estado | Evidencia |
|------------|--------|-----------|
| 1366 × 768 | Render headless OK | dump-dom |
| 768 × 1024 | NO EJECUTADO | Captura falló |
| 390 × 844 | Captura generada (render temprano) | Screenshot PNG |

## CSS responsive existente

`@media (max-width: 768px)`: grid de 1 columna, sidebar colapsable, panel anclado abajo, mapa con altura ajustada.

## Limitaciones

- No se verificó scroll, superposiciones ni usabilidad en dispositivo real.
- El media query solo cubre `max-width: 768px`.

## Conclusión

**Validación responsive: NO EJECUTADO** (solo 1366×768 verificado por dump-dom).
