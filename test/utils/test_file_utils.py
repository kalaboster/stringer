'''
Test to test the file_utils
'''
import stringer.utils.file_utils as file_utils
import stringer.model.mask_model as mask_model
import os


TEST_FILE = os.path.dirname(__file__) + "/../files/test_log.txt"

def test_mask_file():

    file_map = file_utils.mask_file(TEST_FILE, mask_model)



    assert "" == file_map
