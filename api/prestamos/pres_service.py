from bd.bd import db
from api.maestros.mae_model import Maestros
from api.prestamos.pres_models import Prestamos
from api.proyectores.pro_model import Proyectores
from datetime import datetime
from sqlalchemy import func
from bd.bd import db

def get_maestro_and_proyector_by_prestamo(prestamo_id):
    prestamo = Prestamos.query.get(prestamo_id)
    if prestamo:
        maestro = Maestros.query.get(prestamo.id_maestro)
        proyector = Proyectores.query.get(prestamo.id_proyector)
        return maestro, proyector
    return None, None

def get_prestamo_horas(prestamo_id):
    prestamo = Prestamos.query.get(prestamo_id)
    if prestamo and prestamo.fecha_entrada and prestamo.hora_entrada:
        fecha_hora_salida = datetime.combine(prestamo.fecha_salida, prestamo.hora_salida)
        fecha_hora_entrada = datetime.combine(prestamo.fecha_entrada, prestamo.hora_entrada)
        horas_usadas = (fecha_hora_entrada - fecha_hora_salida).total_seconds() / 3600
        return horas_usadas
    return None

def get_proyector_horas_usadas(proyector_id):
    prestamos = Prestamos.query.filter_by(id_proyector=proyector_id).all()
    total_horas = sum(
        (datetime.combine(prestamo.fecha_entrada, prestamo.hora_entrada) - datetime.combine(prestamo.fecha_salida, prestamo.hora_salida)).total_seconds() / 3600
        for prestamo in prestamos if prestamo.fecha_entrada and prestamo.hora_entrada
    )
    return total_horas
