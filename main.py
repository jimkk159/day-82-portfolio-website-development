from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
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
    return render_template('contact.html', contact_form=contact_form)


if __name__ == '__main__':
    app.run(debug=True)
