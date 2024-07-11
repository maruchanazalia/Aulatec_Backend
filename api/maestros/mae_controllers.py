from flask import jsonify, request
from api.maestros.mae_service import get_all_maestros, get_maestro_by_id, create_maestro, update_maestro, delete_maestro

def get_maestros():
    maestros = get_all_maestros()
    return jsonify([{'id': m.id, 'nombre': m.nombre, 'ape_paterno': m.ape_paterno, 'ape_materno': m.ape_materno, 'correo': m.correo} for m in maestros])

def get_maestro(maestro_id):
    maestro = get_maestro_by_id(maestro_id)
    if maestro:
        return jsonify({'id': maestro.id, 'nombre': maestro.nombre, 'ape_paterno': maestro.ape_paterno, 'ape_materno': maestro.ape_materno, 'correo': maestro.correo}), 200
    return jsonify({'message': 'Maestro not found'}), 404

def add_maestro():
    data = request.get_json()
    maestro = create_maestro(data['nombre'], data['ape_paterno'], data['ape_materno'], data['correo'])
    return jsonify({'id': maestro.id, 'nombre': maestro.nombre, 'ape_paterno': maestro.ape_paterno, 'ape_materno': maestro.ape_materno, 'correo': maestro.correo}), 201

def update_maestro_info(maestro_id):
    data = request.get_json()
    maestro = update_maestro(maestro_id, data['nombre'], data['ape_paterno'], data['ape_materno'], data['correo'])
    if maestro:
        return jsonify({'id': maestro.id, 'nombre': maestro.nombre, 'ape_paterno': maestro.ape_paterno, 'ape_materno': maestro.ape_materno, 'correo': maestro.correo}), 200
    return jsonify({'message': 'Maestro not found'}), 404

def remove_maestro(maestro_id):
    success = delete_maestro(maestro_id)
    if success:
        return jsonify({'message': 'Maestro deleted successfully'}), 200
    return jsonify({'message': 'Maestro not found'}), 404
