from django.urls import path
from .views import (CustomTokenObtainPairSerializer,CustomTokenObtainPairView, AdvocatePasswordChangeView,
                    AdvocatesCountView, TestapiForAuthr )
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # path('api/login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('advocates/change-password/<id>', AdvocatePasswordChangeView.as_view(), name='change-password'),
    path('advocates/count', AdvocatesCountView.as_view(),name='AdvocatesCountView'),

    path('test_api_for_authr',TestapiForAuthr.as_view(),name='TestapiForAuthr'),


]
