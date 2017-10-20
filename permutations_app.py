from flask import Flask
from flask import request
import stringer.utils.permutate_utils as permutate_utils
application = Flask(__name__)

@application.route("/api/v1.0/permutations", methods=['GET'])
def get_permutations():

    string_arg = request.args.get('string')

    perm_list = permutate_utils.generate(string_arg)

    return str(perm_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)