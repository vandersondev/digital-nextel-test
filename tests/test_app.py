import pytest


@pytest.fixture
def client_app():
    from app.app import app as app
    app.testing = True
    app = app.test_client()
    return app


def test_home(client_app):
    response = client_app.get('/')
    data = response.data.decode('utf-8')
    opt_city = '<option value="455821">Porto Alegre</option>'
    opt_weather = (
        '<input type="checkbox" class="form-check-input" '
        'id="weather_5" name="weather" value="cold">'
    )
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert opt_city in data
    assert opt_weather in data


def test_result_get(client_app):
    response = client_app.get('/result/')
    assert response.status_code == 302
    assert response.content_type == 'text/html; charset=utf-8'


def test_result_post(client_app):
    response = client_app.post('/result/', data={
        'city': 455821,
        'numberdays': 15,
        'weather': ['clear', 'partly cloudy', 'cold']}, follow_redirects=True)
    data = response.data.decode('utf-8')
    item = '<li>De 20 de Junho a 10 de Julho</li>'
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert item in data
