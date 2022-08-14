from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import validators
from wtforms import StringField, EmailField, SubmitField
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