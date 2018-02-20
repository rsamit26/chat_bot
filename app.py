import falcon
import mongoengine as mongo
from api.v1.resources.admin_feedback.form_questions import AdminFeedbackQuestion
from api.v1.resources.interaction import ResponseResource
from api.v1.resources.user_feedback.post_feedack_response import PostFeedbackResponse
from api.v1.resources.user_feedback.show_feedback_form_questions import FeedBackForm
from api.v1.resources.admin_feedback.addpredefinedanswer import AddPredefinedAnswer
from api.v1.resources.admin_feedback.admin_view_response import ViewResponse
from api.v1.resources.admin_feedback.create_form import CreateForm
from api.v1.resources.admin_feedback.view_question import ViewQuestion
from api.v1.resources.user_feedback.new_users import NewUserApi
from api.v1.resources.static_page.static_page_file import AddQuestions,CreateFormData,Bot


# defining api

api = falcon.API()

# Database connection


mongo.connect('chatterbot-database')

# adding routes
api.add_route('/api/interaction', ResponseResource())
# api.add_route('/api/fbk', FeedbackResources())
api.add_route('/api/form', FeedBackForm())
api.add_route('/api/response', PostFeedbackResponse())
api.add_route('/api/ad_q', AdminFeedbackQuestion())
api.add_route('/api/ad_p', AddPredefinedAnswer())
api.add_route('/api/ad_vr', ViewResponse())
api.add_route('/api/ad_cf', CreateForm())
api.add_route('/api/ad_vq', ViewQuestion())
api.add_route('/questions', AddQuestions())
api.add_route('/createforms', CreateFormData())
api.add_route('/bot', Bot())
api.add_route('/new_user', NewUserApi())

