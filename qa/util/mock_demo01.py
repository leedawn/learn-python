from unittest import mock
import unittest

from modular import Count

class TestCount(unittest.TestCase):
    def test_add(self):
        count=Count()
        count.add=mock.Mock(return_value=13)
        result=count.add(8,5)
        self.assertEqual(result,13)

if __name__=='__main__':
    unittest.main()


import unittest
import function


class MyTestCase(unittest.TestCase):

    def test_add_and_multiply(self):
        x = 3
        y = 5
        addition, multiple = function.add_and_multiply(x, y)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()