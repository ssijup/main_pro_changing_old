from rest_framework import serializers

from .models import LawFirm, AdvocateLawfirm


class LawFirmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawFirm
        fields = "__all__"

class AdvocateLawfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateLawfirm
        fields = "__all__"