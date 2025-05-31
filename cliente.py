import requests
import json
from datetime import datetime, timezone

url = "http://localhost:5000/api/ubicacion"  # Ruta correcta

data = {
    "latitud": 4.6097,
    "longitud": -74.0817,
    "dispositivo": "celular_juan",
    "timestamp": datetime.now(timezone.utc).isoformat()
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

print("Código de respuesta:", response.status_code)
print("Respuesta del servidor:", response.text)

