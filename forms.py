from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import validators
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField("Password", validators=[validators.Length(min=8, max=30)])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[validators.Length(min=8, max=30)])
    password_confirm = StringField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    email = StringField("Email Address", validators=[DataRequired()], render_kw={"placeholder": "Email"})
    phone = StringField("Phone Number", render_kw={"placeholder": "Phone"})
    message = TextAreaField("Message", render_kw={"placeholder": "Message"})
    submit = SubmitField('Submit')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), validators.Length(max=100)])
    subtitle = StringField("Subtitle", validators=[DataRequired(), validators.Length(max=100)])
    body = CKEditorField("Blog Content")
    tags = SelectField('Tag',
                       choices=[("portfolio", "Portfolio"), ("movie", "Movie"), ("book", "Book"), ("life", "Life")])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")
