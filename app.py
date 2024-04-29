from flask import Flask, jsonify, request, render_template, Blueprint, redirect, url_for
from log import globallog
from database.DataControl import DataControl

app = Flask(__name__)

blueprint = Blueprint('api_bp', __name__, static_folder='static', static_url_path='/static')

app.register_blueprint(blueprint)

dc = DataControl()


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
    globallog.log_message("Form submitted (POST request)")
    origin = request.form['origin']
    connection = dc.connect_database()
    results = dc.find_single_point(origin.upper(), connection)
    dc.disconnect_database(connection)
    return render_template('index.html', results=results)


@app.route('/search')
def search():
    globallog.log_message("User GET request sent.")

    origin = request.args.get('start')
    destination = request.args.get('stop')

    if not destination:
        connection = dc.connect_database()
        results = dc.find_single_point(origin.upper(), connection)
        dc.disconnect_database(connection)

    else:
        # placeholder for a more advanced function
        results = {"name": "John", "age": 30}

    return jsonify(results)


# @app.route('/form_search')
# def form_search():
#     origin = request.args.get('start')
#     destination = request.args.get('stop')
#
#     if not destination:
#         connection = dc.connect_database()
#
#         results = dc.find_single_point(origin.upper(), connection)
#
#         dc.disconnect_database(connection)
#
#         globallog.log_message("User GET request sent.")
#
#     else:
#         # placeholder
#         results = {"name": "John", "age": 30}
#
#     globallog.log_message("Results created.")
#
#     # send results to the page via AJAX?
#
#     return render_template('index.html')


@app.route('/<string:origin>/<string:destination>/')
def find_route(origin, destination):
    # empty, keep for upcoming implementation
    return "Found route"


@app.route('/error500')
def force_error():
    # Simulate a server error by dividing by zero (ZeroDivisionError)
    result = 1 / 0
    del result
    return render_template('error.html')


@app.errorhandler(404)
def not_found_error():
    return render_template('error.html', error_code=404, message='Page not found'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template(
        'error.html',
        error_code=500,
        message='Internal Server Error'
    ), 500


if __name__ == '__main__':
    print("Development Server Running on http://127.0.0.1:105")
    app.run(host='0.0.0.0', port=105)
