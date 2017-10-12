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
import logging
import os
import json


def print_report_dict(path=None, name="report_default_name.json", report_list_dict=None):
    logging.debug("print_report_dict")

    if path is None or report_list_dict is None:
        logging.error("path is None or report_list_dict is None")
    else:
        logging.debug("Printing report.")


    with open(os.path.join(path, name), 'w') as file:

        file.write(json.dumps(report_list_dict, indent=4, sort_keys=True))


    return bool(os.path.join(path, name))

'''
Future use to get more data on the file before masking.
'''
def get_file_meta_dict(file):
    logging.debug("get_file_meta_dict")

    file_meta_dict = {}

    if file is None or os.path.isfile(file) is False:
        logging.error("if file is None or os.path.isfile(file) is False")
    else:

        file_name = os.path.basename(file)
        os_stat = os.stat(file)

        file_meta_dict = {'file_name': file_name, 'os_stat': str(os_stat)}


    return file_meta_dict





    return is_file


