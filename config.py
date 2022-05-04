
from email.mime import base
import os, sys 
from decouple import config
basedir = os.path.abspath(os.path.dirname(__file__))
print('basedir: ', basedir) # D:\zenglinlin\flask_example\flask_sayhello

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True # 587
    MAIL_USE_SSL = False # 465
    MAIL_USERNAME = config('MAIL_USERNAME')
    # os.getenv('MAIL_USERNAME') or 'zenglinlin00@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD') 
    # os.getenv('MAIL_PASSWORD') or 'Godgod630!'

    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)
    # python -m smtpd -n -c DebuggingServer localhost:587 

    BLUEBLOG_EMAIL = config('MAIL_USERNAME') 
    BLUEBLOG_POST_PER_PAGE = 10
    BLUEBLOG_MANAGE_POST_PER_PAGE = 15
    BLUEBLOG_COMMENT_PER_PAGE = 8
    BLUEBLOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    DEBUG =True
    BOOTSTRAP_SERVE_LOCAL = True
    
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_CODE_THEME = 'monokai_sublime'
    CKEDITOR_SERVE_LOCAL = True


    WTF_CSRF_CHECK_DEFAULT  = False
    # CKEDITOR_FILE_UPLOADER = 'admin_bp.upload_image' # view function

class ProductionConfig(Config):
    None 

    
config_map = {
    'development': DevelopmentConfig, 'production': ProductionConfig
}
