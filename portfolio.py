from flask import Blueprint, render_template

from extension import get_favicon

portfolio_blueprint = Blueprint('portfolio', __name__)


# Portfolio
@portfolio_blueprint.route('/portfolio-index')
def portfolio_index():
    return render_template('portfolio-index.html', favicon=get_favicon())
