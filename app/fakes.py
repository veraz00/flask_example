from app.models import Admin
from app.extensions import db 


def fake_admin():
    admin = Admin(
        username = 'admin',
        blog_title = 'Blueblog',
        blog_sub_title = 'No, I am the real thig',
        name = 'ZENG Linlin',
        about = 'Umm, I, in the best time of life'
    )
    admin.set_password('helloflask')
    db.session.add(admin)
    db.session.commit()


from faker import Faker
from app.models import Category, Post, Comment
from app.extensions import db 
import random 
from sqlalchemy.exc import IntegrityError


fake = Faker()

def fake_categories(count = 10):
    category = Category(name = 'Default')
    db.session.add(category)
    for i in range(count):
        category = Category(name= fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()  # if generate the duplicates word, it would roll back 
        
def fake_posts(count = 50):
    for i in range(count):
        post = Post(title = fake.sentence(),\
            body = fake.text(2000), 
            category = Category.query.get(random.randint(1, Category.query.count())),
            timestamp = fake.date_time_this_year())
        db.session.add(post)
    db.session.commit()


def fake_comments(count = 500):
    for i in range(count):
        comment = Comment(author = fake.name(), \
        email = fake.email(), \
        site = fake.url(),\
        body = fake.text(100),\
        reviewed = True,\
        post = Post.query.get(random.randint(1, Post.query.count())))
        db.session.add(comment)

    salt = int(count * 0.1)
    for _ in range(salt):
        comment = Comment(author = fake.name(), \
        email = fake.email(), \
        site = fake.url(),\
        body = fake.text(100),\
        timestamp=fake.date_time_this_year(),\
        reviewed = False, \
        post = Post.query.get(random.randint(1, Post.query.count())))
        db.session.add(comment)

        comment = Comment(author = fake.name(), \
        email = fake.email(), \
        site = fake.url(),\
        body = fake.text(100),\
        from_admin = True,\
        post = Post.query.get(random.randint(1, Post.query.count())))
        db.session.add(comment)
    db.session.commit()

    for _ in range(salt):
        comment = Comment(author = fake.name(), \
        email = fake.email(), \
        site = fake.url(),\
        body = fake.text(100),\
        reviewed = True,\
        post = Post.query.get(random.randint(1, Post.query.count())),\
        replied = Comment.query.get(random.randint(1, Comment.query.count())))
        db.session.add(comment)
    db.session.commit()
