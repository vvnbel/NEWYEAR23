from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):

    submit1 = SubmitField('Do this')
    submit2 = SubmitField('Do that')

