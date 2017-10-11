'''
Utilities to search files and retain meta data about files.
'''
import logging
import os
import mmap


def map_file(path=None):
    logging.debug("map_file: " + path)

    file_map = ""

    if path is None or path is os.path.isfile(path):
        logging.error('generate string is None')
        logging.error('path is not a path.')
    else:
        with open(path) as infile:
            file_map = mmap.mmap(infile, 0, access=mmap.ACCESS_READ)

    return file_map


def mask_mmap(file_map=None, mask_model=None):
    logging.debug("file_map: " + file_map)

    masked_line = ""

    if file_map is None:
        logging.error("file_map is None")
    else:
        for line in iter(file_map.readline, ""):
            masked_line = mask_line(line, mask_model)



def mask_line(line=None, mask_model=None):
    logging.debug("mask_line processing.")

    new_line = ""

    if line is None or line is mask_model:
        logging.error("line and or mask_model is None")
    else:
        for mask in mask_model:
            print(mask)


    return new_line

