from json import dumps,loads
import falcon as fn
import controllers_ml_bot as b
from models.models_api import ResponseModel


class ResponseResource(object):

    def on_post(self,req,resp):
        resp.status = fn.HTTP_200
        # print(req.content_type)

        try:
            msg = req.stream.read()
            # reads posted data in inputed format
            # print raw_json
            # print type(raw_json)
        except Exception as e:      # exception for wrong input or if req.stream.read() don't read data
            raise fn.HTTPError(fn.HTTP_400, 'Error', e.message)

        u_input = loads(msg,encoding='utf-8')
        m = u_input.get("msg")
        # print(m)
        response = b.bot.get_response(m)
        # print(response)
        resp.body = dumps(str(response))
        x = ResponseModel(
            user_input=m,
            bot_output = str(response)
        )
        x.save()
