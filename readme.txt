// Ativar servidor interno
source ENV/bin activate        

// Rodar servidor interno
FLASK_ENV=development python3 app.py runserver

// Rodar as migrations
python3 app.py db init
python3 app.py db migrate
python3 app.py db upgrade

// Urls
Gravar dados no banco - http://127.0.0.1:5000/cidade?id=3680
Acesso api externa com retorno em json - http://127.0.0.1:5000/api/cidade/3680
Analise de precipitacao e maior temperatura - http://127.0.0.1:5000/analise?data_inicial=2020-01-21&data_final=2020-01-25

//Banco sqllite
storage.db

// Cidades consultadas e gravadas no banco
Araras
Araraquara
Ribeirão Preto
São Paulo
Florianópolis