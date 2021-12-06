import unittest
from main import print_hi_stephen, print_hi_you, print_hi_steven


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), "Hi, Stephen")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), "Hi, Eagle")

    def test_print_hi_steven(self):
        self.assertEqual(print_hi_steven(),"Hi, Steven")

if __name__ == '__main__':
    unittest.main()
