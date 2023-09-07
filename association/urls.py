from django.contrib import admin
from django.urls import path, include

from .views import ( AssociationListView,CourtListView, SuspendAssociationView,
                    EditCourtView,MembershipPlanView,EditAssociationView,CourtEditFormView,
                    ToggleMembershipFineAmountView,ToggleMembershipPlanView, AssociationEditFormView,
                    MembershipPaymentView,DeleteAssociationView, NotificationView, NotificationEditFormView,
                    NormalAdminView, DeleteAssociationView, CreateCourtView, CreateNormalAdminView, 
                    DeleteNormalAdminView,SuperAdminView, CreateSuperAdminView,DeleteSuperAdminView )


urlpatterns = [
    
#court
   path("court/list", CourtListView.as_view(), name = "CourtListView"),
   path("court/create-court", CreateCourtView.as_view(), name = "CreateCourtView"),
   path("court/edit-court/<id>", EditCourtView.as_view(), name = "EditCourtView"),
   path("court/delete-court/<id>", CourtListView.as_view(), name = "CourtListView"),
   path("court/editform-court/<id>", CourtEditFormView.as_view(), name = "CourtEditFormView"),


#association
   path("list", AssociationListView.as_view(), name = "AssociationListView"),
   path("create-association", AssociationListView.as_view(), name = "AssociationListView"),
   path("edit-association/<id>", EditAssociationView.as_view(), name = "EditAssociationView"),
   path('delete-association/<id>',DeleteAssociationView.as_view(),name="DeleteAssociationView"),
   path("editform-association/<id>",AssociationEditFormView.as_view() ,name="AssociationEditFormView"),
   path("suspend-association/<id>", SuspendAssociationView.as_view(), name = "SuspendAssociationView"),

 #admins  
   path("association-normal-admin/list",NormalAdminView.as_view() ,name="NormalAdminView"),
   path("association-normal-admin/create/<id>",CreateNormalAdminView.as_view() ,name="CreateNormalAdminView"),
   path("association-normal-admin/delete/<id>",DeleteNormalAdminView.as_view() ,name="DeleteNormalAdminView"),
   path("association-super-admin/list",SuperAdminView.as_view() ,name="SuperAdminView"),
   path("association-super-admin/create/<id>",CreateSuperAdminView.as_view() ,name="CreateSuperAdminView"),
   path("association-super-admin/delete/<id>",DeleteSuperAdminView.as_view() ,name="DeleteSuperAdminView"),


#membership plan
   path("membership-plan/list",MembershipPlanView.as_view(),name="MembershipPlanViews"),
   path("membership-plan/create",MembershipPlanView.as_view(),name="MembershipPlanView"),
   path("membership-plan/edit/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),
   path("membership-plan/delete/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),
   path("membership-plan/editform/<id>",ToggleMembershipPlanView.as_view(),name="ToggleMembershipPlanView"),


#membership fine amount
   path("fine-amount/create",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/edit/<id>",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/delete/<id>",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),
   path("fine-amount/list",ToggleMembershipFineAmountView.as_view(),name="ToggleMembershipFineAmountView"),  

#payment
   path("membership-payment/create",MembershipPaymentView.as_view() ,name="MembershipPaymentView"),
   path("membership-payment/list",MembershipPaymentView.as_view() ,name="MembershipPaymentView"),

 #notification
   path("notification/list",NotificationView.as_view() ,name="NotificationView"),
   path("notification/edit/<id>",NotificationView.as_view() ,name="NotificationView"),
   path("notification/create/<id>",NotificationView.as_view() ,name="NotificationView"),
   path("notification/delete/<id>",NotificationView.as_view() ,name="NotificationView"),
   path("editform-notification/<id>",NotificationEditFormView.as_view() ,name="NotificationEditFormView"),
 
]