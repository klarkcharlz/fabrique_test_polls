from django.urls import path
from .views.admin import CreatePolls, CreateQuestions, UpdatePolls, UpdateQuestions
from .views.users import GetPolls, TryPoll, UserPolls


urlpatterns = [
    path('admin_create_polls/', CreatePolls.as_view()),
    path('admin_create_questions/', CreateQuestions.as_view()),
    path('admin_update_polls/<int:pk>', UpdatePolls.as_view()),
    path('admin_update_questions/<int:pk>', UpdateQuestions.as_view()),
    path('user_get_polls/', GetPolls.as_view()),
    path('try_poll/', TryPoll.as_view()),
    path('user_poll/<int:id>/', UserPolls.as_view()),
]
