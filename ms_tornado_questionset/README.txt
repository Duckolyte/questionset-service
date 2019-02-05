2019-01-29

question_set
-> a set of question objects defined by the customer

questionary
-> bound to a patient
-> a dictionary with 0-n question objects from the question_set
-> stores the questions that a user has answered
-> a summary of the questions that a user had answered
-> must be on the vue instance and at the very end when all questions are answered stored in the db

answers
-> bound to a patient
-> referenced by questionary
-> stores the given answers matching the questionary