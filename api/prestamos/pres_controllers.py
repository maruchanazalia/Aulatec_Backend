from flask import jsonify, request
from datetime import datetime, timedelta
from api.prestamos.pres_service import get_maestro_and_proyector_by_prestamo, get_prestamo_horas, get_proyector_horas_usadas, get_all_prestamos_service, get_prestamo_hours, get_prestamo_info, get_prestamos_by_maestro, get_all_proyectores_horas_usadas, get_maestro_horas_usadas, get_proyectores_disponibilidad, create_prestamo

def get_maestro_and_proyector():
    data = request.get_json()
    prestamo_id = data.get('prestamo_id')

    if not prestamo_id:
        return jsonify({'message': 'Prestamo ID is required'}), 400

    maestro, proyector = get_maestro_and_proyector_by_prestamo(prestamo_id)

    if not maestro or not proyector:
        return jsonify({'message': 'Prestamo not found'}), 404

    response = {
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
    }

    return jsonify(response), 200

def get_all_prestamos():
    prestamos_data = get_all_prestamos_service()
    return jsonify(prestamos_data), 200


def get_prestamo_horas_usadas():
    data = request.get_json()
    prestamo_id = data.get('prestamo_id')

    if not prestamo_id:
        return jsonify({'message': 'Prestamo ID is required'}), 400

    horas_usadas = get_prestamo_horas(prestamo_id)

    if horas_usadas is None:
        return jsonify({'message': 'Prestamo not found or not yet returned'}), 404

    return jsonify({'horas_usadas': horas_usadas}), 200

def get_total_horas_usadas_proyector():
    data = request.get_json()
    proyector_id = data.get('proyector_id')

    if not proyector_id:
        return jsonify({'message': 'Proyector ID is required'}), 400

    total_horas = get_proyector_horas_usadas(proyector_id)

    return jsonify({'total_horas_usadas': total_horas}), 200

def get_prestamo_hours_route():
    data = request.get_json()
    prestamo_id = data.get('prestamo_id')

    if not prestamo_id:
        return jsonify({'message': 'Prestamo ID is required'}), 400

    horas = get_prestamo_hours(prestamo_id)

    if horas is None:
        return jsonify({'message': 'Prestamo not found'}), 404

    return jsonify(horas), 200

def get_prestamo_info_route():
    data = request.get_json()
    prestamo_id = data.get('prestamo_id')
    
    if not prestamo_id:
        return jsonify({'message': 'Prestamo ID is required'}), 400

    prestamo_info = get_prestamo_info(prestamo_id)
    
    if prestamo_info is None:
        return jsonify({'message': 'Prestamo not found or invalid'}), 404

    return jsonify({'prestamo_info': prestamo_info}), 200

def get_prestamos_by_maestro_route():
    data = request.get_json()
    maestro_id = data.get('maestro_id')
    prestamos = get_prestamos_by_maestro(maestro_id)
    return jsonify({"prestamos": prestamos})


def get_all_proyectores_hours():
    proyector_horas = get_all_proyectores_horas_usadas()
    return jsonify(proyector_horas), 200

def get_all_maestros_hours():
    maestro_horas = get_maestro_horas_usadas()
    return jsonify(maestro_horas), 200

def get_all_proyectores_disponibilidad():
    proyector_disponibilidad = get_proyectores_disponibilidad()
    return jsonify(proyector_disponibilidad), 200

def create_prestamo_controller():
    data = request.json
    try:
        id_maestro = data.get('id_maestro')
        id_proyector = data.get('id_proyector')
        fecha_salida = datetime.strptime(data.get('fecha_salida'), '%Y-%m-%d').date()
        hora_salida = datetime.strptime(data.get('hora_salida'), '%H:%M:%S').time()
        fecha_entrada = datetime.strptime(data.get('fecha_entrada'), '%Y-%m-%d').date() if data.get('fecha_entrada') else None
        hora_entrada = datetime.strptime(data.get('hora_entrada'), '%H:%M:%S').time() if data.get('hora_entrada') else None

        nuevo_prestamo = create_prestamo(
            id_maestro=id_maestro,
            id_proyector=id_proyector,
            fecha_salida=fecha_salida,
            hora_salida=hora_salida,
            fecha_entrada=fecha_entrada,
            hora_entrada=hora_entrada
        )
        return jsonify({
            'id': nuevo_prestamo.id,
            'id_maestro': nuevo_prestamo.id_maestro,
            'id_proyector': nuevo_prestamo.id_proyector,
            'fecha_salida': nuevo_prestamo.fecha_salida.isoformat(),
            'hora_salida': nuevo_prestamo.hora_salida.isoformat(),
            'fecha_entrada': nuevo_prestamo.fecha_entrada.isoformat() if nuevo_prestamo.fecha_entrada else None,
            'hora_entrada': nuevo_prestamo.hora_entrada.isoformat() if nuevo_prestamo.hora_entrada else None
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400