from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

from .utils import test_form_is_valid, testPlan_form_is_valid
from .tasks import runAgent, runAgentRef

import os

APP_ROOT_DIR = '/home/simon/Projects/dipi/testerApp'


class TestView(generics.ListAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return Test.objects.filter(deletedAt__isnull=True)


class CreateTestView(APIView):
    serializer_class = CreateTestSerializer

    def post(self, request, format=None):
        name = request.data['name']
        testType = request.data['testType']
        implementation = request.data['implementation']

        if test_form_is_valid(name, testType, implementation):
            test = Test(
                name=name,
                testType=testType,
                implementation='fake/path/implementation.cy.js'
            )
            test.save()

            # Save the implementation file and update the test object
            path = os.path.join(
                APP_ROOT_DIR, 'data/cypress/cypress/e2e/test-' + str(test.id) + '.cy.ts')
            with open(path, 'wb+') as destination:
                for chunk in implementation.chunks():
                    destination.write(chunk)
            test.implementation = path
            test.save()

            # Test reference run
            # Run the test and save the reference run
            testExecution = TestExecution(testID=test)
            testExecution.save()
            runAgentRef.delay(testExecution.id)

            return Response(TestSerializer(test).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class TestDeleteView(generics.DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletedAt = timezone.now()
        instance.save()
        # Delete related Contains objects
        Contains.objects.filter(testID=instance).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TestDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return Test.objects.filter(pk=self.kwargs['pk'])


class TestPlanView(generics.ListAPIView):
    serializer_class = TestPlanSerializer

    def get_queryset(self):
        return TestPlan.objects.filter(deletedAt__isnull=True)


class CreateTestPlanView(APIView):
    serialize_class = CreateTestPlanSerializer

    def post(self, request, format=None):
        name = request.data['name']
        runAt = request.data['runAt']

        if testPlan_form_is_valid(name, runAt):
            testPlan = TestPlan(name=name, runAt=runAt)
            testPlan.save()

            return Response(TestPlanSerializer(testPlan).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class TestPlanDeleteView(generics.DestroyAPIView):
    queryset = TestPlan.objects.all()
    serializer_class = TestPlanSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deletedAt = timezone.now()
        instance.save()
        # Delete related Contains objects
        Contains.objects.filter(testPlanID=instance).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TestPlanDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestPlanSerializer

    def get_queryset(self):
        return TestPlan.objects.filter(pk=self.kwargs['pk'])


# Contains views
# add new Contains entry
class CreateContainsView(APIView):
    def post(self, request, format=None):
        testID = request.data['testID']
        testPlanID = request.data['testPlanID']
        # check if test and testPlan exists
        try:
            test = Test.objects.get(pk=testID, deletedAt__isnull=True)
            testPlan = TestPlan.objects.get(pk=testPlanID)
        except:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
        # check if already exists
        try:
            contain = Contains.objects.get(testID=test, testPlanID=testPlan)
            return Response({'Bad Request': 'Already exists...'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            contain = Contains(testID=test, testPlanID=testPlan)
            contain.save()

        return Response(status=status.HTTP_200_OK)


# contains torlese
# get the test and test plan id in post request body
class DeleteContainsView(APIView):
    def post(self, request, *args, **kwargs):
        testID = request.data['testID']
        testPlanID = request.data['testPlanID']

        # check if a connection exists with this test and test plan
        try:
            contain = Contains.objects.get(
                testID=testID, testPlanID=testPlanID)
            # if exists delete it
            contain.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


# Select Test Plans for given test
class TestPlansForTestView(APIView):
    def get(self, request,  *args, **kwargs):
        contains = Contains.objects.filter(testID=self.kwargs['testID'])
        test_palns = []
        for contain in contains:
            test_palns.append(TestPlanSerializer(contain.testPlanID).data)
        return Response(test_palns, status=status.HTTP_200_OK)

# Select Tests for given test plan


class TestsForTestPlanView(APIView):
    def get(self, request, *args, **kwargs):
        contains = Contains.objects.filter(
            testPlanID=self.kwargs['testPlanID'])
        tests = []
        for contain in contains:
            tests.append(TestSerializer(contain.testID).data)
        return Response(tests, status=status.HTTP_200_OK)

# Select TestExecution for given Test


class TestExecutionForTestView(APIView):
    def get(self, request, *args, **kwargs):
        test = Test.objects.get(pk=self.kwargs['testID'])
        testExecutions = TestExecution.objects.filter(
            testID=test).order_by('-createdAt')

        return Response(TestExecutionSerializer(testExecutions, many=True).data, status=status.HTTP_200_OK)


class TestExecutionForTestPlanExecutionView(APIView):
    def get(self, request, *args, **kwargs):
        testPlanExecution = TestPlanExecution.objects.get(
            pk=self.kwargs['testPlanExecutionID'])
        testExecutions = TestExecution.objects.filter(
            testPlanExecutionID=testPlanExecution).order_by('-createdAt')

        return Response(TestExecutionSerializer(testExecutions, many=True).data, status=status.HTTP_200_OK)
    
    
class TestExecutionView(APIView):
    def get(self, request, *args, **kwargs):
        testExecution = TestExecution.objects.get(pk=self.kwargs['pk'])
        return Response(TestExecutionSerializer(testExecution).data, status=status.HTTP_200_OK)

class TestPlanExecutionForTestPlanView(APIView):
    def get(self, request, *args, **kwargs):
        testPlan = TestPlan.objects.get(pk=self.kwargs['testPlanID'])
        testPlanExecutions = TestPlanExecution.objects.filter(
            testPlanID=testPlan).order_by('-createdAt')

        return Response(TestPlanExecutionSerializer(testPlanExecutions, many=True).data, status=status.HTTP_200_OK)


class TestPlanExecutionView(APIView):
    def get(self, request, *args, **kwargs):
        testPlanExecution = TestPlanExecution.objects.get(pk=self.kwargs['pk'])
        return Response(TestPlanExecutionSerializer(testPlanExecution).data, status=status.HTTP_200_OK)


class TestImagesReferenceView(APIView):
    def get(self, request, *args, **kwargs):
        testExecution = TestExecution.objects.get(pk=self.kwargs['pk'])
        test = testExecution.testID
        referenceTestExecution = TestExecution.objects.filter(testID=test, status='Pass').order_by('createdAt').first()
        
        if referenceTestExecution is None:
            return Response({'Bad Request': 'No reference found...'}, status=status.HTTP_400_BAD_REQUEST)
        
        images = TestImage.objects.filter(testExecutionID=referenceTestExecution)
        
        return Response(TestImageSerializer(images, many=True).data, status=status.HTTP_200_OK)
        
    
    
class TestImageForTestExecutionView(APIView):
    def get(self, request, *args, **kwargs):
        testExecution = TestExecution.objects.get(pk=self.kwargs['pk'])
        images = TestImage.objects.filter(testExecutionID=testExecution)
        
        return Response(TestImageSerializer(images, many=True).data, status=status.HTTP_200_OK)
    
    
class TestImageAsImage(APIView):
    def get(self, request, *args, **kwargs):
        testImage = get_object_or_404(TestImage, pk=self.kwargs['testImage'])
        response = FileResponse(open(testImage.imagePath, 'rb'))
        return response


def TestPlanRun(request, pk):
    tp = TestPlan.objects.get(pk=pk)
    TPExecution = TestPlanExecution(testPlanID=tp)
    TPExecution.save()
    response = runAgent.delay(TPExecution.id)
    return HttpResponse(f"Test Plan with id {pk} is running...")
