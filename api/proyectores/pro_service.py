from bd.bd import db
from api.proyectores.pro_model import Proyectores

def get_all_Pro():
    return Proyectores.query.all()

def delete_pro(pro_id):
    proyec = Proyectores.query.get(pro_id)
    if proyec:
        db.session.delete(proyec)
        db.session.commit()
        return True
    return False

def create_pro(marca):
    proyector = Proyectores(marca=marca)
    db.session.add(proyector)
    db.session.commit()
    return proyector
    
