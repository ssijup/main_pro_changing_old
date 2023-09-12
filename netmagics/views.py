from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import ActivityTracker
from rest_framework.response import Response
from .serializer import ActivityTrackerSerializer

class AcivityTrackerView(APIView):
    def get(self, request):
        registrar = ActivityTracker.objects.all()
        serializer = ActivityTrackerSerializer(registrar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
