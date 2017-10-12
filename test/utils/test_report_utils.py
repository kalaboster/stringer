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

TEST_FILE_META_DICT = {'os_stat': "posix.stat_result(st_mode=33204, st_ino=4199090, st_dev=2051L, st_nlink=1, st_uid=1001, "
                                  "st_gid=1001, st_size=10381, st_atime=1507754550, st_mtime=1507656962, st_ctime=1507656962)", 'file_name': 'test_log.txt'}

def test_get_file_meta_dict():

    is_file = report_utils.get_file_meta_dict(TEST_FILE)

    assert  TEST_FILE_META_DICT == is_file

