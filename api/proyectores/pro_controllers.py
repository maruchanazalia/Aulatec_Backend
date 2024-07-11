from flask import jsonify, request
from api.proyectores.pro_service import get_all_Pro, delete_pro, create_pro

def get_proyectores():
    proyectores = get_all_Pro()
    return jsonify([{'id': pro.id, 'marca': pro.marca} for pro in proyectores])

def remove_proyector(pro_id):
    success = delete_pro(pro_id)
    if success:
        return jsonify({'message': 'Proyector deleted successfully'}), 200
    return jsonify({'message': 'Proyector not found'}), 404

def add_proyector():
    data = request.get_json()
    proyector = create_pro(data['marca'])
    return jsonify({'id': proyector.id, 'marca': proyector.marca}), 201
