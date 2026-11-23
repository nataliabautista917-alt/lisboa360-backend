# Guía de instalación y ejecución — Lisboa360

## Requisitos

- Python 3.10+ (backend).
- Node.js (opcional, para servir frontend).
- Navegador moderno (Chrome, Edge, Firefox).

## Backend

```bash
cd lisboa360-backend
pip install -r requirements.txt
python app.py
```

El backend inicia en `http://127.0.0.1:5000`. La base SQLite se inicializa automáticamente con seed de desarrollo.

## Frontend

```bash
cd lisboa360-frontend
python -m http.server 8000 --bind 127.0.0.1
```

Abrir `http://127.0.0.1:8000/?api_url=http://127.0.0.1:5000`.

## Pruebas

```bash
cd lisboa360-backend
python -m pytest tests/ -v
```

Resultado esperado: 39 passed.

## Solución de problemas

- Si el frontend muestra "Sin conexión", verificar que el backend esté corriendo y que `ALLOWED_ORIGINS` incluya el origen del frontend.
- Si faltan capas, verificar que `data/geojson/` contenga los archivos referenciados en el seed.
