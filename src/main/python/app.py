from flask import Flask
from flask import jsonify

import globallog
from query import db_connect, find_point, find_shortest_route, db_disconnect


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello, navigators!</h1>"


@app.route('/<string:waypoint>/')
def find(waypoint):
    connection = db_connect()

    results = find_point(waypoint.upper(), connection)

    db_disconnect(connection)

    globallog.log_message("User GET request sent.")

    return jsonify(results)


@app.route('/<string:origin>/<string:destination>/')
def find_route(origin, destination):
    connection = db_connect()

    find_shortest_route(origin.upper(), destination.upper(), connection)

    db_disconnect(connection)

    return "Found route"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
