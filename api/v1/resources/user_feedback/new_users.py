import falcon
from json import dumps,loads
from models.new_user_details import NewUserDetails


class NewUserApi(object):

    def on_post(self,req,resp):
        resp.status = falcon.HTTP_200
        req_param = ["first Name","last Name", "Phone No", "Email","middle name"]
        raw_json = req.stream.read()
        user_input = loads(raw_json,encoding='utf-8')
        first_name = user_input.get("first Name")
        # middle_name = user_input.get("middle Name")
        last_name = user_input.get("last Name")
        contact_no = int(user_input.get("Phone No"))
        email = user_input.get("Email")

        NewUserDetails(first_name=first_name,last_name=last_name,contact_no=contact_no
                       , email=email).save()
        resp.body = '{"message":"User Created"}'