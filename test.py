import unittest

from random_pass import get_random_string

class TestRand(unittest.TestCase):
    def test_random(self):
        result = get_random_string(8)
        print(result)
        self.assertEqual(len(result),8)

if __name__ == '__main__':
    unittest.main()

