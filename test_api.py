import unittest
from fiboapi import *

class TestImport(unittest.TestCase):
    def setUp(self):
       self.app = web.application(urls,globals())

    def test_is_web(self):
        req = self.app.request("/",method="GET")
        self.assertEqual(req.status,"200 OK")


if __name__ == "__main__":
    unittest.main()

