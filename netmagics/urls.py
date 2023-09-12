from django.urls import path, include

from .views import NetmagicsAdminCreateView, ListNetmagicsAdmin, DeleteNetmagicsAdmin


urlpatterns = [
    #Registrar view
    path("admin/create", NetmagicsAdminCreateView.as_view(), name = "NetmagicsAdminCreateView"),  
    path("admin/list", ListNetmagicsAdmin.as_view(), name = "ListNetmagicsAdmin"),  
    path("admin/delete/<id>", DeleteNetmagicsAdmin.as_view(), name = "DeleteNetmagicsAdmin"),  

]




