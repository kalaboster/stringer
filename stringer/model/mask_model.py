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
A model to define values to mask and the masking string.
'''
import re
class Mask_Model:


    def __init__(self, mask_find_regex=None, mask_replace=None):

        if mask_find_regex is None:
            self._mask_find_regex = re.compile("(\d\d\d-\d\d-\d\d\d\d|\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d)")
        else:
            self._mask_find_regex = re.compile(mask_find_regex)

        if mask_replace is None:
            self._mask_replace =  "XXXXXXXXXXXXXXXX" 
        else:
            self._mask_replace = mask_replace


    @property
    def mask_find_regex(self):
        return self._mask_find_regex

    @mask_find_regex.setter
    def mask_find_regex(self, mask_find_regex):
        self._mask_find_regex = re.compile(mask_find_regex)


    @property
    def mask_replace(self):
        return self._mask_replace

    @mask_replace.setter
    def mask_replace(self, mask_replace):
        self._mask_replace = mask_replace




