from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
'''
app = Flask(__name__)
bootstrap = Bootstrap(app)

#DB CONFIGURATION

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
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO books (`book_name`, `book_category`) VALUES ('обновил', 'нажал')")
    mysql.connection.commit()
    result_value = cursor.execute("SELECT * FROM books")
    print('СЧЕТЧИК КОЛ-ВА ЗАПИСЕЙ: ', result_value)
    colors = ['red', 'blue', 'green']

    return render_template('index.html', colors=colors)


@app.route('/css')
def css():
    return render_template('css.html')


@app.route('/out')
def out():
    list_ = [1111, 2222, 3333]
    return render_template('out.html', option=list_)


if __name__ == '__main__':
    app.run(debug=True)