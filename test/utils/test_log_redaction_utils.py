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
import os
import stringer.utils.log_redaction_utils as log_redaction_utils


GZIP_FILE_TEST =  os.path.dirname(__file__) + "/../files/test.tar.gz"

GZIP_FILE_TEST_OUTPUT =  os.path.dirname(__file__) + "/../files/test_output.tar.gz"

GZIP_OUTPUT_LOCATION_TEST = os.path.dirname(__file__) + "/../files"


def test_process_gz():

    is_file = log_redaction_utils.process_gz(GZIP_FILE_TEST, GZIP_OUTPUT_LOCATION_TEST,"log_redact")

    assert True == is_file