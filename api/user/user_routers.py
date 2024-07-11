from flask import Blueprint
from api.user.user_controllers import get_users, remove_user, login, register, update_password
from Jwt.auth import auth_required

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def users():
    return get_users()

@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
    return remove_user(user_id)

@user_blueprint.route('/login', methods=['POST'])
def user_login():
    return login()

@user_blueprint.route('/register', methods=['POST'])
def user_register():
    return register()

@user_blueprint.route('/password', methods=['PUT'])
def update_password():
    data = request.get_json()
    username = data.get('user')
    new_password = data.get('new_password')
    user = Usuario.query.filter_by(user=username).first()
    if user:
        user = change_password(user, new_password)
        return jsonify({'message': 'Password updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

