# Monitoreo de Flotas - Paso 1

Este proyecto inicia el desarrollo de un sistema de monitoreo de flotas de transporte.
En esta etapa, se implementa una **API Flask** que recibe y guarda la ubicación de un celular en una base de datos SQLite.

## ✅ Funcionalidades actuales

* API REST con Flask
* Recepción de datos de ubicación desde un celular (latitud, longitud, dispositivo)
* Almacenamiento en base de datos local (`SQLite`)
* Validación de datos recibidos

## 🧱 Estructura de carpetas
monitoreo_flotas/
├── app.py # Servidor Flask
├── config.py # Configuración de la base de datos
├── models.py # Función para conexión a la base de datos
├── crear_tablas.py # Script para crear la tabla 'ubicaciones'
├── .gitignore # Ignora archivos innecesarios
└── README.md # Documentación del proyecto

## 🧪 Cómo ejecutar el servidor

1. Crear la base de datos (solo la primera vez):

```bash
python3 crear_tablas.py

2. Iniciar el servidor:
python3 app.py

📡 Cómo enviar datos de prueba
Usando httpie desde consola:
http POST http://localhost:5000/api/ubicacion latitud=4.6097 longitud=-74.0817 dispositivo=celular_juan

