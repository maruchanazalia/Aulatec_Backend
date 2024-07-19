from bd.bd import db
from datetime import date, time

class Prestamos(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    id_maestro = db.Column(db.Integer, db.ForeignKey('maestros.id'), nullable=False)
    id_proyector = db.Column(db.Integer, db.ForeignKey('proyectores.id'), nullable=False)
    fecha_salida = db.Column(db.Date, nullable=False)
    fecha_entrada = db.Column(db.Date, nullable=True)
    hora_salida = db.Column(db.Time, nullable=False)
    hora_entrada = db.Column(db.Time, nullable=True)

    maestro = db.relationship('Maestros', back_populates='prestamos')
    proyector = db.relationship('Proyectores', back_populates='prestamos')