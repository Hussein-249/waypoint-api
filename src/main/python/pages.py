from flask import Blueprints


bp = Blueprints("pages", __name__)


@bp.route('/about')
def about_page():
    return f'This is the about page.'
