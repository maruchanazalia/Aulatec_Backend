from flask import Blueprint
from api.proyectores.pro_controllers import get_proyectores, get_proyector, add_proyector, update_proyector_info, remove_proyector, send_projector_email

proyectores_blueprint = Blueprint('proyectores', __name__)

@proyectores_blueprint.route('/', methods=['GET'])
def proyectores():
    return get_proyectores()

@proyectores_blueprint.route('/<int:proyector_id>', methods=['GET'])
def proyector(proyector_id):
    return get_proyector(proyector_id)

@proyectores_blueprint.route('/', methods=['POST'])
def create():
    return add_proyector()

@proyectores_blueprint.route('/<int:proyector_id>', methods=['PUT'])
def update(proyector_id):
    return update_proyector_info(proyector_id)

@proyectores_blueprint.route('/<int:proyector_id>', methods=['DELETE'])
def delete(proyector_id):
    return remove_proyector(proyector_id)

@proyectores_blueprint.route('/send-email/<int:proyector_id>', methods=['POST'])
def send_email_route(proyector_id):
    return send_projector_email(proyector_id)