from django.contrib import admin
from django.urls import path, include

from .views import RegistrarView, CreateRegistrarView, DeleteRegistrarView, EditRegistrarView, EditFormViewRegistrarView


urlpatterns = [
    #Registrar view
    path("list-registrar", RegistrarView.as_view(), name = "RegistrarView"),  
    path("edit-registrar/<id>", EditRegistrarView.as_view(), name = "EditRegistrarView"),  
    path("delete-registrar/<id>", DeleteRegistrarView.as_view(), name = "DeleteRegistrarView"),  
    path("create-registrar", CreateRegistrarView.as_view(), name = "CreateRegistrarView"),
    path("editform-registrar/<id>",EditFormViewRegistrarView.as_view(),name='EditFormViewRegistrarView')
]