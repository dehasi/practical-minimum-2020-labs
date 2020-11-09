import unittest

from lec10.lab.my_math import inc


class MyTestCase(unittest.TestCase):

    def test_inc(self):
        self.assertEqual(inc(1), 2)

    def test_answer(self):
        assert inc(3) == 4


if __name__ == '__main__':
    unittest.main()
