import pytest


@pytest.fixture
def client_app():
    from app.app import app as app
    app.testing = True
    app = app.test_client()
    return app


def test_home(client_app):
    response = client_app.get('/')
    assert response.status_code == 200