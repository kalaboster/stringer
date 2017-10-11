"""permutations_cli

Usage:
  permutations_cli.py --string <string>
  permutations_cli.py (-h | --help)
  permutations_cli.py --version

Options:
  -h --help     Pass in a string.
  --version     v version

"""
from docopt import docopt
import stringer.utils.permutate_utils as perm


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.9')

    perm_list = perm.generate(arguments.get("<string>"))

    print(str(perm_list))



