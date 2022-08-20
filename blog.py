from datetime import datetime
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for

# self import
from extension import db, get_favicon
from admin import admin_only
from forms import NewPostForm, CommentForm
from SQL.SQL_management import Post, Comment, Tag

blog_blueprint = Blueprint('blog', __name__)


# Blog
@blog_blueprint.route('/blog-index', methods=['GET', 'POST'])
def blog_index():
    blog_posts = Post.query.all()
    return render_template('blog-index.html', favicon=get_favicon(), blog_posts=blog_posts), 200


@blog_blueprint.route('/blog-post/<int:blog_post_id>', methods=['GET', 'POST'])
def show_blog_post(blog_post_id):
    query_post = Post.query.get(blog_post_id)
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        new_comment = Comment(date=datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
                              body=comment_form.comment.data,
                              author=current_user,
                              post=query_post)
        db.session.add(new_comment)
        db.session.commit()
    return render_template('blog-post.html', favicon=get_favicon(), blog_post=query_post, comment_form=comment_form), 200


@blog_blueprint.route('/new-blog-post', methods=['GET', 'POST'])
@login_required
def new_blog_post():
    new_post_form = NewPostForm()
    if new_post_form.validate_on_submit():
        new_post = Post(title=new_post_form.title.data,
                        subtitle=new_post_form.subtitle.data,
                        date=datetime.today().strftime('%B %d, %Y'),
                        body=new_post_form.body.data,
                        author=current_user)
        new_tag = Tag(name=new_post_form.tags.data,
                      post=new_post)
        db.session.add(new_post)
        db.session.add(new_tag)
        db.session.commit()
        return redirect(url_for('blog.show_blog_post', blog_post_id=new_post.id))
    return render_template('new-blog-post.html', favicon=get_favicon(), edit_post_form=new_post_form), 200


@blog_blueprint.route('/delete-blog-post/<int:blog_post_id>', methods=['GET', 'DELETE'])
@login_required
def delete_blog_post(blog_post_id):
    query_post = Post.query.get(blog_post_id)
    db.session.delete(query_post)
    db.session.commit()
    return redirect(url_for('blog.blog_index'))


@blog_blueprint.route('/blog-make-post')
@login_required
def blog_make_post():
    return render_template('new-blog-post.html'), 200


@blog_blueprint.route('/edit-blog-post/<int:edit_post_id>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(edit_post_id):
    query_post = Post.query.get(edit_post_id)
    edit_post_form = NewPostForm(title=query_post.title,
                                 subtitle=query_post.subtitle,
                                 body=query_post.body)
    if edit_post_form.validate_on_submit():
        query_post.title = edit_post_form.title.data
        query_post.subtitle = edit_post_form.subtitle.data
        query_post.body = edit_post_form.body.data
        db.session.commit()
        return redirect(url_for('blog.show_blog_post', blog_post_id=query_post.id))
    return render_template('new-blog-post.html', favicon=get_favicon(), edit_post_form=edit_post_form, is_edit=True), 200


@blog_blueprint.route('/delete-post-comment/<int:comment_id>', methods=['GET', 'DELETE'])
@login_required
@admin_only
def delete_comment(comment_id):
    query_comment = Comment.query.get(comment_id)
    query_post = query_comment.post
    db.session.delete(query_comment)
    db.session.commit()
    return redirect(url_for('blog.show_blog_post', blog_post_id=query_post.id))
