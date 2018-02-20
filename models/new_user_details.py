from mongoengine import *
import datetime
connect('chatterbot-database')
class NewUserDetails(DynamicDocument):
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)
    first_name = StringField(required=True)
    middle_name = StringField()
    last_name = StringField(required=True)
    contact_no = StringField(required=True)
    email = EmailField(required=True)

# function for adding creation date and modified date of data

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(NewUserDetails, self).save(*args, **kwargs)
