from django.urls import path
from .views import CustomTokenObtainPairSerializer,CustomTokenObtainPairView, TestapiForAuthr
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('api/login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('test_api_for_authr',TestapiForAuthr.as_view(),name='TestapiForAuthr')


]
