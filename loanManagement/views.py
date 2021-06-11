from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from .serializers import UserSerialiser, BankSerializer, BranchSerializer, ApplicationSerializer, PostApplicationSerializer
from .models import Bank, BankBranch, Application


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class BankSerializerView(ListAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()

class BranchSerializerView(ListAPIView):
    serializer_class = BranchSerializer
    queryset = BankBranch.objects.all()


class ApplicationSerializerView(ListAPIView):
    permission_classes =[IsAuthenticated, ]
    serializer_class = ApplicationSerializer
    def get_queryset(self):
        user = self.request.user
        group_name = user.groups.all()[0].name

        if user.is_superuser:
            return Application.objects.all(paymentStatus='Complete')

        elif group_name == 'bankBranch':
            banch_name = user.branch.branchName
            return Application.objects.filter(preferredBranch__branchName=banch_name, paymentStatus='Complete')
            
        elif group_name == 'Bank':
            bank_name = user.bank.bankName
            return Application.objects.filter(preferredBank__bankName=bank_name, paymentStatus='Complete')

    


class PostApplicationSerializerView(CreateAPIView):
    serializer_class = PostApplicationSerializer
    queryset = Application.objects.all()

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




