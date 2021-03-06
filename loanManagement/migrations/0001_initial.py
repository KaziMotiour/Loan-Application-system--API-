# Generated by Django 3.2.4 on 2021-06-10 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import loanManagement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('bankAuthor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bankBranch', to='loanManagement.bank')),
                ('branchAuthor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=200)),
                ('incomeRange', models.CharField(max_length=50)),
                ('expectedLoanAmount', models.CharField(max_length=50)),
                ('collateralSecurityAmount', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=200)),
                ('fatherName', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=100)),
                ('presentAddress', models.CharField(max_length=100)),
                ('permanentAddress', models.CharField(max_length=100)),
                ('NIDNumber', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=100)),
                ('dateOfBirth', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('mobileNumber', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to=loanManagement.models.upload_image, verbose_name='Image field')),
                ('signature', models.FileField(upload_to=loanManagement.models.upload_signature, verbose_name='signature field')),
                ('NID', models.FileField(upload_to=loanManagement.models.upload_NID, verbose_name='NID field')),
                ('documents1', models.FileField(upload_to=loanManagement.models.upload_documents1, verbose_name='documents1 field')),
                ('documents2', models.FileField(upload_to=loanManagement.models.upload_documents2, verbose_name='documents2 field')),
                ('documents3', models.FileField(upload_to=loanManagement.models.upload_documents3, verbose_name='documents3 field')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bnApplication', to='loanManagement.bank')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brApplication', to='loanManagement.bankbranch')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
