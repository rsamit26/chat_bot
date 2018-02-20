import falcon
from json import dump,loads
from models.fbk_question import QuestionModel, PredefinedAnswer
from api.v1.resources.admin_feedback.admin_function import Addpredefined

class AddPredefinedAnswer(object):

    def on_post(self,req,resp):
        resp.status = falcon.HTTP_200
        required_param = ["question_id","predefined_answer_id", "predefined_answer"]
        raw_json = req.stream.read()
        op_resp = loads(raw_json, encoding='utf-8')

        query_question_id = int(op_resp.get("question_id"))
        predefined_answer_id = int(op_resp.get("predefined_answer_id"))
        predefined_answer = (op_resp.get("predefined_answer"))
        predefined1 = PredefinedAnswer(predefined_answer_id = predefined_answer_id, predefined_answer = predefined_answer)

        for i in QuestionModel.objects:
            if i.question_id == query_question_id:
                Addpredefined(query_question_id, predefined1)
            else:
                continue

            resp.body = '{"message" : "predefined added"}'


