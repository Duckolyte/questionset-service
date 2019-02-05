#from ms_tornado_questionary.model.questionary import Questionary, Question, Answer
#from ms_tornado_questionary.model.questionary import Question
from ms_tornado_questionset.model.questionset import Question


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


'''
class QuestionaryService:

    def __init__(self):
        pass

    def find_questionary(self, questionary_id):
        return Questionary.objects.get({'_id': questionary_id})

    def create_questionary(self, questionary):
        questionary.save()


class AnswerService:

    def __init__(self):
        pass

    def find_answer(self, answer_id):
        return Answer.objects.get({'_id': answer_id})
'''
