from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import HealthData
from .serializer import HealthDataSerializer

# Create your views here.


def index(request):
    return render(request, 'homeView/react.html')


class HealthDataDetailView(CsrfExemptMixin, APIView):
    authentication_classes = []

    def get(self, request, dateVal):
        healthDataOneDay = get_object_or_404(HealthData, dateVal=dateVal)
        serializer = HealthDataSerializer(healthDataOneDay)
        return Response(serializer.data)

    def post(self, request, dateVal):
        serializer = HealthDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, dateVal, format=None):
        healthDataOneDay = get_object_or_404(HealthData, dateVal=dateVal)
        serializer = HealthDataSerializer(healthDataOneDay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    def put(self, request, HealthDataId):
        serializer = HealthDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
