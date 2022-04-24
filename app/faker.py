
import random

from faker import Faker 
from app.models import Message 
from app.extensions import db 

fake = Faker()

def fake_message(count = 50):
    for i in range(count):
        post = Message(name=fake.word(),\
        message = fake.text(40),\
        timestamp = fake.date_time_this_year())
        db.session.add(post)
    db.session.commit()