from tornado.httpclient import HTTPResponse

from pymodm.errors import \
    DoesNotExist, \
    ModelDoesNotExist, \
    MultipleObjectsReturned, \
    InvalidModel

from ms_tornado_questionset.service.questionset import QuestionService, ImageMapService
from ms_tornado_questionset.controller.base import BaseHandler

from ms_tornado_questionset.model.questionset import ImageMap


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
        # try:
        question = question_service.find_question_by_code(
            question_code=self.get_argument(name="code")
        ).to_son().to_dict()

        # except DoesNotExist:
        #     self.write_error(
        #         HTTPResponse(
        #             code=500,
        #             request=self.request,
        #             reason="Oops we are sorry. An unexpected error occurred."
        #         )
        #     )
        #     return

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(question)


# TODO Questionary Handler uses yield and async loads question by need
class ImageMapHandler(BaseHandler):

    def get(self):
        img_service = ImageMapService()

        '''
        new_question = ImageMap(
            mapId="101",
            mapsQuestionCode="111",
            areas=[
                {
                    "id": 0,
                    "mapsAnswerCode": 0,
                    "shape": "circle",
                    "coords": "100,100,30",
                    "areaPosX": 100,
                    "areaPosY": 100,
                    "areaWidth": "",
                    "areaHeight": "",
                    "areaRadius": 30
                }
            ]
        )

        img_service.create_map(new_question)
        '''

        image_map = img_service.find_image_map(
            question_code=self.get_argument(name="question_code")
        ).to_son().to_dict()

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(image_map)

        # yield self.write(question)



