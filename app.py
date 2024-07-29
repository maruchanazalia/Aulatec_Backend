from flask import Flask
from bd.bd import init_db
from flask_cors import CORS
from Jwt.auth import auth_blueprint
from api.user.user_routers import user_blueprint
from api.maestros.mae_routers import maestros_blueprint
from api.prestamos.pres_router import prestamo_blueprint
from api.proyectores.pro_routers import proyectores_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://martinez:123456789@aulatech.casexdopqnza.us-east-1.rds.amazonaws.com/aulatech'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

init_db(app)

# Registrar blueprints
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(proyectores_blueprint, url_prefix='/proyectores')
app.register_blueprint(maestros_blueprint, url_prefix='/maestros')
app.register_blueprint(prestamo_blueprint, url_prefix='/prestamos')

if __name__ == '__main__':
    app.run()
