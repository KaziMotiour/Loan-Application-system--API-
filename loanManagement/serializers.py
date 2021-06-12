from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BankBranch, Bank, Application
from random import shuffle
User = get_user_model()
from accounts.models import NewUsers

# User Serializer

class UserInfoSerialiser(serializers.ModelSerializer):
    userInfo = serializers.SerializerMethodField(read_only=True,)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'userInfo']
    
    def get_userInfo(self, obj):
        request = self.context.get("request")
        user = request.user
        print(user.is_superuser)
        if request.user.is_superuser:
            return 'superuser'
        else:
            x =  request.user.groups.all()
            print(x)
            return request.user.groups.all()[0].name


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Bank serializer
class BankSerializer(serializers.ModelSerializer):
    bankAuthor = UserSerialiser(read_only=True)
    class Meta:
        model = Bank
        fields = ['id', 'bankAuthor', 'bankName', 'createDate']

# create Bank serializer
class BankCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'bankAuthor', 'bankName', 'createDate']


# branch serializer
class BranchSerializer(serializers.ModelSerializer):

    branchAuthor = UserSerialiser(read_only=True)
    class Meta:
        model = BankBranch
        fields = ['id', 'bank', 'branchAuthor', 'branchName', 'createDate']


# create Branch serializer
class BranchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankBranch
        fields = ['id', 'bank', 'branchAuthor', 'branchName', 'createDate']



# bank serializer with all the branch
class BankSerializerWithBranch(serializers.ModelSerializer):
    bankBranch=BranchSerializer(read_only=True, many=True)
    class Meta:
        model = Bank
        fields = ['id', 'bankAuthor', 'bankName', 'bankBranch', 'createDate']
        # extra_kwargs = {
        #     'url': {'lookup_field': 'id'}
          
        # }

# application serializer
class ApplicationSerializer(serializers.ModelSerializer):
    preferredBank =BankSerializer(read_only=True)
    preferredBranch = BranchSerializer(read_only=True)
    getLoanId = serializers.CharField(max_length=100, required=False)
    getNID = serializers.CharField(max_length=100, required=False)
    class Meta:
        model = Application
        fields = ['id', 'preferredBank', 'preferredBranch', 'profession', 'incomeRange', 'expectedLoanAmount', 'collateralSecurityAmount', 'userName', 'fathersName', 'mothersName', 'presentAddress', 'permanentAddress', 'NID', 
         'dateOfBirth', 'nationality', 'mobileNumber', 'email', 'photo', 'signature', 'nidImg', 'document1', 'document2', 'document3', 'applicationStatus', 'loanId', 'transactionID', 'paymentStatus', 'timestamp','getLoanId', 'getNID']

# create application serializer
class PostApplicationSerializer(serializers.ModelSerializer):
    # 22
    class Meta:
        model = Application
        fields = ['preferredBank', 'preferredBranch', 'profession', 'incomeRange', 'expectedLoanAmount', 'collateralSecurityAmount', 'userName', 'fathersName', 'mothersName', 'presentAddress', 'permanentAddress', 'NID', 'dateOfBirth', 'nationality', 'mobileNumber', 'email', 'photo', 'signature', 'nidImg', 'document1', 'document2', 'document3','applicationStatus', 'loanId']

    def create(self, validated_data):
        name =  validated_data['userName']
        NIDNumber =  validated_data['NID']
        expectedLoanAmount =  validated_data['expectedLoanAmount']
        collateralSecurityAmount =  validated_data['collateralSecurityAmount']
        exp = int(expectedLoanAmount)*.025
        print(exp, collateralSecurityAmount)
        if int(collateralSecurityAmount)>=exp:
            applicationStatus = 'Accepted'
        else:
            applicationStatus = 'Rejected' 
        new_id = name+NIDNumber[len(NIDNumber):len(NIDNumber)-4:-1]
        loanId=list(new_id)
        print(loanId)
        shuffle(loanId)
        loanId=''.join(loanId)
        loanInfo = {
            loanId:loanId
        }

        application = Application.objects.create(**validated_data, applicationStatus=applicationStatus, loanId=loanId)
        return application