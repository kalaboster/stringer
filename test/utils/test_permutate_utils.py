'''
Tests for permutations.
'''
import stringer.utils.permutate_utils as perm

def test_permutations_short_string():

    perm_list1 = perm.generate("aaa")
    perm_list2 = perm.generate("cake")
    perm_list3 = perm.generate("banana")

    assert ['aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'] == perm_list1
    assert ['cake', 'caek', 'ckae', 'ckea', 'ceak', 'ceka', 'acke', 'acek', 'akce', 'akec', 'aeck', 'aekc', 'kcae',
            'kcea', 'kace', 'kaec', 'keca', 'keac', 'ecak', 'ecka', 'eack', 'eakc', 'ekca', 'ekac'] == perm_list2
    assert "anaban" == perm_list3[714]