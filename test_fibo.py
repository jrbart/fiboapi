import unittest
from mymath.fibo import fibo

class TestFibo(unittest.TestCase):

    def test_fib1(self):
        self.assertEqual(fibo(1),[0])

if __name__ == "__main__":
    unittest.main()

