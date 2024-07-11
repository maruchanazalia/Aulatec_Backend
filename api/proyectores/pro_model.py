from bd.bd import db

class Proyectores(db.Model):
    __tablename__ = 'proyectores'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(45), nullable=False)
