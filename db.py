import sqlite3

# Conexión a la base de datos (si no existe, se crea)
conexion = sqlite3.connect('vehiculos.db')
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS datos_vehiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehiculo TEXT NOT NULL,
    temperatura REAL NOT NULL,
    velocidad REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conexion.commit()
conexion.close()
print("✅ Base de datos y tabla creada correctamente.")

