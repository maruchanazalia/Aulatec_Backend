from bd.bd import db

class Proyectores(db.Model):
    __tablename__ = 'proyectores'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(45), nullable=False)
    status = db.Column(db.String(20), nullable=False)  
    numero_serie = db.Column(db.String(100), nullable=False)  
    lumens = db.Column(db.Integer, primary_key=True)

    prestamos = db.relationship('Prestamos', back_populates='proyector')
