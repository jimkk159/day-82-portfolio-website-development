from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import validators
from wtforms import StringField, EmailField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[validators.Email()])
    password = StringField("Password", validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[validators.Email()])
    name = StringField("Name", validators=[DataRequired()])
    password = StringField("Password", validators=[validators.Length(min=8, max=30)])
    password_confirm = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField("Email Address", validators=[validators.Email()])
    phone = StringField("Phone Number")
    message = CKEditorField("Message")
    submit = SubmitField('Submit')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), validators.Length(max=100)])
    subtitle = StringField("Subtitle", validators=[DataRequired(), validators.Length(max=100)])
    body = CKEditorField("Blog Content")
    tags = SelectField('Tag',
                       choices=[("Portfolio", "portfolio"), ("Movie", "movie"), ("Book", "book"), ("life", "life")])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")
