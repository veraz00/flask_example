from flask_login import (LoginManager, UserMixin, current_user,
login_user, login_required, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import sys
sys.path.append('D:/zenglinlin/flask_example/flask_login')  # flask_login include config.py

from app import db, login_manager

class User(UserMixin, db.Model):  # UserMixin: user with is_authentification 
    __tablename__ = 'tbl_user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)

    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<user %s>' % self.username


def init_db():
    db.create_all()  # would not init db

    # Create a test user
    new_user = User(username = 'linlin00')
    new_user.set_password('zeng')
    db.session.add(new_user)
    db.session.commit()

import sqlite3
if __name__ == '__main__':  # how to print the username
    
    
    init_db()
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from tbl_user"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", records)
    print(len(records))