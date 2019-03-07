from tornado.testing import AsyncHTTPTestCase
from pymodm.errors import DoesNotExist

from ms_tornado_questionset.ms_questionset import setup_server
from ms_tornado_questionset.controller.questionset import ImageMapService


class TestImageMapService(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_find_image_map(self):
        service = ImageMapService()
        response = service.find_image_map(question_code='100')
        self.assertEqual(response.mapsQuestionCode, '100')

    def test_find_image_map_bad_input(self):
        service = ImageMapService()
        with self.assertRaises(DoesNotExist):
            response = service.find_image_map(question_code='-1')
