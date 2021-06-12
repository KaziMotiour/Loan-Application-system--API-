from django.db.models.query import QuerySet
from django.http import request
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from .serializers import UserSerialiser, BankSerializer, BranchSerializer, ApplicationSerializer, PostApplicationSerializer, BankSerializerWithBranch, BankCreateSerializer, BranchCreateSerializer, UserInfoSerialiser
from .models import Bank, BankBranch, Application
from accounts.models import NewUsers

User = get_user_model()

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class UserInfoView(ListAPIView):
    serializer_class = UserInfoSerialiser
    permission_classes = [IsAuthenticated,]
    # queryset = User.objects.all()
    def get_queryset(self):
        pk = self.request.user.id
        return User.objects.filter(pk=pk)
    

# Bank list view
class BankSerializerView(ListAPIView):
    serializer_class = BankSerializer
    permission_classes = [IsAuthenticated, IsAdminUser,]
    queryset = Bank.objects.all()

# Single Bank with all the branch view
class BankSerializerWithBranchView(ListAPIView):

    serializer_class = BankSerializerWithBranch
    permission_classes = [IsAuthenticated,]
    # lookup_field = ['id']

    def get_queryset(self):
        bankName = self.kwargs.get('bankname')
        return Bank.objects.filter(bankName=bankName)


# create bank
class BankCreateSerializerView(CreateAPIView):
    serializer_class = BankCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser,]
    queryset = Bank.objects.all()
  

# branch list view
class BranchSerializerView(ListAPIView):
    serializer_class = BranchSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        bankName = self.kwargs.get('bankname')
        print(bankName)
        return BankBranch.objects.filter(bank__bankName=bankName)
    




# create branch
class BranchCreateSerializerView(CreateAPIView):
    serializer_class = BranchCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser,]
    queryset = BankBranch.objects.all()


# List of application

class ApplicationSerializerView(ListAPIView):
    permission_classes =[IsAuthenticated, ]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            group_name = user.groups.all()[0].name

        if user.is_superuser:
            return Application.objects.all()

        elif group_name == 'BankBranch':
            banch_name = user.branch.branchName
            return Application.objects.filter(preferredBranch__branchName=banch_name, paymentStatus='Complete')
            
        elif group_name == 'Bank':
            bank_name = user.bank.bankName
            return Application.objects.filter(preferredBank__bankName=bank_name, paymentStatus='Complete')

# List of application for single to branch
class ApplicationSerializerForBranchView(ListAPIView):
    permission_classes =[IsAuthenticated, ]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        user = self.request.user
        preferredBranch = self.kwargs.get('preferredbranch')
        return Application.objects.filter(preferredBranch__branchName=preferredBranch)

# List of application for single to bank
class ApplicationSerializerForBankView(ListAPIView):
    permission_classes =[IsAuthenticated, ]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        preferredBank = self.kwargs.get('preferredbank')
        return Application.objects.filter(preferredBank__bankName=preferredBank)

# retrive singe of application 
class RetriveApplicationForBankView(RetrieveAPIView):
    permission_classes =[IsAuthenticated, ]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        print(pk)
        return Application.objects.filter(id=pk)
    

    
    

#  craete application
class PostApplicationSerializerView(CreateAPIView):
    serializer_class = PostApplicationSerializer
    queryset = Application.objects.all()

class SearchApplicationForUserView(ListAPIView):
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        loanId = self.kwargs.get('loanId')
        # print(loanId)
        return Application.objects.filter(loanId='6sfnh54ai')

# @api_view(['GET', 'POST'])
# def postApplicationSerializerView(request):
#     serilizer_data = PostApplicationSerializer(data=request.data)
#     if serilizer_data.is_valid():
        
#         expectedLoanAmount = serilizer_data.data.get('expectedLoanAmount')
#         collateralSecurityAmount = serilizer_data.data.get('collateralSecurityAmount')


#         exp =  int(expectedLoanAmount)*.025
#         if exp>=int(collateralSecurityAmount):
#             status = 'Accepted'
#         else:
#             status = 'Rejected'
        
#         createPost = Application.objects.create(**serilizer_data)
#         createPost.save()
#         return Response({'comment':'created'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response({'comment':'validate error'}, status=status.HTTP_400_BAD_REQUEST)




