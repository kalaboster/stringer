'''
Test to test the file_utils
'''
import stringer.utils.file_utils as file_utils
import stringer.model.mask_model as mask_model
import os


TEST_FILE = os.path.dirname(__file__) + "/../files/test_log.txt"

LINE_DELETE = "2016-12-12 01:03:01 Account: 2557 Deleted record: 41043"

LINE_UPDATE = "2016-12-12 00:48:19 Account: 3618 Updated Record: 57685 Fields: Content=\"Bulletin\", Title=\"Nonsense News\", Industry=\"Technology\", FirstName=\"Fred\", LastName=\"Flintstone\""

LINE_UPDATE_CC = "2016-12-12 00:05:37 Account: 3618 Updated Record: 52571 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", CC=\"5424-9259-6687-3767\""
LINE_UPDATE_MASKED_CC = "2016-12-12 00:05:37 Account: 3618 Updated Record: 52571 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", CC=\"XXXXXXXXXXXXXXXX\""

LINE_UPDATE_SSN = "2016-12-12 01:09:19 Account: 3618 Added record: 86329 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"620-07-3092\""
LINE_UPDATE_MASKED_SSN =  "2016-12-12 01:09:19 Account: 3618 Added record: 86329 Fields: Content=\"Payment\", Type=\"Mortgage\", Industry=\"Finance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"XXXXXXXXXXXXXXXX\""


def test_mask_file():

    file_map = file_utils.mask_file(TEST_FILE, mask_model)

    assert True == file_map.has_key(8)
    assert str("2016-12-12 01:16:19 Account: 3618 Updated Record: 85714 Fields: Content=\"Quote\", Type=\"Auto\", "
               "Industry=\"Insurance\", FirstName=\"Fred\", LastName=\"Flintstone\", SSN=\"XXXXXXXXXXXXXXXX\"") == file_map.get(8)[69]


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