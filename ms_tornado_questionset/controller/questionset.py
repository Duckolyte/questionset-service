from tornado.httpclient import HTTPResponse

from pymodm.errors import \
    DoesNotExist, \
    ModelDoesNotExist, \
    MultipleObjectsReturned, \
    InvalidModel

from ms_tornado_questionset.service.questionset import QuestionService, ImageMapService
from ms_tornado_questionset.controller.base import BaseHandler


class QuestionHandler(BaseHandler):

    def get(self):

        question_service = QuestionService()

        '''
        new_question = Question(
            code="101",
            label="Frage0?",
            answers=[
                {
                    "code": "0",
                    "label": "Antwort0",
                    "next": "/question?code=150"
                }
            ]
        )

        question_service.create_question(new_question)
        '''
        try:
            question = question_service.find_question_by_code(
                question_code=self.get_argument(name="code")
            ).to_son().to_dict()
        except DoesNotExist:
            self.write_error(
                HTTPResponse(
                    code=500,
                    request=self.request,
                    reason="Oops we are sorry. An unexpected error occurred."
                )
            )
            return

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(question)


# TODO Questionary Handler uses yield and async loads question by need
class ImageMapHandler(BaseHandler):

    def get(self):
        image_map = ImageMapService.find_image_map(
            questionary_id=self.get_argument(name="id")
        )

        # yield self.write(question)

        '''
        questionary = {
            'questions': [
                {
                    'code': 1,
                    'label': 'frage_1?',
                    'answers': [
                        {
                            'code': 1,
                            'label': 'Ja',
                            'next': 2
                        }
                    ]
                },
                {
                    'code': 2,
                    'label': 'frage_2?',
                    'answers': [
                        {
                            'code': 1,
                            'label': 'Ja',
                            'next': 3
                        }
                    ]
                }
            ]}
            
        self.write(questionary)
        '''



