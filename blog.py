from flask import Blueprint, render_template

blog_blueprint = Blueprint('blog', __name__)

# self import
from SQL.SQL_management import Post


# Blog
@blog_blueprint.route('/blog-index', methods=['GET', 'POST'])
def blog_index():
    blog_posts = Post.query.all()
    return render_template('blog-index.html', blog_posts=blog_posts)


@blog_blueprint.route('/blog-make-post')
def blog_make_post():
    return render_template('blog-make-post.html')


@blog_blueprint.route('/blog-post/<int:blog_post>', methods=['GET', 'POST'])
def show_blog_post(blog_post):
    query_post = Post.query.get(blog_post)
    return render_template('blog-post.html', blog_post=query_post)


@blog_blueprint.route('/new-blog-post')
def new_blog_post():
    return '<h1>new_blog_post</h1>'


@blog_blueprint.route('/delete-blog-post')
def delete_blog_post():
    return '<h1>delete_blog_post</h1>'


@blog_blueprint.route('/edit-blog-post')
def edit_blog_post():
    return '<h1>edit_blog_post</h1>'
