'''
A model to define values to mask and the masking string.
'''
class Mask_Model:


    def __init__(self, mask_key_list=None, mask_value=None):

        if mask_key_list is None:
            self._mask_key_list = ['SSN','CC']
        else:
            self._mask_key_list = mask_key_list

        if mask_value is None:
            self._mask_value = "XXXXXXXXXXXXXXXX"
        else:
            self._mask_value = mask_value



    @property
    def mask_key_list(self):
        return self._mask_key_list

    @mask_key_list.setter
    def mask_key_list(self, mask_key_list):
        self._mask_key_list = mask_key_list


    @property
    def mask_value(self):
        return self._mask_value

    @mask_value.setter
    def mask_value(self, mask_value):
        self._mask_value = mask_value

