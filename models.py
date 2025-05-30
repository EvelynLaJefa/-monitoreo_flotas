from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow)
    dispositivo = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Ubicacion {self.id} - {self.latitud}, {self.longitud}>"

