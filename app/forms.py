
# ·登录表单； ·文章表单； ·分类表单；·登录表单； ·文章表单； ·分类表单；

from this import d
from unicodedata import category
from xml.dom import ValidationErr

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,\
    TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length, Optional, URL
from flask_ckeditor import CKEditorField

from app.models import Category 


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(1, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class SettingForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired(), Length(1, 30)])
    blog_title = StringField('Blog title', validators = [DataRequired(), Length(1, 60)])
    blog_sub_title = StringField('Blog sub title', validators = [DataRequired(), Length(1, 100)])
    about = CKEditorField('About page', validators = [DataRequired()])


class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired(), Length(1, 60)])
    category = SelectField('Category', coerce = int, default = 1)  # coerce is data type 
    body = CKEditorField('Body', validators = [DataRequired()])
    submit = SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)  # so self.title would be StringField
        self.category.choices = [(category.id, category.name) for category in Category.query.order_by(Category.name).all()]
    

class CategoryForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired(), Length(1, 30)])
    submit = SubmitField()
    
    def validate_name(self, field):
        if Category.query.filter_by(name = field.data).first():
            raise ValidationErr('Name already in use.')



class CommentForm(FlaskForm):
    author = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    site = StringField('Site', validators=[Optional(), URL(), Length(0, 255)])
    body = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField()


class AdminCommentForm(CommentForm):
    author = HiddenField()
    email = HiddenField()
    site = HiddenField()


class LinkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 30)])
    url = StringField('URL', validators=[DataRequired(), URL(), Length(1, 255)])
    submit = SubmitField()