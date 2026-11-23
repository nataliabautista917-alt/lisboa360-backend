# Informe de pruebas de integración GIS — Fase 13

## 1. Estado general de la integración GIS

La integración GIS de Lisboa360 (backend + frontend) está **operativa y estable**. Las 4 capas (1 ficticia + 3 reales) se consultan desde el backend y se visualizan en el frontend con estilos diferenciados, toggles, leyenda sincronizada y panel de atributos. Las pruebas automatizadas del backend pasan al 100%.

## 2. Resultados por área

| Área | Clasificación |
|------|---------------|
| Backend (endpoints, servicios, seed, errores) | APROBADO |
| Frontend (carga, toggles, panel, leyenda, assets) | APROBADO CON OBSERVACIONES |
| Validación geográfica (coordenadas, geometrías, extensión) | APROBADO CON OBSERVACIONES |
| Regresión y seguridad | APROBADO |
| Pruebas visuales (navegador) | NO EJECUTADO |
| Pruebas de endpoints en vivo | APROBADO |

## 3. Estado de los cuatro endpoints de capas

| Endpoint | HTTP | Features | CRS | Clasificación |
|----------|------|----------|-----|---------------|
| `/api/v1/capas` | 200 | 4 capas | n/a | APROBADO |
| `/api/v1/capas/1/geojson` | 200 | 3 | n/a | APROBADO |
| `/api/v1/capas/2/geojson` | 200 | 429 | EPSG:4326 | APROBADO |
| `/api/v1/capas/3/geojson` | 200 | 57 | EPSG:4326 | APROBADO |
| `/api/v1/capas/4/geojson` | 200 | 1 | EPSG:4686 (declarado) | APROBADO |

## 4. Estado de las capas

- **Reales:** id=2 (pistas, 429), id=3 (escenarios, 57), id=4 (Suba, 1) — disponibles y servidas.
- **Ficticia:** id=1 (3 features) — preservada e identificada como ficticia.
- Sin duplicados ni mezcla de fuentes.

## 5. Pruebas aprobadas

- 39/39 tests automatizados del backend (pytest).
- Endpoints reales consultados (HTTP 200/404).
- Assets del frontend (HTTP 200).
- Validación estructural de los 4 GeoJSON.
- Atributos requeridos presentes en todos los datasets.
- Regresión de recursos ficticios.

## 6. Pruebas no ejecutadas

- Pruebas visuales en navegador (no disponible).
- Pruebas de responsive en dispositivo real.
- Pruebas de interacción de toggles en UI (no verificadas en navegador).

## 7. Errores detectados y corregidos

Ningún error nuevo detectado en esta fase. Las correcciones de la Fase 12 (cadenas de atributos, soporte `geometry`, `fillOpacity`, indicador de carga, origen real/ficticio) permanecen vigentes y validadas por sintaxis.

## 8. Riesgos técnicos pendientes

1. CRS de Suba (EPSG:4686 declarado vs grados geográficos) sin verificación autoritativa.
2. Sin límite oficial verificable del barrio Lisboa: no realizar recortes ni análisis espaciales focalizados.
3. Sin pruebas visuales: riesgo de defectos de renderizado no detectados.
4. Atribución CC-BY-4.0 / CC-BY-SA-4.0 debe gestionarse en producción.

## 9. Recomendaciones para la Fase 14

1. Ejecutar pruebas visuales en navegador (Chrome/Firefox) con backend real.
2. Validar el CRS de Suba con IDPC/IGAC antes de cualquier operación espacial.
3. Obtener el límite oficial del barrio Lisboa (Alcaldía Local de Suba / Consejo Comunal Lisboa).
4. Incorporar pruebas automatizadas de frontend (p. ej., Playwright) si se autoriza.
5. Revisar la atribución de licencias en la UI de producción.

## Conclusión

**Integración GIS: APROBADO CON OBSERVACIONES.**
