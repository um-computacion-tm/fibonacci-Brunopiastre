import unittest

from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test(self):
        self.assertEqual(1, fibonacci(2))
        self.assertEqual(2, fibonacci(3))

if __name__=="__main__":
    unittest.main()