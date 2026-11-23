# Fuentes, licencias y limitaciones — Lisboa360

## Fuentes

- IDRD (pistas y escenarios): Open Data Bogotá, CC-BY-4.0 / CC-BY-SA-4.0.
- SDP/IDECA (Suba): CC-BY-4.0.
- SDP (Lisboa): CC-BY-4.0 (dataset "Barrio legalizado. Bogotá D.C.").
- OpenStreetMap: capa base (ODbL).

## Limitaciones

- CRS de Lisboa requiere confirmación autoritativa (reproyectado en Fase 20).
- Tipo de geometría de Suba inconsistente (MultiPolygon declarado, estructura Polygon).
- Sin límite oficial verificable del barrio Lisboa hasta la Fase 19 (ahora disponible, pero no integrado al frontend más allá de la Fase 22).
- Dataset IDPC excluido por inconsistencia de CRS.
- Sin datos demográficos ni red vial: no se calcularon densidades ni accesibilidad.
- Responsive y capturas no verificadas visualmente.
- "En Lisboa" se calcula por análisis espacial real (Shapely), resultado: 0 pistas y 0 escenarios.
