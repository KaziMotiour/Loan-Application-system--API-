# Generated by Django 3.2.4 on 2021-06-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanManagement', '0005_auto_20210612_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='accepteance',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
    ]
