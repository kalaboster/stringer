'''
A utility class for functions to permutate tools
'''
import logging
from itertools import permutations

def generate(string=None):
    logging.debug("generate permutations with string: " + string)

    # Create list for permutations.
    permutate_list = []

    if string is None:
        logging.error('generate string is ' + None)
    else:
        logging.debug("generating permutations.")


        permutate_list = [''.join(value) for value in permutations(string)]


    return permutate_list