from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__)


# Blog
@blog_blueprint.route('/blog-index')
def blog_index():
    return render_template('blog-index.html')


@blog_blueprint.route('/blog-make-post')
def blog_make_post():
    return render_template('blog-make-post.html')


@blog_blueprint.route('/blog-post')
def blog_post():
    return render_template('blog-post.html')
