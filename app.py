from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Ruta para comprobar que el servidor funciona
@app.route('/')
def home():
    return '🚀 Servidor Flask funcionando correctamente'

# Ruta POST para recibir y guardar datos
@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    datos = request.get_json()

    if not datos:
        return jsonify({'status': 'error', 'mensaje': 'No se enviaron datos'}), 400

    # Claves requeridas
    claves_requeridas = ['vehiculo', 'temperatura', 'velocidad']
    for clave in claves_requeridas:
        if clave not in datos:
            return jsonify({'status': 'error', 'mensaje': f'Falta el campo: {clave}'}), 400

    # Validación de tipos
    if not isinstance(datos['vehiculo'], str):
        return jsonify({'status': 'error', 'mensaje': 'El campo "vehiculo" debe ser texto'}), 400
    if not isinstance(datos['temperatura'], (int, float)):
        return jsonify({'status': 'error', 'mensaje': 'La temperatura debe ser un número'}), 400
    if not isinstance(datos['velocidad'], (int, float)):
        return jsonify({'status': 'error', 'mensaje': 'La velocidad debe ser un número'}), 400

    # Guardar en base de datos
    try:
        conexion = sqlite3.connect('vehiculos.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO datos_vehiculos (vehiculo, temperatura, velocidad)
            VALUES (?, ?, ?)
        ''', (datos['vehiculo'], datos['temperatura'], datos['velocidad']))
        conexion.commit()
        conexion.close()
    except Exception as e:
        return jsonify({'status': 'error', 'mensaje': f'Error al guardar en BD: {str(e)}'}), 500

    print("✅ Datos guardados:", datos)

    return jsonify({'status': 'ok', 'mensaje': 'Datos validados y guardados correctamente'}), 200
# Ruta GET para obtener datos guardados
@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    try:
        conexion = sqlite3.connect('vehiculos.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT id, vehiculo, temperatura, velocidad, timestamp FROM datos_vehiculos ORDER BY id DESC LIMIT 10')
        filas = cursor.fetchall()
        conexion.close()

        datos = []
        for fila in filas:
            datos.append({
                'id': fila[0],
                'vehiculo': fila[1],
                'temperatura': fila[2],
                'velocidad': fila[3],
                'timestamp': fila[4]
            })

        return jsonify({'status': 'ok', 'datos': datos}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'mensaje': f'Error al obtener datos: {str(e)}'}), 500


# Ejecutar servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

