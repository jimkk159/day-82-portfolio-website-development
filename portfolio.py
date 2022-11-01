from flask import Blueprint, render_template

from extension import get_favicon
from SQL.SQL_management import Post

portfolio_blueprint = Blueprint('portfolio', __name__)


# Portfolio
@portfolio_blueprint.route('/portfolio-index')
def portfolio_index():
    # query_post = Post.query.filter(Post.tags.any(name='portfolio'))
    query_post = Post.query.join(Post.tags, aliased=True).filter_by(name='portfolio')
    return render_template('blog-index.html', favicon=get_favicon(), blog_posts=query_post, portfolio=True), 200
