# Generated by Django 3.2.4 on 2021-06-11 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanManagement', '0003_application_loanid'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='paymentStatus',
            field=models.CharField(choices=[('Complete', 'Complete'), ('InComplete', 'InComplete')], default='InComplete', max_length=20),
        ),
        migrations.AddField(
            model_name='application',
            name='transactionID',
            field=models.CharField(default='', max_length=50),
        ),
    ]
