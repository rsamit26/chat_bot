import mongoengine as m

class TrainingModel(m.Document):
    u_quest = m.StringField()
    b_answer = m.StringField()