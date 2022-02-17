from collections import UserList
import os
from wsgiref.validate import validator 
from flask import Flask, redirect, url_for, render_template, flash
from flask_login import (LoginManager, UserMixin, current_user,
login_user, login_required, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import sys
sys.path.append('D:/zenglinlin/flask_example/flask_login')  # flask_login include config.py
from config import config1
app = Flask(__name__)
app.config.from_object(config1['dev'])

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth/login'  # 验证失败跳转的界面
login_manager.login_message ='login_manager.login_message!'  # login-message：用户重定向到登录页面时闪出的消息

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    user = User.query.get(int(user_id))
    if user != None:
        return user
# user_loader 回调函数
# user session 记录的是用户 ID (user_id)，回调函数的作用就是通过 user_id 返回对应的 User 对象。
# user_loader 回调函数在 user_id 非法的时候不应该抛出异常，而要返回 None。没有这个回调函数的话，Flask-Login 将无法工作


db = SQLAlchemy(app)
db.app = app

def create_app(config_name): # 'dev'
    
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()  # create db here !!

    #     from app.models import User
    #     user = User(username='zeng')
    #     user.set_password('linlin')
    #     db.session.add(user)
    #     db.session.commit()

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    return app

