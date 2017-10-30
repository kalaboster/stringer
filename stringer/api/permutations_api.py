from flask.views import MethodView
import stringer.utils.permutate_utils as permutate_utils

class PermAPI(MethodView):

    def get(self, text):

        """
        Get the permutations of a text.
        swagger_from_file: ./index.yml
        """
        perm_list = permutate_utils.generate(text)

        return str(perm_list)
