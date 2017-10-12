# Open Story License
#
# Story: stringer
# Writer: Kalab J. Oster(TM)
# Copyright Holders: Kalab J. Oster(TM)
# copyright (C) 2017 Kalab J. Oster(TM)
#
# Permission is granted by the Copyright Holders for humans or other intelligent agents to read, write, edit, publish and critique the Story
# if the humans or intelligent agents keep this Open Story License with the Story,
# and if the Story you tell remains free,
# and if another writer writes or edits the Story then the writer's name needs to be appended to the end of the Writer list of this Open Story License.

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