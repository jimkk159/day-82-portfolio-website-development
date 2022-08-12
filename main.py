from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# Portfolio
@app.route('/portfolio-index')
def portfolio_index():
    return render_template('portfolio-index.html')


# Blog
@app.route('/blog-index')
def blog_index():
    return render_template('blog-index.html')


@app.route('/blog-make-post')
def blog_make_post():
    return render_template('blog-make-post.html')


@app.route('/blog-post')
def blog_post():
    return render_template('blog-post.html')


# Login
@app.route('/login')
def login():
    return render_template('login.html')


# Register
@app.route('/register')
def register():
    return render_template('register.html')


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
