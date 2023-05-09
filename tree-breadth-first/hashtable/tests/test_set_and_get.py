import unittest
from hashtable.hashtable import Hashtable


class TestHashtable(unittest.TestCase):
    def test_set_and_get(self):
        # test set and get
        h = Hashtable(5)
        h.set('key1', 'value1')
        self.assertEqual(h.get('key1'), 'value1')
        h.set('key1', 'newvalue')
        self.assertEqual(h.get('key1'), 'newvalue')
        h.set('key2', 'value2')
        self.assertEqual(h.get('key2'), 'value2')

    # other test methods


if __name__ == '__main__':
    unittest.main()
