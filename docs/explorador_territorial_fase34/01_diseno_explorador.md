# Diseño del explorador territorial — Fase 34 (Lisboa360)

## Objetivo
Transformar el explorador deportivo en un explorador territorial con categorías desplegables, listados de lugares reales y navegación al mapa.

## Categorías (conteos desde datos cargados)
| Categoría | Fuente | Conteo verificado (headless) |
|---|---|---:|
| Transporte (Paraderos SITP) | Capa 6 | 74 |
| Educación | Capa 7, categoria=Educacion | 9 |
| Religioso | Capa 7, categoria=Religioso | 6 |
| Espacios públicos | Capa 7, categoria=Espacio publico | 27 |
| Comunitario | Capa 7, categoria=Comunitario | 1 |
| Comercio y servicios | Capa 7, categoria=Comercio y servicios | 5 |
| Infraestructura deportiva | Capas 2 + 3 | 486 (429 pistas + 57 escenarios) |

## Organización
- Categorías en `<details>` desplegables con contador real.
- Scroll interno (`max-height: 180px`) para listas largas.
- Búsqueda dentro del explorador (`#explorador-search`).
- Estadísticas: paraderos, lugares, pistas/escenarios totales y en Lisboa.

## Conclusión
**Diseño: IMPLEMENTADO.**