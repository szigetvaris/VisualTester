from celery import shared_task
from .models import TestPlan, Test, TestPlanExecution, TestExecution, TestImage, Contains
from testerApp.imgdiff import compare_and_draw_rectangles

import os
import subprocess
import shutil
import datetime

APP_ROOT_DIR = '/home/simon/Projects/dipi/testerApp'
CYPRESS_ROOT_DIR = APP_ROOT_DIR + '/data/cypress'


def copy_image_resource(test_id, execution_number):
    test_name = "test-" + str(test_id) + ".cy.ts"
    # Define source and destination directories
    source_dir = os.path.join(
        CYPRESS_ROOT_DIR, f"cypress/screenshots/{test_name}")
    destination_dir = os.path.join(
        APP_ROOT_DIR, f"data/result/{test_name}/{execution_number}")

    # Create destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Copy all files from source to destination directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            # Create the destination filename
            destination_filename = f"{name}_{execution_number}{extension}"
            destination_file = os.path.join(
                destination_dir, destination_filename)
            # Copy the file
            shutil.copyfile(source_file, destination_file)


def extract_test_name(import_path):
    path_parts = import_path.split("/")
    cypress_indices = [i for i, part in enumerate(
        path_parts) if part == "cypress"]
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

    tpExecution.status = "In Progress"
    tpExecution.save()
    # Step 0 - extract file paths and run the Cypress tests
    filePaths = [extract_test_name(t.implementation) for t in tests]

    docker_command = ('docker run -it -v ' + CYPRESS_ROOT_DIR
                      + ':/cypress/e2e -w /cypress/e2e cypress/included:12.12.0 --spec '
                      + ' '.join(filePaths))

    process = subprocess.Popen(
        docker_command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(f"Cypress Process finished {process.returncode}")

    for test in tests:
        # Step 0 - Create the testExecution object
        testExecution = TestExecution(
            testID=test, testPlanExecutionID=tpExecution)
        testExecution.save()
        test.executions += 1
        test.save()

        # Step 1 - copy the images into the persistent folder
        copy_image_resource(test.id, test.executions)

        # Step 2 - create Image objects from the output images
        refPictureDir = os.path.join(
            APP_ROOT_DIR, f"data/result/test-{test.id}.cy.ts/{test.referenceID}")
        os.makedirs(refPictureDir, exist_ok=True)
        actualPictureDir = os.path.join(
            APP_ROOT_DIR, f"data/result/test-{test.id}.cy.ts/{test.executions}")
        os.makedirs(actualPictureDir, exist_ok=True)
        refFiles = os.listdir(refPictureDir)
        actualFiles = os.listdir(actualPictureDir)
        for i in range(len(refFiles)):
            refFileName = refFiles[i]
            actualFileName = actualFiles[i]
            refPicturePath = os.path.join(refPictureDir, refFileName)
            actualPicturePath = os.path.join(actualPictureDir, actualFileName)
            if os.path.isfile(refPicturePath) and os.path.isfile(actualPicturePath):
                testImage = TestImage(
                    testExecutionID=testExecution, name=actualFileName, imagePath=actualPicturePath)
                bug = compare_and_draw_rectangles(
                    refPicturePath, actualPicturePath)
                if bug:
                    testImage.status = "Fail"
                    testExecution.bugs += 1
                    testExecution.save()
                else:
                    testImage.status = "Pass"
                testImage.save()
                print(f"Test Image {actualFileName} saved")

            else:
                print(
                    f"File {refPicturePath} or {actualPicturePath} not found")

        # Step 3 - fill the testExecution with the data, if needed.
        testExecution.status = "Pass" if testExecution.bugs == 0 else "Fail"
        # execution time

    tpExecution.status = "Completed"
    tpExecution.lastRun = datetime.datetime.now()
    tpExecution.save()
    print("Test Plan Execution finished")


@shared_task
def runAgentRef(testExecutionID):
    # Step 0 - extract file paths and run the Cypress tests
    testExecution = TestExecution.objects.get(pk=testExecutionID)
    test = testExecution.testID
    cypress_path = extract_test_name(test.implementation)

    docker_command = ('docker run -it -v ' + CYPRESS_ROOT_DIR
                      + ':/cypress/e2e -w /cypress/e2e cypress/included:12.12.0 --spec '
                      + cypress_path)

    process = subprocess.Popen(
        docker_command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(f"Cypress Process finished {process.returncode}")
    if process.returncode == 0:
        # Step 1 - copy the images into the persistent folder, with correct names
        copy_image_resource(test.id, test.executions)

        # Step 2 - create Image objects from the output images
        # Define the directory
        directory = os.path.join(
            APP_ROOT_DIR, f"data/result/test-{test.id}.cy.ts/{test.executions}")

        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                # Create a new TestImage object
                test_image = TestImage(
                    testExecutionID=testExecution,
                    name=filename,
                    imagePath=file_path,
                    status="Pass"
                )
                test_image.save()

        # Step 3 - fill the testExecution with the data, if needed.
        test.referenceID = 0
        test.save()
        testExecution.status = "Pass"
        testExecution.save()
    else:
        print(f"Error executing {test.name} test...")
