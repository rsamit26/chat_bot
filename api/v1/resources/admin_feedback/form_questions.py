import falcon
from json import dumps, loads
from models.fbk_question import QuestionModel, PredefinedAnswer
from api.v1.resources.admin_feedback.admin_function import UpdateTags,saveData


class AdminFeedbackQuestion(object):

    def on_put(self, req, resp):
        resp.body = falcon.HTTP_200
        param = ["question_id", "question_tag"]

        raw_json = req.stream.read()

        op_resp = loads(raw_json, encoding='utf-8')

        query_question_id = int(op_resp.get("question_id"))
        new_question_tag = (op_resp.get("question_tag")).strip().split(",")
        # print(question_id,new_question_tag)

        for i in QuestionModel.objects:
            if i.question_id == query_question_id:
                UpdateTags(query_question_id, new_question_tag)
            else:
                continue

            # resp.body = dumps()


    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        param = ["question_tag", "answer_type", "question"]

        try:
            raw_json = req.stream.read()
            # reads posted data in inputed format
            # print raw_json
            # print type(raw_json)
        except Exception as e:  # exception for wrong input or if req.stream.read() don't read data
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        try:
            user_feedback = loads(raw_json, encoding='utf-8')
            all_keys = user_feedback.keys()
            difference = list(set(param) - set(all_keys))
            if difference.__len__() > 0:
                raise falcon.HTTPError(status=falcon.HTTP_400,
                                       title="missing params",
                                       description="missing parameters " + str(difference)
                                       )

            else:
                question_tag = user_feedback.get("question_tag").split(",")
                answer_type = int(user_feedback.get("answer_type"))
                # print(answer_type)
                question = user_feedback.get("question")
                if answer_type == 1 or answer_type == 2:

                    param.append("predefined_answer")
                    all_keys = user_feedback.keys()
                    difference = list(set(param) - set(all_keys))

                    if difference.__len__() > 0:
                        raise falcon.HTTPError(status=falcon.HTTP_400,
                                               title="missing params",
                                               description="missing parameters " + str(difference)
                                               )

                    else:
                        saveData(question_tag, question, answer_type)
                        predefined_answer = user_feedback.get("predefined_answer").strip().split("^")
                        QuestionModel.objects(question=question).update(predefined_answer=predefined_answer)
                elif answer_type == 3:
                    param.append("boolean_value")
                    all_keys = user_feedback.keys()
                    difference = list(set(param) - set(all_keys))

                    if difference.__len__() > 0:
                        raise falcon.HTTPError(status=falcon.HTTP_400,
                                               title="missing params",
                                               description="missing parameters " + str(difference)
                                               )
                    else:
                        saveData(question_tag,question,answer_type)
                        Boolean_value = user_feedback.get("boolean_value").strip().split("^")
                        QuestionModel.objects(question=question).update(boolean_value=Boolean_value)
                else:
                    saveData(question_tag, question, answer_type)


        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect.'
                                   'Param Required -> answer_type,question,question_tag')

        resp.body = '{"message": "Data Created"}'
