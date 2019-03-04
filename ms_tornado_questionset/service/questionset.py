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
            usesImage=raw_question.usesImage,
            label=raw_question.label,
            answers=raw_question.answers
        )

    def create_question(self, question):
        question.save()


class ImageMapService:

    def __init__(self):
        pass

    def find_image_map(self, question_code):
        raw_map = ImageMap.objects.get({'mapsQuestionCode': question_code})
        return ImageMap(
            mapId=raw_map.mapId,
            mapsQuestionCode=raw_map.mapsQuestionCode,
            areas=raw_map.areas
        )

    def create_map(self, map):
        map.save()
