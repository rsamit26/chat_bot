import falcon
from json import dumps,loads
from api.v1.resources.admin_feedback.admin_function import AnswerType

class ViewAnswerType(object):
    def on_get(self,req,resp):
        resp.body = dumps(AnswerType())