from flask import jsonify, request
from api.prestamos.pres_service import get_maestro_and_proyector_by_prestamo, get_prestamo_horas, get_proyector_horas_usadas

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
