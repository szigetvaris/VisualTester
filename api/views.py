from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test, TestPlan, Contains, TestPlanExecution, TestExecution
from .serializers import TestSerializer, CreateTestSerializer, TestPlanSerializer, CreateTestPlanSerializer

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
            path = os.path.join(APP_ROOT_DIR, 'data/cypress/cypress/e2e/test-' + str(test.id) + '.cy.ts')
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
    queryset = Test.objects.all()
    serializer_class = TestPlanSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleteAt = timezone.now()
        instance.save()

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
            contain = Contains.objects.get(testID=testID, testPlanID=testPlanID)
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
        contains = Contains.objects.filter(testPlanID=self.kwargs['testPlanID'])
        tests = []
        for contain in contains:
            tests.append(TestSerializer(contain.testID).data)
        return Response(tests, status=status.HTTP_200_OK)
    
def TestPlanRun(request, pk):
    tp = TestPlan.objects.get(pk=pk)
    TPExecution = TestPlanExecution(testPlanID=tp)
    TPExecution.save()
    response = runAgent.delay(TPExecution.id)
    return HttpResponse(f"Test Plan with id {pk} is running...")
