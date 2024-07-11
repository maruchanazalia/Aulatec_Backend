from flask import Blueprint
from api.maestros.mae_controllers import get_maestros, get_maestro, add_maestro, update_maestro_info, remove_maestro
from Jwt.auth import auth_required

maestros_blueprint = Blueprint('maestros', __name__)

@maestros_blueprint.route('/', methods=['GET'])
def maestros():
    return get_maestros()

@maestros_blueprint.route('/<int:maestro_id>', methods=['GET'])
def maestro(maestro_id):
    return get_maestro(maestro_id)

@maestros_blueprint.route('/', methods=['POST'])
def create():
    return add_maestro()

@maestros_blueprint.route('/<int:maestro_id>', methods=['PUT'])
def update(maestro_id):
    return update_maestro_info(maestro_id)

@maestros_blueprint.route('/<int:maestro_id>', methods=['DELETE'])
def delete(maestro_id):
    return remove_maestro(maestro_id)
