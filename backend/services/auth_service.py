# Servicio de autenticación
from models.user import User
from database import db


def register_user(username, password):
    if User.query.filter_by(username=username).first():
        return {"msg": "Usuario ya existe"}, 409

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return {"msg": "Usuario registrado exitosamente"}, 201


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return {"msg": "Credenciales incorrectas"}, 401

    return {"msg": "Autenticación exitosa", "user_id": user.id}, 200
