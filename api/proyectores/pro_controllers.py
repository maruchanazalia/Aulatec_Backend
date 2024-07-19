from flask import jsonify, request, render_template
from api.proyectores.pro_service import get_all_proyectores, get_proyector_by_id, create_proyector, update_proyector, delete_proyector
#from api.email_service import send_email

def get_proyectores():
    proyectores = get_all_proyectores()
    return jsonify([{'id': p.id, 'marca': p.marca, 'status': p.status, 'numero_serie': p.numero_serie, 'lumens': p.lumens} for p in proyectores])

def get_proyector(proyector_id):
    proyector = get_proyector_by_id(proyector_id)
    if proyector:
        return jsonify({'id': proyector.id, 'marca': proyector.marca, 'status': proyector.status, 'numero_serie': proyector.numero_serie, 'lumens': proyector.lumens}), 200
    return jsonify({'message': 'Proyector not found'}), 404

def add_proyector():
    data = request.get_json()
    proyector = create_proyector(data['marca'], data['status'], data['numero_serie'], data['lumens'])
    return jsonify({'id': proyector.id, 'marca': proyector.marca, 'status': proyector.status, 'numero_serie': proyector.numero_serie, 'lumens': proyector.lumens}), 201

def update_proyector_info(proyector_id):
    data = request.get_json()
    proyector = update_proyector(proyector_id, data['marca'], data['status'], data['numero_serie'], data['lumens'])
    if proyector:
        return jsonify({'id': proyector.id, 'marca': proyector.marca, 'status': proyector.status, 'numero_serie': proyector.numero_serie, 'lumens': proyector.lumens}), 200
    return jsonify({'message': 'Proyector not found'}), 404

def remove_proyector(proyector_id):
    success = delete_proyector(proyector_id)
    if success:
        return jsonify({'message': 'Proyector deleted successfully'}), 200
    return jsonify({'message': 'Proyector not found'}), 404


def send_projector_email(proyector_id):
    proyector = get_proyector_by_id(proyector_id)
    if proyector:
        to = "maestro@example.com" 
        subject = "Estado del Proyector"
        template = render_template('projector_email.html', marca=proyector.marca, status=proyector.status, numero_serie=proyector.numero_serie)
        send_email(to, subject, template)
        return jsonify({'message': 'Correo enviado exitosamente'}), 200
    return jsonify({'message': 'Proyector no encontrado'}), 404