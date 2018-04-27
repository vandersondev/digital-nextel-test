import requests

from flask import abort


BASEURL = 'http://localhost:8882'


def get_cities():
    r_cities = requests.get(BASEURL + '/cities/')
    cities = []
    if r_cities.status_code == 200:
        r_cities_data = r_cities.json()
        for i in r_cities_data:
            cities.append({'name': i['district'], 'id': i['woeid']})
        return cities
    else:
        abort(404)


def get_city_by_id(id):
    r_cities = requests.get(BASEURL + '/cities/')
    if r_cities.status_code == 200:
        r_cities_data = r_cities.json()
        for i in r_cities_data:
            if i['woeid'] == id:
                return i['district']


def get_weather():
    r_weather = requests.get(BASEURL + '/weather/')
    weather = []
    if r_weather.status_code == 200:
        r_weather_data = r_weather.json()
        for i in r_weather_data:
            weather.append(i['name'])
        return weather
    else:
        abort(404)


def get_vacations_days(city, days, weathers):
    r_calendar = requests.get(BASEURL + '/cities/{}/year/2018/'.format(city))
    if r_calendar.status_code == 200:
        r_calendar_data = r_calendar.json()
        vacation_days_list = vacation_dates = []
        for date in r_calendar_data:
            if date['weather'] in weathers:
                vacation_days_list.append(date)
            else:
                if len(vacation_days_list) >= days:
                    vacation_dates.append(
                        (vacation_days_list[0]['date'],
                            vacation_days_list[-1]['date'])
                    )
                    vacation_days_list = []
                else:
                    vacation_days_list = []
        return vacation_dates
    else:
        abort(404)
