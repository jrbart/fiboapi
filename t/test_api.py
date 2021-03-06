import unittest
import json
from fiboapi import *

class TestImport(unittest.TestCase):
    def setUp(self):
       self.app = web.application(urls,globals())

    def test_is_web(self):
        req = self.app.request("/",method="GET")
        self.assertEqual(req.status,"200 OK")

    def test_fibo_1(self):
        req = self.app.request("/fibo/1",method="GET")
        self.assertEqual(req.status,"200 OK")
        self.assertEqual(req.headers,{"Content-Type":"application/json"})
        self.assertEqual(json.loads(req.data),[0])

    def test_fibo_2(self):
        req = self.app.request("/fibo/2",method="GET")
        self.assertEqual(req.status,"200 OK")
        self.assertEqual(req.headers,{"Content-Type":"application/json"})
        self.assertEqual(json.loads(req.data),[0, 1])

    def test_fibo_8(self):
        req = self.app.request("/fibo/8",method="GET")
        self.assertEqual(req.status,"200 OK")
        self.assertEqual(req.headers,{"Content-Type":"application/json"})
        self.assertEqual(json.loads(req.data),[0, 1, 1, 2, 3, 5, 8, 13])

    def test_fibo_RangeError(self):
        req = self.app.request("/fibo/-1",method="GET")
        self.assertEqual(req.status,"404 Not Found")
        self.assertEqual(req.data,"Exception: RangeError")

    def test_fibo_ValueError(self):
        req = self.app.request("/fibo/A",method="GET")
        self.assertEqual(req.status,"404 Not Found")
        self.assertEqual(req.data,"Exception: ValueError")

    def test_fibo_weird_path(self):
        req = self.app.request("/fibo/1/2/3",method="GET")
        self.assertEqual(req.status,"404 Not Found")
        self.assertEqual(req.data,"Exception: ValueError")

if __name__ == "__main__":
    unittest.main()

