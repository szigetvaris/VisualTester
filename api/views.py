from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test, TestPlan
from .serializers import TestSerializer, CreateTestSerializer, TestPlanSerializer, CreateTestPlanSerializer

from .utils import test_form_is_valid, testPlan_form_is_valid


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
            # logic
            # ugye itt megkapom majd a file-t nem tudom azt siman at lehet-e passzolni JSON-nel
            # utana eltarolom es a filepath-t adom meg a test entitasnak.
            # itt figyelembe kell venni hogy milyen tarolot hasznalok, osztott kozos tarolo,
            # vagy a local semmi dockerizalassal. HARD
            test = Test(
                name=name,
                testType=testType,
                implementation='fake/path/implementation.cy.js'
            )
            test.save()

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

        if testPlan_form_is_valid(name):
            testPlan = TestPlan(name=name)
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
