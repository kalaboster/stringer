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
Functions to get files from a gzip and loop and put files into gzip.
'''
import logging
import os
import shutil
import tarfile

OUTPUT_DIR = "gzip_files"

def open_gzip(gzip_file=None, gzip_output_loc=None):
    logging.debug("open_gzip")

    # A boolean to return if the dir exists for a simple sanity check
    is_dir = False

    if gzip_file is None or gzip_output_loc is None:
        logging.error("gzip_file is None or gzip_output_loc is None")
    elif os.path.isfile(gzip_file) is False or os.path.isdir(gzip_output_loc) is False:
        logging.error("os.path.isfile(gzip_file) is False or os.path.isdir(gzip_output_loc) is False")
    else:
        logging.debug("opening gzip...")

        # Check and clear old data
        if os.path.isdir(os.path.join(gzip_output_loc, OUTPUT_DIR )):

            shutil.rmtree(os.path.join(gzip_output_loc, OUTPUT_DIR ))

        os.mkdir(os.path.join(gzip_output_loc, OUTPUT_DIR ))

        # Open files and output.
        tar = tarfile.open(gzip_file, "r:gz")

        for member in tar.getmembers():
            file = tar.extractfile(member)
            if file is not None:
                content = file.read()
                file_h = open(os.path.join(gzip_output_loc, OUTPUT_DIR , file.name),'w')
                file_h.write(content)

        tar.close()

    is_dir = os.path.isdir(os.path.join(gzip_output_loc, OUTPUT_DIR ))

    return is_dir


def close_gzip(gzip_file=None, gzip_output_loc=None):
    logging.debug("open_gzip")

    def close_gzip(gzip_file=None, gzip_output_loc=None):
        logging.debug("open_gzip")


    # A boolean to return if the dir exists for a simple sanity check
    is_file = False

    if gzip_file is None or gzip_output_loc is None:
        logging.error("gzip_file is None or gzip_output_loc is None")
    elif os.path.isdir(gzip_output_loc) is False:
        logging.error("os.path.isfile(gzip_file) is False or os.path.isdir(gzip_output_loc) is False")
    else:
        logging.debug("opening gzip...")

        # Check and clear old data
        if os.path.isdir(os.path.join(gzip_output_loc, gzip_file)):

            shutil.rmtree(os.path.join(gzip_output_loc, gzip_file))


        tar = tarfile.open(os.path.join(gzip_output_loc, gzip_file), "w:gz")
        tar.add(gzip_output_loc, arcname=".")
        tar.close()


        is_file = os.path.isfile(gzip_file)

    return is_file