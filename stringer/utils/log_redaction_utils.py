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


import stringer.utils.file_utils as file_utils
import stringer.utils.gzip_utils as gzip_utils
import stringer.utils.report_utils as report_utils
import stringer.model.mask_model as mask_model

def process_gz(file=None,working_dir=None, output_gz_dir=None):
    logging.debug("process_gz")

    is_file = False

    if file is None or os.path.isfile(file) is False:
        logging.error("file is None or os.path.isfile(file)")
    else:
        logging.debug("Processing gz...")
        # Put all files iin working dir.
        is_gzip = gzip_utils.open_gzip(file, working_dir, output_gz_dir)

        # Read all the files to process through.

        files = [f for f in os.listdir(os.path.join(working_dir, output_gz_dir)) if os.path.isfile(os.path.join(working_dir, output_gz_dir, f))]

        # Loop through all the files masking...
        for f in files:
            file_utils.mask_file(os.path.join(working_dir, output_gz_dir, f), mask_model)

        # make new file name
        name = os.path.basename(file).split(".")

        gzip_utils.close_gzip(os.path.join(working_dir, name[0] +'_masked.tar.gz'), os.path.join(working_dir, output_gz_dir))


        is_file = bool(os.path.join(working_dir, name[0] +'_masked.tar.gz'))

    return is_file

