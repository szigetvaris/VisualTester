from django.urls import path
from .views import TestView, CreateTestView, TestDeleteView, TestDetailsView

urlpatterns = [
    path("test", TestView.as_view()),
    path("createTest", CreateTestView.as_view()),
    path("deleteTest/<int:pk>/", TestDeleteView.as_view()),
    path("test/<int:pk>/", TestDetailsView.as_view()),
]
