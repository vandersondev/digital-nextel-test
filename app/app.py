import json
import requests

from datetime import datetime
from flask import Flask, render_template, abort, request

app = Flask('app')

def get_cities():
    r_cities = requests.get('http://localhost:8882/cities/')
    cities = []
    if r_cities.status_code == 200:
        r_cities_data = json.loads(r_cities.text)
        for i in r_cities_data:
            cities.append({'name': i['district'], 'id': i['woeid']})
        print(cities)
        return cities
    else:
        abort(404)


def get_city_by_id(id):
    r_cities = requests.get('http://localhost:8882/cities/')
    if r_cities.status_code == 200:
        r_cities_data = json.loads(r_cities.text)
        for i in r_cities_data:
            if i['woeid'] == id:
                return i['district']


def get_weather():
    r_weather = requests.get('http://localhost:8882/weather/')
    weather = []
    if r_weather.status_code == 200:
        r_weather_data = json.loads(r_weather.text)
        for i in r_weather_data:
            weather.append(i['name'])
        print(weather)
        return weather
    else:
        abort(404)


def get_vacations_days(city, days, weathers):
    r_calendar = requests.get('http://localhost:8882/cities/{}/year/2018/'.format(city))
    if r_calendar.status_code == 200:
        r_calendar_data = json.loads(r_calendar.text)
        vacation_days_list = vacation_dates = []
        for date in r_calendar_data:
            if date['weather'] in weathers:
                vacation_days_list.append(date)
            else:
                if len(vacation_days_list) >= days:
                    vacation_dates.append((vacation_days_list[0]['date'], vacation_days_list[-1]['date']))
                    vacation_days_list = []
                else:
                    vacation_days_list = []
        return vacation_dates
    else:
        abort(404)


@app.route("/")
def home():
    cities = get_cities()
    weather_list = get_weather()
    return render_template('home.html', cities=cities, weather_list=weather_list)


@app.route("/result/", methods=['GET'])
def result():
    city = get_city_by_id(request.args.get('cidade'))
    dias = request.args.get('qtd_dias')
    list_clima = request.args.getlist('clima')
    #vacation_list = get_vacations_days(city, dias, list_clima)
    vacation_list = get_vacations_days(455825, 15, ['clear', 'hot', 'partly cloudy', 'fair'])
    print(vacation_list)
    dt = datetime.strptime(vacation_list[0][0], '%Y-%m-%d')
    print(dt.day)
    return render_template('result.html', city=city)