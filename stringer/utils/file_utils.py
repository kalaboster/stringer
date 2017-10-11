'''
Utilities to search files and retain meta data about files.
'''
import logging
import os
import stringer.model.mask_model as mask_model

'''
Read in the file and call function to mask lines.

Create a list with lines both masked and unmasked to be returned and printed to a new file.
'''
def mask_file(path=None, mask_model=None):
    logging.debug("map_file: " + path)

    file_line_list = []

    if path is None or not os.path.isfile(path):
        logging.error('generate string is None')
        logging.error('path is not a path.')
    else:
        with open(path) as infile:
            for line in infile:
                masked_line = mask_line(line, mask_model)
                file_line_list.append(masked_line)

    return file_line_list


'''
Mask a value of key value pair with Values in object.
'''
def mask_line(line=None, mask_model=None):
    logging.debug("mask_line processing.")

    new_line = ""

    if line is None or mask_model is None:
        logging.error("line and or mask_model is None")
    else:

        print(line)


    return new_line

'''
Print new file from a list of lines.
'''
def print_list_to_file(list=None):
    logging.debug("print_list_to_file" + str(list))


