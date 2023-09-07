from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import status
from .serializer import RegistrarSerializer
from userapp.models import Registrar


class RegistrarView(APIView):
    def get(self, request):
        registrar = Registrar.objects.all()
        serializer = RegistrarSerializer(registrar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateRegistrarView(APIView):
    def post(self, request):
        serializer = RegistrarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    
class DeleteRegistrarView(APIView):
    def delete(self, request, id):
        try:
            registrar = Registrar.objects.get(id=id)
        except Registrar.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        registrar.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class EditRegistrarView(APIView):
    def patch(self, request, id):
        try:
            registrar = Registrar.objects.get(id=id)
        except Registrar.DoesNotExist:
            return Response({"error": "Registrar not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegistrarSerializer(registrar, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditFormViewRegistrarView(APIView):
    def get(self, request, id) :
        try:
            registrar=Registrar.objects.get(id=id)
            serializer=RegistrarSerializer(registrar)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Registrar.DoesNotExist:
                    return Response({
                         "message" : "Registrar  could not be found"
                         },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred "
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




 