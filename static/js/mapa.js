let mapa = L.map('mapa').setView([4.60971, -74.08175], 14);  // Bogotá

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(mapa);

let marcadores = [];
let lineaRuta = null;

function cargarUbicaciones() {
    fetch('/api/ubicacion')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                // Eliminar marcadores anteriores
                marcadores.forEach(m => mapa.removeLayer(m));
                marcadores = [];

                // Eliminar línea anterior
                if (lineaRuta) {
                    mapa.removeLayer(lineaRuta);
                }

                const coordenadas = [];

                data.datos.reverse().forEach(punto => {
                    const lat = parseFloat(punto.latitud);
                    const lon = parseFloat(punto.longitud);
                    const marcador = L.marker([lat, lon])
                        .bindPopup(`📍 ${punto.dispositivo}<br>${punto.fecha_hora}`);
                    marcador.addTo(mapa);
                    marcadores.push(marcador);
                    coordenadas.push([lat, lon]);
                });

                if (coordenadas.length > 1) {
                    lineaRuta = L.polyline(coordenadas, { color: 'blue' }).addTo(mapa);
                    mapa.fitBounds(lineaRuta.getBounds());
                }
            } else {
                console.error("❌ Error al obtener ubicaciones:", data.mensaje);
            }
        })
        .catch(error => console.error("⚠️ Error en la petición:", error));
}

// Cargar la primera vez
cargarUbicaciones();

// Actualizar cada 10 segundos
setInterval(cargarUbicaciones, 10000);
