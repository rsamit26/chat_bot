import falcon
from json import loads,dumps
from models.fbk_form import FbkForm
from api.v1.resources.user_feedback import feedback_function as ff

class FeedBackForm(object):

    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        #
        for i in FbkForm.objects:
            if i.form_name == "gcs":
                results = ff.processQuestionId(i.form_questions_id)
            else:
                continue

        resp.body = dumps(results)
