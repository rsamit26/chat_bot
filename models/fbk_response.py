from mongoengine import *
import datetime

class Response(EmbeddedDocument):
    question_id = StringField()
    answer = StringField()

class FeedbackModel(Document):
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)
    feedback_form_id = StringField()
    user_id = StringField()
    ref_id = StringField()
    user_email = EmailField()
    user_phone = StringField()
    response = ListField(EmbeddedDocumentField(Response))


    """ to save Response format is ->
        
        response1 = Response(question_id = " 1 ",answer = " It was good ")
        x = FeedbackModel(response = [response1,response2,....])
     
    
    """


    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(FeedbackModel, self).save(*args, **kwargs)


# connect('chatterbot-database')
#
# response1 = Response(question_id = " 1 ",answer = " It was good ")
# response2 = Response(question_id = " 2 ",answer = " nice ")
# response3 = Response(question_id = " 3 ",answer = "4")
# response4 = Response(question_id = " 4 ",answer = " Need assistance")
#
# FeedbackModel(
#     feedback_form_id = "gcs",
#     user_id = "rsamit26",
#     user_email = "rsamit26@gmail.com",
#     user_phone = "(+91) 7872706149",
#     response = [response1, response2, response3, response4]
#     ).save()