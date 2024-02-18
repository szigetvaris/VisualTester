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
            implementation = serializer.data.get('implementation')

            #logic
            test = Test(implementation=implementation)
            test.save()
        
            return Response(TestSerializer(test).data, status=status.HTTP_201_CREATED)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
