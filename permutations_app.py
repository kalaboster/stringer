from flask import Flask
from flask import request
import stringer.utils.permutate_utils as permutate_utils
app = Flask(__name__)

@app.route("/api/v1.0/permutations", methods=['GET'])
def get_permutations():

    string_arg = request.args.get('string')

    perm_list = permutate_utils.generate(string_arg)

    return str(perm_list)


if __name__ == "__main__":
    app.run()