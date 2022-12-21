from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
'''

#DB CONFIGURATION
app.config.from_object(Config)
db = yaml.load('db.yaml', Loader=yaml.Loader)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '6439247185'
app.config['MYSQL_DB'] = 'cockdb'
mysql = MySQL(app)
'''

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
'''


from app import routes