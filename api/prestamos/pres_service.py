from bd.bd import db
from api.maestros.mae_model import Maestros
from api.prestamos.pres_models import Prestamos
from api.proyectores.pro_model import Proyectores
from datetime import datetime, timedelta, date
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


def calculate_used_hours(start_time, end_time):
    FMT = '%H:%M:%S'
    start = datetime.strptime(start_time, FMT)
    end = datetime.strptime(end_time, FMT)
    tdelta = end - start
    
    if tdelta.total_seconds() < 0:
        tdelta += timedelta(days=1)
    
    horas_usadas = tdelta.total_seconds() / 3600

    return horas_usadas

def get_prestamos_by_maestro(maestro_id):
    prestamos = Prestamos.query.filter_by(id_maestro=maestro_id).all()
    usage_by_date = {}
    
    for prestamo in prestamos:
        fecha = prestamo.fecha_entrada.strftime('%Y-%m-%d')
        
        horas_usadas = calculate_used_hours(
            prestamo.hora_entrada.strftime('%H:%M:%S'),
            prestamo.hora_salida.strftime('%H:%M:%S')
        )
        
        if fecha in usage_by_date:
            usage_by_date[fecha] += horas_usadas
        else:
            usage_by_date[fecha] = horas_usadas

    result = [{"fecha": date, "horas": hours} for date, hours in usage_by_date.items()]
    return {"prestamos": result}


#get horas proyector
def calculate_used_hours(start_time, end_time):
    FMT = '%H:%M:%S'
    start = datetime.strptime(start_time, FMT)
    end = datetime.strptime(end_time, FMT)

    tdelta = end - start
    if tdelta.total_seconds() < 0:
        tdelta += timedelta(days=1)

    horas_usadas = tdelta.total_seconds() / 3600
    total_horas = horas_usadas + horas_usadas + horas_usadas
    print(f"Start: {start_time}, End: {end_time}, Total Horas: {total_horas}")

    return total_horas

def get_all_proyectores_horas_usadas():
    proyectores = Proyectores.query.all()
    proyector_horas = []

    for proyector in proyectores:
        total_horas = get_proyector_horas_usadas(proyector.id)
        proyector_horas.append({
            'proyector_nombre': proyector.numero_serie,
            'total_horas_usadas': total_horas
        })

    return proyector_horas


#get horas maestros 
def calculate_used_hours(start_time, end_time):
    FMT = '%H:%M:%S'
    start = datetime.strptime(start_time, FMT)
    end = datetime.strptime(end_time, FMT)

    tdelta = end - start
    if tdelta.total_seconds() < 0:
        tdelta += timedelta(days=1)

    horas_usadas = tdelta.total_seconds() / 3600

    return horas_usadas

def get_maestro_horas_usadas():
    maestros = Maestros.query.all()
    maestro_horas = []

    for maestro in maestros:
        prestamos = Prestamos.query.filter_by(id_maestro=maestro.id).all()
        
        total_horas = sum(
            calculate_used_hours(
                prestamo.hora_entrada.strftime('%H:%M:%S'),
                prestamo.hora_salida.strftime('%H:%M:%S')
            )
            for prestamo in prestamos
        )

        maestro_horas.append({
            'maestro_nombre': f"{maestro.nombre} {maestro.ape_paterno} {maestro.ape_materno}",
            'total_horas_usadas': total_horas
        })

    return maestro_horas

#GET de disponibilidad y uso de proyectores
def get_proyector_horas_usadas(proyector_id):
    prestamos = Prestamos.query.filter_by(id_proyector=proyector_id).all()
    total_horas_usadas = sum([(p.hora_salida.hour - p.hora_entrada.hour) for p in prestamos if p.hora_salida and p.hora_entrada])
    return total_horas_usadas

def get_proyectores_disponibilidad():
    proyectores = Proyectores.query.all()
    total_horas_del_dia = 24

    proyector_disponibilidad = []
    for proyector in proyectores:
        total_horas_usadas = get_proyector_horas_usadas(proyector.id)
        porcentaje_disponibilidad = ((total_horas_del_dia - total_horas_usadas) / total_horas_del_dia) * 100
        proyector_disponibilidad.append({
            'proyector_nombre': proyector.numero_serie,
            'total_horas_usadas': total_horas_usadas,
            'porcentaje_disponibilidad': porcentaje_disponibilidad
        })

    return proyector_disponibilidad

#para guardar datos de mysql RFID
def create_prestamo(id_maestro, id_proyector, hora_salida, hora_entrada=None, fecha_entrada=None):
    try:
        if isinstance(hora_salida, str):
            hora_salida = datetime.strptime(hora_salida, "%H:%M:%S").time()
        
        if hora_entrada and isinstance(hora_entrada, str):
            hora_entrada = datetime.strptime(hora_entrada, "%H:%M:%S").time()

        fecha_salida = date.today()

        if not fecha_entrada:
            fecha_entrada = date.today()

        nuevo_prestamo = Prestamos(
            id_maestro=id_maestro,
            id_proyector=id_proyector,
            fecha_salida=fecha_salida,
            hora_salida=hora_salida,
            fecha_entrada=fecha_entrada,
            hora_entrada=hora_entrada
        )
        db.session.add(nuevo_prestamo)
        db.session.commit()
        
        return nuevo_prestamo

    except Exception as e:
        db.session.rollback()
        raise e

