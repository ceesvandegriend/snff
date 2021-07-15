import unittest

import httpimport


class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        URL = "https://www.griend.eu/python"

        httpimport.add_remote_repo(["snff",], URL)

        import snff

        snff.execute()

if __name__ == '__main__':
    unittest.main()
