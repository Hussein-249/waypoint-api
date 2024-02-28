from flask import blueprints


bp = Blueprints("pages", __name__)

@bp.route('/about')
def aboutpage():
    return ('This is the about page.')