from bd.bd import db
from api.maestros.mae_model import Maestros

def get_all_maestros():
    return Maestros.query.all()

def get_maestro_by_id(maestro_id):
    return Maestros.query.get(maestro_id)

def create_maestro(nombre, ape_paterno, ape_materno, correo):
    maestro = Maestros(nombre=nombre, ape_paterno=ape_paterno, ape_materno=ape_materno, correo=correo)
    db.session.add(maestro)
    db.session.commit()
    return maestro

def update_maestro(maestro_id, nombre, ape_paterno, ape_materno, correo):
    maestro = Maestros.query.get(maestro_id)
    if maestro:
        maestro.nombre = nombre
        maestro.ape_paterno = ape_paterno
        maestro.ape_materno = ape_materno
        maestro.correo = correo
        db.session.commit()
        return maestro
    return None

def delete_maestro(maestro_id):
    maestro = Maestros.query.get(maestro_id)
    if maestro:
        db.session.delete(maestro)
        db.session.commit()
        return True
    return False
