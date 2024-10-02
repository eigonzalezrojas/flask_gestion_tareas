import os
from flask import Flask
from database import init_db
from routes.auth import auth_bp
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    init_db(app)

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app