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
import stringer.utils.report_utils as report_utils
import os

TEST_FILE = os.path.dirname(__file__) + "/../files/test_log.txt"

TEST_FILE_OUTPUT_DIR = os.path.dirname(__file__) + "/../files"

TEST_FILE_META_DICT = [{'redact_amount': 8, 'file': '/home/kalab/github/stringer/test/utils/../files/test_log_cp.txt', 'lines_numbers_redacted': [10, 25, 34, 35, 45, 60, 69, 70]},
                       {'redact_amount': 7, 'file': '/home/kalab/github/stringer/test/utils/../files/test_log_cp1.txt', 'lines_numbers_redacted': [10, 34, 35, 45, 60, 69, 70]},
                       {'redact_amount': 1, 'file': '/home/kalab/github/stringer/test/utils/../files/test_log_cp2.txt', 'lines_numbers_redacted': [70]},
                       {'redact_amount': 0, 'file': '/home/kalab/github/stringer/test/utils/../files/test_log_cp3.txt', 'lines_numbers_redacted': []}]

def test_print_report_dict():

    is_file = report_utils.print_report_dict(path=TEST_FILE_OUTPUT_DIR , name="test_print_report.json", report_list_dict=TEST_FILE_META_DICT)

    assert True == is_file

'''
Under work.
def test_get_file_meta_dict():

    is_file = report_utils.get_file_meta_dict(TEST_FILE)

    assert  TEST_FILE_META_DICT == is_file
'''