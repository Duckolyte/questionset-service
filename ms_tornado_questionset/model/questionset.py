from pymongo.write_concern import WriteConcern

from pymodm import MongoModel, fields

class Questionary(MongoModel):
    '''
    _id is auto generated
    '''
    code = fields.CharField()
    questions = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class Question(MongoModel):
    '''
    _id is auto generated
    '''
    code = fields.CharField()
    usesImage = fields.BooleanField()
    label = fields.CharField()
    answers = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class ImageMap(MongoModel):
    '''
    _id is auto generated
    '''
    mapId = fields.CharField()
    mapsQuestionCode = fields.CharField()
    areas = fields.ListField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class QuestionImage(MongoModel):
    '''
    _id is auto generated
    '''
    id = fields.CharField()
    code = fields.IntegerField()
    imageSource = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'


class Answer(MongoModel):
    '''
    _id is auto generated
    '''
    code = fields.CharField()
    label = fields.CharField()
    next = fields.CharField()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'questionary-con'