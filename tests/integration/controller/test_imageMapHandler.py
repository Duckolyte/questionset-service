from json import loads

from tornado.testing import AsyncHTTPTestCase

from ms_tornado_questionset.ms_questionset import setup_server


class TestImageMapHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get_response_code(self):
        response = self.fetch('/imagemap?question_code=100')
        self.assertEqual(response.code, 200)

    def test_get_response_content(self):
        response_body = self.fetch('/imagemap?question_code=100').body
        json_response = loads(response_body)
        self.assertEqual(json_response['mapId'], '0')

    def test_get_bad_code_url_argument(self):
        response = self.fetch('/imagemap?question_code=-1')
        self.assertEqual(response.code, 500)
