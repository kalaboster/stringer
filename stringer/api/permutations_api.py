from flask import Flask, jsonify
from flask.views import MethodView
from flask_swagger import swagger

app = Flask(__name__)

class PermAPI(MethodView):

    def get(self, text):

        """
        Get the permutations of a text.
        swagger_file: text_get.yml
        """
        return {}



perm_view = PermAPI.as_view('perm')
app.add_url_rule('/perm/<string:text>', view_func=perm_view, methods=["GET"])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
    response.headers.add('Access-Control-Expose-Headers', "Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET, OPTIONS")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response


@app.route("/")
def root():
    return "This is not the api call you're looking for."

@app.route("/spec")
def spec():
    return jsonify(swagger(app, from_file_keyword='swagger_file'))

if __name__ == "__main__":
    app.run(debug=True)