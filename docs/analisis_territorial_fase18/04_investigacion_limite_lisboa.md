# Investigación del límite del barrio Lisboa — Fase 18 (Lisboa360)

## 1. Fuentes consultadas

| Fuente | Tipo | Resultado |
|--------|------|-----------|
| Datos Abiertos Bogotá (datosabiertos.bogota.gov.co) | Portal institucional | Dataset "Barrio legalizado. Bogotá D.C." (SDP) existe (3,856 descargas) — **no descargado ni verificado** (restricción de la fase) |
| IDECA (ideca.gov.co) | Infraestructura de Datos Espaciales | Mapa de Referencia incluye capa de Barrio (EPSG 4686). Acceso vía WFS/WMS. No se descargó. |
| Geoportal de Bogotá | Portal | No se consultó directamente (acceso restringido/intermitente en fases anteriores) |
| Alcaldía Local de Suba | Institucional | Plan Ambiental Local de Suba 2025–2028 menciona el barrio Lisboa (Cra. 153 #132A9) como punto, no como polígono |
| Wikipedia (es.wikipedia.org) | Enciclopedia | Describe límites textuales: Noroeste Santa Rita, Norte San Pedro, Nordeste Toscana, Oeste Santa Cecilia, Este Toscana, Suroeste Corredor Calle 80, Sur El Cortijo/Humedal Tibabuyes, Sureste Tibabuyes. Coordenadas centrales: 4.7416, -74.1259 |
| codigo-postal.co | Referencia | Límites aproximados extraídos de mapas de la alcaldía local (imagen, no GIS). Coordenadas centrales: -74.1225, 4.7427 |
| Mapcarta / OSM | Referencia | Nodo OSM 496784647 (place=neighbourhood), punto, no polígono |
| Fincaraíz / Arriendo.com | Comercial | Descripción textual de ubicación (Calle 131–139, Carrera 136–151) |

## 2. Clasificación de resultados

| Clasificación | Fuentes |
|---------------|---------|
| Límite oficial verificado (GIS) | **Ninguno** |
| Fuente oficial parcialmente verificable | "Barrio legalizado. Bogotá D.C." (SDP) — existe pero no se descargó/verificó |
| Delimitación comunitaria no oficial | Wikipedia (límites textuales), Plan Ambiental Local |
| Referencia documental sin geometría GIS | codigo-postal.co (imagen), Mapcarta (punto OSM) |
| No encontrado | Polígono GIS verificable del barrio Lisboa |

## 3. Conclusión

**No se encontró un límite oficial verificable del barrio Lisboa en formato GIS.**

Las fuentes consultadas describen el barrio de forma textual o como punto, pero no proporcionan un polígono GIS verificable. El dataset "Barrio legalizado. Bogotá D.C." (SDP) es la fuente institucional más prometedora y debe obtenerse en una fase autorizada.

**No se inventó ningún polígono, coordenada ni límite.**

## 4. Recomendación institucional

1. Descargar y verificar el dataset "Barrio legalizado. Bogotá D.C." de Datos Abiertos Bogotá (SDP).
2. Filtrar por el barrio "Lisboa" en la localidad de Suba.
3. Verificar el CRS (EPSG 4686 según metadatos del Mapa de Referencia).
4. Validar la geometría con shapely/geopandas.
5. Si se confirma, integrar como capa adicional en una fase autorizada.

## Conclusión

**Investigación del límite de Lisboa: NO ENCONTRADO (GIS verificable).**
