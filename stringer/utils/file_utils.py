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
Utilities to search files and retain meta data about files.
'''
import logging
import os
import re
import stringer.model.mask_model as mask_model

'''
Read in the file and call function to mask lines.

Create a list with lines both masked and unmasked to be returned and printed to a new file.
'''
def mask_file(path=None, mask_model=None):
    logging.debug("map_file: " + path)

    #List for all the .lines to print
    file_line_list = []
    # A list of the lines altered.
    lines_numbers_redacted = []
    # redact things.
    redact_amount = 0
    # Line count to record.
    line_count = 0

    if path is None or not os.path.isfile(path):
        logging.error('generate string is None')
        logging.error('path is not a path.')
    else:
        with open(path) as infile:
            for line in infile:
                line_count += 1
                if is_pattern(line):
                    redact_amount += 1
                    lines_numbers_redacted.append(line_count)
                    line = mask_line(line, mask_model)

                file_line_list.append(line)

        print_list_to_file(file_line_list, path)

    # TODO: Get rid of literals.
    return {'file': path, 'redact_amount':redact_amount, 'lines_numbers_redacted': lines_numbers_redacted}

'''
A thought to create a dataframe and use it to read in log pattern and use pandas. Might better for speed.
This thought will take too much time right now, so save this.
def df_file(path=None):
    logging.debug("df_file: " + path)

    data_frame = ""
    if not os.path.isfile(path):
        logging.error('path is not a path.')
    else:
        data_frame = read_csv(path, sep=r'\s+', usecols=[0, 2, 4, 7, 8, 9, 10])

    return data_frame
'''

'''
Check line for pattern and log
'''
def is_pattern(line=None, mask_model=mask_model):
    logging.debug("note_line_with_pattern")

    contains = False

    if line is None or mask_model is None:
        logging.error("line and or mask_model is None")
    else:
        contains = bool(mask_model.Mask_Model().mask_find_regex.search(line))

    return contains


'''
Mask a value of key value pair with Values in object.
'''
def mask_line(line=None, mask_model=mask_model):
    logging.debug("mask_line processing.")

    if line is None or mask_model is None:
        logging.error("line and or mask_model is None")
    else:

        line = re.sub(mask_model.Mask_Model().mask_find_regex, mask_model.Mask_Model().mask_replace, line.rstrip())

    return line

'''
Print new file from a list of lines.
'''
def print_list_to_file(list=None, path_and_filename=None):
    logging.debug("print_list_to_file" + str(list))

    is_file = False

    if list is None or mask_model is None:
        logging.error("line and or mask_model is None")
    else:

        # Print
        # TODO check to see if file already exists error out to not over write.
        # TODO check to see if the file can write to the location.
        out_file = open(path_and_filename, 'w')

        for item in list:
            out_file.write("%s\n" % item.strip())

        is_file = os.path.isfile(path_and_filename)

    return is_file
