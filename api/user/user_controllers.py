from flask import jsonify, request
from werkzeug.security import generate_password_hash  # Importa generate_password_hash
from api.user.user_service import get_all_users, delete_user, login_user, register_user, change_password
from Jwt.auth import generate_token

def get_users():
    users = get_all_users()
    return jsonify([{'id': user.id, 'user': user.user} for user in users])

def remove_user(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

def login():
    data = request.get_json()
    user = login_user(data['user'], data['contrasena'])
    if user:
        token = generate_token(user.id)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

def register():
    data = request.get_json()
    user = data.get('user')
    contrasena = data.get('contrasena')
    correo = data.get('correo') 
    hashed_password = generate_password_hash(contrasena)
    new_user = register_user(user, hashed_password, correo)
    return jsonify({'id': new_user.id, 'user': new_user.user}), 201

def update_password():
    data = request.get_json()
    username = data.get('user')
    new_password = data.get('new_password')
    user = Usuario.query.filter_by(user=username).first()
    if user:
        user = change_password(user, new_password)
        return jsonify({'message': 'Password updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404
