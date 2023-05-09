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

    def test_has(self):
        # test has
        h = Hashtable(5)
        h.set('key1', 'value1')
        self.assertTrue(h.has('key1'))
        self.assertFalse(h.has('key3'))

    def test_keys(self):
        # test keys
        h = Hashtable(5)
        h.set('key1', 'value1')
        h.set('key2', 'value2')
        h.set('key3', 'value3')
        h.set('key4', 'value4')
        self.assertEqual(set(h.keys()), {'key1', 'key2', 'key3', 'key4'})

    def test_collision(self):
        # test collision
        h = Hashtable(5)
        h.set('key1', 'value1')
        h.set('key6', 'value6')
        h.set('key11', 'value11')
        self.assertEqual(h.get('key1'), 'value1')
        self.assertEqual(h.get('key6'), 'value6')
        self.assertEqual(h.get('key11'), 'value11')

    def test_hash(self):
        # test hash
        h = Hashtable(5)
        self.assertNotEqual(h.hash('key1'), h.hash('key2'))


if __name__ == '__main__':
    unittest.main()
