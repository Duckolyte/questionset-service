from ms_tornado_questionset.service.questionset import QuestionService, ImageMapService
from ms_tornado_questionset.controller.base import BaseHandler


class QuestionHandler(BaseHandler):

    def get(self):

        question_service = QuestionService()

        question = question_service.find_question_by_code(
            question_code=self.get_argument(name="code")
        ).to_son().to_dict()

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(question)


class ImageMapHandler(BaseHandler):

    def get(self):
        img_service = ImageMapService()

        image_map = img_service.find_image_map(
            question_code=self.get_argument(name="question_code")
        ).to_son().to_dict()

        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(image_map)



