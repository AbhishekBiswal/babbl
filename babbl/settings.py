from babbl import app
from models import db

DEBUG = True
SECRET_KEY = '2a4fa65248b047845bddcc970ac87ef9a5b3cd3673483479'

app.secret_key = 'abhishekbiswal123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/babbl'
db.init_app(app)
