from django.contrib import admin
from django.urls import path, include

from .views import AdvocatesListView, SuspendAdvocateView, EditAdvocateProfileView,CreateAdvocatesListView,AdvocateEditFormView 

urlpatterns = [
   path("list", AdvocatesListView.as_view(), name = "AdvocatesListView"),
   path("create-advocate", CreateAdvocatesListView.as_view(), name = "CreateAdvocatesListView"),
   path("suspend-advocate/<id>", SuspendAdvocateView.as_view(), name = "SuspendAssociationView"),
   path("edit-advocate/<id>", EditAdvocateProfileView.as_view(), name = "EditAdvocateProfileView"),
   path("editform-advocate/<id>", AdvocateEditFormView.as_view(), name = "AdvocateEditFormView"),


]