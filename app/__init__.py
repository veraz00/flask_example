from flask import Flask 
import sys, os 
import click
from flask_migrate import Migrate 
from app.extensions import db, bootstrap, moment
sys.path.append('..')

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    Migrate(app, db)


def register_blueprints(app):
    from app.views.sayhello import sayhello
    app.register_blueprint(sayhello, url_prefix = '/sayhello')


def register_commands(app):
    @app.cli.command()  # add command to flask-- flask forge
    # @click.option('--name', prompt = True, help = 'author')  # click.argument() to add argument
    def forge():
        from app.faker import fake_message 
        click.echo('generate message--------')
        fake_message()

        click.echo('Done!')


def create_app(config_name = 'develop'):
    app = Flask(__name__)
    from config import config_map 

    app.config.from_object(config_map[config_name])
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    from app import models 
    return app 