from flask import Flask 
import sys, os 
from flask_migrate import Migrate

sys.path.append('..')
from app.blueprints.auth import auth_bp
from app.blueprints.admin import admin_bp
from app.blueprints.blog import blog_bp
from config import config_map
from app.extensions import bootstrap, db, moment, ckeditor, mail , login_manager, csrf
from app.fakes import fake_admin, fake_categories, fake_comments, fake_posts
from app.models import Admin, Category, Comment

from flask_wtf.csrf import CSRFError 
from flask import render_template
from flask_login import current_user


def register_errors(app):
    
    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template('400.html', description = e.description), 400
# add csrf into admin template ??


def register_blueprint(app):
    app.register_blueprint(auth_bp, url_prefix = '/auth')  # so the statics file would be auth.static by default
    app.register_blueprint(admin_bp, url_prefix = '/admin')
    app.register_blueprint(blog_bp)


def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    moment.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)
    csrf.init_app(app)
    return app 


import click 
def register_commands(app):

    @app.cli.command()
    @click.option('--username', prompt=True, help = 'The usernmae used to login')
    # 将prompt设为True则默认会使用选项值的首字母大写形式作为 提示字符。
    @click.option('--password', prompt = True, hide_input= True, confirmation_prompt= True, help = 'password')
    def init(username, password):
        click.echo('initializing the database...')
        db.create_all()
        admin = Admin.query.first()
        if admin:
            click.echo('The auth already exits, updating...')
            admin.username = username 
            admin.set_password(password)
        else:
            click.echo('creating the temporary auth account...')
            admin =Admin(username = username, blog_title = 'Bluelog',\
            blog_sub_title = 'No, I am a real thing',\
            name = 'Admin', about = 'Anything about you')
            admin.set_password(password)
            db.session.add(admin)
        

    @app.cli.command()
    @click.option('--category', default = 10, help = 'number of category')
    @click.option('--post', default = 50)
    @click.option('--comment', default = 500)
    def forge(category, post, comment):
        db.drop_all()
        db.create_all()

        click.echo('Generating the administator------')
        fake_admin()

        click.echo('Generating %d categories...' % category) 
        fake_categories(category) 
        click.echo('Generating %d posts...' % post) 
        fake_posts(post) 
        click.echo('Generating %d comments...' % comment) 
        fake_comments(comment) 
        click.echo('Done.')
# 管理员→分类→文章→ 评论。


def register_template_context(app):
    @app.context_processor
    def make_template_context():
        admin = Admin.query.first()
        categories = Category.query.order_by(Category.name).all()
        if current_user.is_authenticated:
            unread_comments = Comment.query.filter_by(reviewed = False).count()
        else:
            unread_comments = None
        return dict(admin= admin, categories=categories, unread_comments = unread_comments)



def create_app(config_name = 'development'):
    app = Flask(__name__)
    from config import config_map 

    app.config.from_object(config_map[config_name])
    register_blueprint(app)
    register_extensions(app)
    register_commands(app)
    register_template_context(app)
    register_errors(app)
    from app import models 

    return app 