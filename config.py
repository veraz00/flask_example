
from email.mime import base
import os, sys 
basedir = os.path.abspath(os.path.dirname(__file__))
print('basedir: ', basedir) # D:\zenglinlin\flask_example\flask_sayhello

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    BOOTSTRAP_SERVE_LOCAL = True

class DevelopmentConfig(Config):
    PER_PAGE = 20
    DEBUG = True

class ProductionConfig(Config):
    None 

    
config_map = {
    'develop': DevelopmentConfig, 'product': ProductionConfig
}
