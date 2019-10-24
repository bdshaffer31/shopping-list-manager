import unittest
from book_shelf import BookShelf

class TestAllMethods(unittest.TestCase):

    def test_init_book(self):
        shelf = BookShelf()
        shelf = shelf.populate_bookshelf()

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()