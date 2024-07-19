from bd.bd import db
from api.proyectores.pro_model import Proyectores

def get_all_proyectores():
    return Proyectores.query.all()

def get_proyector_by_id(proyector_id):
    return Proyectores.query.get(proyector_id)

def create_proyector(marca, status, numero_serie, lumens):
    proyector = Proyectores(marca=marca, status=status, numero_serie=numero_serie, lumens=lumens)
    db.session.add(proyector)
    db.session.commit()
    return proyector

def update_proyector(proyector_id, marca, status, numero_serie, lumens):
    proyector = Proyectores.query.get(proyector_id)
    if proyector:
        proyector.marca = marca
        proyector.status = status
        proyector.numero_serie = numero_serie
        proyector.lumens = lumens
        
        db.session.commit()
        return proyector
    return None

def delete_proyector(proyector_id):
    proyector = Proyectores.query.get(proyector_id)
    if proyector:
        db.session.delete(proyector)
        db.session.commit()
        return True
    return False
