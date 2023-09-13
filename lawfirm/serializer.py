from rest_framework import serializers

from .models import LawFirm, AdvocateLawfirm
from userapp.models import Advocate


class AdvocateLawfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateLawfirm
        fields = "__all__"


class LawFirmListSerializer(serializers.ModelSerializer):
    # advocate = AdvocateLawfirmSerializer(read_only=True) 
    # created_by = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Advocate.objects.all(), source='advocate')
    class Meta:
        model = LawFirm
        fields = "__all__"
