from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
bootstrap = Bootstrap(app)

#DB CONFIGURATION
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)



@app.route('/')
def index():
    colors = ['red', 'blue', 'green']
    return render_template('index.html', colors=colors)


@app.route('/css')
def css():
    return render_template('css.html')


if __name__ == '__main__':
    app.run(debug=True)