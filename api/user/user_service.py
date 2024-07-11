from bd.bd import db
from api.user.user_model import Usuario

def get_all_users():
    return Usuario.query.all()

def delete_user(user_id):
    user = Usuario.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

def login_user(username, password):
    user = Usuario.query.filter_by(user=username).first()
    if user:
        print(f"User found: {user.user}")
        print(f"Password hash: {user.contrasena}")
        if user.check_password(password):
            print("Password matches")
            return user
        else:
            print("Password does not match")
    else:
        print("User not found")
    return None


def register_user(user, hashed_password, correo):
    new_user = Usuario(user=user, contrasena=hashed_password, correo=correo)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def change_password(user, new_password):
    user.contrasena = generate_password_hash(new_password)
    db.session.commit()
    return user
