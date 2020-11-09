
import unittest
from mock import MagicMock

from lec10.lab.service import Service


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cache = MagicMock()
        self.service = Service(self.cache, MagicMock())

    def test_get_calls_mongo(self):
        key = "key"
        self.cache.exists.return_value = True

        self.service.get(key)

        self.cache.get.assert_called_with(key)

if __name__ == '__main__':
    unittest.main()
