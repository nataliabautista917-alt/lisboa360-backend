# Limpieza de interfaz — Fase 32 (Lisboa360)

## 1. Cambios en `js/ui.js`

- Eliminadas las tarjetas de Equipamamentos, Espacios públicos, Movilidad y Lugares de interés (ficticios).
- Eliminada la tarjeta de barrio (descripción ficticia).

## 2. Cambios en `js/main.js`

- Omitida la carga de la capa ficticia (id=1) en el bucle dinámico.
- Omitido el bucle de datos estáticos ficticios (paso 6).

## 3. Cambios en `js/layers.js`

- Leyenda solo incluye capas dinámicas (reales).

## 4. Resultado

La interfaz ahora muestra únicamente datos reales: 6 capas (pistas, escenarios, Suba, Lisboa, paraderos SITP, lugares OSM).

## Conclusión

**Limpieza completada.** No aparecen textos "Ejemplo ficticio" ni "Ficticio" en el DOM.
