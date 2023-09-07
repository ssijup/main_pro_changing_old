from rest_framework import serializers

from .models import Association, Jurisdiction ,Court, MembershipPlan, MembershipFineAmount, Notification, AssociationMembershipPayment
from userapp.models import Advocate
from advocates.serializer import UserSerializer



class CourtListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Court
        fields="__all__"

class AssociationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = "__all__"


class ListNormalAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Advocate
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('type_of_user') == 'normal_admin':
            return data
        return None

class ListSuperAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer() 
    class Meta:
        model = Advocate
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data.get('type_of_user') == 'super_admin':
            return data
        return None

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = "__all__"

class MembershipFineAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipFineAmount
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"


class AssociationMembershipPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssociationMembershipPayment
        fields="__all__"