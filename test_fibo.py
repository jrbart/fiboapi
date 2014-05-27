import unittest
from mymath.fibo import fibo

class TestFibo(unittest.TestCase):

    def test_fib1(self):
        self.assertEqual(fibo(1),[0])

    def test_fib2(self):
        self.assertEqual(fibo(2),[0, 1])

    def test_fib3(self):
        self.assertEqual(fibo(3),[0, 1, 1])

if __name__ == "__main__":
    unittest.main()

