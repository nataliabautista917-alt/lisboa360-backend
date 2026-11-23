# Informe final — Fase 17 (Lisboa360)

## 1. Resumen ejecutivo

Se amplió el análisis territorial de Suba con los datasets reales de IDRD (pistas y escenarios deportivos) y el polígono oficial de Suba. Se generaron estadísticas descriptivas, relaciones espaciales y visualizaciones. Los resultados son exploratorios y corresponden a la localidad de Suba, no al barrio Lisboa.

## 2. Análisis ejecutados

- Conteo de pistas (429) y escenarios (57).
- Distribución por Tipo, Estado_Diagnóstico, Material_Piso, Cubierto_.
- Valores nulos por campo.
- Relación espacial pistas–escenarios (intersección).
- Parques con ambos tipos de infraestructura (26).
- Porcentajes de representación dentro de Suba (8.9% pistas, 7.0% escenarios).

## 3. Resultados espaciales

- 38 pistas dentro de Suba.
- 4 escenarios dentro de Suba.
- Concentración en parques como Tibabuyes, Fontanar Del Rio, La Gaitana, Las Flores y PARQUE DEL INDIO O DE LAS COMETAS.

## 4. Visualizaciones generadas

4 archivos PNG en `data/analysis/fase17/` y copiados a `docs/analisis_territorial_fase17/evidencias/`:
- `mapa_suba_pistas_escenarios.png`
- `mapa_pistas_suba.png`
- `mapa_escenarios_suba.png`
- `grafico_conteos_suba.png`

## 5. Validaciones

- Integridad de archivos: OK.
- Validez de CSV y JSON: OK.
- Consistencia de conteos: OK.
- Correspondencia entre tablas y gráficos: OK.
- Reproducibilidad de scripts: OK.
- No se modificaron archivos anteriores: OK.

## 6. Problemas encontrados

- Inconsistencia de CRS y tipo de geometría en Suba (documentada, no corregida).
- Sin diccionario de códigos para campos numéricos.

## 7. Limitaciones

- Sin datos demográficos ni red vial.
- Sin límite oficial del barrio Lisboa.
- IDPC excluido.

## 8. Archivos creados

- `data/analysis/fase17/` — CSVs, JSON, PNGs.
- `docs/analisis_territorial_fase17/` — 6 documentos + evidencias.

## 9. Confirmación de conservación

No se modificó ningún archivo original, procesado, backend, SQLite, OpenAPI, frontend ni remotos Git. No se realizaron commits ni pushes.

## 10. Recomendaciones para la Fase 18

1. Resolver el CRS de Suba con fuente autoritativa.
2. Corregir el tipo de geometría del GeoJSON de Suba.
3. Obtener el límite oficial del barrio Lisboa.
4. Realizar análisis de cobertura/accesibilidad con datos verificados.

Me detengo aquí y espero revisión y autorización.
