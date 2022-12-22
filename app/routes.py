from flask import Flask, render_template, url_for, redirect, request, flash
from app import app, mysql
from app.forms import LoginForm, ContactForm
import sys


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/button/')
def button_clicked():
    print('Hello world!', file=sys.stderr)
    return redirect(url_for('index'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    print('12345')
    form = ContactForm()
    if request.method == 'POST':
        print('000')
        '''
            if form.submit.data:
                pass
            elif form.submit2.data:
                pass
        '''
        if form.submit1.data:
            print('123')
            button_clicked()
        elif form.submit2.data:
            print('234')
        else:
            pass # unknown
    return render_template('contact.html', form=form)



