from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError, HiddenField, BooleanField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional, URL
from werkzeug.security import check_password_hash

class PostForm(FlaskForm):
    author = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    #email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    message = TextAreaField('Message', validators=[DataRequired()])
    天王盖地虎 = TextAreaField('天王盖地虎', validators=[DataRequired()])
    submit = SubmitField('Submit')

    

