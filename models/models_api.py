import mongoengine as mongo
import datetime


class ResponseModel(mongo.Document):
    creation_date = mongo.DateTimeField()
    modified_date = mongo.DateTimeField(default=datetime.datetime.now)
    user_input = mongo.StringField(required=True)
    bot_output = mongo.StringField(required=True)


    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return

