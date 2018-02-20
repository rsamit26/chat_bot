import falcon
from json import dumps,loads
from models.fbk_response import FeedbackModel
from models.fbk_response import Response

class PostFeedbackResponse(object):

    def on_post(self,req,resp):
        """

        :type resp: success
        """
        resp.status = falcon.HTTP_200

        param = ["feedback_form_id", "question_id",
                 "ref_id", "user_id", "user_email",
                 "user_phone", "answer"
                     ]


        try:
            raw_json = req.stream.read()
            # reads posted data in inputed format
            # print raw_json
            # print type(raw_json)
        except Exception as e:      # exception for wrong input or if req.stream.read() don't read data
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
                user_id = user_feedback.get("user_id")
                user_email = user_feedback.get("user_email")
                user_phone = user_feedback.get("user_phone")
                ref_id = user_feedback.get("ref_id")
                feedback_form_id = user_feedback.get("feedback_form_id")
                answer = user_feedback.get("answer")
                question_id = user_feedback.get("question_id")

                user_response = Response(question_id = question_id,answer = answer)


                feedback = FeedbackModel(
                    user_id=user_id,
                    user_email=user_email,
                    user_phone=user_phone,
                    ref_id=ref_id,
                    feedback_form_id = feedback_form_id,
                    response  =  [user_response]
                )

                # feedback.save()

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect.')

        resp.body = '{"message": "Data Created"}'