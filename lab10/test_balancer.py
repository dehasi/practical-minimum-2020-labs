import unittest

import responses
from lec10.lab.balancer import app


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    @responses.activate
    def test_simple(self):
        responses.add(responses.GET, 'http://localhost:8080/storage/11',
                  json={'value': 'value'}, status=200)

        response = self.app.get('/11', follow_redirects=True)

        assert response.data.decode('utf-8') == '{"value": "value"}'

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == 'http://localhost:8080/storage/11'
        assert responses.calls[0].response.text == '{"value": "value"}'


if __name__ == '__main__':
    unittest.main()
