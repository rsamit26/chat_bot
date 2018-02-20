import falcon
from json import loads,dumps
from models.fbk_form import FbkForm
from api.v1.resources.admin_feedback.admin_function import UpdateQuestionIds


class CreateForm(object):
    def on_post(self,req,resp):
        param = ["form_name","form_questions_id"]
        try:
            raw_json = req.stream.read()
            # reads posted data in inputed format
            # print raw_json
            # print type(raw_json)
        except Exception as e:  # exception for wrong input or if req.stream.read() don't read data
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e.message)

        try:
            user_input = loads(raw_json, encoding='utf-8')
            all_keys = user_input.keys()
            difference = list(set(param) - set(all_keys))
            if difference.__len__() > 0:
                raise falcon.HTTPError(status=falcon.HTTP_400,
                                   title="missing params",
                           description="missing parameters " + str(difference)
                                   )

            else:
                form_name = user_input.get("form_name")
                form_questions_id = list(map(int,user_input.get("form_questions_id").split(",")))

            form = FbkForm(

                form_name=form_name,
                form_questions_id=form_questions_id
            )
            form.save()

        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,
                               'Malformed JSON',
                               'Could not decode the request body. The '
                               'JSON was incorrect.')
        resp.body = '{"message": "Form Created"}'
    def on_put(self,req,resp):
        param = ["form_name", "form_questions_id"]
        raw_json = req.stream.read()
        ad_input = loads(raw_json, encoding='utf-8')
        form_name = ad_input.get("form_name")
        form_questions_id = list(map(int, ad_input.get("form_questions_id").split(",")))

        for i in FbkForm.objects:
            if i.form_name == form_name:
                UpdateQuestionIds(form_name,form_questions_id)
            else: continue

