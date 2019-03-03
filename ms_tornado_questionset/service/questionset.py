#from ms_tornado_questionary.model.questionary import Questionary, Question, Answer
#from ms_tornado_questionary.model.questionary import Question
from ms_tornado_questionset.model.questionset import Question, ImageMap


class QuestionSetService:

    def __init__(self):
        pass

    def store_questionset(self, questionset_file):
        # TODO later could offer a service that
        # picks a questionset file and stores it into
        # the mongodb. Eventually offer a csv parser
        pass


class QuestionService:

    def __init__(self):
        pass

    def find_question_by_code(self, question_code):
        raw_question = Question.objects.get({'code': question_code})
        return Question(
            code=raw_question.code,
            label=raw_question.label,
            answers=raw_question.answers
        )

    def create_question(self, question):
        question.save()


class ImageMapService:

    def __init__(self):
        pass

    def find_image_map(self, image_map_id):
        return ImageMap.objects.get({'_id': image_map_id})
