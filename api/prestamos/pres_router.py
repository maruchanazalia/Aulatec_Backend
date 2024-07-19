from flask import Blueprint
from api.prestamos.pres_controllers import get_maestro_and_proyector, get_prestamo_horas_usadas, get_total_horas_usadas_proyector

prestamo_blueprint = Blueprint('prestamo', __name__)

@prestamo_blueprint.route('/maestro_proyector', methods=['POST'])
def get_maestro_and_proyector_route():
    return get_maestro_and_proyector()

@prestamo_blueprint.route('/prestamo_horas', methods=['POST'])
def get_prestamo_horas_usadas_route():
    return get_prestamo_horas_usadas()

@prestamo_blueprint.route('/proyector_horas', methods=['POST'])
def get_total_horas_usadas_proyector_route():
    return get_total_horas_usadas_proyector()

