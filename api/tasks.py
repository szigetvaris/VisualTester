from celery import shared_task
from .models import TestPlan, Test, TestPlanExecution, TestExecution, TestImage, Contains
import os
import subprocess

APP_ROOT_DIR = '/home/simon/Projects/dipi/testerApp'
CYPRESS_ROOT_DIR = APP_ROOT_DIR + '/data/cypress'

def extract_test_name(import_path):
    path_parts = import_path.split("/")
    cypress_indices = [i for i, part in enumerate(path_parts) if part == "cypress"]
    if len(cypress_indices) < 2:
        return "Invalid path"

    relevant_parts = path_parts[cypress_indices[1]:]
    test_name = "/".join(relevant_parts)

    return test_name


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
        
        
@shared_task
def runAgentRef(testExecutionID):
    # Step 0 - extract file paths and run the Cypress tests
    testExecution = TestExecution.objects.get(pk=testExecutionID)
    test = testExecution.testID
    cypress_path = extract_test_name(test.implementation)
    
    docker_command = ('docker run -it -v ' + CYPRESS_ROOT_DIR 
    + ':/cypress/e2e -w /cypress/e2e cypress/included:12.12.0 --spec '
    + cypress_path)
    
    test.status = "In Progress"
    test.save()
    process = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(test.name, test.status)
    if process.returncode == 0:
        # Step 1 - copy the images into the persistent folder, with correct names
        
        # Step 2 - create Image objects from the output images
        
        # Step 3 - fill the testExecution with the data, if needed.
        test.status = "Pass"
        test.save()
    else:
        print(f"Error executing {test.name} test...")
        
