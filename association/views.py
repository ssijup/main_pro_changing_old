from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta
from instamojo_wrapper import Instamojo
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import status
from django.utils import timezone

from .serializer import ( AssociationListSerializer,CourtListSerializer,AssociationMembershipPaymentSerializer,
                         NotificationSerializer,MembershipFineAmountSerializer, MembershipPlanSerializer,
                         ListNormalAdminSerializer, ListSuperAdminSerializer )
from .models import ( Association, Court, Jurisdiction,AssociationMembershipPayment,AssociationPaymentRequest, 
                     MembershipPlan,MembershipFineAmount,Notification, AdvocateAssociation,
                      AssociationSuperAdmin )
from advocates.serializer import NormalAdvocateSerializer
from userapp.models import Advocate, UserData

from django.conf import settings
api = Instamojo(api_key=settings.API_KEY, auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')
 



class CreateCourtView(APIView):
    def post(self, request):
        serializer = CourtListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Court created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourtListView(APIView):
    def get(self, request):
        advocates = Court.objects.all()
        serializer = CourtListSerializer(advocates, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            court=Court.objects.get(id=id)
            court.delete()
            return Response({"message" : "Court deleted sucessfully"})
        
        except Court.DoesNotExist:
            return Response({"message" : "The Court could not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred. Please try again later"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class EditCourtView(APIView):
    def patch(self, request, id):
        try:
            court=Court.objects.get(id=id)
            serializer = CourtListSerializer(court, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Court details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Court could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Court.DoesNotExist:
            return Response({"message" : "Court could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class AssociationListView(APIView):
    def get(self, request):
        advocates = Association.objects.all()
        serializer = AssociationListSerializer(advocates, many = True)
        return Response(serializer.data,status= status.HTTP_200_OK)
        
    def post(self, request):
        data = request.data
        serializer = AssociationListSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Association  created successfully"}, status=status.HTTP_201_CREATED)

        except serializers.ValidationError:  
            return Response({
                "message": "Validation failed"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class EditAssociationView(APIView):
    def patch(self, request, id):
        try:
            association=Association.objects.get(id=id)
            serializer = AssociationListSerializer(association, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "Association details updated sucessfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Association could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Association.DoesNotExist:
            return Response({"message" : "Association could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class SuspendAssociationView(APIView):
    def patch(self, request, id):
        try :
            association = Association.objects.get(id = id)
            serializer=AssociationListSerializer(association) 
            association.is_suspend = not association.is_suspend
            association.save()

            if association.is_suspend:
                return Response({"Message" : "Association suspended sucessfully", "data":serializer.data}, status = status.HTTP_202_ACCEPTED)
            return Response({"Message" : "Association suspension removed sucessfully", "data":serializer.data}, status = status.HTTP_202_ACCEPTED)

        except Association.DoesNotExist:
            return Response({
                "error" : "Association does not found"
                }, status= status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred",
                "errors": str(e) 
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class DeleteAssociationView(APIView):
    def delete(self, request, id):
        try:
            association=Association.objects.get(id=id)
            association.delete()
            return Response({"message" : "Association deleted sucessfully"})
        
        except Association.DoesNotExist:
            return Response({"message" : "The Association could not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred .Please try again later"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class NormalAdminView(APIView):
    def get(self, request):
        normal_admin = Advocate.objects.filter(type_of_user='normal_admin')
        serializer = ListNormalAdminSerializer(normal_admin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateNormalAdminView(APIView):
    def post(self, request, id):
        try:
            user = UserData.objects.get(id=id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            advocate = Advocate.objects.get(user=user, type_of_user='normal_admin')
            return Response({"error": "Role already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except Advocate.DoesNotExist:
            request.data['user'] = user.id
            request.data['type_of_user'] = 'normal_admin'
            serializer = ListNormalAdminSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    
class DeleteNormalAdminView(APIView):
    def delete(self, request, id):
        try:
            normal_admin = Advocate.objects.get(user__id=id,type_of_user='normal_admin')
        except Advocate.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        normal_admin.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class SuperAdminView(APIView):
#     def get(self, request):
#         super_admin = Advocate.objects.filter(type_of_user='super_admin')
#         serializer = ListNormalAdminSerializer(super_admin, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class SuperAdminView(APIView):
    def get(self, request):
        super_admin = AssociationSuperAdmin.objects.all()
        serializer = ListSuperAdminSerializer(super_admin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateSuperAdminView(APIView):
    def post(self, request, id):
        try:
            user = UserData.objects.get(id=id)
        except UserData.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            super_admin = AssociationSuperAdmin.objects.get(user=user)
            return Response({"error": "Role already exists"}, status=status.HTTP_400_BAD_REQUEST)
        except AssociationSuperAdmin.DoesNotExist:
            request.data['user'] = user.id
            request.data['type_of_user'] = 'super_admin'
            serializer = ListSuperAdminSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# class CreateSuperAdminView(APIView):
#     def post(self, request, id):
#         try:
#             user = UserData.objects.get(id=id)
#         except UserData.DoesNotExist:
#             return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#         try:
#             advocate = Advocate.objects.get(user=user, type_of_user='super_admin')
#             return Response({"error": "Role already exists"}, status=status.HTTP_400_BAD_REQUEST)
#         except Advocate.DoesNotExist:
#             request.data['user'] = user.id
#             request.data['type_of_user'] = 'super_admin'
#             serializer = ListSuperAdminSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(user=user)
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class DeleteSuperAdminView(APIView):
    def delete(self, request, id):
        try:
            super_admin = AssociationSuperAdmin.objects.get(user__id=id)
        except AssociationSuperAdmin.DoesNotExist:
            return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        super_admin.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class DeleteSuperAdminView(APIView):
#     def delete(self, request, id):
#         try:
#             super_admin = Advocate.objects.get(user__id=id,type_of_user='super_admin')
#         except Advocate.DoesNotExist:
#             return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
#         super_admin.delete()
#         return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


        

            
class MembershipPlanView(APIView):
    def post(self ,request):
        data = request.data
        serializer = MembershipPlanSerializer(data=data)
        if serializer.is_valid():
            plan = serializer.validated_data['membership_plan']
            unit = serializer.validated_data['unit_of_plan']
            if MembershipPlan.objects.filter(membership_plan = plan ,unit_of_plan = unit).exists() :
                return Response({"message": "Plan already exits"} ,status =status.HTTP_409_CONFLICT)
            serializer.save()
            return Response({"message " : "Plan added sucesfully" ,'data' :serializer.data} ,status =status.HTTP_201_CREATED)
        return Response({"message" : " Error Invalid data " } ,serializer.errors)
    
    def get(self, request) :
        data = MembershipPlan.objects.all()
        serializer = MembershipPlanSerializer(data ,many = True)
        return Response({"data":serializer.data },status=status.HTTP_200_OK)
    

class ToggleMembershipPlanView(APIView):
    def patch(self, request, id):
        data=request.data
        try:
            plan= MembershipPlan.objects.get(id=id)
            serializer=MembershipPlanSerializer(plan, data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message" : "Membership plan updated sucessfully"
                    },status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MembershipPlan.DoesNotExist:
            return Response({
                "message" : "Membership plan could not be found"
                }, status=status.HTTP_404_NOT_FOUND )
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def delete(self, request, id):
        try:
            plan = MembershipPlan.objects.get(id=id)
            plan.delete()
            return Response({"message" : "Membership plan deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)   
        except MembershipPlan.DoesNotExist:
            return Response({"message" : "Membership plan could not be found"}, status= status.HTTP_404_NOT_FOUND)
        


class ToggleMembershipFineAmountView(APIView):
    def post(self, request):
        data= request.data
        serializer=MembershipFineAmountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Fine amount set sucessfully"},status=status.HTTP_201_CREATED)
        return Response({"message" : "Something went wrong"},status=status.HTTP_400_BAD_REQUEST)                                

    def get(self, request):
        data=MembershipFineAmount.objects.all()
        serializer=MembershipFineAmountSerializer(data, many = True)
        return Response({"data":serializer.data },status=status.HTTP_200_OK)
    
    def patch(self, request, id):
        data= request.data
        try:
            fine= MembershipFineAmount.objects.get(id=id)
            serializer=MembershipFineAmountSerializer(fine, data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message" : "The fine amount updated successfully"},status=status.HTTP_200_OK)
            return Response({"message" : "Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
        except MembershipFineAmount.DoesNotExist:
            return Response({"message" : "The Fine amount data could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message" : "An unexcepted error occured "},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request, id):
        try:
            fine= MembershipFineAmount.objects.get(id = id)
            fine.delete()
            return Response({"message" : "The amount deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except MembershipFineAmount.DoesNotExist:
            return Response({"message" : "The finr amount could not be found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({"message" : "An unexcepted error occured "+str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class NotificationGetView(APIView):
    def get(self, request):
        notification=Notification.objects.all()
        serializer=NotificationSerializer(notification,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class NotificationView(APIView):
    def post(self, request, id ):
        data=request.data
        try:
            association=Association.objects.get(id=id)
            serializer=NotificationSerializer(data=data)
            if serializer.is_valid():
                serializer.validated_data['association']=association
                serializer.save()
                # notification=Notification(association=association)
                # notification.save()
                return Response({"message":"Notification content created successfully"})
            return Response({"message" : "Something went wrong"},status=status.HTTP_400_BAD_REQUEST)                                
        except Association.DoesNotExist:
            return Response({"message":"Association could not be found"})
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred "
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    
    def patch(self, request, id):
        try:
            notification=Notification.objects.get(id=id)
            data=request.data
            serializer=NotificationSerializer(notification,data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Notification updated successfully"})
            return Response({"message" : "Something went wrong"},status=status.HTTP_400_BAD_REQUEST)                         
        except Notification.DoesNotExist:
                    return Response({"message" : "Notification content could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred "+str(e) 
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            notification = Notification.objects.get(id=id)
            notification.delete()
            return Response({"message": "Notification deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            return Response({"message": "Notification content could not be found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "An unexpected error occurred: " + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class MembershipPaymentView(APIView):
    def expiry_plan_calculation(request, plan_data):
        if plan_data.unit_of_plan == "month":
            payment_expiry_date = datetime.now() + timedelta(days=30 * plan_data.membership_plan)
            return payment_expiry_date
        elif plan_data.unit_of_plan == "year":
            payment_expiry_date = datetime.now() + timedelta(days=365 * plan_data.membership_plan)
            return payment_expiry_date
        else:
            return Response({"message" : "Incorrect date format"}, status=status.HTTP_401_UNAUTHORIZED)


    def post(self ,request,user_id,plan_id,association_id):
        user_id = request.data.get('user_id')
        plan_id = request.data.get('plan_id')
        association_id = request.data.get('association_id')
        if user_id is None or plan_id is None or association_id is None:
            return Response({"message" : "In valid request, the user id or plan id is missing"})
        try :
            association_data = Association.objects.get(id = association_id)
            user_data = Advocate.objects.get(id = user_id)
            plan_data = MembershipPlan.objects.get(id = plan_id)
            fine_amount_obj = MembershipFineAmount.objects.filter().order_by('-id').first()
            fine_amount = fine_amount_obj.fine_amount
            user_serializer = NormalAdvocateSerializer(user_data)
            plan_serializer = MembershipPlanSerializer(plan_data)
            membership_total_amount = plan_data.membership_price
            if AssociationMembershipPayment.objects.filter(for_user_details=user_data).exists:
                user_last_payment = AssociationMembershipPayment.objects.filter( for_user_details = user_data).order_by('-payment_done_at').first()
                if user_last_payment:
                    if user_last_payment.payment_expiry_date < timezone.now().date():
                        months_passed = (timezone.now().year - user_last_payment.payment_expiry_date.year) * 12 + timezone.now().month - user_last_payment.payment_expiry_date.month
                        fine = months_passed * fine_amount
                        membership_total_amount = fine + int(plan_data.membership_price)
                else :
                    return Response({"message" : "Something went wrong"} ,status=status.HTTP_404_NOT_FOUND)
            payment_expiry_date =self.expiry_plan_calculation(plan_data)
            response = api.payment_request_create(
             purpose= "Membership" ,
            amount =  membership_total_amount,
            buyer_name = user_data.name ,
            email= user_data.email ,
            redirect_url= 'http://127.0.0.1:8000/Paymentsucessfull/'
            )
            print(response['payment_request']['longurl'])

            print(response ,"payment")
            if response['success'] == True :
                AssociationPaymentRequest.objects.create(
                    payment_request_id = response['payment_request']['id'],
                    payment_requested_user = user_data,
                    payment_requested_plan = plan_data,
                    payment_expiry_date = payment_expiry_date,
                    payment_total_amount_paid = membership_total_amount,
                    payment_association = association_data
                )
                payment_request_url = response['payment_request']['longurl']

                return Response( {"message" : "Payment request intiated sucessfully" ,"payment_request_url" :payment_request_url, "data" : user_serializer.data ,
                            "plan_data" : plan_serializer.data} ,status = status.HTTP_200_OK)
        except Advocate.DoesNotExist:
            return Response({"message" :"user does not exixts" }, status = status.HTTP_404_NOT_FOUND)
        except MembershipPlan.DoesNotExist:
            return Response({"message": "Plan does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except MembershipFineAmount.DoesNotExist:
            return Response({"message": "MembershipFine does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Something went wrong: "}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        membershiplist=AssociationMembershipPayment.objects.all()
        serializer=AssociationMembershipPaymentSerializer(membershiplist,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class Paymentsucessfull(APIView):
    def get(self ,request):
        payment_requested_id_in_request = request.GET.get("payment_request_id")
        payment_id = request.GET.get('payment_id')
        try :
            payment_requested_user = AssociationPaymentRequest.objects.get(payment_request_id =payment_requested_id_in_request )
        except AssociationPaymentRequest.DoesNotExist:
            return Response({"message" : "Payment user does not exixtss "} ,status = status.HTTP_401_UNAUTHORIZED)
        plan_data = payment_requested_user.payment_requested_plan
        user_data = payment_requested_user.payment_requested_user
        payment_expiry_date = payment_requested_user.payment_expiry_date
        membership_total_amount = payment_requested_user.payment_total_amount_paid
        association_data = payment_requested_user.payment_association
        response = api.payment_request_payment_status(payment_requested_id_in_request, payment_id)
        
        print(response,"siju")
        if response['success'] == True : 
            if response['payment_request']['status'] == 'Completed' and response['payment_request']['payment']['status'] == 'Credit' :
                AssociationMembershipPayment.objects.create(
                    for_payment_plan = plan_data,
                    for_user_details = user_data,
                    payment_id = response['payment_request']['id'],
                    payment_status = True,
                    payment_expiry_date = payment_expiry_date,
                    payment_total_amount_paid = membership_total_amount,
                    payment_association = association_data
                    )
                AdvocateAssociation.objects.create(
                    advocate = user_data,
                    association = association_data,
                    advocate_status = True)
                print(membership_total_amount)
                return Response( {"message" : "Payment sucessfull"} ,status = status.HTTP_200_OK)
            return Response({"message" : "Payment request intiated but didn't debited the amount (payment status : pending)"} ,status = status.HTTP_402_PAYMENT_REQUIRED)
        return Response( {"message" : "Payment unsucessfull" } ,status = status.HTTP_402_PAYMENT_REQUIRED)
    
class CourtEditFormView(APIView):
    def get(self, request, id) :
        try:
            plan= Court.objects.get(id=id)
            serializer=CourtListSerializer(plan)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Court.DoesNotExist:
            return Response({
                "message" : "Court details could not be found"
                }, status=status.HTTP_404_NOT_FOUND )
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred"       
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AssociationEditFormView(APIView):
    def get(self, request, id) :
        try:
            plan= Association.objects.get(id=id)
            serializer=AssociationListSerializer(plan)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Court.DoesNotExist:
            return Response({
                "message" : "Association details could not be found"
                }, status=status.HTTP_404_NOT_FOUND )
        except Exception as e:
            return Response({
                "message": "An unexpected error occurred"           
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NotificationEditFormView(APIView):
    def get(self, request, id) :
        try:
            notification=Notification.objects.get(id=id)
            serializer=NotificationSerializer(notification)
            return Response(serializer.data ,status=status.HTTP_200_OK)

        except Notification.DoesNotExist:
                    return Response({"message" : "Notification content could not be found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Response({
                        "message": "An unexpected error occurred "
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



