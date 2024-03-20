from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Test
from .serializers import TestSerializer, CreateTestSerializer


class TestView(generics.ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class CreateTestView(APIView):
    serializer_class = CreateTestSerializer

    def post(self, request, format=None):
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            testType = serializer.data.get('testType')
            implementation = serializer.data.get('implementation')

            print(implementation)
            # logic
            # ugye itt megkapom majd a file-t nem tudom azt siman at lehet-e passzolni JSON-nel
            # utana eltarolom es a filepath-t adom meg a test entitasnak.
            # itt figyelembe kell venni hogy milyen tarolot hasznalok, osztott kozos tarolo,
            # vagy a local semmi dockerizalassal. HARD
            test = Test(
                name=name,
                testType=testType,
                implementation=implementation
            )
            # test.save()

            return Response(TestSerializer(test).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
