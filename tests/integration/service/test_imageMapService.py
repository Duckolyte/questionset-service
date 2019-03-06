from tornado.testing import AsyncHTTPTestCase

from ms_tornado_questionset.ms_questionset import setup_server
from ms_tornado_questionset.controller.questionset import QuestionService


class TestImageMapService(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_find_image_map(self):
        service = QuestionService()
        response = service.find_question_by_code(question_code='1')
        self.assertEqual(response.code, '1')
