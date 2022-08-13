from flask import Flask
from flask import render_template

# self import
from blog import blog_blueprint
from user import user_blueprint
from portfolio import portfolio_blueprint

app = Flask(__name__)
app.register_blueprint(blog_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(portfolio_blueprint)


# Home
@app.route('/')
def home():
    return render_template('index.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
