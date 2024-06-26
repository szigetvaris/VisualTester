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
    path("getContainsT/<int:testID>/", TestPlansForTestView.as_view()),
    path("getContainsTP/<int:testPlanID>/", TestsForTestPlanView.as_view()),
    path("deleteContains", DeleteContainsView.as_view()),
    # Test Plan Run
    path("runTestPlan/<int:pk>/", TestPlanRun),
    # Test Execution
    path("testExecution/<int:pk>/", TestExecutionView.as_view()),
    path("testExecution/test/<int:testID>/",
         TestExecutionForTestView.as_view()),
    path("testExecution/testPlan/<int:testPlanExecutionID>/",
         TestExecutionForTestPlanExecutionView.as_view()),
    path("testExecution/reference/<int:pk>/",
         TestImagesReferenceView.as_view()),
    path("testImage/testExecution/<int:pk>/", TestImageForTestExecutionView.as_view()),
    path("testExecution/image/<int:testImage>/", TestImageAsImage.as_view()),
    # TestPlan Execution
    path("testPlanExecution/<int:pk>/", TestPlanExecutionView.as_view()),
    path("testPlanExecution/testPlan/<int:testPlanID>/",
         TestPlanExecutionForTestPlanView.as_view()),
]
