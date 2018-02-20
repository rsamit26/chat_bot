from models.fbk_question import QuestionModel
from mongoengine import *
connect('chatterbot-database')
def processQuestionId(id_list):
    questions = []
    for i in QuestionModel.objects:
        if i.question_id in id_list:
            result = {
            'question_id':i.question_id,
            'question':i.question,
            'answer_type': i.answer_type

            }
            questions.append(result)
        else:
            continue


    # print(questions)
    return questions
# a = [1,3,5]
# processQuestionId(a)