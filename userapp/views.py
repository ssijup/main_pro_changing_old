from .serializers import CustomTokenObtainPairSerializer, PasswordChangeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserData, Advocate
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class PasswordChangeView(APIView):
    def post(self, request, id):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            # user = self.request.user
            try:
                # advocate=Advocate.objects.get(id=id)
                # user=advocate.user
                user=UserData.objects.get(id=id)
            except:
                 pass
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdvocatesCountView(APIView):
    def get(self, request):
        advocates_count = Advocate.objects.count()
        return Response({'advocates_count': advocates_count}, status=status.HTTP_200_OK)