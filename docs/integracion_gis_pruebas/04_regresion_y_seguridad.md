# Regresión y seguridad — Integración GIS (Fase 13)

## 1. Regresión funcional

| Recurso | Estado | Evidencia |
|---------|--------|-----------|
| Barrio Lisboa (`/api/v1/barrios/lisboa`) | OK | HTTP 200, claves id/nombre/descripcion/geometria/created_at |
| Lugares (`/api/v1/lugares`) | OK | 39 tests pasan (incluye paginación, búsqueda, validación) |
| Equipamientos (`/api/v1/equipamientos`) | OK | Tests pasan |
| Espacios públicos (`/api/v1/espacios-publicos`) | OK | Tests pasan |
| Movilidad (`/api/v1/movilidad`) | OK | Tests pasan |
| Capas geográficas (`/api/v1/capas`) | OK | 4 capas, HTTP 200 |
| Capa ficticia id=1 | OK | 3 features, estilo y metadatos intactos |

## 2. Separación de fuentes

- Las 4 capas tienen ids únicos (1 ficticia, 2–4 reales).
- El frontend diferencia con badge «Real»/«Ficticio» y metadatos de origen.
- No se mezclan datos ficticios con reales en un mismo conjunto.

## 3. Seguridad

- **Sin rutas internas expuestas**: el frontend solo consume `/api/v1/...`.
- **Sin HTML inseguro**: `esc()` escapa todos los atributos en `showInfo()` y `buildItem()`.
- **Manejo de errores**: archivos inexistentes → `NotFoundError` → 404 JSON estandarizado (verificado con capa 999).
- **CORS**: restringido a orígenes del frontend (configurado en backend, sin cambios en esta fase).
- **Sin modificación de datos**: no se alteraron GeoJSON, SQLite, OpenAPI ni datasets.

## 4. Datos ficticios preservados

Los 4 conjuntos ficticios (lugares, equipamientos, espacios públicos, movilidad) y la capa ficticia id=1 permanecen intactos. Verificado por tests (39/39) y por endpoint real.

## Conclusión

**Regresión y seguridad: APROBADO.**
