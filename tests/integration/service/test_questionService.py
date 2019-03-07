from tornado.testing import AsyncHTTPTestCase
from pymodm.errors import DoesNotExist

from ms_tornado_questionset.ms_questionset import setup_server
from ms_tornado_questionset.controller.questionset import QuestionService


class TestQuestionService(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_find_question_by_code(self):
        service = QuestionService()
        response = service.find_question_by_code(question_code='1')
        self.assertEqual(response.code, '1')

    def test_find_question_bad_input(self):
        service = QuestionService()
        with self.assertRaises(DoesNotExist):
            response = service.find_question_by_code(question_code='-1')
