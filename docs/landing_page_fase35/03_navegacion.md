# Navegación — Fase 35 (Lisboa360)

## Rutas
| Ruta | Contenido |
|---|---|
| `/` / `index.html` | Landing page institucional |
| `/mapa.html` | Mapa interactivo GIS (aplicación existente) |

## Flujos
- **Landing → Mapa**: botones “Explorar mapa interactivo” / “Comenzar exploración” / nav “Explorar mapa” → `mapa.html`.
- **Mapa → Inicio**: nav “Inicio” en header → `index.html`; marca también enlaza a `index.html`.
- **Mapa interno**: nav activa “Mapa” (`mapa.html`).

## Compatibilidad
- Rutas relativas; funciona con servidor estático desde `lisboa360-frontend`.
- Parámetro `api_url` sigue soportado en `mapa.html`.