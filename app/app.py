import json
import requests

from datetime import datetime
from flask import Flask, render_template, abort, request, redirect, url_for

app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def get_cities():
    r_cities = requests.get('http://localhost:8882/cities/')
    cities = []
    if r_cities.status_code == 200:
        r_cities_data = json.loads(r_cities.text)
        for i in r_cities_data:
            cities.append({'name': i['district'], 'id': i['woeid']})
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


@app.route("/", methods=['GET'])
def home():
    cities = get_cities()
    weather_list = get_weather()
    return render_template('home.html', cities=cities, weather_list=weather_list)


@app.route("/result/", methods=['GET', 'POST'])
def result():
    if request.method == "POST":
        city_id = request.form.get('city')
        numberdays = request.form.get('numberdays')
        weathers = request.form.getlist('weather')
        vacation_list = get_vacations_days(city_id, int(numberdays), weathers)
        vacation_dates = []
        mounth = {
            '01':'Janeiro',
            '02':'Fevereiro',
            '03':'Março',
            '04':'Abril',
            '05':'Maio',
            '06':'Junho',
            '07':'Julho',
            '08':'Agosto',
            '09':'Setembro',
            '10':'Outubro',
            '11':'Novembro',
            '12':'Dezembro'
        }
        for dates in vacation_list:
            dateinit = dates[0].split('-')
            dateend = dates[1].split('-')
            vacation_dates.append({
                'dayinit' : dateinit[2],
                'monthinit' : mounth[dateinit[1]],
                'dayend' : dateend[2],
                'monthend' : mounth[dateend[1]],
            })
        vacation_dates.reverse()
        city = get_city_by_id(request.args.get('city'))
        return render_template('result.html', city=city, vacation_dates=vacation_dates)
    else:
        return redirect(url_for('home'))