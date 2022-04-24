
import os
from datetime import datetime

from app.extensions import bootstrap, db

class Message(db.Model):
    __tablename__ = 'tbl_message'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(24))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index = True)  
