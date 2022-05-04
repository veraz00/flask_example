from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 
from flask_ckeditor import CKEditor 
from flask_moment import Moment 
from flask_wtf import CSRFProtect
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()
login_manager = LoginManager()
csrf = CSRFProtect()
# The client sends a POST request with their credentials to authenticate
# If the credentials are correct, the server generates a session and CSRF token
# The request is sent back the client, and the session is stored in a cookie while the token is rendered in a hidden form field
# The client includes the session cookie and the CSRF token with the form submission
# The server validates the session and the CSRF token and accepts or rejects the request


@login_manager.user_loader
def load_user(user_id):
    from app.models import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in first'
login_manager.login_message_category = 'warning'
# for @login_required