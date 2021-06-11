from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def upload_image(instance, filename):
    return 'User_image/{filename}'.format(filename=filename)

def upload_signature(instance, filename):
    return 'User_signature/{filename}'.format(filename=filename)

def upload_NID(instance, filename):
    return 'User_NID/{filename}'.format(filename=filename)

def upload_documents1(instance, filename):
    return 'User_documents1/{filename}'.format(filename=filename)

def upload_documents2(instance, filename):
    return 'User_documents2/{filename}'.format(filename=filename)

def upload_documents3(instance, filename):
    return 'User_documents3/{filename}'.format(filename=filename)


# Create your models here.
class Bank(models.Model):
    bankAuthor = models.OneToOneField(User, related_name='bank', on_delete=models.CASCADE)
    bankName = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.bankName)


class BankBranch(models.Model):
    bank = models.ForeignKey(Bank, related_name='bankBranch', on_delete=models.CASCADE)
    branchAuthor = models.OneToOneField(User, related_name='branch', on_delete=models.CASCADE)
    branchName = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.branchName)



class Application(models.Model):

    application_status = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
]
    payment_status = [
    ('Complete', 'Complete'),
    ('InComplete', 'InComplete'),
]

    # Loan info
    preferredBank = models.ForeignKey(Bank, related_name='bnApplication', on_delete=models.CASCADE)
    preferredBranch = models.ForeignKey(BankBranch, related_name='brApplication', on_delete=models.CASCADE)
    profession = models.CharField(max_length=200)
    incomeRange = models.CharField(max_length=50)
    expectedLoanAmount = models.CharField(max_length=50)
    collateralSecurityAmount = models.CharField(max_length=50)

    # Personal info
    userName = models.CharField(max_length=200)
    fathersName = models.CharField(max_length=100)
    mothersName = models.CharField(max_length=100)
    presentAddress = models.CharField(max_length=100)
    permanentAddress = models.CharField(max_length=100)
    NID = models.CharField(max_length=50)
    dateOfBirth = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    # Documents
    photo = models.FileField(_("Image field"), upload_to=upload_image)
    signature = models.FileField(_("signature field"), upload_to=upload_signature)
    nidImg = models.FileField(_("NID field"), upload_to=upload_NID, default='')
    document1 = models.FileField(_("documents1 field"), upload_to=upload_documents1, null=True, blank=True)
    document2 = models.FileField(_("documents2 field"), upload_to=upload_documents2, null=True, blank=True)
    document3 = models.FileField(_("documents3 field"), upload_to=upload_documents3, null=True, blank=True)

    applicationStatus = models.CharField(
        max_length=20,
        choices=application_status,
        default='Pending',
    )

    loanId = models.CharField(max_length=50, default='')
    transactionID = models.CharField(max_length=50, default='')
    paymentStatus = models.CharField(
        max_length=20,
        choices=payment_status,
        default='InComplete',
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return str(self.userName)


