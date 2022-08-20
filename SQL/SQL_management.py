from flask_login import UserMixin
from sqlalchemy.orm import relationship

# self import
from extension import db


class Viewer(db.Model):

    __tablename__ = "viewer"
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    message = db.Column(db.Text, nullable=True)


class User(UserMixin, db.Model):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    # Post
    posts = relationship("Post", back_populates="author")

    # Comment
    comments = relationship("Comment", back_populates="author")


class Post(db.Model):

    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text, nullable=False)

    # User
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship("User", back_populates="posts")

    # Comment
    comments = relationship("Comment", back_populates="post")

    # Tag
    tags = relationship("Tag", back_populates="post")


class Comment(db.Model):

    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300))

    # User
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship("User", back_populates="comments")

    # Post
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = relationship("Post", back_populates="comments")


class Tag(db.Model):

    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)

    # Post
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = relationship("Post", back_populates="tags")
