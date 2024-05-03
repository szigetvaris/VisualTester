from celery import shared_task
from .models import TestPlan, Test, TestPlanExecution, TestExecution, TestImage, Contains


@shared_task
def sharedtask():
    return 'go home'


@shared_task
def runAgent(testPlanExecutionID):
    tpExecution = TestPlanExecution.objects.get(pk=testPlanExecutionID)
    contains = Contains.objects.filter(testPlanID=tpExecution.testPlanID)
    tests = [contain.testID for contain in contains]
    
    # Step 0 - extract file paths and run the Cypress tests
    filePaths = [t.implementation for t in tests]
    # docker -it run ...
    
    # for test in tests:
    #     # Step 1 - create a TestExecution object
    #     testExecution = TestExecution(testID=test.testID, testPlanExecutionID=testPlanExecution)
    #     testExecution.save()
        
        # Step 2 - Image diff calculation
        # Case 1: Test did not run before
        # For all images in the cypress screenshots/testName folder
        # Move images from cypress screenshots to the persistent folder
        # Create a TestImage entry for each imageTestExecution
        # Set Test.referenceID to the current  ID
        
        # Case 2: Tast has a reference run
        # For all images in the cypress screenshots/testName folder
        # use imgdiff.py to compare the images
        # update execution.bugs if needed
        # move the output to the persistent folder
        # Create a TestImage entry for each image
        
        # Step 3 - Cypress logs and TestExecution update
        # extract runTime and info from cypress logs
        # update the TestExecution object
        # update testExecution.status 
        # to 'Fail'/'Pass' depends on tetExecution.bugs
        
