import json
import requests

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

get_vacations_days(455821, 15, ['clear', 'partly cloudy', 'cold'])