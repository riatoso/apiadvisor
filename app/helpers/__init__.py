import json
import requests
from app import app
from datetime import datetime

def weather_access(id):
    api_token = 'b22460a8b91ac5f1d48f5b7029891b53'
    api_url = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/'+id+'/days/15?token='+api_token
    headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
    return json.loads(requests.get(api_url, headers=headers).content)


@app.template_filter('date_format')
def date_format(date):
    date_object = datetime.strptime(date, '%Y-%m-%d')
    return datetime.strftime(date_object,'%d/%m/%Y')

@app.template_filter('format_precipitation')
def format_precipitation(value):
    return round(value, 3)
