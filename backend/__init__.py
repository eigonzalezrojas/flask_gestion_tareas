import os
from flask import Flask
from database import init_db, db
from routes.auth import auth_bp
from dotenv import load_dotenv
from flask_migrate import Migrate


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@db:3306/{os.getenv('MYSQL_DATABASE')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Inicializa la base de datos
    init_db(app)

    # Flask-Migrate para gestionar las migraciones
    migrate = Migrate(app, db)  # Conectar Migrate con SQLAlchemy

    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
