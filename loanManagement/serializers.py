from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BankBranch, Bank, Application
from random import shuffle


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class BankSerializer(serializers.ModelSerializer):
    bankAuthor = UserSerialiser(read_only=True)
    class Meta:
        model = Bank
        fields = ['id', 'bankAuthor', 'bankName', 'createDate']


class BranchSerializer(serializers.ModelSerializer):

    bank = BankSerializer(read_only=True)
    branchAuthor = UserSerialiser(read_only=True)
    class Meta:
        model = BankBranch
        fields = ['id', 'bank', 'branchAuthor', 'branchName', 'createDate']

class ApplicationSerializer(serializers.ModelSerializer):
    preferredBank =BankSerializer(read_only=True)
    preferredBranch = BranchSerializer(read_only=True)
    class Meta:
        model = Application
        fields = ['id', 'preferredBank', 'preferredBranch', 'profession', 'incomeRange', 'expectedLoanAmount', 'collateralSecurityAmount', 'userName', 'fathersName', 'mothersName', 'presentAddress', 'permanentAddress', 'NID', 
         'dateOfBirth', 'nationality', 'mobileNumber', 'email', 'photo', 'signature', 'nidImg', 'document1', 'document2', 'document3', 'applicationStatus', 'loanId', 'transactionID', 'paymentStatus', 'timestamp',]

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