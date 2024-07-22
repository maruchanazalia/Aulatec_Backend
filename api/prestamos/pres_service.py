from bd.bd import db
from api.maestros.mae_model import Maestros
from api.prestamos.pres_models import Prestamos
from api.proyectores.pro_model import Proyectores
from datetime import datetime, timedelta
from collections import defaultdict

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
        horas_usadas = (fecha_hora_salida - fecha_hora_entrada).total_seconds() / 3600
        return horas_usadas
    return None

def get_proyector_horas_usadas(proyector_id):
    prestamos = Prestamos.query.filter_by(id_proyector=proyector_id).all()
    total_horas = sum(
        (datetime.combine(prestamo.fecha_entrada, prestamo.hora_entrada) - datetime.combine(prestamo.fecha_salida, prestamo.hora_salida)).total_seconds() / 3600
        for prestamo in prestamos if prestamo.fecha_entrada and prestamo.hora_entrada
    )
    return total_horas

def get_all_prestamos_service():
    prestamos = Prestamos.query.all()
    response = []

    for prestamo in prestamos:
        maestro = Maestros.query.get(prestamo.id_maestro)
        proyector = Proyectores.query.get(prestamo.id_proyector)
        response.append({
            'prestamo_id': prestamo.id,
            'maestro': {
                'id': maestro.id,
                'nombre': maestro.nombre,
                'ape_paterno': maestro.ape_paterno,
                'ape_materno': maestro.ape_materno,
                'correo': maestro.correo
            },
            'proyector': {
                'id': proyector.id,
                'marca': proyector.marca,
                'status': proyector.status,
                'numero_serie': proyector.numero_serie
            }
        })

    return response

def get_prestamo_hours(prestamo_id):
    prestamo = Prestamos.query.get(prestamo_id)
    if prestamo:
        hora_entrada = prestamo.hora_entrada.strftime('%H:%M') if prestamo.hora_entrada else None
        hora_salida = prestamo.hora_salida.strftime('%H:%M') if prestamo.hora_salida else None
        return {
            'hora_entrada': hora_entrada,
            'hora_salida': hora_salida
        }
    return None

def get_prestamo_info(prestamo_id):
    prestamo = Prestamos.query.get(prestamo_id)
    if not prestamo or not prestamo.fecha_entrada or not prestamo.hora_entrada or not prestamo.fecha_salida or not prestamo.hora_salida:
        return None

    return {
        'fecha_entrada': prestamo.fecha_entrada.strftime('%Y-%m-%d'),
        'hora_entrada': prestamo.hora_entrada.strftime('%H:%M:%S'),
        'fecha_salida': prestamo.fecha_salida.strftime('%Y-%m-%d'),
        'hora_salida': prestamo.hora_salida.strftime('%H:%M:%S')
    }

def calculate_hours(start_time, end_time):
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(start_time, FMT)
    if tdelta.days < 0:
        tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    return tdelta.seconds / 3600

def get_prestamos_by_maestro(maestro_id):
    prestamos = Prestamos.query.filter_by(id_maestro=maestro_id).all()
    usage_by_date = {}
    for prestamo in prestamos:
        fecha = prestamo.fecha_entrada.strftime('%Y-%m-%d')
        horas_usadas = calculate_hours(prestamo.hora_entrada.strftime('%H:%M:%S'), prestamo.hora_salida.strftime('%H:%M:%S'))
        if fecha in usage_by_date:
            usage_by_date[fecha] += horas_usadas
        else:
            usage_by_date[fecha] = horas_usadas
    result = [{"fecha": date, "horas": hours} for date, hours in usage_by_date.items()]
    return result
