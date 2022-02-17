from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField, PasswordField, BooleanField)
from wtforms.validators import ValidationError, DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login')