
from werkzeug.security import generate_password_hash, check_password_hash
import re 
from app.utils import *
from app.extensions import db 
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    blog_title = db.Column(db.String(60))
    blog_sub_title = db.Column(db.String(100))
    name = db.Column(db.String(30))
    about = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        # method$salt$hash
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique=True)
    posts = db.relationship('Post', back_populates = 'category')  # correspond1
    # Category'posts  
    # Post.category
    def delete(self):
        default_category = Category.query.get(1)
        posts = self.posts[:]
        for post in posts:
            post.category = default_category
        db.session.delete(self)
        db.session.commit()

from datetime import datetime 



class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60))
    # slug = slugify(title)
    body = db.Column(db.Text)
    can_comment = db.Column(db.Boolean, default=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))  
    # one to many: add foreign id on many side (get categopry.id from one side) - category is name of Category

    category = db.relationship('Category', back_populates = 'posts')  # correspond1  Post.category, Category.posts
    comments = db.relationship('Comment', back_populates = 'post', cascade='all, delete-orphan') # correspond2
     # cascade='all'-- post is deleted, then commmets would be deleted as well
 


class Comment(db.Model):
    __tablename__ = 'table_comment'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    email = db.Column(db.String(254))
    site = db.Column(db.String(254))
    body = db.Column(db.Text)
    from_admin = db.Column(db.Boolean, default = False)
    reviewed = db.Column(db.Boolean, default = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index = True)
    # Indexing is a way of sorting a number of records on multiple fields.
    # Creating an index on a field in a table creates another data structure which holds the field value, 
    # and a pointer to the record it relates to. This index structure is then sorted, 
    # allowing Binary Searches to be performed on it
    post = db.relationship('Post', back_populates = 'comments') # correspond2 Comment.post, Post.comments
    post_id = db.Column('Post', db.ForeignKey('post.id'))

    # build adjacency list relationship; one comment -- multiple replies 
    replied = db.relationship('Comment', back_populates = 'replies', remote_side = [id])  # replied is the parents
    replies = db.relationship('Comment', back_populates = 'replied', cascade = 'all, delete-orphan')
    replied_id = db.Column(db.Integer, db.ForeignKey('table_comment.id'))  # here use tablename.id
 

    # create query
    # comment = Comment(author = fake.name(), \
    # email = fake.email(), \
    # site = fake.url(),\
    # body = fake.text(100),\
    # reviewed = True,\
    # post = Post.query.get(random.randint(1, Post.query.count())),\
    # replied = Comment.query.get(random.randint(1, Comment.query.count())))

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    url = db.Column(db.String(255))