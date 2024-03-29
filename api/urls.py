from django.urls import path
from .views import TestView, CreateTestView, TestDeleteView

urlpatterns = [
    path("test", TestView.as_view()),
    path("createTest", CreateTestView.as_view()),
    path("deleteTest/<int:pk>/", TestDeleteView.as_view()),
]
