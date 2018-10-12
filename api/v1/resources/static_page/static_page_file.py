import falcon
import os

script_dir = str(os.getcwd())  # <-- absolute dir the script is in


class AddQuestions(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        rel_path = "/views2/add_question.html"
        with open(script_dir + rel_path, 'r') as f:
            resp.body = f.read()


class CreateFormData(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        rel_path = "/views2/create_form.html"
        with open(script_dir + rel_path, 'r') as f:
            resp.body = f.read()


class Bot(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        rel_path = "/views/index.html"
        with open(script_dir + rel_path, 'r') as f:
            resp.body = f.read()


class UserFeedback(object):
    """docstring for UserFeedback"""

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        rel_path = "/views2/index.html"
        with open(script_dir + rel_path, 'r') as f:
            resp.body = f.read()
