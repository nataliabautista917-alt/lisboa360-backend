-- Esquema SQLite de Lisboa360.
-- Barrio de referencia: Lisboa (Suba, Bogotá).
-- Nota: los datos descritos en este proyecto son ficticios de desarrollo; no son información real del barrio Lisboa.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS barrio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    geometria TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS lugar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    categoria TEXT,
    observaciones TEXT,
    geometria TEXT,
    barrio_id INTEGER NOT NULL REFERENCES barrio(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS equipamiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descripcion TEXT,
    capacidad INTEGER,
    geometria TEXT,
    estado TEXT,
    categoria TEXT,
    barrio_id INTEGER NOT NULL REFERENCES barrio(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS espacio_publico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descripcion TEXT,
    area_estimada REAL,
    geometria TEXT,
    estado TEXT,
    categoria TEXT,
    barrio_id INTEGER NOT NULL REFERENCES barrio(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS movilidad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    nombre TEXT,
    descripcion TEXT,
    capacidad INTEGER,
    geometria TEXT,
    estado TEXT,
    barrio_id INTEGER NOT NULL REFERENCES barrio(id) ON DELETE CASCADE,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS capa_geografica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT,
    descripcion TEXT,
    formato TEXT,
    ruta_archivo TEXT,
    fecha_generacion TEXT,
    estado TEXT,
    tipo_geometria TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_lugar_categoria ON lugar(categoria);
CREATE INDEX IF NOT EXISTS idx_lugar_nombre ON lugar(nombre);
CREATE INDEX IF NOT EXISTS idx_equipamiento_tipo ON equipamiento(tipo);
CREATE INDEX IF NOT EXISTS idx_equipamiento_categoria ON equipamiento(categoria);
CREATE INDEX IF NOT EXISTS idx_espacio_publico_tipo ON espacio_publico(tipo);
CREATE INDEX IF NOT EXISTS idx_movilidad_tipo ON movilidad(tipo);
CREATE INDEX IF NOT EXISTS idx_capa_geografica_nombre ON capa_geografica(nombre);
