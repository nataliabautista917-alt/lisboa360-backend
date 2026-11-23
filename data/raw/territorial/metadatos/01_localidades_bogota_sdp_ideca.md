# Registro de Metadatos — Localidades de Bogotá D.C. (SDP/IDECA)

## Información del Archivo

- **Nombre del dataset:** Localidad. Bogotá D.C
- **Archivo original:** `localidades_bogota_sdp_ideca_original.geojson`
- **Ubicación del archivo:** `lisboa360-backend/data/raw/territorial/localidades_bogota_sdp_ideca_original.geojson`
- **Fecha de descarga:** 22/11/2026
- **Fecha de consulta de la fuente:** 22/11/2026

## Información de la Fuente

- **Entidad responsable:** Secretaría Distrital de Planeación - SDP / La IDE de Bogotá D.C. (IDECA)
- **URL de la ficha:** https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8
- **URL de descarga:** https://datosabiertos.bogota.gov.co/dataset/856cb657-8ca3-4ee8-857f-37211173b1f8/resource/497b8756-0927-4aee-8da9-ca4e32ca3a8a/download/loca.json
- **Distribuidor:** Secretaría Distrital de Planeación
- **Responsable del metadato:** Secretaría Distrital de Planeación (Autor)

## Información Geoespacial

- **Formato:** GeoJSON (RFC 7946)
- **Tamaño:** 2,363,493 bytes (≈ 2.3 MB)
- **CRS declarado:** EPSG 4686 MAGNA-SIRGAS geographic 2D - 4686
- **Tipo de geometría:** Polígono (rings)
- **Cobertura geográfica:** Bogotá D.C. (polígono: -74.450724, 3.730672 a -73.989018, 4.836829)
- **Número de features:** 20 localidades (una por cada localidad de Bogotá D.C.)
- **Fecha del dato:** 2022-08-05
- **Última actualización del metadato:** 28/02/2023, 23:22 (UTC)
- **Fecha de creación del metadato:** 16/05/2019, 18:48 (UTC)
- **Frecuencia de actualización:** Desconocida
- **Idioma:** Español
- **Forma de presentación:** Mapa Digital
- **Tipo de representación espacial:** Vector
- **Resolución espacial:** Sin información

## Identificación de Suba

- **Nombre del registro:** SUBA
- **Código territorial:** 11 (LocCodigo)
- **Acuerdo administrativo:** Acuerdo 8 de 1977 (LocAAdmini)
- **Área:** 100,560,477.71021648 (LocArea)
- **SHAPE_Length:** 0.59287510508939678
- **SHAPE_Area:** 0.008190624669006016
- **Evidencia:** El registro con OBJECTID:100, LocNombre:"SUBA", LocCodigo:"11" está presente en el dataset

## Licencia

- **Tipo:** Creative Commons Attribution 4.0 (CC-BY-4.0)
- **URL de licencia:** https://creativecommons.org/licenses/by/4.0/

## Procedencia

- **Plataforma:** Datos Abiertos Bogotá (CKAN)
- **Categoría temática:** Límites
- **Grupo temático:** Ordenamiento Territorial
- **Tags:** Entidad territorial, Localidad

## Verificaciones Ejecutadas

1. ✅ **Existencia física del archivo:** El archivo existe en `lisboa360-backend/data/raw/territorial/`
2. ✅ **Tamaño mayor a cero:** 2,363,493 bytes
3. ✅ **No es una página HTML:** El archivo comienza con coordenadas GeoJSON válidas, contiene estructuras de tipo Feature con atributos y geometrías de polígono
4. ✅ **Lectura correcta:** El archivo puede leerse como GeoJSON; contiene el registro de SUBA con OBJECTID:100
5. ✅ **Número de features:** 20 localidades (incluyendo Suba con código 11)
6. ✅ **Campos disponibles:** OBJECTID, LocNombre, LocAAdmini, LocArea, LocCodigo, SHAPE_Length, SHAPE_Area
7. ✅ **CRS declarado:** EPSG 4686 MAGNA-SIRGAS geographic 2D - 4686 (verificado en la ficha CKAN)
8. ✅ **Tipo de geometría:** Polígono (rings)
9. ✅ **Extensión espacial:** Coordenadas dentro del rango de Bogotá D.C. (longitud -74.45 a -73.98, latitud 3.73 a 4.83)
10. ✅ **Registro de Suba encontrado:** SUBA con código 11, verificado en el archivo
11. ✅ **Coherencia con ficha CKAN:** Entidad SDP, licencia CC-BY-4.0, fecha del dato 2022-08-05

## Limitaciones

1. **CRS no homogéneo:** El dataset usa EPSG:4686 (MAGNA-SIRGAS), mientras que Leaflet/OpenStreetMap requieren EPSG:4326 (WGS 84). Será necesaria reproyección para su uso en la aplicación.
2. **No se realizó reproyección:** Cumpliendo con las instrucciones de la fase, el archivo se conserva en su formato original sin transformación.
3. **No se recortó:** El dataset contiene todas las 20 localidades de Bogotá, no solo Suba.
4. **Barrio Lisboa no incluido:** Este dataset contiene localidades, no barrios. El barrio Lisboa no tiene delimitación propia en este dataset.

## Utilidad para Lisboa360

- Proporciona la delimitación oficial verificable de la localidad de Suba (código 11)
- Sirve como contexto administrativo para el barrio Lisboa
- Permite verificar espacialmente si elementos (parques, equipamientos) están dentro de Suba
- Es una fuente oficial verificable con licencia CC-BY-4.0 que permite su uso público con atribución

## Estado de Validación

- **Estado:** Válido — archivo GeoJSON estructuralmente correcto, CRS documentado, registro de Suba verificado
- **Listo para uso:** Sí, como referencia territorial de la localidad de Suba (con atribución CC-BY-4.0)
- **Trazabilidad:** Mantiene trazabilidad completa hacia la fuente oficial en datosabiertos.bogota.gov.co