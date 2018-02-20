import falcon
from json import dumps,loads
from models.fbk_response import FeedbackModel,Response


class ViewResponse(object):
    def on_post(self,req,resp):
        resp.status = falcon.HTTP_200
        raw_json = req.stream.read()
        ad_input = loads(raw_json, encoding='utf-8')

        ref_id = ad_input.get("ref_id")

        for i in FeedbackModel.objects:
            if i.ref_id == ref_id:
                result = dict(user_id=i.user_id, user_email=i.user_email, user_phone=i.user_phone, ref_id=i.ref_id,
                              feedback_form_id=i.feedback_form_id, question_id=i.response[0]["question_id"], answer=i.response[0]["answer"])
                # print("5")
                # print(i.response[0]["question_id"],i.response[0]["answer"])
            else: continue
        # print(result)
        resp.body = dumps(result)
