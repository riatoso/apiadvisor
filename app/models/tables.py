from app import db

class Weather(db.Model):
    __tablename__ = "weather"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cidade = db.Column(db.String(80), unique=False, nullable=False)
    estado = db.Column(db.String(2), unique=False, nullable=False)
    pais = db.Column(db.String(80), unique=False, nullable=False)
    data = db.Column(db.Date, unique=False, nullable=False)
    probabilidade = db.Column(db.String(80), unique=False, nullable=False)
    precipitacao = db.Column(db.String(80), unique=False, nullable=False)
    min = db.Column(db.String(80), unique=False, nullable=False)
    max = db.Column(db.String(80), unique=False, nullable=False)
    code = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, cidade, estado, pais, data, probabilidade, precipitacao, min, max, code):
        self.cidade = cidade
        self.estado = estado
        self.pais= pais
        self.data= data
        self.probabilidade= probabilidade
        self.precipitacao= precipitacao
        self.min= min
        self.max= max
        self.code= code

    def __repr__(self):
        return '<Weather %r>' % self.cidade