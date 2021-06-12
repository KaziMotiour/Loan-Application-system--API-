from django.contrib import admin
from .models import Bank, BankBranch, Application

# Register your models here.
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(Application)
