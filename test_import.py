import unittest

from mymath.fibo import fibo

def noop():
    pass

class TestImport(unittest.TestCase):
    def test_is_fun(self):
        self.assertIs(type(fibo),type(noop))


if __name__ == "__main__":
    unittest.main()

