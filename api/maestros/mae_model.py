from bd.bd import db

class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ape_paterno = db.Column(db.String(100), nullable=False)
    ape_materno = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
