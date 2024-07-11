from flask import Blueprint
from api.proyectores.pro_controllers import get_proyectores, remove_proyector, add_proyector
from Jwt.auth import auth_required

proyectores_blueprint = Blueprint('proyectores', __name__)

@proyectores_blueprint.route('/', methods=['GET'])
#@auth_required
def proyectores():
    return get_proyectores()

@proyectores_blueprint.route('/<int:pro_id>', methods=['DELETE'])
#@auth_required
def delete(pro_id):
    return remove_proyector(pro_id)

@proyectores_blueprint.route('/', methods=['POST'])
#@auth_required
def create():
    return add_proyector()
