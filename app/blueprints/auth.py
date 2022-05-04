
from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_user, current_user, logout_user

from app.forms import LoginForm
from app.models import Admin 
from app.utils import redirect_back

auth_bp = Blueprint('auth', __name__, template_folder = 'templates')  
# 在蓝本对象的名称后添加一个_bp后缀（即blueprint的简写）
# 构造方法中的第一个参数是蓝本的名称；第二个 参数是包或模块的名称

# = auth_bp.add_url_rule()
# add_url_rule（rule，endpoint，view_func）=>/hello（URL规则） - > say_hello（端点） - > say_hello（视图函数）


@auth_bp.route('/login', methods = ['GET', 'POST'])  
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data 
        remember = form.remember.data 
        
        admin = Admin.query.first()  # 从数据库中查询出Admin对象，
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back', 'info')
                return redirect_back()
            flash('Invaid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form = form)
# if there is redirect_back(); the link in response page qould be http://192.168.1.13:8000/auth/login?next=%2F%3F

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout success!', 'info')
    return redirect_back()