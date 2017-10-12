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
Test to test the file_utils
'''
import stringer.utils.file_utils as file_utils
import stringer.model.mask_model as mask_model
import os


TEST_FILE = os.path.dirname(__file__) + "/../files/test_log.txt"

TEST_CREATE_FILE = os.path.dirname(__file__) + "/../files/test_create_log.txt"

LINE_DELETE = "2016-12-12 01:03:01 Account: 2557 Deleted record: 41043"

LINE_UPDATE = "2016-12-12 00:48:19 Account: 3618 Updated Record: 57685 Fields: Content=\"Bulletin\", Title=\"Nonsense News\", Industry=\"Technology\", FirstName=\"Fred\", LastName=\"Flintstone\""

LINE_UPDATE_CC = "2016-12-12 00:05:37 Account: 3618 Updated Record: 52571 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", CC=\"5424-9259-6687-3767\""
LINE_UPDATE_MASKED_CC = "2016-12-12 00:05:37 Account: 3618 Updated Record: 52571 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", CC=\"XXXXXXXXXXXXXXXX\""

LINE_UPDATE_SSN = "2016-12-12 01:09:19 Account: 3618 Added record: 86329 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"620-07-3092\""
LINE_UPDATE_MASKED_SSN =  "2016-12-12 01:09:19 Account: 3618 Added record: 86329 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"XXXXXXXXXXXXXXXX\""

DICT_OF_THINGS_TO_PRINT = {'redact': 2, 'lines': (LINE_UPDATE_SSN, LINE_UPDATE_CC, LINE_UPDATE,LINE_DELETE)}


def test_mask_file():

    file_map = file_utils.mask_file(TEST_FILE, mask_model)

    assert True == file_map.has_key('redact')
    assert str("2016-12-12 01:16:19 Account: 3618 Updated Record: 85714 Fields: Content=\"Quote\", Type=\"Auto\", "
               "Industry=\"Insurance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"XXXXXXXXXXXXXXXX\"") == file_map.get('lines')[69]


def test_mask_line_cc():

    file_masked = file_utils.mask_line(LINE_UPDATE_CC, mask_model)

    assert LINE_UPDATE_MASKED_CC == file_masked

def test_mask_line_ssn():

    file_masked = file_utils.mask_line(LINE_UPDATE_SSN, mask_model)

    assert LINE_UPDATE_MASKED_SSN == file_masked

def test_is_pattern_true():

    contains = file_utils.is_pattern(LINE_UPDATE_SSN, mask_model)

    assert True == contains

def test_is_pattern_false():

    contains = file_utils.is_pattern(LINE_DELETE, mask_model)

    assert False == contains


def test_print_list_to_file():

    if os.path.isfile(TEST_CREATE_FILE):
        os.remove(TEST_CREATE_FILE)

    is_file = file_utils.print_list_to_file(list=DICT_OF_THINGS_TO_PRINT.get('lines'), path_and_filename=TEST_CREATE_FILE)

    assert True == is_file