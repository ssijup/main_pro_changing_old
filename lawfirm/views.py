from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import status
from userapp.models import Advocate

from association.permissions import IsAuthenticatedNetmagicsAdmin
from .permissions import IsAuthenticatedLawfirmAdmin
from .serializer import LawFirmListSerializer, AdvocateLawfirmSerializer
from .models import LawFirm, AdvocateLawfirm




class LawFirmListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        lawfirm = LawFirm.objects.all()
        serializer = LawFirmListSerializer(lawfirm, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    

class CreateLawFirmView(APIView):
    def post(self, request, user_id):
        data = request.data
        # data['created_by']= user_id
        advocate = Advocate.objects.get(id = user_id)

        serializer = LawFirmListSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['created_by'] = advocate
                serializer.save()
                return Response({"message": "Lawfirm details created successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:  
            return Response({
                "message": "Validation failed"+str(e),
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class SuspendLawFirmView(APIView):
    permission_classes = [IsAuthenticatedNetmagicsAdmin]

    def patch(self, request, id):
        try :
            lawfirm = LawFirm.objects.get(id = id)
            serializer=LawFirmListSerializer(lawfirm)
            lawfirm.is_suspend = not lawfirm.is_suspend
            lawfirm.save()

            if lawfirm.is_suspend:
                return Response({"message" : "LawFirm suspended sucessfully",  "data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"message" : "LawFirm suspension removed sucessfully", "data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except LawFirm.DoesNotExist:
            return Response({
                "message" : "LawFirm could not be found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DeletelawFirmView(APIView):
    permission_classes = [IsAuthenticatedNetmagicsAdmin]

    def delete(self, request, id):
        try:
            lawfirm=LawFirm.objects.get(id=id)
            lawfirm.delete()
            return Response({"message" : "LawFirm deleted sucessfully"})
        
        except LawFirm.DoesNotExist:
            return Response({"message" : "The LawFirm cout not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EditLawfirmView(APIView):
    permission_classes = [IsAuthenticatedNetmagicsAdmin | IsAuthenticatedLawfirmAdmin]

    def patch(self, request, id):
        try:
            lawfirm=LawFirm.objects.get(id=id)
            serializer = LawFirmListSerializer(lawfirm, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Lawfirm details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Lawfirm could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except LawFirm.DoesNotExist:
            return Response({"message" : "Lawfirm could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class LawfirmEditFormView(APIView):
    def get(self, request, id) :
        try:
            notification=LawFirm.objects.get(id=id)
            serializer=LawFirmListSerializer(notification)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except LawFirm.DoesNotExist:
                    return Response({"message" : "Lawfirm could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LawfirmCountView(APIView):
    def get(self, request):
        lawfirm_count = LawFirm.objects.count()
        return Response({'lawfirm_count': lawfirm_count}, status=status.HTTP_200_OK)
    

class LawFirmAdvocateListView(APIView):
    def get(self, request, id):
        advocate = AdvocateLawfirm.objects.filter(advocate__id=id)
        serializer = AdvocateLawfirmSerializer(advocate, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
class DeleteLawFirmAdvocateView(APIView):
    def delete(self, request, id):
        try:
            lawfirm=AdvocateLawfirm.objects.get(id=id)
            lawfirm.delete()
            return Response({"message" : "LawFirm deleted sucessfully"})
        
        except AdvocateLawfirm.DoesNotExist:
            return Response({"message" : "The LawFirm cout not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)