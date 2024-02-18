from django.urls import path
from .views import TestView, CreateTestView

urlpatterns = [
    path("test", TestView.as_view()),
    path("createTest", CreateTestView.as_view()),
]