import requests

from flask import Flask, render_template, abort, request, redirect, url_for
from app.getdata import get_cities, get_city_by_id, get_weather, get_vacations_days

app = Flask('app')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


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
        city = get_city_by_id(request.form.get('city'))
        return render_template('result.html', city=city, vacation_dates=vacation_dates)
    else:
        return redirect(url_for('home'))