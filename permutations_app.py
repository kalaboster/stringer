from flask import Flask, jsonify
from flask_swagger import swagger
import stringer.api.permutations_api as permutations_api

app = Flask(__name__)
perm_view = permutations_api.PermAPI.as_view('perm')
app.add_url_rule('/v1/perm/<string:text>', view_func=perm_view, methods=["GET"])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
    response.headers.add('Access-Control-Expose-Headers', "Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET, OPTIONS")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response

@app.route("/v1")
def root():
    return "This is not the api call you're looking for."

@app.route("/spec")
def spec():
    return jsonify(swagger(app, from_file_keyword='swagger_file'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)