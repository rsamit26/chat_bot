from models.fbk_question import QuestionModel
from mongoengine import *
from models.fbk_form import FbkForm

connect('chatterbot-database')


def saveData(question_tag, question, answer_type):
    QuestionModel(
        question_id=QuestionModel.objects.count() + 1,
        question_tag=question_tag,
        question=question,
        answer_type=Ans(answer_type)).save()

def Ans(answer_type1):
    # print(answer_type1)
    answer_type = {
        "1": "SCQ",
        "2": "MCQ",
        "3": "Boolean",
        "4": "Text",
        "5": "Range"
    }
    for k,v in answer_type.items():

        if int(k) == answer_type1:
            return v


def UpdateTags(question_id, new_tags):

    QuestionModel.objects(question_id = question_id).update(set__question_tag = new_tags)
    print("Tags Updated")


def Addpredefined(question_id,predefined1):
    predefined = [predefined1]
    QuestionModel.objects(question_id = question_id).update(set__predefined = predefined)


def UpdateQuestionIds(form_id,q_ids_list):
    FbkForm.objects(form_id = form_id).update(set__form_questions_id = q_ids_list)


# def AddPredefinedAnswer(question_id)

# UpdateTags(5,["hello","tags"])