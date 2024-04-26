from flask import Flask, jsonify, request, render_template, Blueprint, redirect, url_for
import io
import globallog
from query import db_connect, find_point, find_shortest_route, db_disconnect


app = Flask(__name__)

blueprint = Blueprint('api_bp', __name__, static_folder='static', static_url_path='/static')

app.register_blueprint(blueprint)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/conventional')
def conventional_website_view():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    origin = request.form['origin']
    return redirect(url_for('form_search', start=origin))


@app.route('/search')
def search():
    origin = request.args.get('start')
    destination = request.args.get('stop')

    if not destination:
        connection = db_connect()

        results = find_point(origin.upper(), connection)

        db_disconnect(connection)

        globallog.log_message("User GET request sent.")

    else:
        # placeholder
        results = {"name": "John", "age": 30}

    return jsonify(results)


@app.route('/form_search')
def form_search():
    origin = request.args.get('start')
    destination = request.args.get('stop')

    if not destination:
        connection = db_connect()

        results = find_point(origin.upper(), connection)

        db_disconnect(connection)

        globallog.log_message("User GET request sent.")

    else:
        # placeholder
        results = {"name": "John", "age": 30}

    globallog.log_message("Results created.")

    lon = 60
    lat = 55

    image_url = url_for('static', filename='map.png')

    return render_template('index.html', image_url=image_url)


@app.route('/<string:origin>/<string:destination>/')
def find_route(origin, destination):
    connection = db_connect()

    find_shortest_route(origin.upper(), destination.upper(), connection)

    db_disconnect(connection)

    return "Found route"


@app.route('/error500')
def force_error():
    # Simulate a server error by dividing by zero (ZeroDivisionError)
    result = 1 / 0
    return render_template('error.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, message='Page not found'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template(
        'error.html',
        error_code=500,
        message='Internal Server Error'
    ), 500


if __name__ == '__main__':
    print("Development Server Running on http://127.0.0.1:105")
    app.run(host='0.0.0.0', port=105)
