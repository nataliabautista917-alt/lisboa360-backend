# Validación funcional de capas — Fase 14 (Lisboa360)

## 1. Capa 1 — Ficticia (id=1)

- Identificación: badge «Ficticio», nombre con prefijo «Ejemplo ficticio:».
- Carga: OK (3 features: Point, Polygon, LineString).
- Toggle: funcional (activar/desactivar sin nuevas peticiones).
- Panel: muestra atributos reales del dataset ficticio.
- **Clasificación: APROBADO.**

## 2. Capa 2 — Pistas recreativas IDRD (id=2)

- Carga: OK (429 features).
- Geometrías: MultiPolygon, renderizadas.
- Estilo: naranja `#e67e22`, distinguible.
- Panel: muestra `Nombre_del_Parque`, `Ubicación_Referencia`, `Tipo`, `Descripción_`, etc.
- Atribución: IDRD / Open Data Bogotá, CC-BY-4.0 (visible en panel).
- **Clasificación: APROBADO.**

## 3. Capa 3 — Escenarios deportivos IDRD (id=3)

- Carga: OK (57 features).
- Geometrías: MultiPolygon, renderizadas.
- Estilo: verde `#27ae60`, distinguible de pistas.
- Panel: muestra `Descripción_`, `Estado_Diagnóstico`, `Material_Piso`, `Capacidad_`, `Área__m2_`.
- Atribución: IDRD / Open Data Bogotá, CC-BY-SA-4.0.
- **Clasificación: APROBADO.**

## 4. Capa 4 — Localidad de Suba (id=4)

- Carga: OK tras corrección de robustez (1 feature).
- Geometrías: polígono de Suba renderizado.
- Identificación: «Localidad de Suba — contexto administrativo (no límite del barrio Lisboa)».
- No se presenta como límite del barrio Lisboa.
- CRS: inconsistencia documentada (EPSG:4686 declarado vs grados geográficos); sin reproyección.
- Atribución: SDP/IDECA, CC-BY-4.0.
- **Clasificación: APROBADO CON OBSERVACIONES** (CRS pendiente de verificación autoritativa).

## 5. Interacción

- Activar/desactivar: OK (sin nuevas peticiones).
- Múltiples capas simultáneas: OK (render headless con las 4 activas).
- Panel informativo: OK (atributos escapados).
- Leyenda sincronizada: OK.
- Indicadores de carga: OK.
- Errores de red: manejados (estado «Sin datos — error de conexión»).
- Capa inexistente: no aplica en UI (solo backend).

## Conclusión

**Validación funcional de capas: APROBADO.**
