
from flask import Flask, redirect, url_for, render_template, flash
from flask_login import (LoginManager, UserMixin, current_user,
login_user, login_required, logout_user)
import sys
sys.path.append('D:/zenglinlin/flask_example/flask_login')  # flask_login include config.py

from app.auth import auth
from app import db  # app -__init__.py
from app.models import User
from app.auth.forms import LoginForm

@auth.route('/', methods = ['GET'])
def index():
    print('-------------------------------------')
    flash('this is a flash message')
    return render_template('auth/index.html')  # index.html would auto detect the current_user 
    
@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:  # current_user是个函数对象最后调用的Login_Manager的_load_user函数，_load_user中调用了reload_user。
        return redirect(url_for('show_user'))  # function name
    form = LoginForm()
    if form.validate_on_submit():  # only used when it is 'POST', whether there are data submission    
        username = form.username.data 
        password = form.password.data 
        remember = form.remember_me.data 

        user = User.query.filter_by(username=username).first()
        if user:
            print('form.password:', password, 'hashed: ')
            if username == user.username and user.validate_password(password):  # check password hash
                login_user(user, remember)  
                # duration (datetime.timedelta) – The amount of time before the remember cookie expires.

                flash('login successfully')
                return redirect(url_for('auth.show_user'))
        else:
            flash('wrong in password or username')
            return redirect(url_for('login'))
    return render_template('auth/login.html', form = form) # it is used when it is 'GET'

@auth.route('/showuser')
@login_required
def show_user():
    username = current_user.username
    return render_template('auth/index.html', username = username)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))  # where is form, message??