from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.state import token_backend
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class TestapiForAuthr(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user=request.user
        print("user :",user.name,"  ",user.id,"  ", user.email)
        auth_header = request.headers.get('Authorization')
        print("siju",auth_header)
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split('Bearer ')[1]

            decoded_payload = token_backend.decode(token)
            user_id = decoded_payload.get('user_id')
            # username = decoded_payload.get('username')
            email = decoded_payload.get('email')  # If email is included in the token payload
            print("email :", email ,user_id)
            return Response({"message" : "success"})

        else:
            return Response({"message" : "failed"})