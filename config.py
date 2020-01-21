import os

db_path = os.path.join(os.path.dirname(__file__), 'storage.db')
db_uri = 'sqlite:///{}'.format(db_path)

class General():
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = True