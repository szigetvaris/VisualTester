from django.urls import path
from .views import *

urlpatterns = [
    # Test URLs
    path("test", TestView.as_view()),
    path("createTest", CreateTestView.as_view()),
    path("deleteTest/<int:pk>/", TestDeleteView.as_view()),
    path("test/<int:pk>/", TestDetailsView.as_view()),
    # Test Plan URLs
    path("testPlan", TestPlanView.as_view()),
    path("createTestPlan", CreateTestPlanView.as_view()),
    path("deleteTestPlan/<int:pk>/", TestPlanDeleteView.as_view()),
    path("testPlan/<int:pk>/", TestPlanDetailsView.as_view()),
    # Contains URLs
    path("contains", CreateContainsView.as_view()),
]
