from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm
import os

# self import
from blog import blog_blueprint
from user import user_blueprint
from portfolio import portfolio_blueprint

app = Flask(__name__)
app.register_blueprint(blog_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(portfolio_blueprint)

# WTF Form
app.config['SECRET_KEY'] = os.urandom(32)
Bootstrap(app)

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Viewer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(50), nullable=False)


db.create_all()


# Home
@app.route('/')
def home():
    return render_template('index.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(contact_form.name.data, contact_form.email.data, contact_form.phone.data, contact_form.message.data)
        new_viewer = Viewer(name=contact_form.name.data, email=contact_form.email.data, phone=contact_form.phone.data,
                            message=contact_form.phone.data)
        db.session.add(new_viewer)
        db.session.commit()
    return render_template('contact.html', contact_form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)
