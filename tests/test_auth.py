import unittest
from auth import get_spotify_client

class TestAuth(unittest.TestCase):
    def test_get_spotify_client(self):
        sp = get_spotify_client()
        self.assertIsNotNone(sp)

if __name__ == '__main__':
    unittest.main()
