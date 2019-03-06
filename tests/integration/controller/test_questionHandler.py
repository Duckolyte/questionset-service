from json import loads

from tornado.testing import AsyncHTTPTestCase
from pymodm.errors import DoesNotExist


from ms_tornado_questionset.ms_questionset import setup_server


class TestQuestionHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get_response_code(self):
        response = self.fetch('/question?code=1')
        self.assertEqual(response.code, 200)

    def test_get_response_content(self):
        response_body = self.fetch('/question?code=1').body
        json_response = loads(response_body)
        self.assertEqual(json_response['code'], '1')

    def test_get_response_content(self):
        response = self.fetch('/question?code=-1')
        self.assertEqual(response.code, 500)
