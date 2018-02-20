from mongoengine import *
from models.fbk_question import QuestionModel


class FbkForm(Document):
    form_name = StringField()
    form_questions_id = ListField(IntField())
connect('chatterbot-database')

# FbkForm(form_name = "gcs",form_questions_id = [1,3,5]).save()