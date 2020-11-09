import unittest

from lec10.lab.controller import app


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_delete_returns204(self):
        response = self.app.delete('/storage/1', follow_redirects=True)

        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
