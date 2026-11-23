# Validaciones — Fase 35 (Lisboa360)

## Ejecutadas
| Validación | Resultado | Evidencia |
|---|---|---|
| `node --check` landing.js, main.js, ui.js, layers.js | OK | `syntax OK` |
| `pytest tests/ -q` | 39 passed | Backend sin regresión |
| Headless Edge landing (`/`) | OK | Hero, CTA, stats 74/48/429/57, fuentes presentes |
| Headless Edge mapa (`/mapa.html?api_url=...`) | OK | Sin banner, 6 capas dinámicas, explorador territorial, nav Inicio/Mapa |
| Navegación | OK (DOM) | Enlaces a `mapa.html` e `index.html` presentes |

## No ejecutadas / limitaciones
- **Interacción manual**: clics reales, scroll, menú móvil táctil, regreso desde mapa no verificados visualmente.
- **Responsive visual**: 1366x768/768x1024/390x844 no capturadas como evidencia visual válida.
- **Capturas de pantalla**: headless dump-dom usado; no se generaron capturas PNG revisadas.
- **Accesibilidad/contraste**: no auditado formalmente.

## Conclusión
**Validaciones automatizadas: APROBADAS.** Verificación visual/responsive manual: **PENDIENTE**.