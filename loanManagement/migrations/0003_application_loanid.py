# Generated by Django 3.2.4 on 2021-06-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanManagement', '0002_auto_20210610_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='loanId',
            field=models.CharField(default='', max_length=50),
        ),
    ]