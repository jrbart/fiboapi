import unittest
import httplib

class TestImport(unittest.TestCase):
    def test_is_web(self):
        conn = httplib.HTTPConnection("localhost:8080")
        conn.request("GET","/")
        response = conn.getresponse()
        conn.close()
        self.assertEqual(response.status,200)

if __name__ == "__main__":
    unittest.main()

