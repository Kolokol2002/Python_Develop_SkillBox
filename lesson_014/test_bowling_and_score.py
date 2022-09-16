
import unittest
from score import get_score
from bowling import bowling_count




class MyScoreTest(unittest.TestCase):

    def test_x(self):
        result = get_score(["X"])
        self.assertEqual(result, 10)

    def test_slesh(self):
        list_test = ["4", "/"]
        result = get_score(list_test) - int(list_test[0])
        self.assertEqual(result, 6)

    def test_null(self):
        result = get_score(["-"])
        self.assertEqual(result, 0)

    def test_two_number(self):
        result = get_score(["2", "5"])
        self.assertEqual(result, 7)

class MyBowlingTest(unittest.TestCase):

    def test_x(self):
        result = bowling_count(round=1, balls=10)
        self.assertEqual(result, ['X'])

    def test_slesh(self):
        result = bowling_count(round=1, balls=4)
        self.assertEqual(result, ['4', '/'])

    def test_null(self):
        result = bowling_count(round=1, balls=0)
        self.assertEqual(result[0], '-')

    def test_two_number(self):
        result = bowling_count(round=1, balls=3)
        self.assertEqual(result, ['3', '3'])


if __name__ == '__main__':
    unittest.main()