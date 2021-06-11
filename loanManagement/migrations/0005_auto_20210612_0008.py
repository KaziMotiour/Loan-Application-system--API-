# Generated by Django 3.2.4 on 2021-06-11 18:08

from django.db import migrations, models
import loanManagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('loanManagement', '0004_auto_20210611_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='status',
            new_name='applicationStatus',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='documents1',
            new_name='document1',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='documents2',
            new_name='document2',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='documents3',
            new_name='document3',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='fatherName',
            new_name='fathersName',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='motherName',
            new_name='mothersName',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='bank',
            new_name='preferredBank',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='branch',
            new_name='preferredBranch',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='name',
            new_name='userName',
        ),
        migrations.RemoveField(
            model_name='application',
            name='NIDNumber',
        ),
        migrations.RemoveField(
            model_name='application',
            name='occupation',
        ),
        migrations.AddField(
            model_name='application',
            name='nidImg',
            field=models.FileField(default='', upload_to=loanManagement.models.upload_NID, verbose_name='NID field'),
        ),
        migrations.AlterField(
            model_name='application',
            name='NID',
            field=models.CharField(max_length=50),
        ),
    ]