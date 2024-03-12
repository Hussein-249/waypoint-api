from flask import Flask, jsonify, request

import globallog
from query import db_connect, find_point, find_shortest_route, db_disconnect


app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Hello, navigators!</h1>"


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
        #placeholder
        results = {"name": "John", "age": 30}

    return jsonify(results)


@app.route('/<string:origin>/<string:destination>/')
def find_route(origin, destination):
    connection = db_connect()

    find_shortest_route(origin.upper(), destination.upper(), connection)

    db_disconnect(connection)

    return "Found route"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
