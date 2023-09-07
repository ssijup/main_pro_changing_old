from rest_framework import serializers
from userapp.models import Registrar
from advocates.serializer import UserSerializer

class RegistrarSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Registrar
        fields = "__all__"
