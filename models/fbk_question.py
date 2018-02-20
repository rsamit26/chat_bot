from mongoengine import *
import datetime


class PredefinedAnswer(EmbeddedDocument):
    predefined_answer_id = IntField()
    predefined_answer = StringField()


class QuestionModel(DynamicDocument):
    creation_date = DateTimeField()    # Creation Date of Data
    modified_date = DateTimeField(default=datetime.datetime.now)    # Modified Date
    question_id = IntField(unique=True, min_value=1, required=True)   # Question id
    question_tag = ListField(StringField(max_length=30),required=True)   # Question Tags ->
    answer_type = StringField(required=True) # Answer type for this question -> " MCQ, Radio Button, Range , Text, Boolean "
    question = StringField()  # Question whatever
    # predefined = ListField(EmbeddedDocumentField(PredefinedAnswer))

# function for adding creation date and modified date of data

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(QuestionModel, self).save(*args, **kwargs)



# connect('chatterbot-database')
# predefined1 = PredefinedAnswer(predefined_answer_id = "1", predefined_answer = "It was good")
# predefined2 = PredefinedAnswer(predefined_answer_id = "2", predefined_answer = "It was Bad")
# predefined3 = PredefinedAnswer(predefined_answer_id = "3", predefined_answer = "It was not bad")
# predefined4 = PredefinedAnswer(predefined_answer_id = "4", predefined_answer = "It was not good")
# QuestionModel(
#     question_id = "3",
#     question_tag = ["SUV","wash","car"],
#     answer_type = "boolean",
#     question = "How do you like our service",
#     predefined = [predefined1, predefined2, predefined3, predefined4]
#     ).save()