from rest_framework import serializers

from .models import LawFirm, AdvocateLawfirmInvitation, LawfirmNotification
from userapp.models import Advocate


class AdvocateLawfirmInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvocateLawfirmInvitation
        fields = "__all__"


class LawFirmListSerializer(serializers.ModelSerializer):
    # advocate = AdvocateLawfirmSerializer(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Advocate.objects.all())
    class Meta:
        model = LawFirm
        fields = "__all__"


class LawFirmNotificationSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = LawfirmNotification
        fields = "__all__"
