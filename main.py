import os
import smtplib
from flask import Flask, render_template
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
from flask_gravatar import Gravatar
from datetime import datetime

# self import
from extension import db, migrate, get_favicon
from forms import ContactForm
from blog import blog_blueprint
from user import user_blueprint
from portfolio import portfolio_blueprint
from SQL.SQL_management import Viewer, User

MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWORD = os.getenv('MY_PASSWORD')

app = Flask(__name__)

# BluePrint
app.register_blueprint(blog_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(portfolio_blueprint)

# CKEditor
ckeditor = CKEditor(app)

# WTF Form
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)

# SQL
pre_DATABASE_URL = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace('postgres://', 'postgresql://')  # In Heroku
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'  # In Local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db, render_as_batch=True)

# Login
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Home
@app.route('/')
def home():
    return render_template('index.html', favicon=get_favicon()), 200


# About
@app.route('/about')
def about():
    return render_template('about.html', favicon=get_favicon()), 200


# Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        new_viewer = Viewer(datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            name=contact_form.name.data,
                            email=contact_form.email.data,
                            phone=contact_form.phone.data,
                            message=contact_form.message.data)
        db.session.add(new_viewer)
        db.session.commit()
        send_email(contact_form.name.data, contact_form.email.data, contact_form.phone.data, contact_form.message.data)
    return render_template('contact.html', favicon=get_favicon(), contact_form=contact_form), 200


def send_email(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Personal Site New Viewer\n\n"
                                f"Hello Jim!\n"
                                f"I am {name}\n"
                                f"My Email: {email}\n"
                                f"My Phone: {phone}\n"
                                f"Message: {message} "
                            )


if __name__ == '__main__':
    app.run(debug=True)
