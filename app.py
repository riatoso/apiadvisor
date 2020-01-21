from app import app,manager,db

from flask import request, render_template
from app import helpers
from app.models.tables import Weather
from datetime import datetime
from sqlalchemy.sql.expression import func


@app.route('/')
def index():
    return render_template('index.html', title='Home',added=False)


@app.route('/cidade')
def cidade():
    cidade_pesquisada = request.args.get('id')

    if(cidade_pesquisada == ''):
        return 'Você esqueceu de passar a cidade'

    response = helpers.weather_access(cidade_pesquisada)
    
    for data in response['data']:
        weather_create = Weather(
            cidade=response['name'],
            estado=response['state'],
            pais=response['country'].strip(),
            data=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            probabilidade=data['rain']['probability'],
            precipitacao=data['rain']['precipitation'],
            min=data['temperature']['min'],
            max=data['temperature']['max'],
            code=cidade_pesquisada
        )
        db.session.add(weather_create)

    db.session.commit()

    if('error' in response):
        return 'Opa, ocorreu um erro ao acessar a api: '+str(response['detail'])

    return render_template('index.html', title='Cidade',added=True)


@app.route('/api/cidade/')
@app.route('/api/cidade/<id>')
def api_cidade(id=None):

    if id == None:
        return {
            'error':'No id',
            'msg': 'Você esqueceu de passar um ID'
        }


    response = helpers.weather_access(id)

    if('error' in response):
        return {
            'error': str(response['detail']),
            'msg': 'Sinto muito, mas você nâo tem acesso'
        }

    return response


@app.route('/analise')
def analise():

    inicial = request.args.get('data_inicial')
    final = request.args.get('data_final')

    error = None

    try:
        datetime.strptime(inicial, '%Y-%m-%d')
        datetime.strptime(final, '%Y-%m-%d')
    except:
        return 'As datas tem que ser no format YYYY-mm-dd'


    maxima = db.session.query('cidade','max','data',func.max(Weather.max)).filter(Weather.data.between(inicial, final)).order_by(Weather.data.desc()).first()
    media_precipitacao = db.session.execute('select cidade,avg(precipitacao) as precipitacao from weather group by cidade')

    print(media_precipitacao)

    return render_template('analise.html', title='Analise', maxima=maxima, medias=media_precipitacao)


if __name__ == "__main__":
    manager.run()
