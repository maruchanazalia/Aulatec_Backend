from flask import Blueprint, request, jsonify
from functools import wraps
import jwt
from bd.bd import db
from api.user.user_model import Usuario

auth_blueprint = Blueprint('auth', __name__)

def generate_token(user_id):
    payload = {
        'user_id': user_id
    }
    token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
    return token

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            current_user = Usuario.query.get(data['user_id'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(*args, **kwargs)
    return decorated_function
