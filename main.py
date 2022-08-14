from flask import Flask, render_template
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
from datetime import datetime
import os

# self import
from extension import db, migrate
from forms import ContactForm
from blog import blog_blueprint
from user import user_blueprint
from portfolio import portfolio_blueprint
from SQL.SQL_management import Viewer


app = Flask(__name__)
app.register_blueprint(blog_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(portfolio_blueprint)

# CKEditor
ckeditor = CKEditor(app)

# WTF Form
app.config['SECRET_KEY'] = os.urandom(32)
Bootstrap(app)

# SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personal_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.init_app(app, db)


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
        new_viewer = Viewer(datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            name=contact_form.name.data,
                            email=contact_form.email.data,
                            phone=contact_form.phone.data,
                            message=contact_form.phone.data)
        db.session.add(new_viewer)
        db.session.commit()
    return render_template('contact.html', contact_form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)

