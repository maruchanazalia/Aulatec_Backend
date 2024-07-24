from flask import Blueprint
from api.prestamos.pres_controllers import get_maestro_and_proyector, get_prestamo_horas_usadas, get_total_horas_usadas_proyector,get_all_prestamos, get_prestamo_hours, get_prestamo_info_route, get_prestamos_by_maestro_route, get_all_proyectores_hours, get_all_maestros_hours, get_all_proyectores_disponibilidad, create_prestamo_controller

prestamo_blueprint = Blueprint('prestamo', __name__)

@prestamo_blueprint.route('/prestamos', methods=['GET'])
def get_all_prestamos_route():
    return get_all_prestamos()

@prestamo_blueprint.route('/maestro_proyector', methods=['POST'])
def get_maestro_and_proyector_route():
    return get_maestro_and_proyector()

@prestamo_blueprint.route('/prestamo_horas', methods=['POST'])
def get_prestamo_horas_usadas_route():
    return get_prestamo_horas_usadas()

@prestamo_blueprint.route('/proyector_horas', methods=['POST'])
def get_total_horas_usadas_proyector_route():
    return get_total_horas_usadas_proyector()

@prestamo_blueprint.route('/prestamo_horas', methods=['POST'])
def get_prestamo_hours_route():
    return get_prestamo_hours()

@prestamo_blueprint.route('/prestamo_info', methods=['POST'])
def prestamo_info():
    return get_prestamo_info_route()

@prestamo_blueprint.route('/prestamos_by_maestro', methods=['POST'])
def prestamos_by_maestro():
    return get_prestamos_by_maestro_route()

@prestamo_blueprint.route('/horas', methods=['GET'])
def get_all_proyectores_horas():
    return get_all_proyectores_hours()

@prestamo_blueprint.route('/mae_horas', methods=['GET'])
def get_all_maestros_horas():
    return get_all_maestros_hours()

@prestamo_blueprint.route('/disponibilidad', methods=['GET'])
def get_all_proyectores_disponibilidad_route():
    return get_all_proyectores_disponibilidad()

@prestamo_blueprint.route('/nuevo_pres', methods=['POST'])
def create_prestamo_route():
    return create_prestamo_controller()