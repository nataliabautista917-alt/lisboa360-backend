# Licencias y Atribución — Lisboa360 Backend

## 1. Resumen de licencias

| Capa | ID | Fuente | Licencia | URL de licencia | Atribución requerida |
|------|-----|--------|----------|-----------------|---------------------|
| Pistas Recreativas y Deportivas en Parque | 2 | IDRD | CC-BY-4.0 | https://creativecommons.org/licenses/by/4.0/ | Sí |
| Escenario Deportivo en Parque | 3 | IDRD | CC-BY-SA-4.0 | https://creativecommons.org/licenses/by-sa/4.0/ | Sí |
| Delimitación Localidad de Suba | 4 | SDP/IDECA | CC-BY-4.0 | https://creativecommons.org/licenses/by/4.0/ | Sí |
| Capa general ficticia | 1 | Lisboa360 (desarrollo) | N/A | N/A | No (datos ficticios de desarrollo) |

## 2. Detalle de licencias

### CC-BY-4.0 (Creative Commons Attribution 4.0 Internacional)

**Capas afectadas:**
- Pistas Recreativas y Deportivas en Parque (IDRD) — ID 2
- Delimitación Localidad de Suba (SDP/IDECA) — ID 4

**Requisitos:**
- Debe atribuirse el crédito al creador original (IDRD o SDP/IDECA)
- Debe indicarse si se realizaron cambios
- No se pueden aplicar restricciones adicionales que restrinjan el uso de otros

**Formato de atribución sugerido:**
```
Fuente: IDRD. Licencia: CC-BY-4.0. Datos: Lisboa360.
```
o
```
Fuente: SDP/IDECA. Licencia: CC-BY-4.0. Datos: Lisboa360.
```

### CC-BY-SA-4.0 (Creative Commons Attribution Share-Alike 4.0 Internacional)

**Capa afectada:**
- Escenario Deportivo en Parque (IDRD) — ID 3

**Requisitos:**
- Debe atribuirse el crédito al creador original (IDRD)
- Debe indicarse si se realizaron cambios
- Si se adapta o combina el material, debe distribuirse bajo la misma licencia (CC-BY-SA-4.0)
- No se pueden aplicar restricciones adicionales

**Formato de atribución sugerido:**
```
Fuente: IDRD. Licencia: CC-BY-SA-4.0. Datos: Lisboa360.
```

## 3. Atribución en la aplicación

### Mapa Leaflet (frontend)

Cada capa que se visualice en el mapa debe incluir su atribución correspondiente. Ejemplo de implementación en Leaflet:

```javascript
// Capa de pistas IDRD
L.tileLayer(...).addTo(map);

// Atribución para capas IDRD
map.attributionControl.addAttribution('Fuente: IDRD. Licencia: CC-BY-4.0. Datos: Lisboa360.');

// Atribución para capa de Suba
map.attributionControl.addAttribution('Fuente: SDP/IDECA. Licencia: CC-BY-4.0. Datos: Lisboa360.');
```

### Footer de la aplicación

Se recomienda incluir una sección de "Fuentes de datos" en el footer de la aplicación con el siguiente formato:

```
## Fuentes de datos

| Capa | Fuente | Licencia |
|------|--------|----------|
| Pistas Recreativas y Deportivas | IDRD | CC-BY-4.0 |
| Escenario Deportivo en Parque | IDRD | CC-BY-SA-4.0 |
| Delimitación Localidad de Suba | SDP/IDECA | CC-BY-4.0 |

Datos abiertos de Bogotá D.C. disponibles en datosabiertos.bogota.gov.co
```

### En la API REST

Los metadatos de cada capa (incluyendo licencia y entidad responsable) están disponibles a través del endpoint `GET /api/v1/capas`, que devuelve los campos `nombre`, `tipo`, `descripcion` (que incluye información de la fuente y licencia), y otros metadatos.

## 4. Tabla completa de atribuciones

| Capa | Nombre completo | Entidad | Licencia | Atribución mínima |
|------|----------------|---------|----------|-------------------|
| 2 | Pistas Recreativas y Deportivas en Parque (IDRD) | Instituto Distrital de Recreación y Deporte | CC-BY-4.0 | Fuente: IDRD. Licencia: CC-BY-4.0. Datos: Lisboa360. |
| 3 | Escenario Deportivo en Parque (IDRD) | Instituto Distrital de Recreación y Deporte | CC-BY-SA-4.0 | Fuente: IDRD. Licencia: CC-BY-SA-4.0. Datos: Lisboa360. |
| 4 | Delimitación Localidad de Suba (SDP/IDECA) | Secretaría Distrital de Planeación / IDECA | CC-BY-4.0 | Fuente: SDP/IDECA. Licencia: CC-BY-4.0. Datos: Lisboa360. |

## 5. Condiciones de uso

### Permitido
- Usar los datos con fines comerciales y no comerciales
- Adaptar, mezclar y construir sobre el material
- Distribuir el material adaptado

### Requerido
- Dar el crédito correspondiente a la fuente (IDRD o SDP/IDECA)
- Proveer un enlace a la licencia
- Indicar si se realizaron cambios

### No permitido
- Aplicar términos legales o medidas tecnológicas que restrinjan a otros hacer lo que la licencia permite
- Afirmar que los datos son propiedad de Lisboa360 (los datos pertenecen a sus respectivas entidades)

## 6. Datos ficticios

Los datos ficticios de desarrollo (capa ID 1) no están sujetos a ninguna licencia externa, ya que son datos de prueba creados internamente para el proyecto Lisboa360. No representan información real del barrio Lisboa.

## 7. Referencias

- [Datos Abiertos Bogotá](https://datosabiertos.bogota.gov.co) — Plataforma oficial de datos abiertos del Distrito Capital
- [Creative Commons Attribution 4.0 Internacional](https://creativecommons.org/licenses/by/4.0/)
- [Creative Commons Attribution Share-Alike 4.0 Internacional](https://creativecommons.org/licenses/by-sa/4.0/)
- [Instituto Distrital de Recreación y Deporte - IDRD](https://idrd.gov.co)
- [Secretaría Distrital de Planeación - SDP](https://planeacion.bogota.gov.co)
