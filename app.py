from flask import Flask, jsonify, request, render_template, Blueprint, redirect, url_for
import io
import globallog
import Control
from query import db_connect, find_point, find_shortest_route, db_disconnect
from map import map_from_waypoint


app = Flask(__name__)

blueprint = Blueprint('api_bp', __name__, static_folder='static', static_url_path='/static')

app.register_blueprint(blueprint)


@app.route('/')
def index():
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
    control = Control

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
    control = Control

    if not destination:
        connection = db_connect()

        results = find_point(origin.upper(), connection)

        db_disconnect(connection)

        globallog.log_message("User GET request sent.")

    else:
        # placeholder
        results = {"name": "John", "age": 30}

    globallog.log_message("Results created.")

    globallog.log_message("Results created.")

    lon = 60
    lat = 55

    map_image = map_from_waypoint(lon, lat)

    image_url = url_for('static', filename='map.png')

    return render_template('index.html', image_url=image_url)


@app.route('/<string:origin>/<string:destination>/')
def find_route(origin, destination):
    connection = db_connect()

    find_shortest_route(origin.upper(), destination.upper(), connection)

    db_disconnect(connection)

    return "Found route"


if __name__ == '__main__':
    print("Development Server Running on http://127.0.0.1:105")
    app.run(host='0.0.0.0', port=105)
