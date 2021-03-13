from django.contrib.auth.urls import path
from . import views


app_name = "quizgame"
urlpatterns = [
    path("", views.home, name="home"),
    path("<topic>/", views.topic_selector, name="topic_selector"),
    path("<topic>/name", views.set_session, name="set_session"),
    path("<topic>/practice-test", views.practice, name="practice-test"),
    path("result", views.view_result, name="result"),
]
