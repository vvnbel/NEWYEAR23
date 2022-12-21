from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml
from config import Config
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
'''
app = Flask(__name__)
bootstrap = Bootstrap(app)


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

@app.route('/', methods=['GET', 'POST'])
def index():

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO books (`book_name`, `book_category`) VALUES ('обновил', 'нажал')")
    mysql.connection.commit()
    result_value = cursor.execute("SELECT * FROM books")
    print('СЧЕТЧИК КОЛ-ВА ЗАПИСЕЙ: ', result_value)
    colors = ['red', 'blue', 'green']

    if request.method == 'POST':
        form = request.form
        name = form['name']
        age = form['age']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO employee(name, age) VALUES(%s, %s)", (name, age))
        mysql.connection.commit()
    return render_template('index.html')

ButtonPressed = 0

@app.route('/formworkers', methods=['GET', 'POST'])
def formworkers():

    cursor = mysql.connection.cursor()
    cur = cursor.execute("SELECT firstname, lastname FROM persons")
    return render_template('formworkers.html', workers0=cursor.fetchall(), ButtonPressed=ButtonPressed)


@app.route('/process_data/', methods=['POST'])
def doit():
    index = request.form['index']
    print(index)

@app.route('/css')
def css():
    return render_template('css.html')


@app.route('/out', methods=['GET', 'POST'])
def out():
    list_ = [1111, 2222, 3333]
    return render_template('out.html', option=list_)


if __name__ == '__main__':
    app.run(debug=True)