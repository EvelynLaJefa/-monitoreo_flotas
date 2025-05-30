import sqlite3

conexion = sqlite3.connect('vehiculos.db')
cursor = conexion.cursor()

# Crear tabla de ubicaciones
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ubicaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitud REAL NOT NULL,
        longitud REAL NOT NULL,
        fecha_hora TEXT DEFAULT CURRENT_TIMESTAMP,
        dispositivo TEXT
    )
''')

conexion.commit()
conexion.close()
print("✅ Tabla 'ubicaciones' creada correctamente.")

