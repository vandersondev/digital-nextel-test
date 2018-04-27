from app.getdata import (
        get_cities,
        get_city_by_id,
        get_weather,
        get_vacations_days
    )


def test_get_cities():
    cities = get_cities()
    item = {'name': 'Porto Alegre', 'id': '455821'}
    assert item == cities[0]


def test_get_city_by_id():
    city = get_city_by_id('455821')
    assert city == 'Porto Alegre'


def test_get_weather():
    weathers = get_weather()
    assert 'cold' in weathers


def test_get_vacations_days():
    vacations_days = get_vacations_days(455825, 15, [
        'clear',
        'hot',
        'partly cloudy',
        'fair'])
    assert vacations_days[0] == ('2018-11-10', '2018-12-01')
