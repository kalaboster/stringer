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
Test fo gzip.
'''
import stringer.utils.gzip_utils as gzip_utils
import os


GZIP_FILE_TEST =  os.path.dirname(__file__) + "/../files/test.tar.gz"

GZIP_FILE_TEST_OUTPUT =  os.path.dirname(__file__) + "/../files/test_output.tar.gz"

GZIP_OUTPUT_LOCATION_TEST = os.path.dirname(__file__) + "/../files"

OUTPUT_DIR = "gzip_files"

GZIP_FILE_DIR_FILE = os.path.dirname(__file__) + "/../files/" + OUTPUT_DIR + "/test_log_1.txt"

def test_open_gzip():

    is_dir = gzip_utils.open_gzip(GZIP_FILE_TEST, GZIP_OUTPUT_LOCATION_TEST)

    assert True == is_dir
    assert True == os.path.isfile(GZIP_FILE_DIR_FILE)


def test_make_gzip():

    is_file = gzip_utils.close_gzip(GZIP_FILE_TEST_OUTPUT , os.path.join(GZIP_OUTPUT_LOCATION_TEST,OUTPUT_DIR))

    assert True == is_file
    assert True == os.path.isfile(GZIP_FILE_TEST_OUTPUT )