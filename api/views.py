from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test
from .serializers import TestSerializer, CreateTestSerializer

from .utils import test_form_is_valid

class TestView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    

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
