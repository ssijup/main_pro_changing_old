from rest_framework import serializers
from userapp.models import UserData, Advocate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"


class NormalAdvocateSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Advocate
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('type_of_user') == 'normal_advocate':
            return data
        return None
