import falcon
from json import dumps,loads
from models.fbk_question import QuestionModel

class ViewQuestion(object):
    def on_post(self, req, resp):
        param_required = ["question_id"]
        resp.status = falcon.HTTP_200


        try:
            raw_json = req.stream.read()
            # reads posted data in inputed format
            # print raw_json
            # print type(raw_json)
        except Exception as e:  # exception for wrong input or if req.stream.read() don't read data
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)



        try:
            op_resp = loads(raw_json, encoding='utf-8')
            question_id = int(op_resp.get("question_id"))

            for i in QuestionModel.objects:
                if i.question_id == question_id:
                    pre = []
                    for j in i.predefined:
                        d = dict(predefined_answer_id=j.predefined_answer_id, predefined_answer=j.predefined_answer)
                        pre.append(d)

                    result = dict(question_id=i.question_id, question=i.question, answer_type=i.answer_type,
                                  question_tag=i.question_tag, predefined=pre)


                else:
                    continue
                print(result)
                resp.body = dumps(result, indent=4, sort_keys=True)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Question Id not found'
                                   )

    def on_get(self,req,resp):
        questions = []
        for i in QuestionModel.objects:
            row = {
                "question_id": i.question_id,
                "question": i.question,
                "question_tag": i.question_tag,
                "id" :str(i.id),
                "answer_type": i.answer_type
            }
            if row["answer_type"] == "MCQ" or row["answer_type"] == "SCQ":
                row["predefined_answer"] = i.predefined_answer
            elif row["answer_type"] == "Boolean":
                row["boolean_value"] = i.boolean_value
            questions.append(row)
        resp.body = dumps(questions)