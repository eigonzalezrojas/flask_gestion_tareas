import pytest
from backend import create_app
from backend.database import db


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
    yield app
    db.session.remove()
    db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_register(client):
    response = client.post('/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    assert response.get_json()['msg'] == 'Usuario registrado exitosamente'


def test_login(client):
    # Registrar primero al usuario
    client.post('/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })

    # Intentar iniciar sesión
    response = client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert response.get_json()['msg'] == 'Autenticación exitosa'