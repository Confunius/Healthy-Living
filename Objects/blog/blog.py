from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from os import path

app = Flask(__name__)

db = SQLAlchemy(app)
db.init_app(app)


class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    lastname = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comments', backref='user', lazy=True)
    likes = db.relationship('Likes', backref='user', lazy=True)

    def __repr__(self):
        return f"User <{self.username}>"
    
class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comments', backref='post', lazy=True)
    likes = db.relationship('Likes', backref='post', lazy=True)
    views = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(200), unique=False, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)

    def __repr__(self):
        return f"Comment('{self.author}', '{self.text}')"

class Likes(db.Model):
    __tablename__='likes'
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact('{self.email}', '{self.message}')"
    
   

